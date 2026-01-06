# **COGNIFLOW — FINAL TECHNICAL DESIGN DOCUMENT**

**(Post-Audit, Long-Game Version)**

---

## **0\. Product Definition (One Sentence)**

**Cogniflow is a cognitive observability system that captures evidence of how students engage with coding problems and presents that evidence in a misuse-resistant, non-judgmental way to support teaching, self-reflection, and curriculum improvement.**

Not:

* an assessment engine  
* a grading tool  
* a ranking system  
* a cheating detector

---

## **1\. Constitutional Rules (Hard Constraints)**

These rules apply to **all versions**.

Breaking any one of them invalidates the product.

1. Cogniflow never outputs intelligence, ability, or quality judgments.  
2. Cogniflow never produces global or cross-student comparisons.  
3. Cogniflow never collapses behavior into a single score.  
4. Absence of observable evidence is neutral and non-actionable.  
5. Every insight must be traceable to observable behavior.  
6. Every insight must be explainable to the student it concerns.  
7. Cogniflow can inform decisions but cannot enforce them.

These are enforced **architecturally**, not via policy text.

---

## **2\. Core Abstraction (What the System Actually Does)**

### **Correct Mental Model**

Cogniflow does **not** analyze thinking.

It analyzes **behavioral traces of problem-solving**.

### **Canonical Pipeline**

User Actions  
   ↓  
Behavioral Signals  
   ↓  
Evidence Aggregation  
   ↓  
Human-Readable Insights  
   ↓  
Optional Human Action

There is **no automated decision point**.

---

## **3\. Scope Boundary (Non-Negotiable)**

### **In Scope (Initial \+ Long Game)**

* Coding problems  
* Observable editor behavior  
* Session-level and longitudinal analysis  
* Advisory insights only

### **Permanently Out of Scope**

* Intelligence prediction  
* Grades or marks  
* Hiring or placement use  
* Proctoring or surveillance  
* Psychological profiling  
* Enforcement or compliance actions

---

## **4\. Version Roadmap (Capability Layers)**

---

# **VERSION 1 — FOUNDATIONAL OBSERVABILITY**

**“Capture behavior. Prove value. Build trust.”**

---

## **v1.1 Functional Scope**

### **Input**

* Browser-based code editor  
* Python only  
* One problem per session

### **Captured Events (Strictly Limited)**

* code\_insert  
* code\_delete  
* run\_code  
* error (syntax/runtime/test)  
* idle (coarse)  
* submit

### **Explicitly NOT captured**

* raw keystrokes  
* clipboard sources  
* browsing behavior  
* screen or camera data

---

## **v1.2 Session Visibility (Critical Change)**

There is **no “NOP student” state**.

Instead, each session has a **Visibility Level**:

* High Process Visibility  
* Medium Process Visibility  
* Low Process Visibility

Low-visibility sessions:

* generate no insights  
* are excluded from aggregation  
* are not flagged or highlighted  
* are visually neutral in the UI

Silence is treated as **non-evidence**, not deficiency.

---

## **v1.3 Behavioral Signals (Derived, Not Stored Raw)**

Examples:

* planning\_latency  
* iteration\_depth  
* rewrite\_ratio  
* error\_transition\_pattern  
* structural\_convergence

These are computed from events, then raw events may be discarded or archived.

---

## **v1.4 Evidence Aggregation (Internal Model)**

Each signal contributes to **internal confidence scalars**:

confidence ∈ \[0.0, 1.0\]

These scalars:

* exist only server-side  
* are never serialized to clients  
* are never queryable by role-based APIs

They exist to support:

* longitudinal analysis  
* trend detection  
* future ML

---

## **v1.5 Teacher-Facing Output (UI Rule)**

Teachers do **not** see:

* raw signals  
* confidence values  
* graphs requiring interpretation

Teachers see **action-oriented cues only**:

“This student likely needs help with:  
▢ Understanding the problem  
▢ Translating logic into code  
▢ Debugging effectively”

Each cue:

* is binary  
* is explainable on click  
* links to observed session evidence

If no cue is reliable → nothing is shown.

---

## **v1.6 Student-Facing Output**

Students see:

* their own session timeline  
* descriptive feedback (non-comparative)  
* self-comparison over time only

Students never see:

* class distributions  
* teacher dashboards  
* institutional summaries

---

## **v1 Success Criteria**

* Teachers recognize patterns as plausible  
* Students do not feel judged  
* No stigmatization emerges  
* No misuse affordances exist

---

# **VERSION 2 — LONGITUDINAL EVIDENCE**

**“Trends, not moments.”**

---

## **v2 Additions**

* Multi-session aggregation  
* Trend consistency detection  
* Regression and improvement signals  
* Difficulty-normalized comparisons (self only)

### **New Rule**

**Single sessions never trigger interventions.**

---

## **v2 Insight Language (Mandatory)**

All insights are phrased as **deltas**:

* “More than your previous attempts”  
* “Less than before”  
* “No change detected”

No absolutes survive v2.

---

## **v2 Institutional View (Restricted)**

Institutions see:

* problem-level trends  
* curriculum friction points  
* teaching method signals

They never see:

* individual students  
* teacher comparisons  
* performance rankings

---

# **VERSION 3 — ML AS A MICROSCOPE**

**“Discover patterns, never judge.”**

---

## **v3 ML Scope (Strict)**

Allowed:

* clustering  
* anomaly surfacing  
* latent pattern discovery

Forbidden:

* scoring  
* prediction  
* ranking  
* automation of decisions

### **ML Output Rule**

ML outputs are **never user-facing**.

They are converted into:

* candidate hypotheses  
* which must pass rule-based explanation  
* before becoming visible insights

---

# **VERSION 4 — GUIDED REFLECTION**

**“Improve awareness, not obedience.”**

---

## **v4 Student Features**

* session replays with highlights  
* reflection prompts  
* self-questioning tools

No prescriptions.

No “do this next”.

---

## **v4 Teacher Features**

* intervention suggestions mapped to:  
  * concept clarity  
  * execution practice  
  * debugging support

Only one suggested action per insight.

---

# **VERSION 5 — FINAL PRODUCT**

**“Cognitive Infrastructure for Learning Systems.”**

---

## **End-State Capabilities**

* Supports coding, math, logic (domain-aware)  
* Acts as curriculum feedback loop  
* Improves teaching methods over time  
* Enhances student self-understanding

---

## **End-State Non-Capabilities**

* No rankings  
* No intelligence labels  
* No enforcement hooks  
* No hidden authority

---

## **6\. Misuse Resistance (Explicit)**

### **UI Guardrails**

* No sortable student lists  
* No side-by-side comparisons  
* No exportable tables  
* No stable ordering  
* Slight phrasing variation to resist scraping

### **Data Guardrails**

* No global normalization  
* No percentile math  
* No score-like artifacts

Bad faith use is not impossible — it is **operationally unattractive**.

---

## **7\. Business Reality (Long-Game Alignment)**

### **Buyer**

Institutions

### **Value Proposition**

* Curriculum risk detection  
* Teaching effectiveness insight  
* Accreditation and audit support  
* Defense against “bad cohort” narratives

### **Users**

Teachers and students

Cogniflow sells **institutional intelligence**, not student surveillance.

---

## **8\. Final Integrity Test**

If Cogniflow ever answers:

“How good is this student?”

instead of:

“What evidence do we have of their engagement with this problem?”

the product has failed.

---

## **Final Verdict**

This version of Cogniflow is:

* architecturally honest  
* incentive-aware  
* ethically survivable  
* resistant to power misuse  
* scalable without moral collapse

It is not easy.

But it is **real**.

