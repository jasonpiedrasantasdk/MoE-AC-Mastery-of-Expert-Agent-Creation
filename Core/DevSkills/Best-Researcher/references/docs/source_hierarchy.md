# Source Hierarchy & Evaluation Guide

## Overview

This document provides the definitive source hierarchy for the Best_Researcher skill, including detailed evaluation criteria, trusted source lists, and tier assignment guidelines.

---

## Source Tier Framework

```
┌─────────────────────────────────────────────────────────────┐
│                    TIER 1: ABSOLUTE                         │
│         Peer-Reviewed • Official • Verified Code            │
│         → Use for: Baseline facts, hard limits, specs       │
├─────────────────────────────────────────────────────────────┤
│                  TIER 2: HIGH-SIGNAL                        │
│         Moderated Forums • Issue Trackers • Whitepapers     │
│         → Use for: Edge cases, bugs, implementations        │
├─────────────────────────────────────────────────────────────┤
│                  TIER 3: SUBJECTIVE                         │
│         General Forums • Blogs • Social Media               │
│         → Use for: User experiences, qualitative data       │
└─────────────────────────────────────────────────────────────┘
```

---

## Tier 1: Absolute / Authoritative Sources

### Characteristics

- **Verifiable**: Claims can be independently confirmed
- **Accountable**: Named authors/institutions with reputations
- **Reviewed**: Peer review, technical review, or official approval process
- **Stable**: Persistent URLs, versioned, archived
- **Primary**: Original source, not commentary on other work

### Accepted Source Types

| Category | Sources | Confidence Weight |
|----------|---------|-------------------|
| **Peer-Reviewed Research** | arXiv, IEEE, ACM, DOI-indexed journals | 1.0 |
| **Official Documentation** | Vendor docs, man pages, RFCs, standards bodies | 1.0 |
| **Verified Source Code** | Official repos (verified org), tagged releases | 1.0 |
| **Technical Specifications** | W3C, ISO, ECMA, IETF standards | 1.0 |
| **Government/Regulatory** | NIST, NSA, CISA, FDA guidance | 1.0 |

### Trusted Source Lists by Domain

#### Computer Science & Software

```
# Documentation
docs.python.org
developer.mozilla.org
docs.microsoft.com
docs.aws.amazon.com
kubernetes.io/docs
docker.com/docs

# Standards & RFCs
rfc-editor.org
w3.org/TR
ecma-international.org
iso.org

# Code Repositories (Official)
github.com/[verified-organizations]
gitlab.com/[verified-organizations]
```

#### Academic Databases

```
# Computer Science
arxiv.org (cs.* categories)
dl.acm.org
ieeexplore.ieee.org
usenix.org

# Multi-Disciplinary
doi.org
scholar.google.com
pubmed.ncbi.nlm.nih.gov
```

#### Linux & Open Source

```
# Distribution Documentation
wiki.archlinux.org
ubuntu.com/server/docs
debian.org/doc

# Man Pages & Technical
man7.org
kernel.org/doc
freedesktop.org/wiki
```

### Evaluation Checklist for Tier 1

```
□ Is this the primary/original source?
□ Does the author have verifiable credentials?
□ Is there a review process (peer/editorial)?
□ Is the publication venue reputable?
□ Is the information current (within 3 years for tech)?
□ Are claims backed by evidence or specification?
□ Is there a clear version/date stamp?
□ Can I find this in multiple Tier 1 sources?
```

---

## Tier 2: High-Signal / Moderated Sources

### Characteristics

- **Moderated**: Some quality control (votes, moderation, review)
- **Technical**: Focused on implementation and troubleshooting
- **Attributed**: User identities with reputation history
- **Specific**: Addresses concrete problems with reproducible details

### Accepted Source Types

| Category | Sources | Confidence Weight |
|----------|---------|-------------------|
| **Technical Q&A** | Stack Overflow, Server Fault, Stack Exchange | 0.8 |
| **Issue Trackers** | GitHub Issues, GitLab Issues (with confirmation) | 0.7-0.9 |
| **Industry Whitepapers** | Google Research, Microsoft Research, etc. | 0.8-0.9 |
| **Conference Talks** | Recorded presentations from reputable conferences | 0.7 |
| **Verified Experts** | Recognized community experts with track record | 0.7-0.8 |

