"""Commvault's own job JSON, and the typed Job the SDK returns.

Field names follow the `jobSummary` object the REST API returns from
POST /Jobs and GET /Job/{id} (the same one cvpysdk's JobController
reads). Everything except jobId is optional: which fields are present
varies by job type and CommServe version, and the untouched summary is
kept in Job.raw regardless.

JobAttempt is one entry of `attemptsInfo`, which POST /JobDetails adds
to its answer when asked with showAttempt. JobEvent is one entry of
`commservEvents` from GET /Events. JobDetail is the `jobDetail` object
of POST /JobDetails. JobExplanation is the SDK's own: those three put
together for one job. JobTask is the `taskInfo` object of
GET /Job/{id}/TaskDetails.
"""

from __future__ import annotations

import re
from datetime import UTC, datetime
from typing import Any

from pydantic import AwareDatetime, BaseModel, ConfigDict, Field


class Reason(BaseModel):
    """One reason Commvault gave for a job being delayed, failed or
    killed, with the ending it puts on each taken off: the message, the
    machine that reported it and the process on that machine."""

    text: str
    source: str | None = None
    process: str | None = None


# How every reason seen so far ends. A reason field can hold several,
# one after another, each with its own ending.
_REASON_ENDING = re.compile(r"<br/>Source: (?P<source>[^\n]*?), Process: (?P<process>[^\n]*)\n?")


def split_reason(text: str | None) -> list[Reason]:
    """Commvault's reason text as the reasons in it.

    A reason arrives as "Killed by Admin.<br/>Source: CS, Process:
    JobManager", and a job that was held up more than once has several
    in the one field. Text with no such ending comes back whole, as one
    reason with no source or process, so nothing is ever dropped."""
    reasons = []
    rest_from = 0
    for ending in _REASON_ENDING.finditer(text or ""):
        message = (text or "")[rest_from : ending.start()].strip()
        reasons.append(
            Reason(
                text=message,
                source=ending["source"].strip() or None,
                process=ending["process"].strip() or None,
            )
        )
        rest_from = ending.end()
    rest = (text or "")[rest_from:].strip()
    if rest:
        reasons.append(Reason(text=rest))
    return reasons


class Job(BaseModel):
    """One job as the CommServe reports it: the fields most callers want,
    typed, with times as real timestamps - and `raw`, Commvault's
    jobSummary untouched, for everything else."""

    job_id: int
    status: str
    job_type: str | None = None
    operation: str | None = None
    backup_level: str | None = None
    app_type: str | None = None
    client_id: int | None = None
    client_name: str | None = None
    subclient_name: str | None = None
    backupset_name: str | None = None
    instance_name: str | None = None
    storage_policy: str | None = None
    percent_complete: float | None = None
    start_time: AwareDatetime | None = None
    end_time: AwareDatetime | None = None
    last_update_time: AwareDatetime | None = None
    # Commvault's own figure. Not wall-clock time: it stops while a job
    # is suspended or waiting.
    elapsed_seconds: int | None = None
    size_of_application: int | None = None
    size_of_media: int | None = None
    total_files: int | None = None
    failed_files: int | None = None
    failed_folders: int | None = None
    pending_reason: str | None = None
    # Commvault's code for pending_reason, e.g. "19:1132" - the same
    # form as JobEvent.code. It names the kind of failure where the
    # text names the client, path and job it happened to, so it is the
    # thing to group failures by. None when there is no reason.
    pending_reason_code: str | None = None
    is_aged: bool | None = None
    raw: dict[str, Any] = Field(default_factory=dict)

    @property
    def reasons(self) -> list[Reason]:
        """pending_reason, split into message, source and process."""
        return split_reason(self.pending_reason)


class _Subclient(BaseModel):
    model_config = ConfigDict(extra="ignore", populate_by_name=True)

    client_id: int | None = Field(default=None, alias="clientId")
    client_name: str | None = Field(default=None, alias="clientName")
    subclient_name: str | None = Field(default=None, alias="subclientName")
    backupset_name: str | None = Field(default=None, alias="backupsetName")
    instance_name: str | None = Field(default=None, alias="instanceName")


