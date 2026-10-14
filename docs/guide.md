# Using the Commvault SDK

How to do the things the SDK is for, with examples. The README lists
every call with its endpoint and how far it has been proven; this guide
is about putting them together. Every example here uses calls that have
been run against a real CommServe (software 11 SP46) unless it says
otherwise.

1. [Installing](#installing)
2. [Connecting](#connecting)
3. [Keeping a renewed token](#keeping-a-renewed-token)
4. [Logging](#logging)
5. [Collecting jobs](#collecting-jobs)
6. [Why a job failed](#why-a-job-failed)
7. [Clients, instances and SQL Server databases](#clients-instances-and-sql-server-databases)
8. [Plans, storage and credentials](#plans-storage-and-credentials)
9. [Changing a CommServe](#changing-a-commserve)
10. [Commvault Cloud and MSPs](#commvault-cloud-and-msps)
11. [Errors](#errors)
12. [What comes back](#what-comes-back)
13. [An endpoint the SDK does not wrap](#an-endpoint-the-sdk-does-not-wrap)

## Installing

The SDK is not on PyPI. Depend on a tag of its repository:

```
uv add "commvault-sdk @ git+https://github.com/blueneptune/yoki-py-commvault-sdk.git@v0.2.0"
```

or, in `pyproject.toml`:

```toml
[project]
dependencies = ["commvault-sdk"]

[tool.uv.sources]
commvault-sdk = { git = "https://github.com/blueneptune/yoki-py-commvault-sdk.git", tag = "v0.2.0" }
```

To work on the SDK and its caller together, point the source at a
checkout instead: `{ path = "../yoki-py-commvault-sdk", editable = true }`.

It needs Python 3.12 or later, and brings
[sdk-primer-core](https://github.com/blueneptune/sdk-primer-core) (the
transport underneath) with it.

## Connecting

One `CommvaultClient` is one connection to one CommServe. Use it as a
context manager, so its connections are closed:

```python
from commvault_sdk import CommvaultClient, TokenSet

with CommvaultClient(
    "https://commserve.example.com/commandcenter/api",
    access_token=TokenSet(access, refresh),
) as cv:
    info = cv.commcell.info()
    print(info["csVersionInfo"])
```

`cv.commcell.info()` is the cheapest way to prove the credentials work:
it needs a valid session and changes nothing.

**The URL** is the REST base, without a trailing slash. On a CommServe
with Command Center it is `https://<host>/commandcenter/api`; older ones
use `https://<host>/webconsole/api` or
`http://<webserver>:81/SearchSvc/CVWebService.svc`.

**Credentials**, one of:

- **An access token** (Command Center > your user > Access tokens).
  Pass `access_token=TokenSet(access, refresh)`. With the refresh token
  the SDK renews the access token itself when it runs out - and then you
  must keep the new pair (next section). A bare string,
  `access_token="..."`, works too, but without a refresh token it stops
  working when the token expires (two hours on the eval CommServe).
- **A user name and password**: `CommvaultClient(url, "user", "password")`.
  The SDK logs in on first use and again whenever its session times out.
  Simpler, but it means keeping a password.

An access token is the better choice for anything that runs unattended.

**TLS.** A CommServe with a certificate from a private CA:
`ca_bundle=Path("/etc/pki/tls/certs/commserve-ca.pem")`. The eval OVA's
self-signed certificate does not match its host name, so a lab needs
`verify_tls=False`; production should never.

**Other options:** `page_size` (default 500, how many jobs per page of
a listing), `timeout` (seconds per request, default 120). Requests that
fail on the network, or with 429, 502, 503 or 504, are retried with
backoff, three attempts in all; a change is never retried (see
[Changing a CommServe](#changing-a-commserve)).

## Keeping a renewed token

Renewing an access token **replaces** it: Commvault hands back a new
access token and a new refresh token, and the old pair stops working at
once. Whatever you started the client with is dead after the first
renewal. So a caller that uses a refresh token has to save the new pair
the moment it arrives, or its next run starts with a token that no
longer works and someone has to make a new one in Command Center.

`on_token_renew` is called with the new `TokenSet` (and Commvault's raw
reply) before the request that needed it carries on:

```python
import json
import os
from datetime import datetime
from pathlib import Path

from commvault_sdk import CommvaultClient, TokenSet

TOKENS = Path("cv-tokens.json")


def _when(text: str | None) -> datetime | None:
    return datetime.fromisoformat(text) if text else None


def load_tokens() -> TokenSet | None:
    if not TOKENS.exists():
        return None
    saved = json.loads(TOKENS.read_text())
    return TokenSet(
        saved["access_token"],
        saved["refresh_token"],
        _when(saved.get("expires_at")),
        _when(saved.get("renewable_until")),
    )


def save_tokens(tokens: TokenSet, raw_reply: dict) -> None:
    # Write a new file and swap it in, so a crash halfway leaves the old
    # file rather than half of each; owner-only, since these are secrets.
    tmp = TOKENS.with_name(f".{TOKENS.name}.tmp")
    fd = os.open(tmp, os.O_WRONLY | os.O_CREAT | os.O_TRUNC, 0o600)
    with os.fdopen(fd, "w") as handle:
        json.dump(
            {
                "access_token": tokens.access_token,
                "refresh_token": tokens.refresh_token,
                "expires_at": tokens.expires_at and tokens.expires_at.isoformat(),
                "renewable_until": tokens.renewable_until and tokens.renewable_until.isoformat(),
            },
            handle,
        )
    os.replace(tmp, TOKENS)


with CommvaultClient(url, access_token=load_tokens(), on_token_renew=save_tokens) as cv:
    ...
```

The first time, write the file by hand with the token pair from Command
Center (the two dates can be left out).

**Renewal happens** before a request when the token is known to be about
to expire, and after a request that comes back 401 when it is not known
(that request is then sent once more). A token can only be renewed until
its *renewable until* date (`TokenSet.renewable_until`, about two months
after it was made); after that, make a new one in Command Center. It is
worth warning a week ahead.

**More than one process on the same token** - two scheduled runs that
can overlap, say - must not both renew it: the second renewal uses a
refresh token the first has just retired. Give the client a way to read
the current pair, and a lock they all take while renewing:

```python
with CommvaultClient(
    url,
    access_token=load_tokens(),
    on_token_renew=save_tokens,
    token_reload=load_tokens,              # read the pair as it is now
    token_renew_lock=lambda: file_lock(),  # a context manager all of them share
) as cv:
    ...
```

Inside the lock the client first reloads; if another process has already
renewed, it adopts that pair instead of renewing again. `file_lock` can
be anything that excludes the others - on one machine, `fcntl.flock` on
a file beside the token file. blt's `blt.collector.tokens` and
`blt.collector.lock` are a complete, tested version of all of this
(tokens kept in the `.env` file that configures the CommCell), and the
lab repository has a copy.

**Two tools, two tokens.** Two programs that each keep their own copy of
one token pair will lock each other out on the first renewal. Give each
its own Commvault user and token, or have them share one file and one
lock as above.

## Logging

The SDK logs with [loguru](https://github.com/Delgan/loguru): one line
per page of jobs at INFO, every request and its answer at DEBUG, token
renewals at INFO, anything skipped as unreadable at ERROR. loguru's
default prints everything, DEBUG included, to stderr. To choose a level:

```python
from sdk_primer import configure_logging

configure_logging(level="INFO")
```

or configure loguru directly (`logger.remove()`, `logger.add(...)`); to
silence the SDK entirely, `logger.disable("commvault_sdk")` and
`logger.disable("sdk_primer")`.

The transport logs every failed request at ERROR before raising, even
ones the SDK expects and turns into an answer - a 404 for "there are
none", the 500 `failed_items()` gets for a job that is not a backup. An
ERROR line from `sdk_primer.client` is therefore not always a problem;
an exception reaching your code is.

## Collecting jobs

### Everything recent

```python
for page in cv.jobs.iter_pages(lookup_seconds=24 * 3600):
    for job in page:
        print(job.job_id, job.job_type, job.status, job.client_name, job.end_time)
```

`iter_pages(lookup_seconds)` gives every job that is active now plus
every job that finished in the last `lookup_seconds`, aged jobs
included, one page (`page_size` jobs) at a time. Pages are in job-id
order, oldest first, so a job that starts while you are paging lands
after the last page rather than shifting the ones you have not read
yet. It has been run at 60,000+ jobs.

Each is a `Job`: type, status, level, client, subclient, times, sizes,
file counts, and the reason if it did not end well (see
[What comes back](#what-comes-back)).

### A slice of history

```python
from datetime import UTC, datetime, timedelta

end = datetime.now(UTC)
start = end - timedelta(days=1)
for page in cv.jobs.iter_pages(lookup_seconds=0, ended_between=(start, end)):
    ...
```

With `ended_between`, only finished jobs whose end time falls in the
range (both ends inclusive), and nothing active. That is how to fetch a
long history a day at a time instead of in one heavy query, or to
re-read a window you collected before. `cv.jobs.oldest_start(lookup)`
says when the oldest finished job the CommServe still has started, so
you know where history ends.

### Incrementally

A collector that runs every few minutes should not re-read a day each
time. Keep the time of your last successful run and ask for what ended
since, with some overlap, plus what is active now:

```python
since = last_run - timedelta(minutes=60)   # overlap: clocks, late finishers
now = datetime.now(UTC)
finished = [j for page in cv.jobs.iter_pages(0, ended_between=(since, now)) for j in page]
running = cv.jobs.active()
```

Store jobs by `job_id` and overwrite: a job read twice is the same job,
and a running job read again later has moved on.

### A job in progress

```python
job = cv.jobs.get(job_id)                 # from the summary: a few seconds behind
job.status, job.current_phase_name, job.percent_complete

detail = cv.jobs.detail(job_id)           # fresher
detail.status, detail.phase_name, detail.percent_complete
detail.files_transferred, detail.network_bytes, detail.size_of_application
```

While a job is active, `Job` has its phase (`current_phase`,
`current_phase_name`) and when the current attempt at it started
(`attempt_start_time`), and `JobDetail` adds files transferred, bytes
sent over the network, average throughput (`average_gib_per_hour`) and
the file being worked on. All of them are `None` once the job has
ended. What two lab backups showed:

- **The summary lags.** `get()` and the job listing were up to ten
  seconds behind `detail()`: the summary still said Backup at 25% when
  the details said Archive Index at 85%. To follow one job, poll
  `detail()`.
- **Waiting is normal.** A backup waits for resources between phases -
  `Waiting`, with no reason given and `attempt_start_time` `None` -
  for a few seconds. A job that waits with a reason is another matter
  (`pending_reason`, `pending_reason_code`).
- **Percent moves in steps** at phase changes (0, 25, 70, 85, 98 on a
  file-system backup), so it says which stage a job is at, not how long
  is left. Commvault's own estimate of the time left was 0 throughout.
- **Attempts list finished phases only.** `attempts()` has no entry for
  the phase in progress until it ends, so `explain()` on a running job
  shows only what has already gone wrong.
- **`task()` may only answer while the job runs.** A backup started
  through the API answered while running, and afterwards was refused as
  a job "initiated from command line".

### Small things

- `cv.jobs.active()` - jobs active right now (one page, up to 500).
- `cv.jobs.get(job_id)` - one job's current summary, or `None` if the
  CommCell no longer knows it.
- `cv.jobs.sample(lookup_seconds, limit=5)` - a few jobs and the
  CommServe's count of how many match, in one request: a quick check
  that listing works, or how big a full pull would be.

An entry the SDK cannot read as a `Job` is logged at ERROR and skipped,
so one strange job does not stop a collection; its id is in the log.

## Why a job failed

The job listing already says a little about each failure at no extra
cost: `Job.pending_reason`, one sentence, and `Job.pending_reason_code`,
Commvault's code for that kind of failure (`19:1132`). The text names
the client, path or job involved, so it differs every time; the code
does not, which makes it the thing to count and group failures by.

For more, ask about the jobs that need it. Each of these is one or two
requests **per job**, so on a large CommCell ask about the failed ones,
not every job you collect.

### The short way

```python
why = cv.jobs.explain(job_id)
if why and not why.clean:
    print(why.status, why.reason_codes)
    for reason in why.reasons:
        print(reason.text, "-", reason.source, reason.process)
    for attempt in why.incomplete_attempts:
        print(attempt.phase_name, attempt.status, attempt.failure_reason)
    for event in why.events:
        print(event.time, event.severity, event.code, event.description)
```

`explain()` is two requests: the job's details with its attempts, and
its events. `why.detail` is the full `JobDetail`. `None` means the
CommCell does not know the job.

A job can complete and still not be `clean`: in the lab, 9 of 207
completed jobs had an attempt that was suspended, interrupted or failed
before a later one succeeded. `explain()` includes major and critical
events; `min_severity=0` gives all of them.

### The pieces

```python
cv.jobs.detail(job_id)        # JobDetail: who started it, schedule, plan, what it scanned and failed on
cv.jobs.attempts(job_id)      # [JobAttempt]: each try at each phase, and how it ended
cv.jobs.events(job_id)        # [JobEvent]: the event log for the job, oldest first
cv.jobs.task(job_id)          # JobTask | None: what it was asked to do
cv.jobs.failed_items(job_id)  # [FailedItem] | None: the files and folders it could not read
```

What to expect from each:

- **A job that failed to start** has no attempts - it never reached a
  phase - so its events are all there is.
- **A job that ran cleanly** usually has no events.
- **`task()`** is the request Commvault keeps for resubmitting the job,
  and it gives it only for jobs it would resubmit: it is `None` for an
  interactive job more than 7 days old, a job started from the command
  line, and a workflow job (104 of the lab's 272 jobs). Its
  `requested_level` is what was asked for, which is not always what ran:
  a plan's log schedule asks for an incremental and runs a transaction
  log backup. `Job.backup_level` is what ran.
- **`failed_items()`** is the list behind `Job.failed_files` and
  `failed_folders`. Ask only about jobs where those are above 0.
  Commvault keeps the list for about 7 days - after that it is an empty
  list although the count remains - and answers a job that is not a
  backup with an HTTP 500, which comes back as `None` (and is logged as
  an error by the transport). Proven on files that failed the scan;
  files that fail in the backup phase itself are not yet.

### Reasons

Commvault ends each reason with the machine and process that reported
it - `...<br/>Source: CS01, Process: JobManager` - and puts several in
one field when a job was held up more than once. `pending_reason` and
`failure_reason` are that text as it came. `.reasons`, on a `Job`,
`JobDetail` or `JobAttempt`, is the same thing split into
`Reason(text, source, process)`:

```python
for reason in job.reasons:
    reason.text, reason.source, reason.process
```

`split_reason(text)` does the same for a reason you stored earlier.

### Grouping failures across a CommCell

```python
from collections import Counter

failed = [
    job
    for page in cv.jobs.iter_pages(7 * 24 * 3600)
    for job in page
    if job.status not in ("Completed", "Running", "Waiting", "Pending")
]
by_code = Counter(job.pending_reason_code for job in failed)
for code, count in by_code.most_common(10):
    example = next(job for job in failed if job.pending_reason_code == code)
    print(count, code, example.reasons[0].text if example.reasons else "")
```

One listing, no request per job: then `explain()` one example of each
code that matters.

## Clients, instances and SQL Server databases

```python
for client in cv.clients.list():                 # clientId, clientName, hostName, ...
    agents = cv.clients.agents(client["clientId"])          # ["File System", "SQL Server"]
    for instance in cv.instances.list(client["clientId"]):  # instanceId, instanceName, appName
        if instance["appName"] == "SQL Server":
            for db in cv.sql.databases(instance["instanceId"]):
                print(client["clientName"], instance["instanceName"],
                      db["dbName"], db["bkpTime"], db["planName"])
```

`bkpTime` is the last backup's time in epoch seconds, as Commvault sends
it; `jobId` and `fullJobId` are the last backup and the last full.

- `cv.clients.find(name)` - one client by name, ignoring case, or `None`.
- `cv.instances.get(instance_id)` / `cv.subclients.get(subclient_id)` -
  one in full, as Commvault's JSON.
- `cv.subclients.list(client_id)` - a client's subclients.
- **An instance id is not unique across clients**: every file-system
  agent's `DefaultInstanceName` is instance 1. Keep the client with it.
- **`sql.databases()` lists what Commvault has backed up**: user
  databases only (master, model and msdb are backed up but never listed
  here), and only ones a backup has already reached. A database created
  since the last backup is not there. `cv.sql.discovered(cv.subclients.get(id))`
  is what Commvault's own discovery saw on a SQL subclient, system
  databases included.

Inventory is one request per client and per instance; on a CommCell with
thousands of clients, that is thousands of requests. A listing across
the whole CommCell is on the SDK's TODO.

## Plans, storage and credentials

```python
cv.plans.ids()          # {"Standard Plan": 1, ...}
cv.plans.list()         # each plan's summary: plan.name, plan.id, planType, status, numberOfCopies
cv.storage.disk()       # disk storage pools
cv.credentials.names()  # names of the stored credentials (never their secrets)
```

These are summaries. Reading a plan, a pool or a policy in full, and
schedules, alerts and the rest of a CommCell's configuration, is laid
out in the SDK's TODO.md, not built yet.

## Changing a CommServe

The client is read-only unless you say otherwise. A call that would
change the CommServe - start or kill a job, create a subclient, delete a
client - raises `ChangesNotAllowed` before sending anything, unless the
client was built with `allow_changes=True`:

```python
with CommvaultClient(url, access_token=tokens, allow_changes=True) as cv:
    client = cv.clients.find("fileserver-01")
    plan_id = cv.plans.ids()["Standard Plan"]
    cv.subclients.create(
        client["clientName"],
        "docs",
        content=[{"path": "/srv/docs"}],
        plan={"planName": "Standard Plan", "planId": plan_id},
    )
    subclient = next(s for s in cv.subclients.list(client["clientId"])
                     if s["subclientName"] == "docs")
    job_id = cv.subclients.backup(subclient["subclientId"], "Full")
```

Leave `allow_changes` off in anything that only reads - a collector, a
report. Then nothing it does, and no bug in it, can alter a production
CommServe.

**A change is sent once and never retried.** If it times out, Commvault
may well have acted on it already: sending "start a backup" again
starts a second backup. So a change that fails on the network raises,
and it is for you to look before trying again (`cv.jobs.active()` shows
whether the backup started).

**A refusal inside a 200.** Commvault reports many failed changes as
HTTP 200 with an error in the body. Changes check for that and raise
`CommvaultError` with Commvault's words.

What can be changed today: starting a backup
(`subclients.backup(id, level)`, levels `Full`, `Incremental`,
`Differential`, `Transaction_Log`), suspending, resuming and killing a
job, creating a subclient and giving it a plan, updating an instance,
giving a SQL instance a stored credential, creating a credential, and
asking for an install authcode. `subclients.delete()` and
`clients.delete()` are written but have never been run. Try changes on a
lab CommServe first; the lab rig (`yoki-commvault-lab`) exists for that.

## Commvault Cloud and MSPs

The same client talks to Commvault Cloud (SaaS, formerly Metallic):

```python
CommvaultClient(
    "https://api.metallic.io",
    access_token=tokens,
    on_token_renew=save_tokens,
    deployment="saas",
    max_calls_per_hour=800,
)
```

- `deployment="saas"` sends the token as `Authorization: Bearer ...`
  rather than the CommServe's `Authtoken` header.
- `max_calls_per_hour` makes the client wait when it has sent that many
  requests in the last hour. SaaS limits a tenant to 1000 reads and 100
  writes an hour across all its API users, so leave room for the others.
  Every request counts - logins and renewals too. `cv.budget.used`
  says how many have gone.
- A managed service provider reaches each customer's tenant with
  `extra_headers={"lhAccountId": account_id}`, one client per tenant.
  `cv.partner.accounts()` lists the MSP's customer accounts.

**None of this has been run against a real tenant yet**; the request
shapes come from Commvault's documentation. Treat it as a start.

## Errors

| You get | When |
|---|---|
| `ChangesNotAllowed` | a change on a client without `allow_changes=True`; nothing was sent |
| `CommvaultError` | Commvault refused a change in an HTTP 200 (`ChangesNotAllowed` is one too) |
| `AuthenticationError` | 401 that renewal could not fix, a rejected login, a dead refresh token |
| `NotFoundError` | 404 (most listings turn "none" into an empty list instead) |
| `ClientError` | another 4xx - e.g. 409 starting a backup on a subclient that already has one running |
| `ServerError` | 5xx after retries, or a 200 that is not JSON: the "Scheduled Maintenance" page a CommServe serves while its web tier restarts |
| `NetworkError` | no answer at all after retries |
| `RateLimitedError` | 429 after retries |

All of them are `sdk_primer.SDKError`, so `except SDKError` catches
anything the SDK raises for a failed request. `ChangesNotAllowed` and
`CommvaultError` come from `commvault_sdk`; the rest from `sdk_primer`.

Reads do not raise for an answer that is simply "nothing": an unknown
job is `None` from `get()`, `detail()`, `explain()` and `task()`, and
an empty list from `events()` and `attempts()`.

## What comes back

**Jobs are typed.** `Job`, `JobDetail`, `JobAttempt`, `JobEvent`,
`JobExplanation`, `JobTask`, `FailedItem` and `Reason` are pydantic
models with named, typed fields: times are timezone-aware `datetime`s in
UTC, sizes are bytes, numbers are numbers even where Commvault sent
strings. Each keeps Commvault's own JSON in `.raw`, so a field the model
does not name yet is still there:

```python
job.raw.get("jobSubmitErrorCode")
```

A field Commvault did not send is `None`, not 0 or `""` - a job that
has not ended has `end_time=None`.

The `Job` fields most used: `job_id`, `status`, `job_type`
(`Backup`, `CS DR Backup`, `Data Aging`, ...), `operation`,
`backup_level`, `app_type`, `client_id`, `client_name`,
`subclient_name`, `instance_name`, `storage_policy`, `start_time`,
`end_time`, `elapsed_seconds`, `size_of_application`, `size_of_media`,
`total_files`, `failed_files`, `failed_folders`, `pending_reason`,
`pending_reason_code`, `is_aged`. The docstrings in `models.py` describe
each model and what was seen of its fields in the lab.

**Everything else is Commvault's JSON**, as dictionaries, with the
envelope taken off: `clients.list()` is the list of client entities, not
the `clientProperties` wrapper around them. Field names are Commvault's
(`clientId`, `clientName`). Typed models for these come as it becomes
clear which fields matter.

## An endpoint the SDK does not wrap

`cv.api` is the authenticated transport itself - the same retries, token
renewal and logging:

```python
response = cv.api.get("/V4/ServerPlan/12")
plan = response.json()
```

It is for finding out what an endpoint returns. Anything you come to
rely on belongs in the SDK, run against a real CommServe and with tests;
the SDK's docs/development.md says how to add one.
