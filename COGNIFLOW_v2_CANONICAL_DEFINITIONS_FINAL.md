# COGNIFLOW v2 — CANONICAL DEFINITIONS

**Status**: AUTHORITATIVE — v2 SPECIFICATION  
**Scope**: COGNIFLOW v2 only  
**Depends on**: v1 outputs (Session, Derived_Signal, Insight)

---

## 1. v2 ELIGIBILITY DEFINITIONS

### Session v2-Eligibility

A session is **v2-eligible** if and only if:

```
session.insight_eligible == true
AND
Derived_Signal record exists for session.session_id
```

### Student v2-Eligibility

A student is **v2-eligible** if and only if:

```
COUNT(v2-eligible sessions for student_id) >= 3
```

### Session Disqualification

A session is **disqualified** from v2 consideration if:

- `session.insight_eligible == false`, OR
- No Derived_Signal record exists for `session.session_id`, OR
- Session belongs to a student who is not v2-eligible

---

## 2. BASELINE CONSTRUCTION

### Baseline Set Selection

The baseline set is constructed as follows:

1. Filter all sessions where:
   - `session.student_id == target_student_id`
   - Session is v2-eligible
2. Sort filtered sessions by `session_start_utc` ascending
3. Select first 3 sessions from sorted list
4. This set is the **baseline**

### Baseline Size

Baseline always contains exactly 3 sessions.

### Insufficient Sessions

If fewer than 3 v2-eligible sessions exist for a student:

**v2 REMAINS SILENT** (no baseline, no deltas, no insights)

---

## 3. CURRENT COMPARISON TARGET

### Target Session Selection

The **current comparison target** is:

1. Filter all v2-eligible sessions for `student_id`
2. Sort by `session_start_utc` ascending
3. Exclude the first 3 sessions (baseline)
4. Select the most recent session from remaining sessions

If no sessions remain after excluding baseline:

**v2 REMAINS SILENT**

### Multiple Recent Sessions

Only the single most recent v2-eligible session is compared.

Earlier sessions beyond baseline are ignored.

### Ties

If multiple sessions have identical `session_start_utc`:

Select session with lexicographically smallest `session_id`.

---

## 4. SIGNAL-LEVEL DELTA RULES

### planning_latency_seconds

**v2-Eligible**: Yes

**Baseline Envelope Computation**:
```
non_null_values = FILTER(planning_latency_seconds from 3 baseline sessions, WHERE value IS NOT NULL)
baseline_min = MIN(non_null_values)
baseline_max = MAX(non_null_values)
```

**Delta Direction**:

| Condition | Output |
|-----------|--------|
| `current > baseline_max` | "More than your previous attempts" |
| `current < baseline_min` | "Less than before" |
| `baseline_min <= current <= baseline_max` | "No change detected" |

---

### iteration_depth

**v2-Eligible**: Yes

**Baseline Envelope Computation**:
```
non_null_values = FILTER(iteration_depth from 3 baseline sessions, WHERE value IS NOT NULL)
baseline_min = MIN(non_null_values)
baseline_max = MAX(non_null_values)
```

**Delta Direction**:

| Condition | Output |
|-----------|--------|
| `current > baseline_max` | "More than your previous attempts" |
| `current < baseline_min` | "Less than before" |
| `baseline_min <= current <= baseline_max` | "No change detected" |

---

### rewrite_ratio

**v2-Eligible**: Yes

**Baseline Envelope Computation**:
```
non_null_values = FILTER(rewrite_ratio from 3 baseline sessions, WHERE value IS NOT NULL)
baseline_min = MIN(non_null_values)
baseline_max = MAX(non_null_values)
```

**Delta Direction**:

| Condition | Output |
|-----------|--------|
| `current > baseline_max` | "More than your previous attempts" |
| `current < baseline_min` | "Less than before" |
| `baseline_min <= current <= baseline_max` | "No change detected" |

---

### error_transition_pattern

**v2-Eligible**: UNDEFINED BY DESIGN

Rationale: No mechanical, non-judgmental comparison exists for categorical sequences.

Comparing list lengths would judge error quantity.  
Comparing error types would judge error quality.  
Both violate constitutional rules.

---

## 5. NULL, CONFLICT, AND AMBIGUITY HANDLING

### Baseline Contains NULL Values

If any baseline session has NULL for a signal:

**Exclude that session from baseline envelope computation.**

If all 3 baseline sessions have NULL for a signal:

**v2 REMAINS SILENT for that signal** (no delta shown)

---

