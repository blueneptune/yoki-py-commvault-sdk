"""Job detail beyond the summary: the attempts at each phase, and the
job's events. The reply
shapes are the lab CommServe's (11 SP46), cut down."""

from __future__ import annotations

import json
from datetime import UTC, datetime

import respx

from commvault_sdk import CommvaultClient

BASE = "https://cs.test/commandcenter/api"


def _attempt(phase: int, name: str, status: str = "Completed", **extra: object) -> dict:
    return {
        "phase": phase,
        "phaseName": name,
        "status": status,
        "failureReason": "",
        # Commvault sends these three as strings.
        "startTime": "1791511253",
        "endTime": "1791511266",
        "elapsedTime": "13",
        "numObjects": 0,
        "numFolders": 0,
        "numFailures": 0,
        "numSkipped": 0,
        "uncompBytes": 0,
        "compBytes": 0,
        "dataWritten": 0,
        "maxStreamsUsed": 0,
        "throughPut": "Not Applicable",
        "accessNodeClientName": "",
        "mediaAgent": {"mediaAgentName": ""},
        "library": {"libraryName": ""},
        "storagePolicy": {"storagePolicyId": 0},
        "copy": {"copyId": 0},
        **extra,
    }


def _details(*attempts: dict) -> dict:
    return {"job": {"jobDetail": {"detailInfo": {}, "attemptsInfo": list(attempts)}}}


@respx.mock
def test_attempts_are_asked_for_and_read() -> None:
    route = respx.post(f"{BASE}/JobDetails").respond(
        json=_details(
            _attempt(4, "Scan" + " " * 60),
            _attempt(
                7,
                "Backup",
                numObjects=6,
                numFolders=2,
                uncompBytes=1262194,
                compBytes=828015,
                dataWritten=47176,
                maxStreamsUsed=1,
                accessNodeClientName="web01",
                mediaAgent={"mediaAgentName": "MA1"},
                library={"libraryName": "Pool"},
                storagePolicy={"storagePolicyName": "Standard Plan", "storagePolicyId": 3},
                copy={"copyId": 2, "copyName": "Primary"},
            ),
        )
    )

    with CommvaultClient(BASE, access_token="tok") as cv:
        scan, backup = cv.jobs.attempts(278)

    assert json.loads(route.calls[0].request.content) == {"jobId": 278, "showAttempt": True}
    # Padding is removed; a blank name is None rather than "".
    assert (scan.phase, scan.phase_name, scan.status) == (4, "Scan", "Completed")
    assert scan.failure_reason is None
    assert scan.media_agent is None and scan.storage_policy is None and scan.copy_name is None
    assert scan.start_time == datetime.fromtimestamp(1791511253, tz=UTC)
    assert scan.end_time == datetime.fromtimestamp(1791511266, tz=UTC)
    assert scan.elapsed_seconds == 13
    assert (backup.objects, backup.folders, backup.streams) == (6, 2, 1)
    assert (backup.uncompressed_bytes, backup.compressed_bytes, backup.data_written) == (
        1262194,
        828015,
        47176,
    )
    assert (backup.access_node, backup.media_agent, backup.library) == ("web01", "MA1", "Pool")
    assert (backup.storage_policy, backup.copy_name) == ("Standard Plan", "Primary")
    assert backup.raw["throughPut"] == "Not Applicable"


@respx.mock
def test_a_failed_attempt_keeps_commvaults_reason() -> None:
    reason = "Configured content does not exist [C:\\nope].<br/>Source: CS, Process: FileScan"
    respx.post(f"{BASE}/JobDetails").respond(
        json=_details(_attempt(4, "Scan", "Failed", failureReason=reason))
    )

    with CommvaultClient(BASE, access_token="tok") as cv:
        (scan,) = cv.jobs.attempts(279)

    assert (scan.status, scan.failure_reason) == ("Failed", reason)


@respx.mock
def test_a_job_with_no_attempts_gives_an_empty_list() -> None:
    # Failed to start: details, but no attemptsInfo. Unknown job: a bare {}.
    respx.post(f"{BASE}/JobDetails").mock(
        side_effect=[
            respx.MockResponse(200, json={"job": {"jobDetail": {"detailInfo": {}}}}),
            respx.MockResponse(200, json={}),
        ]
    )

    with CommvaultClient(BASE, access_token="tok") as cv:
        assert cv.jobs.attempts(271) == []
        assert cv.jobs.attempts(999999) == []


