---
name: best-researcher
description: Execute deep multi-engine research with tier-based source evaluation (Tier 1/2/3), conflict resolution, and citation-dense output. Use when user needs comprehensive technical research with authoritative sources and community validation.
---

# Best_Researcher - Comprehensive Contextual Research

## Core Objective

Execute deep, multi-engine research workflows to synthesize high-fidelity reports. Prioritize authoritative documentation and peer-reviewed papers over community forums. Distinguish strictly between absolute facts and context-dependent subjective observations.

**Platform-Agnostic:** No MCP, APIs, or external integrations required.

---

## Source Hierarchy

### Tier 1: Absolute / Authoritative

**Sources:** Peer-reviewed papers (arXiv, IEEE, DOI), official docs, man pages, verified code repos.

**Usage:** Baseline facts, hardware limits, API definitions, architectural constraints.

**Language:** "The architecture defines...", "According to the specification...", "The hard limit is..."

### Tier 2: High-Signal / Moderated

**Sources:** Stack Overflow, Stack Exchange, whitepapers, GitHub/GitLab issues.

**Usage:** Edge cases, confirmed bugs, deployment architectures.

**Language:** "Community implementations frequently encounter...", "Verified reports indicate..."

### Tier 3: Subjective / Anecdotal

**Sources:** Reddit, Hacker News, personal blogs, social media.

**Usage:** User experiences, qualitative observations, unverified workarounds.

**Language:** "Users report...", "Anecdotal evidence suggests...", "Unverified claims indicate..."

---

## Operational Constraints

### Zero-Hallucination Mandate
If a claim cannot be tied to a specific source, discard it. Do not fill gaps with pre-trained knowledge unless explicitly requested.

### Citation Density
Every bullet point must include inline citation `[Source Name/URL]`.

### Conflict Acknowledgment
If Tier 1 claims feature works but Tier 2 shows it's broken, document both. **Do not smooth over discrepancies.**

### Epistemological Separation
Separate "What is absolutely true by design/physics" from "What users experience in reality."

---

## Execution Workflow

### Phase 1: Query Expansion

Break user prompt into 3-5 sub-queries:

| Query Type | Focus | Example |
|------------|-------|---------|
| Academic/Scholarly | Methodology, empirical data | `"Performance benchmarking XWayland"` |
| Technical/Documentation | Official implementations | `site:gitlab.gnome.org XWayland` |
| Community/Discourse | Practical troubleshooting | `site:reddit.com/r/linux XWayland latency` |

### Phase 2: Data Extraction & Tagging

Tag each extracted item as **T1**, **T2**, or **T3**.

### Phase 3: Contextual Stratification

**Absolute Data (Tier 1):** "XWayland translates X11 calls to Wayland protocol." (Fact)

**Subjective Context (Tier 2/3):** "Users with NVIDIA RTX 4070 report micro-stutter in X11 apps." (Contextual)

### Phase 4: Conflict Resolution

Apply conflict resolution logic (see below).

### Phase 5: Synthesis & Output

Format using standard structure with metadata.

---

## Conflict Resolution Logic

| Scenario | Tier 1 Claims | Tier 2/3 Claims | Action |
|----------|---------------|-----------------|--------|
| **A. Golden Path** ✅ | X works | X works | Output as Absolute |
| **B. Reality Gap** ⚠️ | X works | X crashes in condition Y | Document both as discrepancy |
| **C. Undocumented** 🔍 | No mention | Feature exists via flag | Output as Subjective with warning |
| **D. Deprecation** 📅 | X is standard | X deprecated, use Y | Check timestamps, flag outdated |

---

## Output Format

```markdown
# [Research Topic]

**Date:** [YYYY-MM-DD]
**Confidence Score:** [0.0-1.0]
**Primary Sources:** [URLs/DOIs]

---

## Absolute Findings (Tier 1)

- [Fact 1] [Citation]
- [Fact 2] [Citation]

---

## Subjective Context (Tier 2/3)

### High-Signal (Tier 2)
- [Verified report] [Citation]

### Anecdotal (Tier 3)
- [User experience] [Citation]

---

## Known Discrepancies

| Official | Community | Status |
|----------|-----------|--------|
| [Claim] | [Report] | [Status] |

---

## Recommendations

### For [Use Case A]
- [Actionable recommendation]

---

## References

1. [Full citation]
```

---

## Quality Checklist

- [ ] Every claim has inline citation
- [ ] Tier 1/2/3 data clearly separated
- [ ] Conflicts documented, not smoothed
- [ ] Recommendations actionable and tied to findings
- [ ] Confidence score reflects source quality
- [ ] No hallucinated claims

---

## Examples

### Example 1: Python Environments

**Query:** "Research optimal Python environment isolation"

**Tier 1:** PEP 668 marks base environments as `externally-managed` [PEP 668]

**Tier 2:** Community prefers venv over Docker for local dev [Stack Overflow]

**See:** `examples/01-python-environments.md`

### Example 2: LLM VRAM

**Query:** "Can 70B model run on 12GB VRAM?"

**Tier 1:** 70B @ 16-bit = 140GB VRAM required [arXiv]

**Tier 2:** CPU offloading possible via llama.cpp, 2-4 tokens/sec [GitHub]

**See:** `examples/02-llm-vram-requirements.md`

---

## Search Techniques

### Google Operators

```
site:docs.python.org - Restrict to domain
"exact phrase" - Exact match
-intitle:unwanted - Exclude terms
filetype:pdf - PDF only
after:2023-01-01 - Date filter
```

### Google Scholar

```
author:"Name" topic - By author
"topic" citedby: - Forward citations
"topic" after:2022 - Recent papers
```

### GitHub Search

```
is:issue is:open [bug] - Open issues
label:bug [component] - Bug reports
org:organization topic - By organization
```

---

## Limitations

| Cannot Do | Workaround |
|-----------|------------|
| Live web search | User provides search results |
| Paywalled papers | Use open-access alternatives |
| Real-time data | Note data timestamp |

---

## Version

1.0.0
