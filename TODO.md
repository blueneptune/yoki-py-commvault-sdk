# TODO

What has been worked on and what is open, by piece of work. A done item
is struck through and names the commit it was done in and the release
branch that commit is on; `git show <commit>` has the full account,
including what running it against a real CommServe showed.

"Lab" below is the eval CommServe, software 11 SP46.30.

## Job detail

Why a job failed, beyond the one sentence in its summary. Items 1-4 are
one piece of work, on branch `2026.10.W03/F/Job_details`; 5-7 each need
a look at what the CommServe really returns first, so each gets a
branch of its own.

| | Item | Commit | Release |
|---|---|---|---|
| ~~0a~~ | ~~`jobs.attempts()`~~ | `51e3cea` | 2026.10.W03 |
| ~~0b~~ | ~~`jobs.events()`~~ | `affd9db` | 2026.10.W03 |
| ~~1~~ | ~~Failure fields on `Job`~~ | `49888ae` | 2026.10.W03 |
| ~~2~~ | ~~Typed `jobs.detail()`~~ | `a99db21` | 2026.10.W03 |
| ~~3~~ | ~~Reasons split into message, source and process~~ | `714067d` | 2026.10.W03 |
| 4 | `jobs.explain()` | | |
| 5 | `jobs.task()` | | |
| 6 | Failed files for a job | | |
| 7 | Detail of a running job | | |

0a. ~~**`jobs.attempts(job_id)`** - each attempt at each phase of a
    job, as a typed `JobAttempt`.~~ **Done 2026-10-13**, `51e3cea`.
    `POST /JobDetails` with `showAttempt`. Run over all 258 lab jobs. A
    job that failed to start has no attempts at all.

0b. ~~**`jobs.events(job_id)`** - the CommServe's event log for a job,
    as typed `JobEvent`, oldest first.~~ **Done 2026-10-13**, `affd9db`.
    `GET /Events?jobId=`. Run over all 258 lab jobs, 191 events. Event
    ids do not follow event time, so the order is by time.
    - Still unknown: whether the CommServe cuts short a job with a
      great many events. The most the lab has for one job is 14.

1. ~~**Failure fields on `Job`** - read what the job summary already
   carries about a failure, at no extra request.~~ **Done 2026-10-13**,
   `49888ae`. Added `pending_reason_code` (Commvault's code for the
   reason, e.g. `19:1132`, the thing to group failures by) and
   `failed_folders`. Run over all 270 lab jobs.
   - Left out because they were 0 or blank on every finished job:
     `errorType`, `currentPhase`, `currentPhaseName`,
     `attemptStartTime`. The phase fields may matter for a running job
     (item 7).
   - Left in `raw`, meaning unknown: `jobSubmitErrorCode`, which is 8 on
     42 of the 43 lab jobs that failed to start.
   - For blt to use the code: a column for it and a line in its
     `source.py`, once it pins a tag that has this.

2. ~~**Typed `jobs.detail(job_id)`** - the rest of `POST /JobDetails` as
   a `JobDetail`: who or what started the job, its schedule and plan,
   ids as well as names, and what it scanned, skipped and failed
   on.~~ **Done 2026-10-13**, `a99db21`. Run over all 270 lab jobs.
   - Unproven: `encrypted` was "No" on every lab job that had it, so
     reading "Yes" as `True` is by inference.
   - Not typed, still in `raw`: throughput figures (units not
     established), deduplication store, and the per-kind sections
     (`mssqlJob`, an install job's `clientStatusInfo`).

3. ~~**Split the reason text** - Commvault ends each reason with
   `<br/>Source: X, Process: Y` and puts several in one field.~~
   **Done 2026-10-13**, `714067d`. `split_reason()` and a `.reasons`
   property on `Job`, `JobDetail` and `JobAttempt`, giving
   `Reason(text, source, process)`. Run over all 272 lab jobs and their
   attempts; every reason split and rebuilt exactly.

4. **`jobs.explain(job_id)`** - one call that gathers the summary's
   reason and code, the attempts that did not complete, and the major
   and critical events into a single answer to "why did this fail".
   Two requests per job, on top of calls already proven. To decide:
   what it returns (a small typed object, not text), and whether events
   below "major" are ever wanted.

5. **`jobs.task(job_id)`** - the options a job was submitted with:
   backup level, associations (`GET /Job/{id}/TaskDetails`). Seen
   working for most lab jobs. Jobs started from the command line answer
   200 with an error in the body ("Resubmit operation is not supported
   ..."), which has to become an empty result or a clear error, not a
   crash.

6. **Failed files for a job** - the individual files and folders a
   backup could not read. Not looked at yet. cvpysdk points at
   `GET /Job/{id}/AdvancedDetails?infoType=`. The lab has 11 jobs with
   a scan failure to try it on.

7. **Detail of a running job** - current phase, progress, the reason it
   is waiting. Nothing was active in the lab when the calls above were
   run, so none of them is proven on a running job. Needs a backup
   started in the lab first, which is a change to the CommServe and so
   goes through blt's `lab/cvlab.py`, not through a read-only client.

## Further groups

8. **`cv.events`** - the CommServe's event log across the CommCell, by
   time range and severity, not one job at a time. A new group, so a
   branch of its own. `GET /Events` is proven only with `jobId=`.

9. The groups the README names as likely next - restores, schedules,
   alerts, storage policies, VM and file-system content - and the
   inventory needs on blt's list: bulk or paged listings of clients and
   subclients, workloads other than SQL Server.

## Housekeeping

10. **`F/Release_process_docs`** (local and on GitHub) describes this
    SDK as not being on the weekly clock. It was never merged and is
    replaced by the README's "Releases" section (`bcbab82`). To delete.

11. **blt's README**, "The SDKs", still says the SDKs are not on the
    weekly clock. To correct in `blt-v5-poc`.

12. **First release from the weekly branch**, Monday 2026-10-19: the
    version in `pyproject.toml` and the tag. Everything above is new
    calls and fields with nothing removed, so `v0.2.0`.