@respx.mock
def test_details_does_not_ask_for_attempts_unless_told_to() -> None:
    route = respx.post(f"{BASE}/JobDetails").respond(json=_details())

    with CommvaultClient(BASE, access_token="tok") as cv:
        cv.jobs.details(1)
        cv.jobs.details(1, attempts=True)

    assert [json.loads(call.request.content) for call in route.calls] == [
        {"jobId": 1},
        {"jobId": 1, "showAttempt": True},
    ]


@respx.mock
def test_one_unreadable_attempt_does_not_hide_the_rest(log_messages: list[str]) -> None:
    respx.post(f"{BASE}/JobDetails").respond(
        json=_details(_attempt(4, "Scan"), _attempt(7, "Backup", startTime="not-a-time"))
    )

    with CommvaultClient(BASE, access_token="tok") as cv:
        attempts = cv.jobs.attempts(5)

    assert [a.phase_name for a in attempts] == ["Scan"]
    assert any("Skipping an attempt of job 5" in message for message in log_messages)


def _event(event_id: int, code: str, description: str, **extra: object) -> dict:
    return {
        "id": event_id,
        "jobId": 279,
        "severity": 9,
        "eventCode": "285212830",
        "eventCodeString": code,
        "subsystem": "FileScan",
        "description": description,
        "timeSource": 1791511232,
        "type": 0,
        "acknowledge": 0,
        "clientEntity": {"clientName": "web01", "displayName": "web01", "clientId": 2},
        **extra,
    }


@respx.mock
def test_events_are_read_and_put_oldest_first() -> None:
    # Newest first, as Commvault sends them. Two share a second, and one
    # with a lower id is later than both: ids do not follow time.
    respx.get(f"{BASE}/Events", params={"jobId": 279}).respond(
        json={
            "commservEvents": [
                _event(1099, "17:2", "File system scan failed.", timeSource=1791511237),
                _event(1101, "17:12", "Backup job is aborted.", severity=6),
                _event(1100, "17:158", "Configured content does not exist."),
            ]
        }
    )

    with CommvaultClient(BASE, access_token="tok") as cv:
        events = cv.jobs.events(279)

    assert [e.event_id for e in events] == [1100, 1101, 1099]
    first = events[0]
    assert (first.job_id, first.severity, first.code) == (279, 9, "17:158")
    assert (first.subsystem, first.description) == (
        "FileScan",
        "Configured content does not exist.",
    )
    assert (first.client_id, first.client_name) == (2, "web01")
    assert first.time == datetime.fromtimestamp(1791511232, tz=UTC)
    assert events[1].severity == 6
    assert first.raw["eventCode"] == "285212830"


@respx.mock
def test_a_job_with_no_events_gives_an_empty_list() -> None:
    respx.get(f"{BASE}/Events", params={"jobId": 306}).respond(json={"commservEvents": []})
    respx.get(f"{BASE}/Events", params={"jobId": 7}).respond(404)

    with CommvaultClient(BASE, access_token="tok") as cv:
        assert cv.jobs.events(306) == []
        assert cv.jobs.events(7) == []


@respx.mock
def test_one_unreadable_event_does_not_hide_the_rest(log_messages: list[str]) -> None:
    respx.get(f"{BASE}/Events", params={"jobId": 279}).respond(
        json={"commservEvents": [_event(2, "17:2", "ok"), {"description": "no id"}]}
    )

    with CommvaultClient(BASE, access_token="tok") as cv:
        events = cv.jobs.events(279)

    assert [e.event_id for e in events] == [2]
    assert any("Skipping an event of job 279" in message for message in log_messages)


