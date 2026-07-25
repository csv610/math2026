import re

with open('math_21_century.tex', 'r', encoding='utf-8') as f:
    lines = f.readlines()

# Find the lines that start with \input{chapters/
input_lines = []
other_lines = []

# We need to preserve the structure around the inputs
# So we'll identify the block of inputs.
start_idx = -1
end_idx = -1

for i, line in enumerate(lines):
    if line.strip().startswith(r'\input{chapters/'):
        if start_idx == -1:
            start_idx = i
        end_idx = i

if start_idx != -1:
    # Extract all input lines in that block
    block = lines[start_idx : end_idx + 1]
    
    # Extract the actual filenames for sorting
    # \input{chapters/filename} -> filename
    def get_filename(line):
        match = re.search(r'\\input\{chapters/([^}]*)\}', line)
        return match.group(1) if match else ""

    # Sort the block based on the filename
    sorted_block = sorted(block, key=get_filename)
    
    # Replace the old block with the sorted block
    lines[start_idx : end_idx + 1] = sorted_block

with open('math_21_century.tex', 'w', encoding='utf-8') as f:
    f.writelines(lines)
