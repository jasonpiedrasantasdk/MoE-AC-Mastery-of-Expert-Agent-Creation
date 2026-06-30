import os
import sys
import yaml
import shutil
import re

def standardize_skill(src_dir, dest_root):
    skill_name = os.path.basename(src_dir)
    dest_dir = os.path.join(dest_root, skill_name)
    os.makedirs(dest_dir, exist_ok=True)
    os.makedirs(os.path.join(dest_dir, "references"), exist_ok=True)
    os.makedirs(os.path.join(dest_dir, "examples"), exist_ok=True)
    
    # Try to find the primary content file
    content_files = [f for f in os.listdir(src_dir) if f.endswith('.md')]
    main_file = None
    
    # Prefer SKILL.md, then <skill-name>.md, then README.md, then the first .md
    if 'SKILL.md' in content_files:
        main_file = 'SKILL.md'
    elif f"{skill_name}.md" in content_files:
        main_file = f"{skill_name}.md"
    elif 'README.md' in content_files:
        main_file = 'README.md'
    elif content_files:
        main_file = content_files[0]
    
    content = ""
    if main_file:
        with open(os.path.join(src_dir, main_file), 'r') as f:
            content = f.read()
            
    # Clean up frontmatter if it exists
    if content.startswith('---'):
        parts = content.split('---', 2)
        if len(parts) >= 3:
            content = parts[2].strip()

    # Generate standardized frontmatter
    # Extract description from the first paragraph or title
    description = f"Handles {skill_name.replace('-', ' ')} tasks. Triggered by {skill_name.replace('-', ' ')} requests."
    match = re.search(r'^#\s+.*?\n+(.*?)\n', content, re.MULTILINE)
    if match:
        extracted = match.group(1).strip()
        if extracted and len(extracted) < 200:
            description = extracted

    frontmatter = {
        "name": skill_name,
        "description": description
    }
    
    final_content = f"""---
{yaml.dump(frontmatter, sort_keys=False)}---

{content}
"""
    
    with open(os.path.join(dest_dir, "SKILL.md"), "w") as f:
        f.write(final_content)
        
    # Copy other files to references/
    for item in os.listdir(src_dir):
        if item == main_file:
            continue
        src_item = os.path.join(src_dir, item)
        if os.path.isdir(src_item):
            shutil.copytree(src_item, os.path.join(dest_dir, "references", item), dirs_exist_ok=True)
        else:
            shutil.copy2(src_item, os.path.join(dest_dir, "references", item))

    print(f"Standardized: {skill_name}")

def bulk_convert(src_root, dest_root):
    if not os.path.exists(dest_root):
        os.makedirs(dest_root)
        
    for item in os.listdir(src_root):
        src_path = os.path.join(src_root, item)
        if os.path.isdir(src_path):
            try:
                standardize_skill(src_path, dest_root)
            except Exception as e:
                print(f"Failed to standardize {item}: {e}")

if __name__ == "__main__":
    if len(sys.argv) < 3:
        print("Usage: python3 convert_skills.py <src_root> <dest_root>")
    else:
        bulk_convert(sys.argv[1], sys.argv[2])