def _job_detail(**general: object) -> dict:
    """A file system backup's jobDetail, as the lab sends it."""
    return {
        "generalInfo": {
            "jobId": 279,
            "operationType": "Backup",
            "backupType": "Full",
            "jobStartedBy": "Admin",
            "jobStartedFrom": "Scheduled",
            "scheduleName": "",
            "taskData": {"taskId": 40, "taskName": "Standard Plan", "subtaskName": ""},
            "plan": {"planId": 1, "planName": "Standard Plan"},
            "storagePolicy": {"storagePolicyId": 3, "storagePolicyName": "Standard Plan"},
            "priority": 166,
            "subclient": {
                "clientId": 2,
                "clientName": "web01",
                "appName": "Windows File System",
                "instanceId": 1,
                "instanceName": "DefaultInstanceName",
                "backupsetName": "defaultBackupSet",
                "subclientId": 15,
                "subclientName": "data",
            },
            "encrypted": "No",
            "softwareCompression": "Storage Policy",
            "pendingReasonErrorCode": "17:158",
            **general,
        },
        "detailInfo": {
            "startTime": 1791511223,
            "endTime": 1791511283,
            "numOfObjects": 6,
            "skippedItems": 1,
            "scannedFiles": 340,
            "scannedFolders": 2,
            "scanFileFailures": 1,
            "scanFolderFailures": 0,
            "backupFileFailures": 0,
            "backupFolderFailures": 0,
            # Commvault sends these three as strings.
            "sizeOfApplication": "1262194",
            "savingsPercent": "84.07",
            "transferTime": "5",
            "compressedBytes": 828015,
            "sizeOfMediaOnDisk": 47176,
            "numOfStreams": 1,
            "failures": "0 Folders, 1 Files",
        },
        "progressInfo": {
            "state": "Failed",
            "reasonForJobDelay": "Configured content does not exist.<br/>Source: CS",
            "elapsedTime": "60",
        },
    }


@respx.mock
def test_detail_reads_what_the_summary_does_not_have() -> None:
    respx.post(f"{BASE}/JobDetails").respond(json={"job": {"jobDetail": _job_detail()}})

    with CommvaultClient(BASE, access_token="tok") as cv:
        detail = cv.jobs.detail(279)

    assert detail is not None
    assert (detail.job_id, detail.status, detail.operation) == (279, "Failed", "Backup")
    assert (detail.backup_type, detail.started_by, detail.started_from) == (
        "Full",
        "Admin",
        "Scheduled",
    )
    # Scheduled by a plan: no schedule name of its own.
    assert (detail.schedule_name, detail.schedule_policy) == (None, "Standard Plan")
    assert (detail.plan, detail.storage_policy, detail.priority) == (
        "Standard Plan",
        "Standard Plan",
        166,
    )
    assert (detail.client_id, detail.client_name, detail.app_name) == (
        2,
        "web01",
        "Windows File System",
    )
    assert (detail.instance_id, detail.instance_name) == (1, "DefaultInstanceName")
    assert (detail.backupset_name, detail.subclient_id, detail.subclient_name) == (
        "defaultBackupSet",
        15,
        "data",
    )
    assert (detail.encrypted, detail.software_compression) == (False, "Storage Policy")
    assert detail.pending_reason == "Configured content does not exist.<br/>Source: CS"
    assert detail.pending_reason_code == "17:158"
    assert detail.start_time == datetime.fromtimestamp(1791511223, tz=UTC)
    assert detail.end_time == datetime.fromtimestamp(1791511283, tz=UTC)
    assert detail.elapsed_seconds == 60
    assert (detail.objects, detail.skipped) == (6, 1)
    assert (detail.scanned_files, detail.scanned_folders) == (340, 2)
    assert (detail.scan_failed_files, detail.scan_failed_folders) == (1, 0)
    assert (detail.backup_failed_files, detail.backup_failed_folders) == (0, 0)
    assert (detail.size_of_application, detail.compressed_bytes, detail.size_of_media) == (
        1262194,
        828015,
        47176,
    )
    assert (detail.savings_percent, detail.streams, detail.transfer_seconds) == (84.07, 1, 5)
    assert detail.raw["detailInfo"]["failures"] == "0 Folders, 1 Files"