class _StoragePolicy(BaseModel):
    model_config = ConfigDict(extra="ignore", populate_by_name=True)

    name: str | None = Field(default=None, alias="storagePolicyName")


class JobSummary(BaseModel):
    model_config = ConfigDict(extra="ignore", populate_by_name=True)

    job_id: int = Field(alias="jobId")
    status: str = "Unknown"
    job_type: str | None = Field(default=None, alias="jobType")
    operation: str | None = Field(default=None, alias="localizedOperationName")
    backup_level: str | None = Field(default=None, alias="backupLevelName")
    app_type: str | None = Field(default=None, alias="appTypeName")
    percent_complete: float | None = Field(default=None, alias="percentComplete")
    job_start_time: int | None = Field(default=None, alias="jobStartTime")
    job_end_time: int | None = Field(default=None, alias="jobEndTime")
    last_update_time: int | None = Field(default=None, alias="lastUpdateTime")
    job_elapsed_time: int | None = Field(default=None, alias="jobElapsedTime")
    size_of_application: int | None = Field(default=None, alias="sizeOfApplication")
    size_of_media: int | None = Field(default=None, alias="sizeOfMediaOnDisk")
    total_files: int | None = Field(default=None, alias="totalNumOfFiles")
    failed_files: int | None = Field(default=None, alias="totalFailedFiles")
    failed_folders: int | None = Field(default=None, alias="totalFailedFolders")
    pending_reason: str | None = Field(default=None, alias="pendingReason")
    pending_reason_code: str | None = Field(default=None, alias="pendingReasonErrorCode")
    is_aged: bool | None = Field(default=None, alias="isAged")
    dest_client_name: str | None = Field(default=None, alias="destClientName")
    subclient: _Subclient = Field(default_factory=_Subclient)
    storage_policy: _StoragePolicy = Field(default_factory=_StoragePolicy, alias="storagePolicy")


class JobAttempt(BaseModel):
    """One attempt at one phase of a job. A backup that ran cleanly has
    one per phase (Scan, Backup, Archive Index); a phase that was
    interrupted and run again has one for each time it was tried.

    `failure_reason` is Commvault's text, with its "<br/>Source: ...,
    Process: ..." ending left on. It is not cleared when the job gets
    going again: a later attempt that completed can still carry the
    reason an earlier one stopped, so read it together with `status`."""

    phase: int | None = None
    phase_name: str | None = None
    status: str
    failure_reason: str | None = None
    start_time: AwareDatetime | None = None
    end_time: AwareDatetime | None = None
    elapsed_seconds: int | None = None
    objects: int | None = None
    folders: int | None = None
    failures: int | None = None
    skipped: int | None = None
    uncompressed_bytes: int | None = None
    compressed_bytes: int | None = None
    # What reached storage, after deduplication.
    data_written: int | None = None
    streams: int | None = None
    access_node: str | None = None
    media_agent: str | None = None
    library: str | None = None
    storage_policy: str | None = None
    copy_name: str | None = None
    raw: dict[str, Any] = Field(default_factory=dict)

    @property
    def reasons(self) -> list[Reason]:
        """failure_reason, split into message, source and process."""
        return split_reason(self.failure_reason)


class _MediaAgent(BaseModel):
    model_config = ConfigDict(extra="ignore", populate_by_name=True)

    name: str | None = Field(default=None, alias="mediaAgentName")


class _Library(BaseModel):
    model_config = ConfigDict(extra="ignore", populate_by_name=True)

    name: str | None = Field(default=None, alias="libraryName")


class _Copy(BaseModel):
    model_config = ConfigDict(extra="ignore", populate_by_name=True)

    name: str | None = Field(default=None, alias="copyName")


