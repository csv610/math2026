import os
import re

def process_file(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Regex to find \chapter{The ...} and replace with \chapter{...}
    # We match \chapter{ and then optionally "The " (case insensitive)
    # We use a capture group for the content inside the braces.
    
    # This pattern looks for \chapter{ followed by "The " (optional) and then the rest of the title.
    # It uses a non-greedy match for the title to ensure it stops at the first closing brace.
    pattern = re.compile(r'\\chapter\{(?i:The\s+)([^}]*)\}')
    
    new_content = pattern.sub(r'\\chapter{\1}', content)
    
    if new_content != content:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(new_content)
        return True
    return False

chapters_dir = 'chapters'
files = [os.path.join(chapters_dir, f) for f in os.listdir(chapters_dir) if f.endswith('.tex')]
count = 0
for f in files:
    if process_file(f):
        count += 1
        print(f"Updated {f}")

print(f"Total updated: {count}")
