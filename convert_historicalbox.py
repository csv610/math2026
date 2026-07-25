import os
import re

def convert_file(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    # Find the range of "The Problem" section
    problem_start = content.find(r'\section{The Problem}')
    if problem_start == -1:
        return False

    # Find the start of the next \section{...} after \section{The Problem}
    next_section = re.search(r'\\section\{', content[problem_start + 20:])
    if next_section:
        problem_end = problem_start + 20 + next_section.start()
    else:
        problem_end = len(content)

    problem_section = content[problem_start:problem_end]
    
    # Check for historicalbox in this section
    if r'\begin{historicalbox}' in problem_section:
        # Use regex to replace only within the problem_section
        pattern = re.compile(r'\\begin\{historicalbox\}(.*?)\\end\{historicalbox\}', re.DOTALL)
        
        new_problem_section = pattern.sub(r'\\subsection{Historical Context}\1', problem_section)
        # Also remove the trailing \end{historicalbox} content if the regex didn't catch it perfectly, 
        # but the regex above captures the inner content and replaces the whole block.
        # The only thing left is to make sure we don't leave a trailing \end{historicalbox}.
        # The regex (.*?) combined with \end{historicalbox} in the pattern handles the closing tag.
        
        # Clean up any double newlines that might occur from the replacement
        new_problem_section = new_problem_section.replace('\n\n\n', '\n\n')
        
        content = content[:problem_start] + new_problem_section + content[problem_end:]
        
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)
        return True
    
    return False

chapters_dir = 'chapters'
files = [os.path.join(chapters_dir, f) for f in os.listdir(chapters_dir) if f.endswith('.tex')]
count = 0
for f in files:
    if convert_file(f):
        count += 1
        print(f"Converted {f}")

print(f"Total converted: {count}")