### Current Session Has NULL Signal

If current session has NULL for a signal:

**v2 REMAINS SILENT for that signal** (no delta shown)

---

### Envelope Computation with NULLs

```
non_null_values = FILTER(baseline_signals, WHERE value IS NOT NULL)

if LENGTH(non_null_values) == 0:
  baseline_min = NULL
  baseline_max = NULL
  # v2 silent for this signal
else:
  baseline_min = MIN(non_null_values)
  baseline_max = MAX(non_null_values)
```

---

### Inconsistent Signal Fluctuation

UNDEFINED BY DESIGN.

v2 compares current to baseline only.

No trend consistency checking is performed.

No smoothing or averaging beyond median baseline.

---

## 6. v2 INSIGHT INSTANTIATION RULES

### v2 Insight Creation Conditions

A v2 insight is created if and only if:

1. Student is v2-eligible, AND
2. Current comparison target exists, AND
3. At least one signal has a computable delta (non-NULL baseline + non-NULL current), AND
4. Delta direction is determined per Section 4

### Suppression Rules

v2 insights are **suppressed** if:

- Student has fewer than 3 v2-eligible sessions, OR
- Current session is within first 3 sessions (baseline), OR
- All signals have NULL baseline or NULL current

### Multiple v2 Insights Per Student

Yes, allowed.

Each v2-eligible session beyond baseline may produce one v2 insight per signal dimension.

### Single-Session Prohibition

**Invariant**: A single v2-eligible session never triggers a v2 insight.

Minimum: 4 v2-eligible sessions required (3 baseline + 1 current).

---

## 7. USER-FACING LANGUAGE (LOCKED)

### Allowed Strings (Exhaustive)

The following strings are the ONLY permitted v2 insight language:

1. `"More than your previous attempts"`
2. `"Less than before"`
3. `"No change detected"`

### Forbidden Variations

All other phrasing is **explicitly forbidden**, including:

- "Significantly more"
- "Slightly less"
- "Much faster"
- "Improved"
- "Regressed"
- "Better"
- "Worse"
- Any quantified deltas ("20% more")
- Any temporal references ("Recently")

---

## 8. v2 FAILURE MODES

### Scenarios Requiring Silence

v2 **must remain silent** in the following scenarios:

1. **Insufficient history**: Student has < 3 v2-eligible sessions
2. **Baseline-only student**: Student has exactly 3 v2-eligible sessions (no comparison target)
3. **All NULLs**: All baseline sessions have NULL for a given signal
4. **Current NULL**: Current session has NULL for a given signal
5. **error_transition_pattern**: Always silent (undefined by design)

---

### Scenarios Prohibiting Direction Inference

v2 **must not infer direction** when:

1. Baseline median cannot be computed (all NULL)
2. Current value is NULL
3. Signal is not v2-eligible (e.g., `error_transition_pattern`)

Default: **"No change detected"** only when both baseline and current are computable and equal.

If non-computable: **silence** (no insight shown).

---

### Scenarios Prohibiting Insight Surfacing

v2 insights **must not be surfaced** when:

1. Requested for a student who is not v2-eligible
2. Requested for a session that is part of baseline
3. Requested for a signal that has NULL baseline or NULL current
4. Requested for `error_transition_pattern`

---

## FINAL INVARIANTS

### Baseline Immutability

Once a student becomes v2-eligible, their baseline is the first 3 v2-eligible sessions, sorted by `session_start_utc`.

This baseline **never changes** in v2.

New sessions do not shift baseline.

---

### Cross-Student Prohibition

v2 deltas are **always self-referential**.

Baseline for `student_A` never includes sessions from `student_B`.

Comparison targets for `student_A` never reference `student_B`.

---

### Difficulty Normalization

UNDEFINED IN v2.

TDD mentions "difficulty-normalized comparisons (self only)" but provides no difficulty quantification method.

v2 performs raw signal deltas only, with no normalization.

---

## UNDEFINED BY DESIGN (SUMMARY)

The following are explicitly undefined and must not be implemented in v2:

1. **error_transition_pattern deltas**: No mechanical comparison exists
2. **Trend consistency detection**: Only single current-vs-baseline comparison
3. **Difficulty normalization**: No difficulty metric defined
4. **Institutional views**: Out of scope for v2 (see TDD Section 2.4)
5. **Multi-session trends**: Only most recent session compared
6. **Regression/improvement signals**: Terminology violates neutrality; use locked language only

---

**END OF v2 CANONICAL DEFINITIONS**
