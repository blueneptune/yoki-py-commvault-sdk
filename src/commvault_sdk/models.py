"""Commvault's own job JSON, and the typed Job the SDK returns.

Field names follow the `jobSummary` object the REST API returns from
POST /Jobs and GET /Job/{id} (the same one cvpysdk's JobController
reads). Everything except jobId is optional: which fields are present
varies by job type and CommServe version, and the untouched summary is
kept in Job.raw regardless.

JobAttempt is one entry of `attemptsInfo`, which POST /JobDetails adds
to its answer when asked with showAttempt.
"""

from __future__ import annotations

from datetime import UTC, datetime
from typing import Any

from pydantic import AwareDatetime, BaseModel, ConfigDict, Field


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
    pending_reason: str | None = None
    is_aged: bool | None = None
    raw: dict[str, Any] = Field(default_factory=dict)


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
    pending_reason: str | None = Field(default=None, alias="pendingReason")
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
        pending_reason=summary.pending_reason or None,
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
