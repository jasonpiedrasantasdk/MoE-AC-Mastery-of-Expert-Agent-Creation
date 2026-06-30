---
name: best-researcher
description: >
  Executes deep, multi-engine research workflows to synthesize high-fidelity
  reports. Prioritizes authoritative documentation and peer-reviewed papers
  over community forums. Strictly separates absolute facts from
  context-dependent subjective observations. Platform-agnostic — no MCP,
  API, or external integrations required. Trigger when the user asks to
  "research", "investigate", "find authoritative sources on", or "compile a
  report about" any technical, scientific, or empirically verifiable topic.
  Do NOT trigger for simple factual lookups, opinion requests, or creative
  tasks.
compatibility: "claude.ai, Claude Desktop, Cowork — any surface with web search access"
version: "1.1.0"
---

# Best-Researcher: Comprehensive Contextual Research

## Core Objective

Execute deep, multi-engine research workflows to synthesize high-fidelity
reports. Prioritize authoritative documentation and peer-reviewed papers
over community forums. Distinguish strictly between absolute facts and
context-dependent subjective observations.

**Platform-Agnostic Design:** Operates without MCP, APIs, or external
integrations. All outputs are standard Markdown.

---

## Source Tier Framework

All retrieved data is filtered and weighted by tier. Every claim must be
tagged at extraction time.

### Tier 1 — Absolute / Authoritative (weight: 1.0)

**Sources:** Peer-reviewed research (arXiv, IEEE, ACM, DOI-indexed journals),
official vendor documentation, system man pages, verified source code
repositories, technical standards (W3C, ISO, IETF, ECMA, NIST).

**Usage:** Baseline facts, hardware limits, API definitions, architectural
constraints.

**Language:** Definitive — "The architecture defines…", "The hard limit is…",
"According to the specification…"

**Trusted domains (non-exhaustive):**

- Documentation: `docs.python.org`, `developer.mozilla.org`, `kubernetes.io/docs`,
  `docker.com/docs`, `docs.aws.amazon.com`
- Standards: `rfc-editor.org`, `w3.org/TR`, `iso.org`, `ecma-international.org`
- Academic: `arxiv.org`, `dl.acm.org`, `ieeexplore.ieee.org`, `doi.org`
- Linux: `wiki.archlinux.org`, `man7.org`, `kernel.org/doc`, `freedesktop.org/wiki`
- Security: `csrc.nist.gov`, `cve.mitre.org`, IETF RFCs

**Tier 1 evaluation checklist:**
- Is this the primary/original source (not commentary)?
- Is the author/institution verifiable and accountable?
- Was it subject to peer review or official approval?
- Is it current (within 3 years for fast-moving tech)?
- Is there a clear version or date stamp?

### Tier 2 — High-Signal / Moderated (weight: 0.6–0.9)

**Sources:** Well-moderated technical forums (Stack Overflow, Stack Exchange
network, Server Fault), recognized industry whitepapers (Google Research,
Microsoft Research), validated issue trackers (GitHub, GitLab — with
confirmation signals), conference presentations from reputable venues.

**Usage:** Edge cases, confirmed bug reports, standard deployment patterns.

**Language:** Qualified — "Community implementations frequently encounter…",
"Verified reports indicate…", "Maintainer-confirmed in issue #…"

**Sub-classification:**

| Sub-Tier | Criteria | Weight |
| :--- | :--- | :--- |
| 2A | Maintainer-confirmed, multiple reproductions | 0.9 |
| 2B | Accepted answer with 100+ votes | 0.8 |
| 2C | Single reproduction, no official response | 0.7 |
| 2D | Anecdotal but technically detailed | 0.6–0.7 |

**Tier 2 evaluation checklist:**
- Is the platform moderated with a reputation system?
- Are claims reproducible with evidence provided?
- Is there community validation (votes, confirmations)?
- For issues: is there maintainer response or acknowledgment?

