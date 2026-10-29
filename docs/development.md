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

While blt and the yoki SDKs are still being built, there is no weekly
release train: it was paused on 2026-10-29, and comes back once
something outside the project depends on these releases. Work is merged
to `main` as soon as it is finished and CI passes, and this SDK gets a
tag when a project needs what changed.

### The loop for one piece of work

```
git checkout main && git pull
git checkout -b F/What_it_does
# small commits, each with its tests; run the checks before every one
git push -u origin F/What_it_does        # and push often: CI runs on every push
git checkout main && git pull
git merge --no-ff F/What_it_does
git push
git branch -d F/What_it_does && git push origin --delete F/What_it_does
```

| Thing | Name | Example |
|---|---|---|
| Feature branch | `F/<What_it_does>` | `F/Job_details` |
| Bug-fix branch | `B/<What_it_fixes>` | `B/Paging_stops_early` |
| Release tag, on `main` | `v<major>.<minor>.<patch>` | `v0.2.0` |

- **Commit small and often.** One change or one fix per commit, with
  its tests in the same commit, and the checks passing at each one.
  Push as you go; the branch on GitHub should never be far behind.
- **A new or changed call is run against a real CommServe before its
  commit**, and the commit message says what that showed. That is where
  most of this SDK's corrections have come from.
- **`main` always passes.** Merge a branch only once CI is green on it.
- **Delete a branch once it is merged**, locally and on GitHub.
  `git branch -d` refuses a branch that is not merged, which is the
  check that nothing is lost.

### Tagging a release

When a project needs a change that is on `main`, check `main` first:

1. `ruff check`, `ruff format --check`, `mypy`, and the unit tests.
2. Every call added or changed since the last tag, run against a real CommServe,
   and the README's tables saying truthfully which are proven.
3. blt's own tests with its `commvault-sdk` source pointed at this
   checkout (`{ path = "../yoki-py-commvault-sdk", editable = true }`),
   so a change that breaks its first user is found before the tag.

If no CommServe is reachable, step 2 has not happened: the calls stay
marked "written, never run" and the tag message says so.

Then set the version and tag it:

```
git checkout -b B/Version_0_3_0
# version in pyproject.toml, without the v; then:
uv lock
git commit -am "Version 0.3.0"
git checkout main && git merge --no-ff B/Version_0_3_0 && git push
git tag -a v0.3.0 -m "What changed, in a line or two"
git push origin v0.3.0
```

The version and `uv lock` go in the same commit: a version set without
it leaves the lockfile behind. The tag has to be pushed by name, as
above: a plain `git push` does not send tags, and nothing can pin a tag
that is not on GitHub. A new call or option is a minor step (`v0.1.0`
to `v0.2.0`), only fixes a patch step (`v0.2.0` to `v0.2.1`), and a
change that would break a caller a major step.

blt, yoki-commvault-lab and the other projects that use it then take the new tag: change the tag for `commvault-sdk` under
`[tool.uv.sources]` in their `pyproject.toml`, run `uv lock`, run their
tests, commit. Projects pin tags. A pin to a commit is only for a
change still on its way, and is replaced by the tag before that
project's own branch is merged.