@respx.mock
def test_detail_of_an_administrative_job_leaves_the_backup_fields_empty() -> None:
    # Data Aging: no subclient to speak of, no scan, blanks for names.
    raw = {
        "generalInfo": {
            "jobId": 288,
            "operationType": "Data Aging",
            "jobStartedBy": "SystemCreatedAdmin",
            "jobStartedFrom": "Scheduled",
            "scheduleName": "Data Aging",
            "taskData": {"taskName": "", "subtaskName": "Data Aging"},
            "plan": {"planId": 0},
            "storagePolicy": {"storagePolicyId": 0, "storagePolicyName": ""},
            "subclient": {"displayName": "", "instanceName": "", "workloadId": 0},
            "pendingReasonErrorCode": "",
        },
        "detailInfo": {"startTime": 1791565380, "endTime": 0, "numOfObjects": 0},
        "progressInfo": {"state": "Completed", "reasonForJobDelay": "", "elapsedTime": "-5445"},
    }
    respx.post(f"{BASE}/JobDetails").respond(json={"job": {"jobDetail": raw}})

    with CommvaultClient(BASE, access_token="tok") as cv:
        detail = cv.jobs.detail(288)

    assert detail is not None
    assert (detail.schedule_name, detail.schedule_policy) == ("Data Aging", None)
    assert (detail.plan, detail.storage_policy, detail.backup_type) == (None, None, None)
    assert (detail.client_id, detail.client_name, detail.instance_name) == (None, None, None)
    assert (detail.encrypted, detail.scanned_files, detail.scan_failed_files) == (None, None, None)
    assert (detail.pending_reason, detail.pending_reason_code) == (None, None)
    # 0 is Commvault's "not yet"; the elapsed figure is passed on as it is.
    assert (detail.end_time, detail.elapsed_seconds) == (None, -5445)


@respx.mock
def test_detail_is_none_for_an_unknown_or_unreadable_job(log_messages: list[str]) -> None:
    respx.post(f"{BASE}/JobDetails").mock(
        side_effect=[
            respx.MockResponse(200, json={}),
            respx.MockResponse(200, json={"job": {"jobDetail": _job_detail(priority="high")}}),
        ]
    )

    with CommvaultClient(BASE, access_token="tok") as cv:
        assert cv.jobs.detail(999999) is None
        assert cv.jobs.detail(279) is None

    assert any("Could not read the details of job 279" in message for message in log_messages)
    assert any("generalInfo.priority" in message for message in log_messages)


@respx.mock
def test_explain_gathers_the_reasons_the_attempts_that_fell_short_and_the_serious_events() -> None:
    reason = "The Job Manager service was restarted.<br/>Source: CS, Process: JobManager"
    raw = _job_detail(pendingReasonErrorCode="19:601, 19:601, 17:158")
    raw["progressInfo"] = {
        "state": "Completed w/ one or more errors",
        "reasonForJobDelay": f"{reason}\n{reason}",
        "elapsedTime": "60",
    }
    raw["attemptsInfo"] = [
        _attempt(4, "Scan", "Interrupted", failureReason=reason),
        _attempt(4, "Scan"),
        _attempt(7, "Backup", "Completed w/ one or more errors"),
    ]
    details = respx.post(f"{BASE}/JobDetails").respond(json={"job": {"jobDetail": raw}})
    events = respx.get(f"{BASE}/Events", params={"jobId": 279}).respond(
        json={
            "commservEvents": [
                _event(4, "17:2", "critical", severity=9, timeSource=1791511240),
                _event(3, "17:12", "major", severity=6, timeSource=1791511239),
                _event(2, "19:122", "minor", severity=3, timeSource=1791511238),
                _event(1, "19:1451", "information", severity=0, timeSource=1791511237),
            ]
        }
    )

    with CommvaultClient(BASE, access_token="tok") as cv:
        why = cv.jobs.explain(279)
        everything = cv.jobs.explain(279, min_severity=0)

    assert why is not None and everything is not None
    # One request for the details and attempts together, one for events.
    assert json.loads(details.calls[0].request.content) == {"jobId": 279, "showAttempt": True}
    assert (details.call_count, events.call_count) == (2, 2)
    assert (why.job_id, why.status) == (279, "Completed w/ one or more errors")
    assert [r.text for r in why.reasons] == ["The Job Manager service was restarted."] * 2
    # Each code once, in the order given.
    assert why.reason_codes == ["19:601", "17:158"]
    assert [(a.phase_name, a.status) for a in why.incomplete_attempts] == [
        ("Scan", "Interrupted"),
        ("Backup", "Completed w/ one or more errors"),
    ]
    assert [e.description for e in why.events] == ["major", "critical"]
    assert [e.description for e in everything.events] == [
        "information",
        "minor",
        "major",
        "critical",
    ]
    assert why.detail.started_by == "Admin"
    assert not why.clean


