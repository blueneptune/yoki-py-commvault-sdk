# yoki-py-commvault-sdk
Your Org's Keepsake Integrations - python - CommVault - SDK

A small SDK for Commvault's REST API - a CommServe you run yourself, or
Commvault Cloud (SaaS, formerly Metallic) - written as a facade: one object per CommServe connection, with a named group of
calls for each kind of thing.

```python
from commvault_sdk import CommvaultClient, TokenSet

with CommvaultClient(url, access_token=TokenSet(access, refresh)) as cv:
    cv.commcell.info()["csVersionInfo"]
    for page in cv.jobs.iter_pages(lookup_seconds=3600):
        ...
    for client in cv.clients.list():
        for instance in cv.instances.list(client["clientId"]):
            ...
```

## Software and SaaS

The same SDK talks to a CommServe you run and to Commvault Cloud:

```python
CommvaultClient("https://api.metallic.io", access_token=tokens,
                deployment="saas", max_calls_per_hour=800)
```

`deployment="saas"` sends the token as `Authorization: Bearer ...`
instead of `Authtoken: Bearer ...`. `max_calls_per_hour` puts every
request the client sends through a budget and waits when it is spent,
for SaaS's per-tenant rate limit (1000 reads and 100 writes an hour).
For a managed service provider, `extra_headers={"lhAccountId": ...}`
says which customer tenant the calls are for. None of the SaaS support
has been run against a real tenant yet.

## Read-only unless you say otherwise

Every call is one of three kinds, and the SDK treats them differently:

| Kind | Examples | Allowed by default |
|---|---|---|
| A GET | `clients.list()`, `sql.databases()` | yes |
| A query sent as a POST (Commvault puts some filters in the body) | `jobs.iter_pages()`, `jobs.details()` | yes |
| A change to the CommServe | `subclients.backup()`, `jobs.kill()`, `clients.delete()` | **no** |

A change raises `ChangesNotAllowed` before any request is sent, unless
the client was built with `allow_changes=True`. A caller that only
collects never passes it, so nothing it does - and no bug in it - can
alter a production CommServe.

## What is in it

The endpoint is given so each call can be matched against Commvault's
API documentation. "Proven" means that request has been run against a
real CommServe (11 SP46).

### `cv.commcell`

| Call | Endpoint | |
|---|---|---|
| `info()` | `GET /CommServ` | proven |
| `packages()` | `GET /V4/commcell/available-packages` | proven |
| `install_authcode()` *change* | `POST /Organization/0/Authtoken` | proven |

### `cv.jobs`

| Call | Endpoint | |
|---|---|---|
| `iter_pages(lookup_seconds, ended_between=)` | `POST /Jobs` | proven, at 60,000+ jobs |
| `sample(lookup_seconds, limit, ended_between=)` | `POST /Jobs` | proven |
| `active()` | `POST /Jobs` (category 1) | proven |
| `oldest_start(lookup_seconds)` | `POST /Jobs` (limit 1) | proven |
| `get(job_id)` | `GET /Job/{id}` | proven |
| `details(job_id)`, `counts(job_id)` | `POST /JobDetails` | proven |
| `detail(job_id)` | `POST /JobDetails` | proven, on all 270 lab jobs |
| `attempts(job_id)`, `details(job_id, attempts=True)` | `POST /JobDetails` (showAttempt) | proven, on all 258 lab jobs |
| `events(job_id)` | `GET /Events?jobId=` | proven, on all 258 lab jobs |
| `explain(job_id, min_severity=)` | `POST /JobDetails` (showAttempt) + `GET /Events?jobId=` | proven, on all 272 lab jobs |
| `task(job_id)` | `GET /Job/{id}/TaskDetails` | proven, on all 272 lab jobs; answers for 168 |
| `suspend`, `resume`, `kill` *change* | `POST /Job/{id}/action/pause\|resume\|kill` | proven |

### `cv.clients`, `cv.instances`

| Call | Endpoint | |
|---|---|---|
| `clients.list()`, `clients.find(name)` | `GET /Client` | proven |
| `clients.agents(client_id)` | `GET /Agent?clientId=` | proven |
| `clients.delete(client_id)` *change* | `DELETE /Client/{id}?forceDelete=1` | written, **never run** |
| `instances.list(client_id)` | `GET /Instance?clientId=` | proven |
| `instances.get(instance_id)` | `GET /Instance/{id}` | proven |
| `instances.update(instance, properties)` *change* | `POST /Instance/{id}` | proven |