### Trusted Source Lists by Category

#### Technical Q&A Platforms

```
# Stack Exchange Network
stackoverflow.com (general programming)
serverfault.com (system administration)
superuser.com (general computing)
unix.stackexchange.com (Unix/Linux)
security.stackexchange.com (infosec)
dba.stackexchange.com (databases)
```

#### Issue Trackers (Quality Varies by Project)

```
# High-Quality Trackers (Strict Triage)
github.com/kubernetes/kubernetes/issues
github.com/torvalds/linux/issues
github.com/python/cpython/issues
gitlab.gnome.org/GNOME/mutter/issues
```

#### Research & Whitepapers

```
# Industry Research Labs
research.google
microsoft.com/research
meta.com/research
ibm.com/research
```

### Evaluation Checklist for Tier 2

```
□ Is the platform moderated/curated?
□ Does the author have established reputation?
□ Are claims reproducible with evidence provided?
□ Is there community validation (votes, confirmations)?
□ Are workarounds/solutions tested by others?
□ Is the issue confirmed by multiple users?
□ For issues: Is there maintainer response/acknowledgment?
```

### Tier 2 Sub-Classification

| Sub-Tier | Criteria | Weight |
|----------|----------|--------|
| **2A** | Maintainer-confirmed, multiple reproductions | 0.9 |
| **2B** | High-vote accepted answer (100+ votes) | 0.8 |
| **2C** | Single reproduction, no official response | 0.7 |
| **2D** | Anecdotal but detailed technical report | 0.6-0.7 |

---

## Tier 3: Subjective / Anecdotal Sources

### Characteristics

- **Unmoderated**: Minimal or no quality control
- **Personal**: Individual experiences, opinions, recommendations
- **Variable**: Quality ranges from expert insight to misinformation
- **Ephemeral**: May disappear, change, or lack versioning

### Accepted Source Types (With Caveats)

| Category | Sources | Confidence Weight | Usage |
|----------|---------|-------------------|-------|
| **Discussion Forums** | Reddit, Hacker News, Lobsters | 0.3-0.5 | User experiences |
| **Personal Blogs** | Medium, Dev.to, Substack, personal sites | 0.3-0.5 | Tutorials, opinions |
| **Social Media** | Twitter, Mastodon, LinkedIn | 0.2-0.4 | Breaking news, quick tips |
| **Video Content** | YouTube, Twitch, TikTok | 0.3-0.5 | Demonstrations, reviews |
| **Chat Logs** | Discord, Slack, IRC (archived) | 0.2-0.4 | Informal troubleshooting |

### Evaluation Checklist for Tier 3

```
□ Does the author demonstrate expertise (portfolio, history)?
□ Are claims specific and detailed (not vague)?
□ Is there supporting evidence (logs, screenshots, code)?
□ Do other users corroborate the experience?
□ Is the post recent enough to be relevant?
□ Are potential biases disclosed (sponsorship, affiliation)?
□ Can claims be verified against Tier 1/2 sources?
```

### When Tier 3 Becomes Valuable

Tier 3 sources gain credibility when:

1. **Multiple Independent Reports**: 5+ users report identical experience
2. **Expert Authors**: Recognized experts sharing unpublished insights
3. **Detailed Evidence**: Full logs, reproduction steps, benchmarks
4. **Emerging Issues**: Before Tier 1/2 coverage exists (zero-days, new releases)
5. **Niche Domains**: Areas without formal documentation

---

## Cross-Tier Validation Matrix

Use this matrix to determine confidence levels:

| Tier 1 | Tier 2 | Tier 3 | Combined Confidence | Action |
|--------|--------|--------|---------------------|--------|
| ✅ Confirms | ✅ Confirms | ✅ Confirms | **Very High (0.95+)** | Output as Absolute |
| ✅ Confirms | ❌ Contradicts | ❌ Contradicts | **High (0.8-0.9)** | Document discrepancy (Scenario B) |
| ❌ Silent | ✅ Confirms | ✅ Confirms | **Moderate-High (0.7)** | Output as Subjective with note |
| ❌ Silent | ❌ Conflicting | ✅ Mixed | **Low (0.4-0.6)** | Output as Unconfirmed |
| ❌ Silent | ❌ Silent | ✅ Reports | **Very Low (0.2-0.3)** | Mention as anecdotal only |
| ✅ Confirms | ✅ Confirms | ❌ Contradicts | **High (0.8)** | Investigate edge case |

