import os
import re

REQUIRED_SUBSECTIONS = [
    "Informal",
    "Formal",
    "Historical Context",
    "What Was Known",
    "Why It Matters",
    "Simplified Version"
]

def analyze_file(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    problem_start = content.find(r'\section{The Problem}')
    if problem_start == -1:
        return ("Missing 'The Problem' section", [])

    next_section = re.search(r'\\section\{', content[problem_start + 20:])
    problem_end = problem_start + 20 + next_section.start() if next_section else len(content)
    problem_section = content[problem_start:problem_end]
    
    # Also count historicalbox as Historical Context
    found_subsections = []
    
    # Find all \subsection{...}
    subsection_pattern = re.compile(r'\\subsection\{([^{}]*)\}')
    for match in subsection_pattern.finditer(problem_section):
        found_subsections.append(match.group(1).strip())
    
    # Check for historicalbox
    if r'\begin{historicalbox}' in problem_section:
        found_subsections.append("Historical Context")

    missing = [req for req in REQUIRED_SUBSECTIONS if not any(req.lower() == found.lower() for found in found_subsections)]
    return (f"Found {len(found_subsections)}", missing)

chapters_dir = 'chapters'
files = sorted([os.path.join(chapters_dir, f) for f in os.listdir(chapters_dir) if f.endswith('.tex')])
print(f"{'File':<40} | {'Status':<15} | {'Missing'}")
print("-" * 80)
for f in files:
    status, missing = analyze_file(f)
    missing_str = ", ".join(missing) if missing else "None"
    print(f"{f:<40} | {status:<15} | {missing_str}")
