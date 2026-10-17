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

**[The usage guide](docs/guide.md)** shows how to do the things the
SDK is for: connecting and keeping a renewed token, collecting jobs,
finding out why they failed, inventory, changes, Commvault Cloud, errors.
This README lists what is in it. Working on the SDK itself - how it is
built, adding a call, checks and releases - is
[docs/development.md](docs/development.md); what is done and open is
[TODO.md](TODO.md).

## Installing

It is not on PyPI. Depend on a tag of this repository (the newest is
the one to use; tags are listed on GitHub). The repository is
`yoki-py-commvault-sdk`; the package it provides is `commvault-sdk`,
imported as `commvault_sdk`:

```
uv add "commvault-sdk @ git+https://github.com/blueneptune/yoki-py-commvault-sdk.git@v0.2.0"
```

It builds on [`sdk-primer-core`](https://github.com/blueneptune/sdk-primer-core)
for transport, which comes with it. More in the guide,
[Installing](docs/guide.md#installing).

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
| `detail(job_id)` | `POST /JobDetails` | proven, on all 270 lab jobs, and on two running ones |
| `attempts(job_id)`, `details(job_id, attempts=True)` | `POST /JobDetails` (showAttempt) | proven, on all 258 lab jobs |
| `events(job_id)` | `GET /Events?jobId=` | proven, on all 258 lab jobs |
| `explain(job_id, min_severity=)` | `POST /JobDetails` (showAttempt) + `GET /Events?jobId=` | proven, on all 272 lab jobs |
| `task(job_id)` | `GET /Job/{id}/TaskDetails` | proven, on all 272 lab jobs; answers for 168 |
| `failed_items(job_id)` | `GET /Job/{id}/FailedItems` | proven, on all 286 lab jobs; scan failures only |
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

### `cv.users`, `cv.access_tokens`

Command Center shows each user only their own tokens; the API lists
them per user, and an administrator may ask for anyone's: `everyone()`
shows them all (proven 2026-10-17, as Admin, a token of another user's).

| Call | Endpoint | |
|---|---|---|
| `users.list()`, `users.find(name)` | `GET /User` | proven |
| `access_tokens.list(user_id=)` | `GET /V4/AccessToken?userId=` | proven, for another user's tokens too |
| `access_tokens.everyone()`, `get(token_id)` | `GET /User` + the above per user | proven |
| `access_tokens.create(name, ...)` *change* | `POST /V4/AccessToken` | written, **never run** |
| `access_tokens.update(token_id, ...)` *change* | `PUT /V4/AccessToken/{id}` | written, **never run** |
| `access_tokens.delete(token_id)` *change* | `DELETE /V4/AccessToken/{id}` | written, **never run** |
| `access_tokens.rotate(token)` *change* | create, then delete the old one | written, **never run** |

The same from a shell: `commvault-tokens list | rotate | delete` (see
`src/commvault_sdk/cli.py`). It signs in with a username and password,
so it never renews - and so never invalidates - a token pair that some
other tool holds.

Authentication (`POST /Login`, `POST /V4/AccessToken/Renew`) is handled
underneath, in `auth.py` and `client.py`.

**How far "proven" goes.** Every read call marked proven has been run
through this code against a CommServe (software 11 SP46), and the job
listing against production CommServes at 60,000+ jobs. Of the change
calls, starting a backup and suspending, resuming and killing a job have
been run through it; the rest send requests that were proven before
this code was a library, checked here by unit tests. Nothing has been
run against Commvault Cloud.

## What is not here, deliberately

Commvault's API has hundreds of endpoints. This covers the ones its
first user (blt, a job-history collector, and its lab) has needed and
tested, not the catalogue. Wrapping the rest
untested would produce an SDK that looks complete and is wrong in ways
only a live CommServe reveals; `cvpysdk` already exists for breadth.
Add groups as work calls for them - restores, schedules, alerts, storage
policies, VM and file-system content are the likely next ones.
