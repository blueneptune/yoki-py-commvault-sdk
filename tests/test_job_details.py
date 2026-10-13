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