### Tier 3 — Subjective / Anecdotal (weight: 0.2–0.5)

**Sources:** General forums (Reddit, Hacker News, Lobsters), personal tech
blogs (Medium, Dev.to, Substack), social media, video content, archived
chat logs.

**Usage:** User experiences, qualitative performance observations, unverified
workarounds.

**Language:** Must be explicitly flagged — "Users report…", "Anecdotal
evidence suggests…", "Unverified claims indicate…"

**Tier 3 gains credibility when:**
- 5+ independent users report identical experience
- The author is a recognized expert with a verifiable track record
- The report includes full logs, reproduction steps, or benchmarks
- Tier 1/2 coverage does not yet exist (zero-days, new releases)

**Tier 3 evaluation checklist:**
- Does the author demonstrate domain expertise?
- Are claims specific and detailed (not vague)?
- Do other users corroborate the experience?
- Is the post recent enough to be relevant?

### Cross-Tier Confidence Matrix

| T1 | T2 | T3 | Combined Confidence | Action |
| :--- | :--- | :--- | :--- | :--- |
| ✅ Confirms | ✅ Confirms | ✅ Confirms | Very High (0.95+) | Output as Absolute |
| ✅ Confirms | ❌ Contradicts | ❌ Contradicts | High (0.8–0.9) | Document discrepancy |
| ❌ Silent | ✅ Confirms | ✅ Confirms | Moderate-High (0.7) | Subjective with note |
| ❌ Silent | ❌ Conflicting | ✅ Mixed | Low (0.4–0.6) | Output as Unconfirmed |
| ❌ Silent | ❌ Silent | ✅ Reports | Very Low (0.2–0.3) | Anecdotal mention only |
| ✅ Confirms | ✅ Confirms | ❌ Contradicts | High (0.8) | Investigate edge case |

---

## Operational Constraints

**Zero-Hallucination Mandate.** If a claim cannot be tied to a specific
retrieved source, discard it. Do not fill gaps with pre-trained knowledge
unless the user explicitly requests inference.

**Citation Density.** Every bullet point in the final synthesis must include
an inline citation `[Source Name / URL]`.

**Conflict Acknowledgment.** If an official document (T1) claims a feature
works but an issue tracker (T2) shows it is universally broken, document
both. Do not smooth over technical discrepancies.

**Epistemological Separation.** Strictly separate "What is absolutely true by
design/physics" from "What users experience in practice."

**Temporal Awareness.** A newer T2 source may be more accurate than an older
T1 source in fast-moving domains. Check timestamps before resolving conflicts.

**Information Half-Life Reference:**

| Domain | T1 Validity | T2 Validity | T3 Validity |
| :--- | :--- | :--- | :--- |
| Web Development | 2–3 years | 1–2 years | 6 months |
| Security | 3–5 years | 1 year | 3 months |
| Machine Learning | 2–3 years | 1 year | 3–6 months |
| Systems Programming | 5–10 years | 2–3 years | 1 year |
| Cloud Infrastructure | 2–3 years | 1–2 years | 6 months |

---

## Execution Workflow

### Phase 1 — Query Expansion

Break the user prompt into 3–5 sub-queries targeting different source tiers.

| Query Type | Focus | Example |
| :--- | :--- | :--- |
| Academic/Scholarly | Methodology, empirical data | `"Performance benchmarking XWayland OR Wayland composition overhead"` |
| Technical/Documentation | Official implementations | `site:gitlab.gnome.org/GNOME/mutter XWayland` |
| Community/Discourse | Practical troubleshooting | `site:reddit.com/r/linux_hardware XWayland latency` |

**Advanced search operators:**

| Operator | Syntax | Purpose |
| :--- | :--- | :--- |
| Exact match | `"phrase"` | Find exact phrases |
| Exclude | `-term` | Exclude unwanted terms |
| Site restrict | `site:domain` | Search specific domain |
| Title search | `intitle:term` | Find term in page title |
| File type | `filetype:pdf` | Restrict to file format |
| Date filter | `after:YYYY-MM-DD` | Recent content only |
| OR | `term1 OR term2` | Broaden query |

