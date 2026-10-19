"""Jobs: listing them, looking one up, and (lab only) controlling them."""

from __future__ import annotations

from collections.abc import Iterator
from datetime import UTC, datetime
from typing import Any

from loguru import logger
from pydantic import ValidationError
from sdk_primer import NotFoundError, ServerError

from ._base import Resource, error_in, json_body
from .models import (
    FailedItem,
    Job,
    JobAttempt,
    JobDetail,
    JobEvent,
    JobExplanation,
    JobTask,
    attempt_from_info,
    detail_from_job_detail,
    event_from_commserv,
    failed_item_from_entry,
    job_from_summary,
    task_from_info,
)

# POST /Jobs "category": 0 = all, 1 = active only, 2 = finished only.
CATEGORY_ALL = 0
CATEGORY_ACTIVE = 1
CATEGORY_FINISHED = 2

# pagingConfig "sortDirection": 0 = oldest first, 1 = newest first
# (checked against a live 11 SP46 CommServe). Oldest first is what makes
# offset paging safe: a job that starts mid-run lands after the last
# page instead of pushing every later job down by one.
_ASCENDING = 0

# Sorts an event with no time before the ones that have one.
_NO_TIME = datetime.fromtimestamp(0, tz=UTC)

# JobEvent.severity: 0 information, 3 minor, 6 major, 9 critical.
SEVERITY_MAJOR = 6


def _problems(exc: ValidationError) -> str:
    return "; ".join(
        f"{'.'.join(str(part) for part in error['loc'])}: {error['msg']}" for error in exc.errors()
    )


def parse_job(entry: dict[str, Any]) -> Job | None:
    """One entry of a job listing as a Job, or None if it can't be read.

    A CommServe holds years of jobs from many agents and versions, and
    one whose summary has a field in an unexpected shape should cost that
    one job, loudly, not the whole collection run."""
    summary = entry.get("jobSummary")
    if summary is None:
        return None
    try:
        return job_from_summary(summary)
    except ValidationError as exc:
        logger.error(
            "Skipping job {}: could not read its summary - {}", summary.get("jobId"), _problems(exc)
        )
        return None


