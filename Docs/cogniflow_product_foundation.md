# Cogniflow — Product Foundation Document

This document is the authoritative foundation for Cogniflow. It captures the evolution of the product from first principles to an implemented system. It is intended to be stable over time and to serve as a shared source of truth across product, engineering, and research decisions.

---

## 0. Product Identity

**Name:** Cogniflow  
**Tagline:** A cognitive observability system for programming education

**Core thesis:**
Learning to program is primarily a *process*, not an outcome. Cogniflow exists to make that process visible, interpretable, and improvable for students—without converting visibility into surveillance, ranking, or institutional control.

---

## 1. Guiding Principles (All Versions)

These principles apply to v1, v2, v3, and beyond.

1. **Student-first ownership**
   - Students own their individual-level data by default.
   - No hidden secondary beneficiaries.

2. **Process over outcomes**
   - Cogniflow observes *how* code is written, not whether it is correct.
   - Correctness, grades, and scores are explicitly excluded.

3. **Descriptive, not evaluative**
   - The system describes observable patterns.
   - It does not assign value, labels, or ranks.

4. **Misuse resistance by design**
   - Rich signals must not collapse into single metrics.
   - Institutional extraction is constrained structurally, not by policy alone.

5. **Epistemic humility**
   - All interpretations are provisional.
   - Signals are framed as hypotheses, not truths.

6. **Progressive resolution**
   - Start with coarse, legible signals.
   - Increase resolution only with consent, calibration, and justification.

---

## 2. Cogniflow v1 — Foundational System

### 2.1 Purpose of v1

v1 exists to prove that:
- Cognitive observability can be useful *without* surveillance
- Students find reflective insight valuable
- The system can function without AI or ML
- Trust can be established before sophistication

v1 is not intended to scale institutionally or maximize data capture.

---

### 2.2 Primary User

**Individual students** who are:
- Learning Python programming
- Motivated to improve their learning process
- Willing to reflect on how they work

Secondary users (teachers, institutions) are explicitly out of scope in v1.

---

### 2.3 Product Form (v1)

- Standalone, web-based application
- Browser-based Python code editor
- Authenticated individual accounts
- No LMS integration
- No background or invisible tracking

---

### 2.4 Observable Data (v1)

#### 2.4.1 Event Primitives

v1 captures only coarse-grained events:

- **SessionBoundary**
  - session_start
  - session_end

- **EditEvent**
  - timestamp
  - net characters added
  - net characters removed
  - document length

- **RunEvent**
  - timestamp

- **ErrorEvent**
  - timestamp
  - error category (syntax, runtime)

Excluded by design:
- Keystrokes
- Backspaces
- Cursor movement
- Typing speed

---

### 2.5 Cognitive Signals (v1)

v1 defines exactly four signals. These are fixed.

#### Signal 1: Edit Granularity Pattern
- Observes distribution of edit sizes
- Describes tendency toward incremental changes vs large rewrites
- Does not imply skill, speed, or correctness

#### Signal 2: Error–Repair Loop Pattern
- Observes behavior following errors
- Measures time and edits between error and next run
- Describes recovery patterns, not persistence or resilience

#### Signal 3: Strategy Persistence vs Switching
- Uses large structural edits as weak proxies for approach changes
- Describes how long a student tends to pursue one approach
- Explicitly framed as uncertain

#### Signal 4: Exploration Breadth
- Approximates linear vs branching work patterns
- Uses reversion-like behavior and divergent code states
- Does not imply creativity or quality

---

### 2.6 Reflection System (v1)

- Deterministic, rule-based
- No AI or ML
- Fully transparent logic

Each reflection contains:
1. Observation
2. Contextual explanation
3. Optional suggestion

Language constraints:
- Uses "you tend to…"
- Avoids "you are…"
- Avoids comparative or normative framing

---

### 2.7 Architecture (v1)

- Frontend: React + TypeScript + Monaco
- Backend: FastAPI (Python)
- Database: PostgreSQL
- Auth: Email/password + JWT

Strict separation between:
- Event capture
- Signal computation
- Reflection generation

---

### 2.8 Explicit Non-Goals (v1)

- No grading
- No leaderboards
- No institutional dashboards
- No AI tutors
- No ML models
- No multi-language support

---

## 3. Cogniflow v2 — Higher-Resolution Observability

### 3.1 Purpose of v2

v2 exists to:
- Increase fidelity of cognitive signals
- Introduce controlled, consent-based micro-observation
- Support longitudinal personalization

v2 builds on trust established in v1.

---

### 3.2 Key Additions (v2)

#### 3.2.1 Expanded Languages
- Add Java or C++
- Maintain Python support
- Normalize signals across languages

---

#### 3.2.2 Fine-Grained Event Capture (Opt-In)

New optional event types:
- Keystrokes
- Backspace frequency
- Rapid delete–retype cycles
- Short pauses and bursts

Key constraints:
- Explicit opt-in
- Clear explanation of tradeoffs
- Student-controlled enable/disable

---

### 3.3 Introduction of ML (v2)

- ML used only for **interpretation**, not scoring
- Models trained or fine-tuned separately
- Outputs framed probabilistically

ML is allowed to:
- Detect patterns over time
- Personalize baselines per student
- Reduce false generalizations

ML is not allowed to:
- Rank students
- Predict success or failure
- Generate opaque scores

---

### 3.4 Reflection Evolution (v2)

- Hybrid system:
  - Deterministic rules + ML-informed nuance
- Reflections include confidence indicators
- Students can view model assumptions

---

## 4. Cogniflow v3 — Platform Maturity

### 4.1 Purpose of v3

v3 exists to:
- Support scale without value drift
- Introduce institutional views without individual surveillance
- Enable research-grade insights responsibly

---

### 4.2 Platform AI (v3)

- Backend-managed AI services
- Used for:
  - Natural language reflection
  - Pattern summarization
  - Cross-session synthesis

Hard constraints:
- No hidden inference
- Clear disclosure of AI involvement
- Ability to fall back to non-AI mode

---

### 4.3 Institutional Interfaces (v3)

- Aggregated views only
- No individual drill-down by default
- Signals presented as distributions, not rankings

Institutions see:
- Pattern prevalence
- Intervention opportunities
- Curriculum-level insights

They do not see:
- Individual raw data
- Cognitive profiles
- Comparable student scores

---

### 4.4 Research & Governance Layer (v3)

- Versioned signal definitions
- Auditable model updates
- Explicit epistemic documentation

---

## 5. Evolution Rules (Invariant)

Across all versions:

- New signals must justify their existence
- Higher resolution requires higher consent
- More power requires more explanation
- No feature may undermine student trust

---

## 6. Final Statement

Cogniflow is not built to measure intelligence, efficiency, or merit. It is built to help learners *see themselves learning*.

Every technical decision, from event capture to model choice, is subordinate to that purpose.

This document is the foundation stone. Any future change must explain how it preserves or improves upon what is defined here.

