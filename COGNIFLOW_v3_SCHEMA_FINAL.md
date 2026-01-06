COGNIFLOW v3 — PERSISTENT DATA SCHEMA (FINAL)

Status: AUTHORITATIVE — v3 SCHEMA FREEZE
Depends on:
	•	v1 Session, Derived_Signal
	•	v3 Canonical Definitions

⸻

SCHEMA: Stability_Assessment

CREATE TABLE Stability_Assessment (
  stability_id UUID PRIMARY KEY,
  student_id VARCHAR NOT NULL,
  session_id UUID NOT NULL REFERENCES Session(session_id),
  signal_name VARCHAR NOT NULL,
  stability_label VARCHAR NOT NULL,
  created_utc TIMESTAMP NOT NULL
);


⸻

FIELD-BY-FIELD EXPLANATION (PLAIN ENGLISH)

stability_id
	•	Unique ID for this record
	•	Internal use only

⸻

student_id
	•	Used only for filtering by student
	•	Denormalized on purpose
	•	Prevents joins that could enable cross-student analysis

⸻

session_id
	•	The current session being evaluated
	•	Never a baseline session
	•	One session can generate up to 3 records (one per signal)

⸻

signal_name

Allowed values (enforced by logic, not DB):
	•	"planning_latency_seconds"
	•	"iteration_depth"
	•	"rewrite_ratio"

Not stored as enum to avoid schema rigidity.

⸻

stability_label

Allowed values (EXHAUSTIVE, locked):
	1.	"Within your usual range"
	2.	"Outside your usual range"

No other strings permitted.

⸻

created_utc
	•	Audit only
	•	Never shown to users
	•	No ordering guarantees implied

⸻

INTENTIONALLY OMITTED (VERY IMPORTANT)

The following fields do not exist and must never be added:

❌ No numbers
	•	No current value
	•	No baseline min/max
	•	No window size
	•	No deviation amount

Why: Numbers invite scoring and judgment.

⸻

❌ No history metadata
	•	No list of window session IDs
	•	No “window start” or “window end”

Why: v3 is observational, not explanatory.

⸻

❌ No aggregation fields
	•	No stability score
	•	No volatility index
	•	No consistency percentage

Why: Those are rankings in disguise.

⸻

❌ No cross-student fields
	•	No class_id
	•	No cohort_id
	•	No percentiles

Why: Constitutionally prohibited.

⸻

STRUCTURAL INVARIANTS

One Record Rule

For a given:

(session_id, signal_name)

At most one Stability_Assessment record may exist.

⸻

Silence Rule

If:
	•	student has < 5 eligible sessions, OR
	•	current signal is NULL, OR
	•	envelope cannot be computed

→ NO ROW IS CREATED

Silence is the output.

⸻

ALLOWED QUERIES

-- Student-scoped
SELECT * FROM Stability_Assessment
WHERE student_id = ?;

-- Session-scoped
SELECT * FROM Stability_Assessment
WHERE session_id = ?;


⸻

FORBIDDEN QUERIES

-- Aggregation (FORBIDDEN)
SELECT stability_label, COUNT(*) FROM Stability_Assessment GROUP BY stability_label;

-- Ranking (FORBIDDEN)
SELECT * FROM Stability_Assessment ORDER BY created_utc;

-- Cross-student (FORBIDDEN)
SELECT * FROM Stability_Assessment WHERE signal_name = 'iteration_depth';


⸻

FINAL GUARANTEE

If this table exists, it is impossible to answer:
	•	“Who is better?”
	•	“Who improved?”
	•	“Who is inconsistent compared to others?”

The schema enforces that impossibility.

