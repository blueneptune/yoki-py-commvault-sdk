# Developing the Commvault SDK

For working on the SDK itself: how it is built, how to add a call, the
checks, and the weekly release cadence. For using it, see
[guide.md](guide.md).

## How it is built

```
client.py      CommvaultClient: connection, auth, and the groups
budget.py      the hourly call budget
_base.py       Resource (get / list / query / change), error handling
auth.py        access-token header and renewal
jobs.py  clients.py  subclients.py  sql.py  commcell.py   the groups
models.py      Job, JobDetail, JobAttempt, JobEvent, JobExplanation, JobTask,
               FailedItem, Reason,
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
4. Add it to the README's tables, with whether it has been run, and to
   [guide.md](guide.md) if it changes how something is done.

## Checks

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
  `pytest` passing at each one (see Checks). Push as you go; the
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

By Thursday's cut-off, the release branch already carries the new
version: `version` in `pyproject.toml` set to the coming tag without its
`v`, then `uv lock`, on an `H/` branch like any other change. Friday
then tests what Monday ships, and the tag and the package agree.

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
git merge --no-ff release/2026.10.W03 -m "Release v0.2.0 (2026.10.W03)"
git tag -a v0.2.0 -m "2026.10.W03: what changed, in a line or two"
git push origin main v0.2.0
git checkout -b release/2026.10.W04 && git push -u origin release/2026.10.W04
```

The tag has to be pushed by name, as above: a plain `git push` does not
send tags, and blt cannot pin a tag that is not on GitHub.

blt takes the new SDK on its own release branch for the following week:
change the tag for `commvault-sdk` under `[tool.uv.sources]` in its
`pyproject.toml`, run `uv lock`, run blt's tests, commit.

The same Monday, the branches of any release that went out a month or
more ago come off GitHub (see Tidying up).

### Tidying up

A branch is deleted locally once it has been merged, and from GitHub a
month after the release it went out in.

Locally, straight after the merge:

```
git branch -d 2026.10.W03/F/Job_details
```

`git branch -d` refuses to delete a branch that has not been merged
into the branch you are on, which is the check that nothing is lost. A
release branch is deleted locally the same way after its Monday
release; the tag keeps that release reachable.

On GitHub, each release's branches - its work branches and the release
branch itself - stay up for a month after that release, so a week's
work can still be looked at branch by branch while it is recent. They
come off on the first release Monday a month or more after the
release: `2026.10.W03`, released Monday 19 October, has its branches
deleted from GitHub on Monday 23 November, as part of releasing
`2026.11.W04`.

```
git fetch --prune
git branch -r --list 'origin/2026.10.W03/*' 'origin/release/2026.10.W03'
git push origin --delete 2026.10.W03/F/Job_details 2026.10.W03/F/Job_task_details ... release/2026.10.W03
git fetch --prune
```

Only a release that has been tagged is tidied this way. A branch that
was never merged stays until someone decides about it.