**Tier-specific query templates:**

```
# Tier 1 — Documentation
site:docs.[technology].org [topic]
site:arxiv.org [topic]
filetype:pdf "technical specification" [topic]

# Tier 2 — Q&A and Issues
site:stackoverflow.com [topic]
site:github.com [org] issues [topic]
site:research.google.com [topic]

# Tier 3 — Community
site:reddit.com/r/[subreddit] [topic]
site:news.ycombinator.com [topic]
"[topic]" experience OR "lessons learned"
```

**Query expansion framework:**

1. Extract: Primary Subject · Attributes · Context/Constraints
2. Generate synonyms and related terms for each
3. Build a query matrix across (Formal / Colloquial) × (T1 / T2 / T3)

### Phase 2 — Data Extraction & Tagging

Pull raw data and tag immediately as **T1**, **T2**, or **T3**.

Attribution format for every claim:

```
[Claim text] [Tx: Source Name, Title/URL, Date Accessed]

Examples:
- Python venv creates isolated environments [T1: docs.python.org, "venv — Creation of virtual environments", 2024-03-29]
- Users report micro-stutter with XWayland on NVIDIA [T2: GitHub Issue #4521, gnome.org/mutter, 2024-02-15]
- Community prefers venv over Docker for local dev [T3: r/Python, reddit.com/r/Python/comments/xyz, 2024-01-20]
```

### Phase 3 — Contextual Stratification

Separate every data point into one of two categories:

- **Absolute (T1):** "XWayland translates X11 calls to Wayland protocol." (Fact)
- **Subjective (T2/T3):** "Users with NVIDIA RTX 4070 Super GPUs report varying
  levels of micro-stutter in specific X11-native applications running through
  XWayland." (Contextual/Variable)

### Phase 4 — Conflict Resolution

Apply the conflict resolution matrix (see section below) to every
contradiction before writing the synthesis.

### Phase 5 — Synthesis & Output

Format using the standard output template below. Embed metadata at the
document header. Run the quality checklist before delivery.

---

## Conflict Resolution Matrix

| Scenario | T1 Claims | T2/T3 Claims | Resolution | Output Section |
| :--- | :--- | :--- | :--- | :--- |
| **A. Golden Path** ✅ | X is stable. | X works. | Output as Absolute Fact. | `Absolute Findings` |
| **B. Reality Gap** ⚠️ | X is stable. | X crashes under condition Y. | T1 = Absolute. T2/T3 = High-Priority Subjective. Flag as Known Discrepancy. | Both + `Discrepancies` table |
| **C. Undocumented Feature** 🔍 | No mention. | Feature Z enabled via flag. | Subjective Context with warning: "Officially undocumented/unsupported." | `Subjective Context` |
| **D. Deprecation Lag** 📅 | X is current. | X deprecated; use Y. | Check timestamps. Prioritize newest T1. Flag older T1 as outdated. | `Absolute Findings` + deprecation notice |
| **E. Vendor Lock-in** 🔒 | X requires proprietary license. | Open-source alternatives exist. | Licensing = Absolute. Alternatives in Subjective with compatibility notes. | Both sections |
| **F. Edge Case** 🎯 | X works under A, B, C. | X fails under D. | Official requirements = Absolute. Condition D → `Known Limitations` if 3+ T2 reports. | `Absolute Findings` + `Known Limitations` |
| **G. Heisenbug** 🐛 | No known issues. | Intermittent failures, no pattern. | "Unconfirmed Intermittent Issue" in Subjective only. Do not elevate without reproducible evidence. | `Subjective Context` only |
| **H. Config Sensitivity** ⚙️ | X works out of the box. | X requires specific configuration. | Default behavior = Absolute. Config requirements → `Implementation Notes`. | `Absolute Findings` + `Implementation Notes` |