class AttemptInfo(BaseModel):
    model_config = ConfigDict(extra="ignore", populate_by_name=True)

    phase: int | None = None
    phase_name: str | None = Field(default=None, alias="phaseName")
    status: str = "Unknown"
    failure_reason: str | None = Field(default=None, alias="failureReason")
    # Epoch seconds, sent as strings.
    start_time: int | None = Field(default=None, alias="startTime")
    end_time: int | None = Field(default=None, alias="endTime")
    elapsed_time: int | None = Field(default=None, alias="elapsedTime")
    num_objects: int | None = Field(default=None, alias="numObjects")
    num_folders: int | None = Field(default=None, alias="numFolders")
    num_failures: int | None = Field(default=None, alias="numFailures")
    num_skipped: int | None = Field(default=None, alias="numSkipped")
    uncomp_bytes: int | None = Field(default=None, alias="uncompBytes")
    comp_bytes: int | None = Field(default=None, alias="compBytes")
    data_written: int | None = Field(default=None, alias="dataWritten")
    max_streams_used: int | None = Field(default=None, alias="maxStreamsUsed")
    access_node_client_name: str | None = Field(default=None, alias="accessNodeClientName")
    media_agent: _MediaAgent = Field(default_factory=_MediaAgent, alias="mediaAgent")
    library: _Library = Field(default_factory=_Library)
    storage_policy: _StoragePolicy = Field(default_factory=_StoragePolicy, alias="storagePolicy")
    copy_: _Copy = Field(default_factory=_Copy, alias="copy")


class JobEvent(BaseModel):
    """One line of the CommServe's event log that belongs to a job - what
    Command Center shows under the job's Events tab.

    `severity` is Commvault's number. Seen: 0 (information), 3 (minor),
    6 (major) and 9 (critical). `code` is the "17:158" form that
    Commvault's documentation and support use to identify a message."""

    event_id: int
    job_id: int | None = None
    time: AwareDatetime | None = None
    severity: int | None = None
    code: str | None = None
    subsystem: str | None = None
    description: str | None = None
    client_id: int | None = None
    client_name: str | None = None
    raw: dict[str, Any] = Field(default_factory=dict)


class _EventClient(BaseModel):
    model_config = ConfigDict(extra="ignore", populate_by_name=True)

    client_id: int | None = Field(default=None, alias="clientId")
    client_name: str | None = Field(default=None, alias="clientName")


class CommservEvent(BaseModel):
    model_config = ConfigDict(extra="ignore", populate_by_name=True)

    event_id: int = Field(alias="id")
    job_id: int | None = Field(default=None, alias="jobId")
    time_source: int | None = Field(default=None, alias="timeSource")
    severity: int | None = None
    event_code_string: str | None = Field(default=None, alias="eventCodeString")
    subsystem: str | None = None
    description: str | None = None
    client: _EventClient = Field(default_factory=_EventClient, alias="clientEntity")


class JobDetail(BaseModel):
    """What POST /JobDetails knows about a job that its summary does
    not: who or what started it, how it was set to run, and what it
    found, skipped and failed on. The fields a summary already has
    (status, times, sizes, the reason) are here too, so a JobDetail can
    be read on its own; `raw` is Commvault's whole jobDetail.

    Which fields are filled varies by kind of job: the scan and failure
    counts are there for backups, not for administrative jobs."""

    job_id: int
    status: str
    operation: str | None = None
    # "Full", "Incremental", "Differential", "Transaction Log".
    backup_type: str | None = None
    # The user name, and "Scheduled", "Interactive" or "System".
    started_by: str | None = None
    started_from: str | None = None
    # What scheduled it. Jobs scheduled by a plan have the plan's name
    # (or its schedule policy's) in schedule_policy and no
    # schedule_name; a schedule of its own has a schedule_name.
    schedule_name: str | None = None
    schedule_policy: str | None = None
    plan: str | None = None
    # Named here ("CV_DEFAULT") for some administrative jobs whose
    # summary leaves it blank.
    storage_policy: str | None = None
    priority: int | None = None
    client_id: int | None = None
    client_name: str | None = None
    app_name: str | None = None
    instance_id: int | None = None
    instance_name: str | None = None
    backupset_name: str | None = None
    subclient_id: int | None = None
    subclient_name: str | None = None
    encrypted: bool | None = None
    # Where compression was done: "Client", "Storage Policy" or "Off".
    software_compression: str | None = None
    pending_reason: str | None = None
    # Unlike Job.pending_reason_code this repeats the code once for each
    # line of the reason: "19:601, 19:601, 19:601".
    pending_reason_code: str | None = None
    start_time: AwareDatetime | None = None
    end_time: AwareDatetime | None = None
    # Commvault's figure, and it is end minus start by the CommServe's
    # clock: a job that ran across a clock change can have a negative one.
    elapsed_seconds: int | None = None
    # For a SQL Server job an object is a database.
    objects: int | None = None
    skipped: int | None = None
    scanned_files: int | None = None
    scanned_folders: int | None = None
    scan_failed_files: int | None = None
    scan_failed_folders: int | None = None
    backup_failed_files: int | None = None
    backup_failed_folders: int | None = None
    # 0 here for a CommServe DR backup and a software download, whose
    # summaries do have the size: for those, trust Job.
    size_of_application: int | None = None
    compressed_bytes: int | None = None
    size_of_media: int | None = None
    savings_percent: float | None = None
    streams: int | None = None
    transfer_seconds: int | None = None
    raw: dict[str, Any] = Field(default_factory=dict)

    @property
    def reasons(self) -> list[Reason]:
        """pending_reason, split into message, source and process."""
        return split_reason(self.pending_reason)