@respx.mock
def test_explain_of_a_clean_job_says_so() -> None:
    raw = _job_detail(pendingReasonErrorCode="")
    raw["progressInfo"] = {"state": "Completed", "reasonForJobDelay": "", "elapsedTime": "60"}
    raw["attemptsInfo"] = [_attempt(4, "Scan"), _attempt(7, "Backup")]
    respx.post(f"{BASE}/JobDetails").respond(json={"job": {"jobDetail": raw}})
    # Information only: below what is asked for.
    respx.get(f"{BASE}/Events", params={"jobId": 279}).respond(
        json={"commservEvents": [_event(1, "19:1451", "converted to a full", severity=0)]}
    )

    with CommvaultClient(BASE, access_token="tok") as cv:
        why = cv.jobs.explain(279)

    assert why is not None and why.clean
    assert (why.reasons, why.reason_codes, why.incomplete_attempts, why.events) == ([], [], [], [])


@respx.mock
def test_explain_of_a_job_that_failed_to_start_has_reasons_and_events_but_no_attempts() -> None:
    raw = _job_detail(pendingReasonErrorCode="19:1132")
    raw["progressInfo"] = {
        "state": "Failed to Start",
        "reasonForJobDelay": "Another backup is running.<br/>Source: CS, Process: JobManager",
        "elapsedTime": "0",
    }
    respx.post(f"{BASE}/JobDetails").respond(json={"job": {"jobDetail": raw}})
    respx.get(f"{BASE}/Events", params={"jobId": 279}).respond(
        json={"commservEvents": [_event(1, "19:1132", "Another backup is running.", severity=6)]}
    )

    with CommvaultClient(BASE, access_token="tok") as cv:
        why = cv.jobs.explain(279)

    assert why is not None and not why.clean
    assert (why.status, why.reason_codes, why.incomplete_attempts) == (
        "Failed to Start",
        ["19:1132"],
        [],
    )
    assert [e.code for e in why.events] == ["19:1132"]


@respx.mock
def test_explain_is_none_for_an_unknown_job_and_does_not_ask_for_its_events() -> None:
    respx.post(f"{BASE}/JobDetails").respond(json={})
    # No /Events route is mocked: asking would fail the test.

    with CommvaultClient(BASE, access_token="tok") as cv:
        assert cv.jobs.explain(999999) is None


def _task(level: int | None = 2, **options: object) -> dict:
    backup = {} if level is None else {"backupOpts": {"backupLevel": level, "incLevel": 1}}
    return {
        "taskInfo": {
            "task": {"ownerId": 1, "runUserId": 1, "taskType": 1},
            "associations": [
                {"clientId": 16, "clientName": "sql-02", "subclientId": 44, "appName": "SQL Server"}
            ],
            "subTasks": [
                {
                    "subTaskOperation": 1,
                    "subTask": {"subTaskType": 2, "operationType": 2},
                    "options": {**backup, **options},
                }
            ],
        }
    }


@respx.mock
def test_task_reads_what_a_job_was_asked_to_do() -> None:
    respx.get(f"{BASE}/Job/306/TaskDetails").respond(
        json=_task(2, commonOpts={"notifyUserOnJobCompletion": False})
    )

    with CommvaultClient(BASE, access_token="tok") as cv:
        task = cv.jobs.task(306)

    assert task is not None
    assert (task.job_id, task.operation_type) == (306, 2)
    assert (task.requested_level, task.requested_level_code) == ("Incremental", 2)
    assert task.associations == [
        {"clientId": 16, "clientName": "sql-02", "subclientId": 44, "appName": "SQL Server"}
    ]
    # Options are Commvault's own, whatever the agent put there.
    assert task.options["backupOpts"]["incLevel"] == 1
    assert task.options["commonOpts"] == {"notifyUserOnJobCompletion": False}
    assert task.raw["task"]["ownerId"] == 1


