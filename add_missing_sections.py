import os
import re

REQUIRED = [
    "Informal",
    "Formal",
    "Historical Context",
    "What Was Known",
    "Why It Matters",
    "Simplified Version"
]

def fix_file(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    problem_start = content.find(r'\section{The Problem}')
    if problem_start == -1:
        return False

    next_section = re.search(r'\\section\{', content[problem_start + 20:])
    problem_end = problem_start + 20 + next_section.start() if next_section else len(content)
    problem_section = content[problem_start:problem_end]
    
    # Identify what's missing
    found = []
    subsection_pattern = re.compile(r'\\subsection\{([^{}]*)\}')
    for match in subsection_pattern.finditer(problem_section):
        found.append(match.group(1).strip())
    
    if r'\begin{historicalbox}' in problem_section:
        found.append("Historical Context")

    missing = [req for req in REQUIRED if not any(req.lower() == f.lower() for f in found)]
    
    if not missing:
        return False

    # Add missing subsections at the end of the problem section
    # Just before the next \section or end of file
    addition = "\n\n" + "\n\n".join([f"\\subsection{{{m}}}\n% TODO: Add content" for m in missing]) + "\n\n"
    
    content = content[:problem_end] + addition + content[problem_end:]
    
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)
    return True

chapters_dir = 'chapters'
files = [os.path.join(chapters_dir, f) for f in os.listdir(chapters_dir) if f.endswith('.tex')]
count = 0
for f in files:
    if fix_file(f):
        count += 1
        print(f"Added missing sections to {f}")

print(f"Total fixed: {count}")
