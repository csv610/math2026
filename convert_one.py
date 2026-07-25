import sys
import re

def convert_file(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    problem_start = content.find(r'\section{The Problem}')
    if problem_start == -1:
        return False

    next_section = re.search(r'\\section\{', content[problem_start + 20:])
    problem_end = problem_start + 20 + next_section.start() if next_section else len(content)

    problem_section = content[problem_start:problem_end]
    
    if r'\begin{historicalbox}' in problem_section:
        pattern = re.compile(r'\\begin\{historicalbox\}(.*?)\\end\{historicalbox\}', re.DOTALL)
        new_problem_section = pattern.sub(r'\\subsection{Historical Context}\1', problem_section)
        new_problem_section = new_problem_section.replace('\n\n\n', '\n\n')
        content = content[:problem_start] + new_problem_section + content[problem_end:]
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)
        return True
    return False

if __name__ == "__main__":
    if convert_file(sys.argv[1]):
        print(f"Converted {sys.argv[1]}")