@respx.mock
def test_task_names_the_levels_seen_and_leaves_the_rest_as_a_code() -> None:
    replies = [_task(1), _task(3), _task(6), _task(4), _task(None, adminOpts={"x": 1})]
    respx.get(f"{BASE}/Job/1/TaskDetails").mock(
        side_effect=[respx.MockResponse(200, json=reply) for reply in replies]
    )

    with CommvaultClient(BASE, access_token="tok") as cv:
        tasks = [cv.jobs.task(1) for _ in replies]

    assert [(t.requested_level, t.requested_level_code) for t in tasks if t] == [
        ("Full", 1),
        ("Differential", 3),
        ("Transaction Log", 6),
        # Not seen in the lab: the number is kept, no name is guessed.
        (None, 4),
        # An administrative job has no backup options at all.
        (None, None),
    ]


@respx.mock
def test_task_is_none_when_commvault_will_not_resubmit_the_job(log_messages: list[str]) -> None:
    refusal = {
        "errorMessage": "Unable to resubmit job as job is older than [7] days.",
        "errorCode": 587204882,
    }
    respx.get(f"{BASE}/Job/50/TaskDetails").respond(json=refusal)
    respx.get(f"{BASE}/Job/51/TaskDetails").respond(404)

    with CommvaultClient(BASE, access_token="tok") as cv:
        assert cv.jobs.task(50) is None
        assert cv.jobs.task(51) is None

    # Commvault's own words are kept, for whoever needs to know why.
    assert any(
        "No task details for job 50" in message and "older than [7] days" in message
        for message in log_messages
    )


@respx.mock
def test_failed_items_are_read_with_commvaults_reason() -> None:
    respx.get(f"{BASE}/Job/279/FailedItems").respond(
        json={
            "isFailedItemsCSV": False,
            "failedItems": [
                {
                    "failureReason": "The system cannot find the path specified.",
                    "entity": "C:\\blt-lab\\does-not-exist\\",
                },
                {"failureReason": "Access is denied.", "entity": "C:\\data\\locked.db"},
            ],
        }
    )

    with CommvaultClient(BASE, access_token="tok") as cv:
        items = cv.jobs.failed_items(279)

    assert items is not None
    assert [(item.path, item.reason) for item in items] == [
        ("C:\\blt-lab\\does-not-exist\\", "The system cannot find the path specified."),
        ("C:\\data\\locked.db", "Access is denied."),
    ]
    assert items[1].raw == {"failureReason": "Access is denied.", "entity": "C:\\data\\locked.db"}


@respx.mock
def test_a_backup_with_no_failed_items_gives_an_empty_list() -> None:
    # What a clean backup gets - and an old one whose list is gone.
    respx.get(f"{BASE}/Job/306/FailedItems").respond(json={})

    with CommvaultClient(BASE, access_token="tok") as cv:
        assert cv.jobs.failed_items(306) == []


@respx.mock
def test_failed_items_is_none_where_commvault_will_not_list_them(
    log_messages: list[str],
) -> None:
    # Any job that is not a backup, and a job id the CommCell does not know.
    respx.get(f"{BASE}/Job/12/FailedItems").respond(
        500, json={"errorMessage": "View failed items operation failed.", "errorCode": 1}
    )

    with CommvaultClient(BASE, access_token="tok") as cv:
        assert cv.jobs.failed_items(12) is None

    assert any("No failed items for job 12" in message for message in log_messages)


@respx.mock
def test_one_unreadable_failed_item_does_not_hide_the_rest(log_messages: list[str]) -> None:
    respx.get(f"{BASE}/Job/279/FailedItems").respond(
        json={
            "isFailedItemsCSV": True,
            "failedItems": [{"failureReason": "no path"}, {"entity": "/etc/shadow"}],
        }
    )

    with CommvaultClient(BASE, access_token="tok") as cv:
        items = cv.jobs.failed_items(279)

    assert items is not None
    assert [(item.path, item.reason) for item in items] == [("/etc/shadow", None)]
    assert any("Skipping a failed item of job 279" in message for message in log_messages)
    assert any("as a CSV" in message for message in log_messages)
