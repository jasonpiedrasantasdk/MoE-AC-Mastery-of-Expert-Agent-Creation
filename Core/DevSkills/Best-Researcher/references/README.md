# Best-Researcher Skill Package

## Overview

**Best_Researcher** is a comprehensive, platform-agnostic research skill that executes deep multi-engine research workflows to synthesize high-fidelity reports. The skill prioritizes authoritative documentation and peer-reviewed papers over community forums, distinguishing strictly between absolute facts and context-dependent subjective observations.

### Key Features

- **Universal Format**: No MCP, API, or platform dependencies
- **Tier-Based Source Hierarchy**: Rigorous source evaluation framework
- **Conflict Resolution Logic**: Systematic handling of contradictory information
- **Advanced Search Methodology**: Platform-specific search techniques
- **Structured Output**: Consistent, citation-dense markdown format

---

## Directory Structure

```
Best-Researcher/
├── SKILL.md                    # Core skill definition
├── README.md                   # This file
├── docs/
│   ├── conflict_logic.md       # Conflict resolution framework
│   ├── search_methodology.md   # Search techniques & operators
│   └── source_hierarchy.md     # Source evaluation guide
└── examples/
    ├── 01-python-environments.md    # Example: Python isolation
    └── 02-llm-vram-requirements.md  # Example: LLM hardware requirements
```

---

## Quick Start

### Basic Usage

Invoke the skill by requesting research on any technical topic:

```
"Research [topic] and provide findings with source citations"
```

### Example Requests

```
"Research the optimal configuration for isolating Python application environments"
"Research the feasibility of running a 70B parameter model on 12GB VRAM"
"Research Wayland vs X11 performance characteristics for gaming"
```

---

## Core Workflow

### Phase 1: Query Expansion
Break the user prompt into 3-5 sub-queries targeting different source tiers.

### Phase 2: Data Extraction & Tagging
Pull raw data and tag immediately as **Tier 1**, **Tier 2**, or **Tier 3**.

### Phase 3: Contextual Stratification
Separate absolute facts from subjective observations.

### Phase 4: Conflict Resolution
Apply conflict resolution logic to handle contradictions.

### Phase 5: Synthesis & Output
Format using the standard markdown structure with citations.

---

## Source Tiers

| Tier | Name | Sources | Usage |
|------|------|---------|-------|
| **Tier 1** | Absolute | Peer-reviewed papers, official docs, source code | Baseline facts, hard limits |
| **Tier 2** | High-Signal | Stack Overflow, GitHub issues, whitepapers | Edge cases, bugs, implementations |
| **Tier 3** | Subjective | Reddit, blogs, social media | User experiences, qualitative data |

See [`docs/source_hierarchy.md`](docs/source_hierarchy.md) for detailed evaluation criteria.

---

## Output Structure

All research outputs follow this structure:

```markdown
# [Research Topic]

**Date:** [YYYY-MM-DD]
**Confidence Score:** [0.0 - 1.0]
**Primary Sources:** [URLs/DOIs]

---

## Absolute Findings (Tier 1)
- [Facts with citations]

---

## Subjective Context (Tier 2/3)
### High-Signal Observations (Tier 2)
- [Verified community reports]

### Anecdotal Reports (Tier 3)
- [User experiences]

---

## Known Implementation Discrepancies
| Official Claim | Community Reality | Status |
|----------------|-------------------|--------|

---

## Recommendations
### For [Use Case A]
- [Actionable recommendations]

---

## References
1. [Full citations]
```

---

## Documentation

### Conflict Resolution

When sources contradict each other, the skill applies systematic logic to resolve or document discrepancies.

**See:** [`docs/conflict_logic.md`](docs/conflict_logic.md)

| Scenario | Resolution |
|----------|------------|
| Golden Path | Output as absolute fact |
| Reality Gap | Document both, flag discrepancy |
| Undocumented Feature | Output as subjective with warning |
| Deprecation Lag | Check timestamps, flag outdated |

### Search Methodology

Comprehensive search strategies for different engines and source types.

**See:** [`docs/search_methodology.md`](docs/search_methodology.md)

**Key Techniques:**
- Google advanced operators (`site:`, `filetype:`, `intitle:`)
- Google Scholar citation chaining
- GitHub issue tracking
- Academic database queries

---

## Examples

### Example 1: Python Environment Isolation

**Topic:** Isolating Python applications to prevent system package conflicts

**Key Findings:**
- PEP 668 marks base environments as externally-managed
- `python -m venv` creates isolated directories
- Community prefers venv over Docker for local development

**See:** [`examples/01-python-environments.md`](examples/01-python-environments.md)

### Example 2: LLM VRAM Requirements

**Topic:** Running 70B parameter models on 12GB VRAM

**Key Findings:**
- 70B @ 16-bit requires 140GB VRAM (absolute)
- 4-bit quantization reduces to ~35-40GB
- 12GB VRAM requires CPU offloading (2-4 tokens/sec)

**See:** [`examples/02-llm-vram-requirements.md`](examples/02-llm-vram-requirements.md)

---

## Quality Checklist

Before delivering research:

```
□ Every claim has an inline citation
□ Tier 1, 2, and 3 data are clearly separated
□ Conflicts between tiers are documented
□ Recommendations are actionable and tied to findings
□ Confidence score reflects source quality/consensus
□ No hallucinated claims (all data traceable to sources)
```

---

## Version History

| Version | Date | Changes |
|---------|------|---------|
| 1.0.0 | 2024-03-29 | Initial release (hybrid version) |

---

## Related Files

Original skill files archived in [`../Research-Driver/base_data/`](../Research-Driver/base_data/):
- `SKILL.md` - Original skill definition
- `conflict_logic.md` - Original conflict resolution table
- `openapi.yaml` - Original API schema (MCP-dependent)

---

## License

This skill package is provided for use within AI assistant contexts. No external license required.
