# COGNIFLOW v1 CANONICAL DEFINITIONS

Status: AUTHORITATIVE — SUPERSEDES ALL PRIOR CANONICAL DEFINITION DRAFTS
Scope: Cogniflow v1 only

1. EVENT PAYLOAD SCHEMA
code_insert
{
  "event_type": "code_insert",
  "timestamp_utc": <ISO 8601 string>,
  "session_id": <UUID>,
  "line_number": <integer, 1-indexed>,
  "column_number": <integer, 0-indexed>,
  "inserted_text": <string>
}
code_delete
{
  "event_type": "code_delete",
  "timestamp_utc": <ISO 8601 string>,
  "session_id": <UUID>,
  "line_number": <integer, 1-indexed>,
  "column_number": <integer, 0-indexed>,
  "deleted_text": <string>
}
run_code
{
  "event_type": "run_code",
  "timestamp_utc": <ISO 8601 string>,
  "session_id": <UUID>
}
error
{
  "event_type": "error",
  "timestamp_utc": <ISO 8601 string>,
  "session_id": <UUID>,
  "error_category": <"syntax" | "runtime" | "test">,
  "line_number": <integer, 1-indexed, null if not applicable>
}
idle
{
  "event_type": "idle",
  "timestamp_utc": <ISO 8601 string>,
  "session_id": <UUID>,
  "duration_seconds": <integer, rounded to nearest 60>
}
submit
{
  "event_type": "submit",
  "timestamp_utc": <ISO 8601 string>,
  "session_id": <UUID>
}



2. SESSION START AND END CONDITIONS
Session Start
A session starts when:

A problem page is loaded in the browser AND
The code editor receives focus for the first time
Session receives a new UUID at this point.

Session End
A session ends when ANY of the following occurs:

submit event is captured
Browser tab is closed
30 minutes elapse with no events (any type)
User navigates away from problem page
Multiple ends can occur; first one wins.

3. VISIBILITY LEVEL ASSIGNMENT LOGIC

Computed at session end only.

Visibility level is determined by comparing the total count of observable events
(code_insert, code_delete, run_code, error, submit) against server-side constants.

These constants:
- HIGH_VISIBILITY_EVENT_FLOOR
- MEDIUM_VISIBILITY_EVENT_FLOOR

Properties:
- Defined in server configuration
- Never serialized
- Never exposed via API
- Never displayed in UI
- Never logged verbatim

Assignment:
- High Process Visibility: event_count >= HIGH_VISIBILITY_EVENT_FLOOR
- Medium Process Visibility: MEDIUM_VISIBILITY_EVENT_FLOOR <= event_count < HIGH_VISIBILITY_EVENT_FLOOR
- Low Process Visibility: event_count < MEDIUM_VISIBILITY_EVENT_FLOOR


4. BEHAVIORAL SIGNAL DEFINITIONS
All signals computed only for High and Medium Visibility sessions.

planning_latency
Time in seconds from session start to first run_code event.

If no run_code exists: signal is null.

iteration_depth
Count of run_code events in the session.

rewrite_ratio
rewrite_ratio = (count of code_delete events) / (count of code_insert events)
If code_insert count is 0: signal is null.

error_transition_pattern
Sequence of error categories in chronological order.

Example output: ["syntax", "syntax", "runtime", "test"]

If no error events exist: signal is empty list.

structural_convergence
UNDEFINED BY DESIGN.

(Requires semantic analysis of code structure, which is not mechanically definable without inference.)

5. BINARY CUE OPERATIONAL MEANING
Each cue has two states:

Shown: Checkbox appears in teacher UI
Not Shown: Checkbox does not appear in teacher UI
There is no "checked vs unchecked" distinction within shown state. If shown, the checkbox is always checked.

6. EXPLAINABLE ON CLICK
What is Revealed
When a teacher clicks a shown cue, the UI displays:

Signal values that contributed to this cue (numeric or list as defined in Section 4)
Event count by type for this session

All values are displayed as raw numbers or lists, with labels only.

What Must NOT Be Revealed
Individual event timestamps
inserted_text or deleted_text payloads
Line numbers or column numbers
idle durations
Confidence scalars
Comparisons to other students
Comparisons to prior sessions of this student (v1 only; prohibited until v2)
7. UI BEHAVIOR FOR LOW-VISIBILITY SESSIONS
Teacher View
Session appears in session list with:

Student identifier (as usual)
Problem name (as usual)
Timestamp of session start (as usual)
No cues shown (cue area is blank, not grayed or marked)
Clicking on session shows:

"Insufficient process data for this session"
No event counts
No signals
No explanations
Student View
Student sees their own session in timeline with:

Problem name
Timestamp
"Session completed" or "Session incomplete" (based on presence of submit event)
No feedback text
No signals
8. DATA RETENTION RULE FOR RAW EVENTS IN v1
Invariant:
Raw event payload fields that are marked for deletion must not exist in persistent
storage beyond the completion of signal computation for the session.

This deletion must occur synchronously at session end.
Asynchronous deletion, delayed cleanup, background jobs, or retry queues are forbidden in v1.
Raw events (full payloads from Section 1) are:

Retained until signals (Section 4) are computed
Discarded immediately after signal computation completes, except:
event_type (kept)
timestamp_utc (kept)
error_category (kept if event_type is "error")
All inserted_text, deleted_text, line_number, column_number, and duration_seconds fields are deleted from persistent storage after signals are computed.

This occurs synchronously at session end.