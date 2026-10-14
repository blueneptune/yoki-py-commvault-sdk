"""Commvault's reason text, split into what was said, by which machine
and by which process. The texts are the lab CommServe's (11 SP46)."""

from __future__ import annotations

from commvault_sdk import Job, JobAttempt, JobDetail, Reason, split_reason

KILLED = "Killed by Admin. Reason:[].<br/>Source: CS01, Process: JobManager"
RESTARTED = "The Job Manager service was restarted.<br/>Source: CS01, Process: JobManager"


def test_a_reason_is_split_from_its_ending() -> None:
    assert split_reason(KILLED) == [
        Reason(text="Killed by Admin. Reason:[].", source="CS01", process="JobManager")
    ]


def test_a_field_can_hold_several_reasons() -> None:
    # A job held up three times: the same line three times over.
    text = "\n".join([RESTARTED, RESTARTED, KILLED])

    reasons = split_reason(text)

    assert [r.text for r in reasons] == [
        "The Job Manager service was restarted.",
        "The Job Manager service was restarted.",
        "Killed by Admin. Reason:[].",
    ]
    assert {(r.source, r.process) for r in reasons} == {("CS01", "JobManager")}


def test_commas_and_brackets_in_the_message_are_left_alone() -> None:
    text = (
        "Another backup is running for client [sql-01], iDataAgent [SQL Server], "
        "Instance [sql-01], Subclient [default].<br/>Source: CS01, Process: JobManager"
    )

    (reason,) = split_reason(text)

    assert reason.text.endswith("Instance [sql-01], Subclient [default].")
    assert (reason.source, reason.process) == ("CS01", "JobManager")


def test_text_without_the_ending_comes_back_whole() -> None:
    assert split_reason("Something new.") == [Reason(text="Something new.")]
    # Even after a reason that does have one.
    assert split_reason(KILLED + "\nAnd a line\nover two.") == [
        Reason(text="Killed by Admin. Reason:[].", source="CS01", process="JobManager"),
        Reason(text="And a line\nover two."),
    ]


def test_no_reason_is_no_reasons() -> None:
    assert split_reason(None) == []
    assert split_reason("") == []


def test_jobs_attempts_and_details_offer_their_reasons_split() -> None:
    expected = [Reason(text="Killed by Admin. Reason:[].", source="CS01", process="JobManager")]

    assert Job(job_id=1, status="Killed", pending_reason=KILLED).reasons == expected
    assert JobDetail(job_id=1, status="Killed", pending_reason=KILLED).reasons == expected
    assert JobAttempt(status="Killed", failure_reason=KILLED).reasons == expected
    assert Job(job_id=2, status="Completed").reasons == []
    # The text Commvault sent is still there, untouched.
    assert Job(job_id=1, status="Killed", pending_reason=KILLED).pending_reason == KILLED
