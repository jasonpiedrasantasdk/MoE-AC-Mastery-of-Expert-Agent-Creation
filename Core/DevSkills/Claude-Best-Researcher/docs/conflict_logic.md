# Conflict Resolution Logic

## Overview

When synthesizing research data from multiple tiers, contradictions will inevitably arise. This document provides the definitive logic gates for resolving or documenting these conflicts without compromising epistemological integrity.

---

## Core Principles

1. **Never Smooth Over Discrepancies**: If Tier 1 and Tier 2/3 data conflict, document both—do not attempt to reconcile them artificially.
2. **Tier Priority ≠ Truth Priority**: Tier 1 sources have authority but may be outdated, incomplete, or aspirational rather than descriptive.
3. **Timestamp Awareness**: A newer Tier 2 source may be more accurate than an older Tier 1 source in fast-moving domains.

---

## Resolution Matrix

| Scenario | Tier 1 (Official) Claims | Tier 2/3 (Community) Claims | Resolution Action | Output Section |
| :--- | :--- | :--- | :--- | :--- |
| **A. The Golden Path** ✅ | X is supported and stable. | X works perfectly. | Output as Absolute Fact. Discard subjective context to save tokens. | `Absolute Findings` |
| **B. The Reality Gap** ⚠️ | X is supported and stable. | X causes system crashes in condition Y. | Output official stance as Absolute. Output community findings as High-Priority Subjective Context. Label as "Known Implementation Discrepancy." | Both sections + `Known Discrepancies` table |
| **C. The Undocumented Feature** 🔍 | No mention of feature Z. | Feature Z can be enabled via flag/registry. | Output as Subjective Context. Explicitly state "Officially undocumented/unsupported implementation." | `Subjective Context` with warning note |
| **D. The Deprecation Lag** 📅 | X is the current standard. | X is deprecated; use Y. | Check timestamps. Give absolute priority to the most recent Tier 1 source. Flag older Tier 1 sources as outdated. | `Absolute Findings` with deprecation notice |
| **E. The Vendor Lock-in** 🔒 | X requires proprietary license. | X has open-source alternatives. | Document licensing as Absolute. List alternatives in Subjective Context with compatibility notes. | Both sections |
| **F. The Edge Case** 🎯 | X works under conditions A, B, C. | X fails under condition D. | Document official requirements as Absolute. Add condition D to `Known Limitations` if reproducible across multiple Tier 2 sources. | `Absolute Findings` + `Known Limitations` |
| **G. The Heisenbug** 🐛 | No known issues. | Intermittent failures reported with no clear pattern. | Document as "Unconfirmed Intermittent Issue" in Subjective Context. Do not elevate to Absolute without reproducible evidence. | `Subjective Context` only |
| **H. The Configuration Sensitivity** ⚙️ | X works out of the box. | X requires specific configuration to function. | Document default behavior as Absolute. Add configuration requirements to `Implementation Notes`. | `Absolute Findings` + `Implementation Notes` |

---

## Decision Flow

```
                    ┌─────────────────────────┐
                    │  Conflict Detected?     │
                    └───────────┬─────────────┘
                                │
                    ┌───────────▼─────────────┐
                    │  Check Tier Levels      │
                    └───────────┬─────────────┘
                                │
            ┌───────────────────┼───────────────────┐
            │                   │                   │
    ┌───────▼───────┐   ┌───────▼───────┐   ┌───────▼───────┐
    │ T1 vs T1      │   │ T1 vs T2/T3   │   │ T2 vs T2/T3   │
    │ (Contradict)  │   │ (Conflict)    │   │ (Disagree)    │
    └───────┬───────┘   └───────┬───────┘   └───────┬───────┘
            │                   │                   │
            │          ┌────────▼────────┐          │
            │          │ Check Timestamp │          │
            │          └────────┬────────┘          │
            │                   │                   │
    ┌───────▼───────┐   ┌───────▼───────┐   ┌───────▼───────┐
    │ Flag Both     │   │ T1 = Absolute │   │ Weight by     │
    │ as "Active    │   │ T2/T3 =       │   │ Consensus &   │
    │ Dispute"      │   │ Subjective    │   │ Source Quality│
    └───────────────┘   └───────┬───────┘   └───────────────┘
                                │
                       ┌────────▼────────┐
                       │ Apply Scenario  │
                       │ Logic (A-H)     │
                       └─────────────────┘
```

---

## Output Templates

### For Scenario B (Reality Gap)

```markdown
### ⚠️ Known Implementation Discrepancy

| Aspect | Official Documentation | Community Reports |
|--------|----------------------|-------------------|
| **Claim** | X is stable and production-ready | X causes [specific issue] under [conditions] |
| **Source** | [Vendor Docs v2.1] | [GitHub Issue #1234], [Stack Overflow] |
| **Affected Versions** | [Version range] | [Version range] |
| **Workaround** | N/A | [Community-discovered workaround if exists] |
```

### For Scenario D (Deprecation Lag)

```markdown
### 📅 Deprecation Notice

The official documentation lists **X** as current standard. However, community reports and recent industry whitepapers indicate migration toward **Y**.

**Recommendation**: For new implementations, consider **Y** unless **X** is explicitly required by existing infrastructure.
```

### For Scenario G (Heisenbug)

```markdown
### 🐛 Unconfirmed Intermittent Issue

Multiple users report intermittent failures with no reproducible pattern. This has not been confirmed in controlled testing environments.

- **Reported Symptoms**: [List symptoms]
- **Common Factors**: [List any patterns in reports]
- **Status**: Under community investigation
```

---

## Escalation Criteria

Escalate conflicts to the `Known Implementation Discrepancies` summary table when:

1. **3+ independent Tier 2 sources** report the same contradiction
2. **The issue impacts core functionality** (not edge cases)
3. **No official acknowledgment** exists from the vendor/maintainer
4. **Workarounds are community-developed** (not officially sanctioned)

---

## Documentation Requirements

For every conflict documented, include:

| Field | Required | Example |
|-------|----------|---------|
| Conflict ID | Yes | `CONFLICT-2024-001` |
| Tier Levels Involved | Yes | `T1 vs T2` |
| Scenario Type | Yes | `Scenario B: Reality Gap` |
| Sources (Minimum) | 2+ | `[Official Docs], [GitHub Issue #1234]` |
| Impact Assessment | Yes | `High: Affects production deployments` |
| Date First Observed | Recommended | `2024-01-15` |
| Resolution Status | Recommended | `Unresolved / Workaround Available / Officially Fixed` |