---

## Domain-Specific Source Hierarchies

### Security & Cryptography

```
Tier 1:
- NIST publications (csrc.nist.gov)
- IETF RFCs (rfc-editor.org)
- Vendor security advisories
- CVE database (cve.mitre.org)

Tier 2:
- Security researcher blogs (with technical detail)
- Bug bounty reports (sanitized)
- Security conference talks (DEF CON, Black Hat)

Tier 3:
- Security Twitter
- r/netsec discussions
```

### Machine Learning / AI

```
Tier 1:
- arXiv (cs.LG, stat.ML)
- Conference proceedings (NeurIPS, ICML, ICLR)
- Official framework docs (pytorch.org, tensorflow.org)

Tier 2:
- Hugging Face issues/discussions
- Fast.ai forums
- Distill.pub articles

Tier 3:
- ML Twitter
- r/MachineLearning
- Personal experiment blogs
```

### DevOps & Infrastructure

```
Tier 1:
- Official product documentation
- CNCF specifications
- RFCs and standards

Tier 2:
- GitHub issues for tools
- DevOps Stack Exchange
- Postmortems from reputable companies

Tier 3:
- r/devops
- DevOps blogs on Medium
- Twitter #DevOps
```

---

## Source Decay & Temporal Considerations

### Half-Life of Information

| Domain | Tier 1 Validity | Tier 2 Validity | Tier 3 Validity |
|--------|-----------------|-----------------|-----------------|
| **Web Development** | 2-3 years | 1-2 years | 6 months |
| **Security** | 3-5 years | 1 year | 3 months |
| **Machine Learning** | 2-3 years | 1 year | 3-6 months |
| **Systems Programming** | 5-10 years | 2-3 years | 1 year |
| **Cloud Infrastructure** | 2-3 years | 1-2 years | 6 months |

### Red Flags for Outdated Sources

```
□ References to deprecated features/APIs
□ Screenshots showing old UI versions
□ Version numbers significantly behind current
□ Comments noting "this no longer works"
□ Archived/deprecated documentation notices
□ Links to resources that no longer exist
```

---

## Source Attribution Format

For every claim, use this attribution format:

```markdown
[Claim text] [Source Type: Source Name, Title/URL, Date Accessed]

Examples:
- Python venv creates isolated environments [T1: docs.python.org, "venv — Creation of virtual environments", 2024-03-29]
- Users report micro-stutter with XWayland on NVIDIA [T2: GitHub Issue #4521, gnome.org/mutter, 2024-02-15]
- Community prefers venv over Docker for local dev [T3: r/Python discussion, reddit.com/r/Python/comments/xyz, 2024-01-20]
```

---

## Quick Reference: Source Evaluation Decision Tree

```
                        ┌─────────────────┐
                        │  Found Source   │
                        └────────┬────────┘
                                 │
                    ┌────────────▼────────────┐
                    │ Is this peer-reviewed   │
                    │ or official docs?       │
                    └────────────┬────────────┘
                                 │
                    ┌────────────▼────────────┐
                    │  YES → TIER 1           │
                    │  Check: Current?        │
                    │  Verified? Primary?     │
                    └─────────────────────────┘
                                 │
                    ┌────────────▼────────────┐
                    │  NO → Continue          │
                    └────────────┬────────────┘
                                 │
                    ┌────────────▼────────────┐
                    │ Is this moderated       │
                    │ with reputation system? │
                    └────────────┬────────────┘
                                 │
                    ┌────────────▼────────────┐
                    │  YES → TIER 2           │
                    │  Check: Confirmed?      │
                    │  Multiple sources?      │
                    └─────────────────────────┘
                                 │
                    ┌────────────▼────────────┐
                    │  NO → TIER 3            │
                    │  Check: Expert author?  │
                    │  Corroborated?          │
                    │  Detailed evidence?     │
                    └─────────────────────────┘
```