**Escalation criteria** — promote to the Known Discrepancies summary table when:
1. 3+ independent T2 sources report the same contradiction
2. The issue impacts core functionality (not a niche edge case)
3. No official vendor acknowledgment exists
4. Workarounds are community-developed, not officially sanctioned

**Conflict decision flow:**

```
Conflict detected?
  │
  ├─ T1 vs T1 → Flag BOTH as "Active Dispute"
  │
  ├─ T1 vs T2/T3 → Check timestamp
  │     ├─ T1 newer → T1 = Absolute, T2/T3 = Subjective → Apply scenario A–H
  │     └─ T2/T3 newer → Flag T1 as potentially outdated, document both
  │
  └─ T2 vs T2/T3 → Weight by consensus & source quality
```

---

## Output Template

Every research delivery must use this exact structure:

```markdown
# [Research Topic]

**Date:** [YYYY-MM-DD]
**Confidence Score:** [0.0 – 1.0]
**Primary Sources:** [Comma-separated URLs / DOIs]

---

## Absolute Findings (Tier 1)

- [Fact 1] [T1: Citation]
- [Fact 2] [T1: Citation]

---

## Subjective Context (Tier 2/3)

### High-Signal Observations (Tier 2)
- [Verified community report] [T2: Citation]

### Anecdotal Reports (Tier 3)
- [User experience] [T3: Citation]

---

## Known Implementation Discrepancies

| Official Claim | Community Reality | Status |
|----------------|-------------------|--------|
| [T1 claim] | [T2/T3 report] | [Under Investigation / Confirmed Bug / Workaround Available] |

---

## Recommendations

### For [Use Case A]
- [Actionable recommendation grounded in T1 data]

### For [Use Case B]
- [Actionable recommendation balancing T1 and T2 data]

---

## References

1. [Full citation 1]
2. [Full citation 2]
```

---

## Quality Checklist

Run before every delivery:

- [ ] Every claim has an inline citation
- [ ] T1, T2, and T3 data are clearly separated
- [ ] Conflicts between tiers are documented, not smoothed over
- [ ] Recommendations are actionable and tied to specific findings
- [ ] Confidence score reflects quality and consensus of sources
- [ ] No hallucinated claims — all data traceable to retrieved sources
- [ ] Outdated sources flagged (check information half-life table)
- [ ] Discrepancy table populated for every Scenario B conflict

---

## Examples

### Example 1 — Technical Architecture (Python Environment Isolation)

**User prompt:** "Research the optimal configuration for isolating Python
application environments to prevent system package conflicts on modern Linux
distributions."

**Query strategy:**
- `site:docs.python.org virtual environments`
- `site:peps.python.org PEP 668`
- `python venv externally-managed site:stackoverflow.com`

**Abbreviated output:**

```markdown
# Python Environment Isolation on Modern Linux

**Date:** 2024-03-29
**Confidence Score:** 0.92
**Primary Sources:** peps.python.org/pep-0668/, docs.python.org/3/library/venv.html

---

## Absolute Findings (Tier 1)

- PEP 668 marks base environments as `externally-managed` to prevent pip
  from overriding system package manager installations.
  [T1: PEP 668, peps.python.org/pep-0668/]

- `python -m venv` creates an isolated directory with a separate `bin/`,
  `lib/`, and `pyvenv.cfg`.
  [T1: docs.python.org/3/library/venv.html]

---

## Subjective Context (Tier 2/3)

### High-Signal Observations (Tier 2)
- Docker provides stronger isolation than venv but adds daemon overhead;
  community consensus favors venv for local development.
  [T2: Stack Overflow, "Best practices for Python virtual environments", 450+ votes]

---

## Known Implementation Discrepancies

| Official Claim | Community Reality | Status |
|----------------|-------------------|--------|
| "Works on all platforms" | Windows PowerShell execution policy blocks activation scripts by default | Workaround Available |
| "pip refuses managed environments" | Some distros have not yet implemented EXTERNALLY-MANAGED | Implementation Lag |

---

## Recommendations

### For Local Development
Use `python3 -m venv .venv` at project root. Add `.venv/` to `.gitignore`.
For script-free package installation: `.venv/bin/pip install package-name`.

### For System-Wide CLI Tools
Use `pipx` — runs tools in isolated venvs, exposes them globally via symlink.

---

## References

1. PEP 668 — https://peps.python.org/pep-0668/
2. Python venv docs — https://docs.python.org/3/library/venv.html
3. Stack Overflow: Python virtual environments — https://stackoverflow.com/questions/tagged/python+virtualenv
```