class JobExplanation(BaseModel):
    """Why a job ended as it did, gathered from everything Commvault
    says about it: the reasons on the job, the attempts that did not
    complete, and the events serious enough to matter.

    Any of the three can be empty. A job that failed to start never
    reached a phase, so it has no attempts and its reasons and events
    are all there is; a job that ran cleanly has none of the three,
    which `clean` says in one word."""

    job_id: int
    status: str
    reasons: list[Reason] = Field(default_factory=list)
    # Commvault's codes for those reasons, each once, in order.
    reason_codes: list[str] = Field(default_factory=list)
    # Every attempt that ended as anything but "Completed": failed,
    # killed, interrupted, completed with errors.
    incomplete_attempts: list[JobAttempt] = Field(default_factory=list)
    # Events at or above the severity asked for, oldest first.
    events: list[JobEvent] = Field(default_factory=list)
    detail: JobDetail

    @property
    def clean(self) -> bool:
        """Nothing to explain: no reason, no attempt that fell short and
        no serious event."""
        return not (self.reasons or self.incomplete_attempts or self.events)


# backupOpts.backupLevel in a job's task, as matched against what the
# lab's jobs ran as. Other numbers exist (a synthetic full, for one)
# and have not been seen; they give a code with no name.
_REQUESTED_LEVELS = {1: "Full", 2: "Incremental", 3: "Differential", 6: "Transaction Log"}


class JobTask(BaseModel):
    """What a job was asked to do: what it was pointed at and the
    options it was submitted with. It is the request Commvault would
    send again to resubmit the job, which is why it exists only for
    jobs Commvault is willing to resubmit (see Jobs.task).

    `requested_level` is what was asked for, not what ran. Commvault
    turns an incremental into a full when there is no full to build on,
    and a plan's log schedule asks for an incremental and runs a
    transaction log backup; Job.backup_level is what ran.

    `options` is Commvault's own options object. Its contents depend on
    the agent and the kind of job - backupOpts for a backup, adminOpts
    for data aging or a DR backup - so it is left as it comes."""

    job_id: int
    # Commvault's numbers for the kind of operation: 2 is a backup.
    operation_type: int | None = None
    requested_level: str | None = None
    requested_level_code: int | None = None
    # The subclients, clients or storage the job was pointed at, each
    # an entity as Commvault writes it (clientName, subclientId, ...).
    associations: list[dict[str, Any]] = Field(default_factory=list)
    options: dict[str, Any] = Field(default_factory=dict)
    raw: dict[str, Any] = Field(default_factory=dict)


class _Reply(BaseModel):
    model_config = ConfigDict(extra="ignore", populate_by_name=True)


class _DetailSubclient(_Subclient):
    app_name: str | None = Field(default=None, alias="appName")
    instance_id: int | None = Field(default=None, alias="instanceId")
    subclient_id: int | None = Field(default=None, alias="subclientId")


class _Plan(_Reply):
    name: str | None = Field(default=None, alias="planName")


class _TaskData(_Reply):
    task_name: str | None = Field(default=None, alias="taskName")


