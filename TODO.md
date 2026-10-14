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
| ~~4~~ | ~~`jobs.explain()`~~ | `b4e0b2c` | 2026.10.W03 |
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

4. ~~**`jobs.explain(job_id)`** - one call that gathers a job's
   reasons and codes, the attempts that did not complete, and its major
   and critical events into a single answer to "why did this
   fail".~~ **Done 2026-10-13**, `b4e0b2c`. Returns a typed
   `JobExplanation`; two requests per job. Run over all 272 lab jobs.
   Every job that did not end well has something to show, and 9 of the
   207 completed jobs turned out not to be clean: they completed after
   an attempt that was suspended, interrupted or had failed.
   - With this the branch `2026.10.W03/F/Job_details` is complete and
     ready to merge into `release/2026.10.W03`.

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

## Events

8. **`cv.events`** - the CommServe's event log across the CommCell, by
   time range and severity, not one job at a time. A new group, so a
   branch of its own. `GET /Events` is proven only with `jobId=`.

## Configuration management

Reading how a CommCell is set up, and changing it. Requested
2026-10-13; nothing here is started. Each numbered item is a branch of
its own.

Two rules from the rest of the SDK apply to all of it:

- **Reads first.** For each area, the listing and the single-item read
  come before any change, typed where it is clear which fields matter.
  A read of the whole configuration is useful on its own - for an
  inventory, and for seeing what differs between two CommCells or
  between today and last week.
- **Every change goes through `_change`**, so it is refused unless the
  client was built with `allow_changes=True`, is never retried, and is
  run in the lab before it is called proven. Deletes are run in the lab
  against things created for the purpose.

What exists today is in the README's tables; in short: `storage.disk()`
lists disk pools; `plans.list()` and `plans.ids()`; subclients can be
listed, read, created, given a plan and backed up; clients and
instances can be listed and read; credentials can be listed by name and
created. `subclients.delete()` and `clients.delete()` are written and
have never been run.

9. **Storage.** Today: a listing of disk pools only.
   - Read: one disk pool in full (`GET /V4/Storage/Disk/{id}`: its
     backup locations, media agents, capacity, deduplication); cloud
     storage (`/V4/Storage/Cloud`); tape and HyperScale if present;
     media agents and libraries; deduplication stores and their state.
   - Change: create a disk or cloud pool, add a backup location, delete
     a pool.
   - The lab has one disk pool and two deduplication stores to read.

10. **Plans.** Today: a summary listing, and name to id.
    - Read: one plan in full (`GET /V4/ServerPlan/{id}`): its RPO and
      backup windows, its copies with storage and retention for each,
      what is associated with it. Other kinds of plan as they are met.
    - Change: create a server plan, change its RPO or retention, add a
      copy, delete a plan.
    - Typed, because "what is this plan's retention" is the question
      asked most.

11. **Storage policies and copies.** The older model that plans sit on
    top of, and what jobs still name (`Job.storage_policy`).
    - Read: the policies, each one's copies, a copy's retention,
      storage and schedule for auxiliary copy.
    - Change: only if something needs it that a plan cannot do. On a
      CommCell run by plans, changing the policy underneath one is
      usually a mistake.

12. **Subclients.** Today: list, read, create, set a plan, start a
    backup; delete unrun.
    - Read: a typed subclient - its content, filters and exceptions,
      plan, whether backup is enabled, last backup. Listing across a
      whole CommCell without one request per client, which blt's
      inventory needs before thousands of clients.
    - Change: replace or add to content, set filters, enable and
      disable backup, rename; run `delete()` in the lab and mark it
      proven.
    - Backup sets with it: list, create, delete.

13. **Clients and client groups.** Today: list, find, agents; delete
    unrun.
    - Read: one client's properties (version, OS, time zone, whether
      backup and restore activity are enabled, when it last
      checked in); client groups and their members, including the
      rules of automatic groups.
    - Change: enable and disable activity on a client, retire a client,
      create a group and change its members; run `delete()` in the lab.

14. **Instances and agents.** Today: list, read, update; SQL Server
    databases and credential.
    - Read: typed instances for the agents in use; what the SQL
      instance settings are. Other database agents as they are needed.
    - Change: create and delete an instance.

15. **Schedules and schedule policies.** Nothing today.
    - Read: schedule policies and what they are associated with; the
      schedules on a subclient or client; when each next runs.
      `JobDetail.schedule_name` and `schedule_policy` already name the
      schedule a job came from; this is the other end of that.
    - Change: enable and disable a schedule, create one, change its
      pattern, delete it.

16. **Credentials.** Today: names, and create.
    - Read: a credential's type, owner and what uses it (never the
      secret, which the API does not return).
    - Change: update a password, delete a credential.

17. **Alerts.** Nothing today.
    - Read: the alert definitions, who they notify and what they watch;
      triggered alerts.
    - Change: enable and disable an alert, create one, delete one.

18. **Users, roles and access.** Nothing today.
    - Read: users, user groups, roles and what each is associated
      with - enough to answer "who can change this CommCell".
    - Change: last, if at all. It is the area where a mistake does the
      most harm and where Command Center is the safer tool.

19. **The configuration as one document.** Once the reads above exist:
    one call that gathers storage, plans, policies, schedules, client
    groups and subclients into a single structure that can be saved and
    compared - to another CommCell, or to the same one earlier. Reads
    only. To decide: what is left out so that two snapshots of an
    unchanged CommCell are equal (counters, last-run times).

Not known for any of it: how far Commvault Cloud allows these calls.
The SaaS side has not been run at all, and several of these (storage,
media agents) are managed by Commvault there.

## Further groups

20. The other groups the README names as likely next - restores, VM and
    file-system content - and workloads other than SQL Server for blt's
    inventory.

## Housekeeping

21. **`F/Release_process_docs`** (local and on GitHub) describes this
    SDK as not being on the weekly clock. It was never merged and is
    replaced by the README's "Releases" section (`bcbab82`). To delete.

22. **blt's README**, "The SDKs", still says the SDKs are not on the
    weekly clock. To correct in `blt-v5-poc`.

23. **First release from the weekly branch**, Monday 2026-10-19: the
    version in `pyproject.toml` and the tag. Everything above is new
    calls and fields with nothing removed, so `v0.2.0`.
