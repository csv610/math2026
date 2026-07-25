import os
import re

def clean_and_restructure(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    # 1. Remove duplicate \section{The Problem}
    # This replaces multiple consecutive (or nearly consecutive) \section{The Problem} with just one.
    content = re.sub(r'(\\section\{The Problem\}.*?)\n\s*(\\section\{The Problem\})', r'\1', content, flags=re.DOTALL)
    # Also handle case where there are just blank lines between them
    while content.count(r'\section{The Problem}') > 1:
        content = re.sub(r'(\\section\{The Problem\}).*?(\\section\{The Problem\})', r'\1', content, flags=re.DOTALL)

    # 2. Fix glue-on sections (e.g., "text\section{...}")
    content = re.sub(r'([^\n])(\\section\{)', r'\1\n\n\2', content)

    # 3. Now perform the restructuring of "The Problem"
    problem_start = content.find(r'\section{The Problem}')
    if problem_start == -1:
        return False

    next_section_match = re.search(r'\\section\{', content[problem_start + 20:])
    if next_section_match:
        problem_end = problem_start + 20 + next_section_match.start()
    else:
        problem_end = len(content)
    
    problem_section = content[problem_start:problem_end]
    
    # Convert historicalbox to subsection
    pattern_box = re.compile(r'\\begin\{historicalbox\}(.*?)\\end\{historicalbox\}', re.DOTALL)
    problem_section = pattern_box.sub(r'\\subsection{Historical Context}\1', problem_section)

    # Extract subsections
    subsection_pattern = re.compile(r'(\\subsection\{([^{}]*)\}(.*?))(?=\\subsection\{|\\section\{|$)', re.DOTALL)
    matches = subsection_pattern.findall(problem_section)
    
    subsections = {title.strip(): full_text.strip() for full_text, title, _ in matches}
    
    desired_order = [
        "Informal",
        "Formal",
        "Historical Context",
        "What Was Known",
        "Why It Matters",
        "Simplified Version"
    ]
    
    def find_best_match(target):
        for actual in subsections.keys():
            if target.lower() == actual.lower():
                return actual
        return None

    ordered_content = []
    used_titles = set()
    
    for target in desired_order:
        best = find_best_match(target)
        if best:
            ordered_content.append(subsections[best])
            used_titles.add(best)
    
    for title, content_val in subsections.items():
        if title not in used_titles:
            ordered_content.append(content_val)
    
    new_problem_body = "\n\n".join(ordered_content)
    
    # Robustly identify the start of the subsections to keep intro text
    first_sub_match = re.search(r'\\subsection\{', problem_section)
    if first_sub_match:
        # Keep everything from \section{The Problem} up to the first \subsection
        header_and_intro = problem_section[:first_sub_match.start()].strip()
        new_problem_section = header_and_intro + "\n\n" + new_problem_body
    else:
        new_problem_section = problem_section # No subsections to reorder

    new_problem_section += "\n\n"
    content = content[:problem_start] + new_problem_section + content[problem_end:]
    
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)
    return True

chapters_dir = 'chapters'
files = [os.path.join(chapters_dir, f) for f in os.listdir(chapters_dir) if f.endswith('.tex')]
count = 0
for f in files:
    if clean_and_restructure(f):
        count += 1
        print(f"Processed {f}")

print(f"Total processed: {count}")