class _GeneralInfo(_Reply):
    job_id: int = Field(alias="jobId")
    operation_type: str | None = Field(default=None, alias="operationType")
    backup_type: str | None = Field(default=None, alias="backupType")
    job_started_by: str | None = Field(default=None, alias="jobStartedBy")
    job_started_from: str | None = Field(default=None, alias="jobStartedFrom")
    schedule_name: str | None = Field(default=None, alias="scheduleName")
    task_data: _TaskData = Field(default_factory=_TaskData, alias="taskData")
    plan: _Plan = Field(default_factory=_Plan)
    storage_policy: _StoragePolicy = Field(default_factory=_StoragePolicy, alias="storagePolicy")
    priority: int | None = None
    subclient: _DetailSubclient = Field(default_factory=_DetailSubclient)
    # "Yes" or "No".
    encrypted: str | None = None
    software_compression: str | None = Field(default=None, alias="softwareCompression")
    pending_reason_error_code: str | None = Field(default=None, alias="pendingReasonErrorCode")


class _DetailInfo(_Reply):
    start_time: int | None = Field(default=None, alias="startTime")
    end_time: int | None = Field(default=None, alias="endTime")
    num_of_objects: int | None = Field(default=None, alias="numOfObjects")
    skipped_items: int | None = Field(default=None, alias="skippedItems")
    scanned_files: int | None = Field(default=None, alias="scannedFiles")
    scanned_folders: int | None = Field(default=None, alias="scannedFolders")
    scan_file_failures: int | None = Field(default=None, alias="scanFileFailures")
    scan_folder_failures: int | None = Field(default=None, alias="scanFolderFailures")
    backup_file_failures: int | None = Field(default=None, alias="backupFileFailures")
    backup_folder_failures: int | None = Field(default=None, alias="backupFolderFailures")
    # These three numbers arrive as strings.
    size_of_application: int | None = Field(default=None, alias="sizeOfApplication")
    savings_percent: float | None = Field(default=None, alias="savingsPercent")
    transfer_time: int | None = Field(default=None, alias="transferTime")
    compressed_bytes: int | None = Field(default=None, alias="compressedBytes")
    size_of_media: int | None = Field(default=None, alias="sizeOfMediaOnDisk")
    num_of_streams: int | None = Field(default=None, alias="numOfStreams")


class _ProgressInfo(_Reply):
    state: str = "Unknown"
    reason_for_job_delay: str | None = Field(default=None, alias="reasonForJobDelay")
    elapsed_time: int | None = Field(default=None, alias="elapsedTime")


class JobDetailInfo(_Reply):
    general: _GeneralInfo = Field(alias="generalInfo")
    detail: _DetailInfo = Field(default_factory=_DetailInfo, alias="detailInfo")
    progress: _ProgressInfo = Field(default_factory=_ProgressInfo, alias="progressInfo")


def _from_epoch(seconds: int | None) -> datetime | None:
    """Commvault reports times as epoch seconds and uses 0 for "not yet"
    (e.g. the end time of a job that is still running)."""
    if not seconds:
        return None
    return datetime.fromtimestamp(seconds, tz=UTC)


def job_from_summary(raw: dict[str, Any]) -> Job:
    summary = JobSummary.model_validate(raw)
    return Job(
        job_id=summary.job_id,
        status=summary.status,
        job_type=summary.job_type,
        operation=summary.operation,
        backup_level=summary.backup_level,
        app_type=summary.app_type,
        client_id=summary.subclient.client_id,
        client_name=summary.subclient.client_name or summary.dest_client_name,
        subclient_name=summary.subclient.subclient_name,
        backupset_name=summary.subclient.backupset_name,
        instance_name=summary.subclient.instance_name,
        storage_policy=summary.storage_policy.name,
        percent_complete=summary.percent_complete,
        start_time=_from_epoch(summary.job_start_time),
        end_time=_from_epoch(summary.job_end_time),
        last_update_time=_from_epoch(summary.last_update_time),
        elapsed_seconds=summary.job_elapsed_time,
        size_of_application=summary.size_of_application,
        size_of_media=summary.size_of_media,
        total_files=summary.total_files,
        failed_files=summary.failed_files,
        failed_folders=summary.failed_folders,
        pending_reason=summary.pending_reason or None,
        pending_reason_code=summary.pending_reason_code or None,
        is_aged=summary.is_aged,
        raw=raw,
    )