### `cv.subclients`

| Call | Endpoint | |
|---|---|---|
| `list(client_id)` | `GET /Subclient?clientId=` | proven |
| `get(subclient_id)` | `GET /Subclient/{id}` | proven |
| `create(...)` *change* | `POST /Subclient` | proven |
| `set_plan(subclient_id, plan)` *change* | `POST /Subclient/{id}` | proven |
| `backup(subclient_id, level)` *change* | `POST /Subclient/{id}/action/backup` | proven |
| `delete(subclient_id)` *change* | `DELETE /Subclient/{id}` | written, **never run** |

### `cv.sql`

| Call | Endpoint | |
|---|---|---|
| `databases(instance_id)` | `GET /sql/databases?instance=` | proven |
| `discovered(subclient_properties)` | (reads `subclients.get()`) | proven |
| `set_instance_credential(instance, name)` *change* | `POST /Instance/{id}` | proven |

### `cv.partner` (Commvault Cloud MSPs)

| Call | Endpoint | |
|---|---|---|
| `accounts()` | `GET /api/v1/partner/accounts` | written, **never run** |
| `account(account_id)` | `GET /api/v1/partner/accounts/{id}` | written, **never run** |

### `cv.plans`, `cv.storage`, `cv.credentials`

| Call | Endpoint | |
|---|---|---|
| `plans.list()`, `plans.ids()` | `GET /V4/Plan/Summary` | proven |
| `storage.disk()` | `GET /V4/Storage/Disk` | proven |
| `credentials.names()` | `GET /CommCell/Credentials` | proven |
| `credentials.create(...)` *change* | `POST /Commcell/Credentials` | proven |

Authentication (`POST /Login`, `POST /V4/AccessToken/Renew`) is handled
underneath, in `auth.py` and `client.py`.

**How far "proven" goes.** Every read call marked proven has been run
through this code against a CommServe (software 11 SP46), and the job
listing against production CommServes at 60,000+ jobs. Of the change
calls, starting a backup and suspending, resuming and killing a job have
been run through it; the rest send requests that were proven before
this code was a library, checked here by unit tests. Nothing has been
run against Commvault Cloud.

## What it returns

Commvault's own JSON for each thing, as dictionaries, with the envelope
removed (`clients.list()` gives the list of client entities, not the
`clientProperties` wrapper). Jobs are the exception: they come back as
the SDK's typed `Job`, their details as `JobDetail`, their attempts as
`JobAttempt` and their events as `JobEvent`, each with Commvault's own JSON kept in `.raw`. Typed
models for the rest are worth adding once it is clear which fields
matter.

### Why a job failed

`cv.jobs.explain(job_id)` is the short way: one answer, from two
requests, holding the job's reasons and their codes, the attempts that
did not complete, and its major and critical events.

```python
why = cv.jobs.explain(job_id)
if why and not why.clean:
    why.status, why.reason_codes
    for reason in why.reasons: ...               # text, source, process
    for attempt in why.incomplete_attempts: ...  # phase_name, status
    for event in why.events: ...                 # severity, code, description
```

A job can complete and still not be `clean`: in the lab, 9 of 207
completed jobs had an attempt that was suspended, interrupted or failed
before a later one succeeded. The pieces it is made from follow, for
when only one is wanted.

The job summary has one sentence (`Job.pending_reason`) and Commvault's
code for it (`Job.pending_reason_code`, e.g. `19:1132`). Both arrive
with the job listing, at no extra request. The text names the client,
path or job involved, so it differs from one failure to the next; the
code is the same for every failure of that kind, which makes it the
thing to count and group by. Two calls say more:

```python
for attempt in cv.jobs.attempts(job_id):   # each try at each phase
    attempt.phase_name, attempt.status, attempt.failure_reason
for event in cv.jobs.events(job_id):       # the event log, oldest first
    event.time, event.severity, event.code, event.description
```

`cv.jobs.detail(job_id)` is the rest of what Commvault knows about one
job, typed as `JobDetail`: who or what started it (`started_by`,
`started_from`), its schedule and plan, whether it was encrypted and
where it was compressed, and what it scanned, skipped and failed on.
`details()` remains for the same reply as Commvault's JSON.

Commvault ends each reason with the machine and process that reported
it, as `...<br/>Source: CS01, Process: JobManager`, and puts several
reasons in one field when a job was held up more than once.
`pending_reason` and `failure_reason` are that text untouched;
`.reasons`, on a `Job`, `JobDetail` or `JobAttempt`, is the same thing
split:

```python
for reason in job.reasons:
    reason.text, reason.source, reason.process
```

`split_reason(text)` does the same for a reason held anywhere else, such
as one stored earlier.

`cv.jobs.task(job_id)` is what the job was asked to do: what it was
pointed at, the level requested (which is not always the level that
ran - `Job.backup_level` is that) and the options it was submitted
with. Commvault keeps this for resubmitting a job and gives it only for
jobs it would resubmit, so it is `None` for an interactive job more
than 7 days old, a job started from the command line and a workflow
job.

A job that failed to start has no attempts - it never reached a phase -
so its events are all there is. A job that ran cleanly usually has no
events. Each call is one request per job, so on a large CommCell ask
only for the jobs that need explaining, not for every job collected.

## Errors

- HTTP failures raise sdk-primer's typed errors (`AuthenticationError`,
  `NotFoundError`, `ServerError`, ...), all `SDKError`.
- Commvault reports many failures as a 200 with an error in the body. A
  changing call checks for that and raises `CommvaultError`.
- An HTML "Scheduled Maintenance" page with a 200 raises `ServerError`.
- A listing that answers 404 for "there are none" returns an empty list.

## How it is built

```
client.py      CommvaultClient: connection, auth, and the groups
budget.py      the hourly call budget
_base.py       Resource (get / list / query / change), error handling
auth.py        access-token header and renewal
jobs.py  clients.py  subclients.py  sql.py  commcell.py   the groups
models.py      Job, JobDetail, JobAttempt, JobEvent, JobExplanation, JobTask, Reason,
               and Commvault's JSON -> each
```

It sits on `sdk-primer-core` for transport - retries, typed exceptions,
request logging - but does not use its `BaseAPIModel` / `ResourceManager`.
Those model a resource you save, load and find at a path; Commvault's
API is not shaped that way, so each group is written against the
transport directly and shares Commvault's conventions through
`_base.Resource`.

## Adding an endpoint

1. Find the request in Commvault's API documentation, and in cvpysdk if
   the documentation is thin.
2. Add a method to the group it belongs to, using `_get`, `_list`,
   `_query` or `_change` - `_change` for anything that alters the
   CommServe, however harmless it looks.
3. Run it against a real CommServe before relying on it. Nearly every
   endpoint here differed from first expectations in some way: a sort
   flag that meant the opposite, an id that was not unique, a listing
   that left out system databases, a 404 for an empty list.
4. Add it to the tables above, with whether it has been run.

## What is not here, deliberately

Commvault's API has hundreds of endpoints. This covers the ones its
first user (blt, a job-history collector, and its lab) has needed and
tested, not the catalogue. Wrapping the rest
untested would produce an SDK that looks complete and is wrong in ways
only a live CommServe reveals; `cvpysdk` already exists for breadth.
Add groups as work calls for them - restores, schedules, alerts, storage
policies, VM and file-system content are the likely next ones.

What has been done, in which commit, and what is open is in
[`TODO.md`](TODO.md).

## Installing

It is not on PyPI. Depend on a tag of this repository. The repository is
`yoki-py-commvault-sdk`; the package it provides is `commvault-sdk`,
imported as `commvault_sdk`:

```
uv add "commvault-sdk @ git+https://github.com/blueneptune/yoki-py-commvault-sdk.git@v0.1.0"
```