class Jobs(Resource):
    def _listing_body(
        self,
        lookup_seconds: int,
        category: int,
        offset: int,
        limit: int,
        extra_filter: dict[str, Any] | None = None,
    ) -> dict[str, Any]:
        return {
            "scope": 1,
            "category": category,
            "pagingConfig": {
                "sortField": "jobId",
                "sortDirection": _ASCENDING,
                "offset": offset,
                "limit": limit,
            },
            "jobFilter": {
                "completedJobLookupTime": lookup_seconds,
                "showAgedJobs": True,
                "hideAdminJobs": False,
                "clientList": [],
                "jobTypeList": [],
                **(extra_filter or {}),
            },
        }

    def iter_pages(
        self,
        lookup_seconds: int,
        *,
        ended_between: tuple[datetime, datetime] | None = None,
    ) -> Iterator[list[Job]]:
        """Jobs Commvault will report, one page at a time (POST /Jobs).

        By default: all jobs currently active, plus every job that
        finished within the last `lookup_seconds` (aged jobs included).

        With `ended_between`, a slice of history instead: only finished
        jobs whose end time falls in that range, both ends inclusive.
        That is what lets old history be fetched a bounded piece at a
        time rather than in one query for everything.

        Paged oldest first. New jobs get higher ids, so ones started
        while this is running land after the last page instead of
        shifting earlier ones.
        """
        category = CATEGORY_ALL
        extra: dict[str, Any] = {}
        if ended_between is not None:
            # Without "finished only", every slice would also come back
            # with whatever happens to be active right now.
            category = CATEGORY_FINISHED
            extra["endTimeRange"] = {
                "fromTime": int(ended_between[0].timestamp()),
                "toTime": int(ended_between[1].timestamp()),
            }
        page_size = self._client.page_size
        offset = 0
        while True:
            body = self._query(
                "/Jobs", self._listing_body(lookup_seconds, category, offset, page_size, extra)
            )
            entries = body.get("jobs") or []
            jobs = [job for e in entries if (job := parse_job(e)) is not None]
            logger.info(
                "Jobs page offset={} returned {} of {} total",
                offset,
                len(entries),
                body.get("totalRecordsWithoutPaging"),
            )
            if jobs:
                yield jobs
            if len(entries) < page_size:
                return
            offset += page_size

    def sample(
        self,
        lookup_seconds: int,
        limit: int = 5,
        *,
        ended_between: tuple[datetime, datetime] | None = None,
    ) -> tuple[int | None, list[Job]]:
        """A few jobs and the CommServe's count of how many there are, in
        one request - for checking that the listing works at all without
        paging through it."""
        category = CATEGORY_ALL
        extra: dict[str, Any] = {}
        if ended_between is not None:
            category = CATEGORY_FINISHED
            extra["endTimeRange"] = {
                "fromTime": int(ended_between[0].timestamp()),
                "toTime": int(ended_between[1].timestamp()),
            }
        body = self._query("/Jobs", self._listing_body(lookup_seconds, category, 0, limit, extra))
        jobs = [job for e in body.get("jobs") or [] if (job := parse_job(e)) is not None]
        return body.get("totalRecordsWithoutPaging"), jobs

    def active(self, limit: int = 500) -> list[Job]:
        """Jobs that are active right now (one page)."""
        body = self._query("/Jobs", self._listing_body(0, CATEGORY_ACTIVE, 0, limit))
        return [job for e in body.get("jobs") or [] if (job := parse_job(e)) is not None]

    def oldest_start(self, lookup_seconds: int) -> datetime | None:
        """When the oldest finished job the CommServe still has a record
        of started - the point a backfill has nothing left behind. One
        row, oldest first; None if there are no finished jobs at all."""
        body = self._query("/Jobs", self._listing_body(lookup_seconds, CATEGORY_FINISHED, 0, 1))
        for entry in body.get("jobs") or []:
            started = entry.get("jobSummary", {}).get("jobStartTime")
            if started:
                return datetime.fromtimestamp(int(started), tz=UTC)
        return None

    def get(self, job_id: int) -> Job | None:
        """One job's current summary (GET /Job/{id}), or None if the
        CommCell no longer knows the job at all."""
        try:
            body = self._get(f"/Job/{job_id}")
        except NotFoundError:
            return None
        for entry in body.get("jobs") or []:
            job = parse_job(entry)
            if job is not None:
                return job
        return None

    def details(self, job_id: int, *, attempts: bool = False) -> dict[str, Any]:
        """Everything the CommServe reports about one job
        (POST /JobDetails): general, progress and detail info - and, with
        `attempts`, attemptsInfo as well. Empty if the CommCell does not
        know the job; that is a 200 with nothing in it, not a 404."""
        body: dict[str, Any] = {"jobId": job_id}
        if attempts:
            body["showAttempt"] = True
        detail: dict[str, Any] = (
            self._query("/JobDetails", body).get("job", {}).get("jobDetail", {})
        )
        return detail

    def detail(self, job_id: int) -> JobDetail | None:
        """What details() returns, typed (POST /JobDetails): who or what
        started the job, its schedule and plan, and what it scanned,
        skipped and failed on. None if the CommCell does not know the
        job, or - logged - if its details cannot be read."""
        return self._read_detail(job_id, self.details(job_id))

    def _read_detail(self, job_id: int, raw: dict[str, Any]) -> JobDetail | None:
        if not raw:
            return None
        try:
            return detail_from_job_detail(raw)
        except ValidationError as exc:
            logger.error("Could not read the details of job {} - {}", job_id, _problems(exc))
            return None

    def attempts(self, job_id: int) -> list[JobAttempt]:
        """Each attempt at each phase of a job, in the order they ran
        (POST /JobDetails with showAttempt): the phase, how the attempt
        ended and why, when, and what it moved.

        Empty for a job that failed to start - it never reached a phase -
        and for one the CommCell does not know."""
        return self._read_attempts(job_id, self.details(job_id, attempts=True))

    def _read_attempts(self, job_id: int, raw: dict[str, Any]) -> list[JobAttempt]:
        found = []
        for entry in raw.get("attemptsInfo") or []:
            try:
                found.append(attempt_from_info(entry))
            except ValidationError as exc:
                logger.error(
                    "Skipping an attempt of job {}: could not read it - {}", job_id, _problems(exc)
                )
        return found

    def explain(self, job_id: int, *, min_severity: int = SEVERITY_MAJOR) -> JobExplanation | None:
        """Why a job ended as it did, in one answer: its reasons and
        their codes, the attempts that did not complete, and its events
        of `min_severity` and above (major and critical unless told
        otherwise; 0 for all of them).

        Two requests - POST /JobDetails with showAttempt, and
        GET /Events?jobId= - so ask for the jobs that need explaining,
        not for every job collected. None if the CommCell does not know
        the job."""
        raw = self.details(job_id, attempts=True)
        detail = self._read_detail(job_id, raw)
        if detail is None:
            return None
        # The details repeat a code once per line of the reason.
        codes = [code.strip() for code in (detail.pending_reason_code or "").split(",")]
        return JobExplanation(
            job_id=detail.job_id,
            status=detail.status,
            reasons=detail.reasons,
            reason_codes=list(dict.fromkeys(code for code in codes if code)),
            incomplete_attempts=[
                attempt
                for attempt in self._read_attempts(job_id, raw)
                if attempt.status != "Completed"
            ],
            events=[
                event for event in self.events(job_id) if (event.severity or 0) >= min_severity
            ],
            detail=detail,
        )

    def task(self, job_id: int) -> JobTask | None:
        """What a job was asked to do (GET /Job/{id}/TaskDetails): what
        it was pointed at, the level requested and the options it was
        submitted with.

        This is the request Commvault keeps for resubmitting a job, and
        it refuses - in a 200, with the refusal in the body - for jobs
        it will not resubmit. Seen: an interactive job more than 7 days
        old, a job started from the command line, a workflow job. An
        unknown job id gets the "older than 7 days" answer too. All of
        those are None here, with Commvault's words logged at debug, so
        expect None for a good share of jobs: 104 of the lab's 272."""
        body = self._list(f"/Job/{job_id}/TaskDetails")
        info = body.get("taskInfo")
        if not info:
            logger.debug(
                "No task details for job {}: {}", job_id, error_in(body) or "nothing returned"
            )
            return None
        try:
            return task_from_info(job_id, info)
        except ValidationError as exc:
            logger.error("Could not read the task of job {} - {}", job_id, _problems(exc))
            return None

    def failed_items(self, job_id: int) -> list[FailedItem] | None:
        """The files and folders a backup could not read, each with
        Commvault's reason (GET /Job/{id}/FailedItems) - the list behind
        Job.failed_files and Job.failed_folders.

        Empty for a backup with no failures, and also for one whose
        list Commvault no longer keeps: in the lab, backups that ended
        more than about 7 days earlier answered with an empty list
        although their summary still counted a failure. Compare with
        Job.failed_files to tell the two apart.

        None when Commvault will not list failed items for the job at
        all. It answers those with an HTTP 500 ("View failed items
        operation failed."): every job that is not a backup - DR
        backup, data aging, DDB verification, installs - and a job id
        it does not know. sdk_primer logs each of those 500s as an
        error before it reaches here, so ask only about jobs whose
        summary counts a failed file or folder."""
        try:
            body = json_body(self._client.api.get(f"/Job/{job_id}/FailedItems"))
        except ServerError as exc:
            logger.debug("No failed items for job {}: {}", job_id, exc)
            return None
        if body.get("isFailedItemsCSV"):
            # Never seen in the lab; perhaps a list too long to give
            # inline. Whatever did come inline is still returned.
            logger.warning(
                "Commvault offers the failed items of job {} as a CSV, which is not read here",
                job_id,
            )
        found = []
        for entry in body.get("failedItems") or []:
            try:
                found.append(failed_item_from_entry(entry))
            except (KeyError, ValidationError) as exc:
                logger.error(
                    "Skipping a failed item of job {}: could not read it - {!r}", job_id, exc
                )
        return found

    def events(self, job_id: int) -> list[JobEvent]:
        """What the CommServe's event log says about a job
        (GET /Events?jobId=), oldest first: each message's severity,
        code, subsystem and text. Where a failed job's reason is one
        sentence, its events are the steps that led there.

        Many jobs have none - a clean backup logs no events - and so
        does a job the CommCell does not know."""
        found = []
        for entry in self._list(f"/Events?jobId={job_id}").get("commservEvents") or []:
            try:
                found.append(event_from_commserv(entry))
            except ValidationError as exc:
                logger.error(
                    "Skipping an event of job {}: could not read it - {}", job_id, _problems(exc)
                )
        # Commvault lists them newest first, by the time on the machine
        # that reported each one. Ids are given out as events reach the
        # CommServe, which is not always the same order (seen in the
        # lab), so the id only settles events of the same second.
        return sorted(found, key=lambda event: (event.time or _NO_TIME, event.event_id))

    def counts(self, job_id: int) -> dict[str, Any]:
        """The CommServe's own totals for a job: how many objects it
        backed up and how many it skipped. For a SQL Server job an object
        is a database."""
        info = self.details(job_id).get("detailInfo", {})
        return {
            "job_id": job_id,
            "backed_up": info.get("numOfObjects"),
            "skipped": info.get("skippedItems"),
        }

    # -- changes: these alter running work on the CommServe ---------------

    def suspend(self, job_id: int) -> None:
        self._change("POST", f"/Job/{job_id}/action/pause")

    def resume(self, job_id: int) -> None:
        self._change("POST", f"/Job/{job_id}/action/resume")

    def kill(self, job_id: int) -> None:
        self._change("POST", f"/Job/{job_id}/action/kill")