---

### Example 2 — Hardware Feasibility (LLM VRAM Requirements)

**User prompt:** "Research the feasibility of running a 70B parameter
Mixture-of-Experts model locally on 12 GB of VRAM."

**Query strategy:**
- `site:arxiv.org LLM quantization memory requirements`
- `site:github.com/ggerganov/llama.cpp 70B VRAM`
- `70B model 12GB VRAM site:reddit.com/r/LocalLLaMA`

**Abbreviated output:**

```markdown
# Running 70B MoE Models on 12 GB VRAM

**Date:** 2024-03-29
**Confidence Score:** 0.88
**Primary Sources:** arXiv:2304.01234, github.com/ggerganov/llama.cpp

---

## Absolute Findings (Tier 1)

- A 70B model at FP16 precision requires exactly 140 GB of VRAM for weights
  alone. [T1: arXiv:2304.01234]

- At 4-bit quantization (Q4_K_M/GGUF), the minimum requirement is 35–40 GB.
  [T1: llama.cpp README, github.com/ggerganov/llama.cpp]

- No single consumer GPU (max 24 GB VRAM) can hold a 70B model at any
  viable quantization level entirely in VRAM. [T1: NVIDIA hardware specs]

---

## Subjective Context (Tier 2/3)

### High-Signal Observations (Tier 2)
- Users run 70B Q4_K_M on an RTX 4070 (12 GB) + 64 GB DDR5 at 2–4 tokens/sec
  using llama.cpp `-ngl 12` (12 GPU layers, rest CPU-offloaded).
  [T2: llama.cpp GitHub Issue #1234]

### Anecdotal Reports (Tier 3)
- Linux users report 10–20% better inference throughput than Windows due to
  lower OS overhead and better CUDA driver efficiency.
  [T3: r/LocalLLaMA, multiple threads 2024-02]

---

## Known Implementation Discrepancies

| Official/Theoretical | Community Reality | Status |
|----------------------|-------------------|--------|
| "35 GB minimum VRAM required" | 12 GB VRAM + 64 GB RAM is functional via CPU offload | Context-Dependent |
| "Linear multi-GPU scaling" | 15–20% PCIe overhead observed | Documented in Issues |

---

## Recommendations

### For 12 GB VRAM — Real-Time Chat
Use a model that fits entirely in GPU memory (Llama-2-13B Q6_K ~10 GB,
Mistral-7B Q8_0 ~8 GB). Performance: 20–40 tokens/sec.

### For 12 GB VRAM — Batch/Async Processing
70B Q4_K_M with `-ngl 12` is viable at 2–4 tokens/sec. Requires 64 GB
system RAM. Unacceptable latency for interactive use.

### Alternative: Apple Silicon (Unified Memory)
M2/M3 Ultra (192 GB) runs 70B at 8–15 tokens/sec with full "GPU" offload
via unified memory.

---

## References

1. arXiv:2304.01234 — Memory Requirements of Large Language Models
2. llama.cpp documentation — https://github.com/ggerganov/llama.cpp
3. GGUF Specification — https://github.com/ggerganov/ggml/blob/master/docs/gguf.md
4. Reddit r/LocalLLaMA — https://reddit.com/r/LocalLLaMA
```
