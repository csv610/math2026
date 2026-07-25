import os
import re

def restructure_file(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    problem_start = content.find(r'\section{The Problem}')
    if problem_start == -1:
        return False

    # Find the start of the next \section
    next_section_match = re.search(r'\\section\{', content[problem_start + 20:])
    if next_section_match:
        problem_end = problem_start + 20 + next_section_match.start()
    else:
        problem_end = len(content)
    
    problem_section = content[problem_start:problem_end]
    
    # 1. Convert historicalbox to a subsection
    pattern_box = re.compile(r'\\begin\{historicalbox\}(.*?)\\end\{historicalbox\}', re.DOTALL)
    problem_section = pattern_box.sub(r'\\subsection{Historical Context}\1', problem_section)

    # 2. Extract subsections
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
    
    # We want to keep the original header but replace the body
    # Find the end of the \section{The Problem} line
    header_end = problem_section.find('\n', problem_section.find(r'\section{The Problem}'))
    if header_end == -1:
        header_end = problem_section.find(r'\subsection{') if r'\subsection{' in problem_section else 0

    # Extract intro text (anything between \section{The Problem} and the first \subsection)
    first_sub_match = re.search(r'\\subsection\{', problem_section)
    if first_sub_match:
        intro_text = problem_section[header_end : first_sub_match.start()].strip()
    else:
        intro_text = ""

    # Reconstruct the problem section
    header = r'\section{The Problem}'
    if intro_text:
        new_problem_section = header + "\n\n" + intro_text + "\n\n" + new_problem_body
    else:
        new_problem_section = header + "\n\n" + new_problem_body

    # Ensure there's a trailing newline for the next section
    new_problem_section += "\n\n"

    content = content[:problem_start] + new_problem_section + content[problem_end:]
    
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)
    return True

chapters_dir = 'chapters'
files = [os.path.join(chapters_dir, f) for f in os.listdir(chapters_dir) if f.endswith('.tex')]
count = 0
for f in files:
    if restructure_file(f):
        count += 1
        print(f"Restructured {f}")

print(f"Total restructured: {count}")
