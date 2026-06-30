---
name: claude-skill-converter
description: "Bulk converts ingested skills into Claude-compatible formats. Triggered by 'standardize skills', 'bulk convert', or 'prepare for claude'. Handles YAML frontmatter, SKILL.md creation, and directory restructuring."
---

# Claude Skill Converter

An agentic skill designed to bulk-process existing documentation or "raw" skill directories into standardized Claude Skills.

## Workflow

### 1) Ingest & Scan
- Scans the source directory (e.g., `ingested-skills/`) for subdirectories.
- Identifies the primary content file (`SKILL.md`, `README.md`, etc.).

### 2) Standardize Content
- Extracts or generates a kebab-case `name` from the folder name.
- Generates a 3rd-person `description` by analyzing the content or using a default template.
- Removes old frontmatter and injects standardized Claude YAML frontmatter.
- Renames the primary file to `SKILL.md`.

### 3) Restructure
- Creates `references/` and `examples/` directories.
- Moves all secondary files and subdirectories into `references/` to keep the root clean.
- Ensures the final output is in a new target directory (e.g., `standardized-skills/`).

### 4) Automation
- Uses `scripts/convert_skills.py` to automate the entire lifecycle for hundreds of skills at once.

## Usage
`python3 scripts/convert_skills.py <source_root> <destination_root>`

## References
- `references/` — internal documentation.
- `scripts/convert_skills.py` — the core conversion engine.
