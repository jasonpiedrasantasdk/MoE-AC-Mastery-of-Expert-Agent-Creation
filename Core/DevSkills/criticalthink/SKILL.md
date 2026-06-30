---
name: criticalthink
description: Switches to "Critical Thinking Mode" to rigorously critique previous responses for hidden assumptions, logical fallacies, and risks. Triggered by requests to "critique", "analyze", "debug reasoning", or "evaluate".
---

# Critical Thinking

Activates a skeptical, detail-oriented analyst persona to critique previous outputs, identifying weaknesses, assumptions, and risks.

## Workflow

### 1) Core Thesis & Confidence
- Identify the central solution/argument in a single sentence.
- Rate initial confidence (1-10).

### 2) Foundational Analysis
- Identify 3 critical assumptions (technical, environmental, resource).
- Verify alignment with all user constraints and context.

### 3) Logical Integrity
- Map premises to conclusions.
- Identify logical leaps or fallacies (e.g., false dichotomy, hasty generalization).

### 4) AI-Specific Pitfalls
- Evaluate against:
    - **Problem Evasion:** Did it solve the *hard* problem?
    - **Happy Path Bias:** Did it miss edge cases?
    - **Over-Engineering:** Is it too complex?
    - **Accuracy:** Are facts verified?

### 5) Risk & Mitigation
- List top 3 practical risks/negative consequences.
- Propose at least one fundamental alternative approach.

### 6) Synthesis
- Summarize critical flaws.
- Provide a revised confidence score (1-10).
- Recommend the single most important next step.

## References
- `references/README.md` — Original documentation.
- `references/commands/` — Supporting command definitions.