It builds on [`sdk-primer-core`](https://github.com/blueneptune/sdk-primer-core)
for transport, which comes with it.

## Tokens

`TokenSet(access, refresh)` gives the client an access token it can
renew. Renewal replaces both tokens on the CommServe, so pass
`on_token_renew=` a function that stores the new pair somewhere durable
the moment it arrives. If several processes share one token, also pass
`token_reload=` (read the stored pair) and `token_renew_lock=` (a
context manager they all take), so they adopt each other's renewals
instead of trading in a pair that has just been replaced.

## Development

```
uv sync
uv run pytest
uv run ruff check . && uv run ruff format --check .
uv run mypy
```

The tests mock HTTP with respx; none needs a CommServe. Before trusting
a new endpoint, run it against a real one.

## Releases

This SDK is released on the same weekly clock as blt, with the same
branch names. `main` holds only released code; nothing is committed to
it directly.

### The week

| Day | What happens |
|---|---|
| Monday | The previous week's release branch is merged to `main` and tagged. The new week's release branch opens from `main`. |
| Monday - Thursday | Work happens on short branches and is merged into the week's release branch as each piece is finished. |
| Thursday, end of day | Cut-off. What is not merged waits for next week. |
| Friday | The release branch is tested as a whole (see below). No new work goes in - only fixes for what the testing finds. |
| Monday | If Friday's tests passed, release. If not, the release is held until they do, or skipped. A week in which nothing was merged has no release. |

### Names

A release is named for the Monday it is released on: `YYYY.MM.Wnn`,
where `nn` counts the Mondays of that month. Work done in the week of
12 October 2026 goes into `release/2026.10.W03` and is released on
Monday 19 October, the third Monday of October. So the branch to be on
is always the one named for **next** Monday.

| Thing | Name | Example |
|---|---|---|
| Release branch | `release/<release>` | `release/2026.10.W03` |
| Feature branch | `<release>/F/<What_it_does>` | `2026.10.W03/F/Job_details` |
| Bug-fix branch | `<release>/B/<What_it_fixes>` | `2026.10.W03/B/Paging_stops_early` |
| Hotfix branch | `<release>/H/<What_it_fixes>` | `2026.10.W03/H/Token_renewal_loop` |
| Release tag, on `main` | `v<major>.<minor>.<patch>` | `v0.2.0` |

The one difference from blt is the tag. blt is deployed, and its tag is
the week's name. This is a library that other projects pin, so its tag
and the version in `pyproject.toml` say what a caller needs to know
about the change: a new call or option is a minor step (`v0.1.0` to
`v0.2.0`), a week of only fixes is a patch step (`v0.2.0` to `v0.2.1`),
and a change that would break a caller is a major step. The tag's
message names the release branch it came from.

### The loop for one piece of work

```
git checkout release/2026.10.W03 && git pull
git checkout -b 2026.10.W03/F/Job_details
# small commits, each with its tests; run the checks before every one
git push -u origin 2026.10.W03/F/Job_details     # and push often
git checkout release/2026.10.W03
git merge --no-ff 2026.10.W03/F/Job_details
git push
```

- **Commit small and often.** One call, one fix or one finding per
  commit, with its tests in the same commit, and `ruff`, `mypy` and
  `pytest` passing at each one (see Development). Push as you go; the
  branch on GitHub should never be far behind.
- **A new or changed call is run against a real CommServe before its
  commit**, and the commit message says what that showed. That is where
  most of this SDK's corrections have come from.
- **Feature and bug-fix branches** start from the week's release branch
  and merge back into it.
- **Hotfix branches** are for something a user of the SDK cannot wait
  until Monday for. They start from `main`, merge to `main` with a patch
  tag, and are then merged into the open release branch as well.

### Friday's test

On the release branch, all of:

1. `ruff check`, `ruff format --check`, `mypy`, and the unit tests.
2. Every call added or changed that week, run against a real CommServe,
   and the README's tables saying truthfully which are proven.
3. blt's own tests with its `commvault-sdk` source pointed at this
   checkout (`{ path = "../yoki-py-commvault-sdk", editable = true }`),
   so a change that breaks its first user is found before the tag.

If no CommServe is reachable, step 2 has not happened: the calls stay
marked "written, never run" and the tag message says so.

### Releasing, on Monday

```
git checkout main && git pull
git merge --no-ff release/2026.10.W03
# set the new version in pyproject.toml, then:
uv lock
git commit -am "Release v0.2.0 (2026.10.W03)"
git tag -a v0.2.0 -m "2026.10.W03: what changed, in a line or two"
git push origin main v0.2.0
git checkout -b release/2026.10.W04 && git push -u origin release/2026.10.W04
```

The tag has to be pushed by name, as above: a plain `git push` does not
send tags, and blt cannot pin a tag that is not on GitHub.

blt takes the new SDK on its own release branch for the following week:
change the tag for `commvault-sdk` under `[tool.uv.sources]` in its
`pyproject.toml`, run `uv lock`, run blt's tests, commit.

### Tidying up

A branch is deleted once it has been merged, locally and on GitHub:

```
git branch -d 2026.10.W03/F/Job_details
git push origin --delete 2026.10.W03/F/Job_details
```

`git branch -d` refuses to delete a branch that has not been merged
into the branch you are on, which is the check that nothing is lost. A
release branch is deleted the same way after its Monday release; the
tag keeps that release reachable.