def attempt_from_info(raw: dict[str, Any]) -> JobAttempt:
    info = AttemptInfo.model_validate(raw)
    return JobAttempt(
        phase=info.phase,
        # Some phase names arrive padded with spaces to 64 characters.
        phase_name=(info.phase_name or "").strip() or None,
        status=info.status,
        failure_reason=info.failure_reason or None,
        start_time=_from_epoch(info.start_time),
        end_time=_from_epoch(info.end_time),
        elapsed_seconds=info.elapsed_time,
        objects=info.num_objects,
        folders=info.num_folders,
        failures=info.num_failures,
        skipped=info.num_skipped,
        uncompressed_bytes=info.uncomp_bytes,
        compressed_bytes=info.comp_bytes,
        data_written=info.data_written,
        streams=info.max_streams_used,
        # Blank, not absent, is how Commvault says "none" for these.
        access_node=info.access_node_client_name or None,
        media_agent=info.media_agent.name or None,
        library=info.library.name or None,
        storage_policy=info.storage_policy.name or None,
        copy_name=info.copy_.name or None,
        raw=raw,
    )


def event_from_commserv(raw: dict[str, Any]) -> JobEvent:
    event = CommservEvent.model_validate(raw)
    return JobEvent(
        event_id=event.event_id,
        job_id=event.job_id,
        time=_from_epoch(event.time_source),
        severity=event.severity,
        code=event.event_code_string or None,
        subsystem=event.subsystem or None,
        description=event.description or None,
        client_id=event.client.client_id,
        client_name=event.client.client_name or None,
        raw=raw,
    )


def detail_from_job_detail(raw: dict[str, Any]) -> JobDetail:
    info = JobDetailInfo.model_validate(raw)
    general, detail, progress = info.general, info.detail, info.progress
    subclient = general.subclient
    return JobDetail(
        job_id=general.job_id,
        status=progress.state,
        operation=general.operation_type or None,
        backup_type=general.backup_type or None,
        started_by=general.job_started_by or None,
        started_from=general.job_started_from or None,
        schedule_name=general.schedule_name or None,
        schedule_policy=general.task_data.task_name or None,
        plan=general.plan.name or None,
        storage_policy=general.storage_policy.name or None,
        priority=general.priority,
        client_id=subclient.client_id,
        client_name=subclient.client_name or None,
        app_name=subclient.app_name or None,
        instance_id=subclient.instance_id,
        instance_name=subclient.instance_name or None,
        backupset_name=subclient.backupset_name or None,
        subclient_id=subclient.subclient_id,
        subclient_name=subclient.subclient_name or None,
        encrypted={"Yes": True, "No": False}.get(general.encrypted or ""),
        software_compression=general.software_compression or None,
        pending_reason=progress.reason_for_job_delay or None,
        pending_reason_code=general.pending_reason_error_code or None,
        start_time=_from_epoch(detail.start_time),
        end_time=_from_epoch(detail.end_time),
        elapsed_seconds=progress.elapsed_time,
        objects=detail.num_of_objects,
        skipped=detail.skipped_items,
        scanned_files=detail.scanned_files,
        scanned_folders=detail.scanned_folders,
        scan_failed_files=detail.scan_file_failures,
        scan_failed_folders=detail.scan_folder_failures,
        backup_failed_files=detail.backup_file_failures,
        backup_failed_folders=detail.backup_folder_failures,
        size_of_application=detail.size_of_application,
        compressed_bytes=detail.compressed_bytes,
        size_of_media=detail.size_of_media,
        savings_percent=detail.savings_percent,
        streams=detail.num_of_streams,
        transfer_seconds=detail.transfer_time,
        raw=raw,
    )


def task_from_info(job_id: int, raw: dict[str, Any]) -> JobTask:
    # One sub-task per job in everything seen; the first is read.
    sub_tasks = raw.get("subTasks") or [{}]
    options = sub_tasks[0].get("options") or {}
    level = (options.get("backupOpts") or {}).get("backupLevel")
    return JobTask(
        job_id=job_id,
        operation_type=(sub_tasks[0].get("subTask") or {}).get("operationType"),
        requested_level=_REQUESTED_LEVELS.get(level) if isinstance(level, int) else None,
        requested_level_code=level,
        associations=raw.get("associations") or [],
        options=options,
        raw=raw,
    )
