# Plan: Sort Chapters Alphabetically in math_21_century.tex

## Goal
Reorder the `\input{chapters/...}` commands in `math_21_century.tex` to be in alphabetical order by the filename.

## Steps
1. **Extract and Sort**: Identify all lines matching `\input{chapters/([^}]*)}`.
2. **Alphabetize**: Sort the extracted filenames alphabetically.
3. **Reconstruct**: Create the sorted list of `\input` commands.
4. **Update File**: Replace the original sequence of chapter inputs in `math_21_century.tex` with the sorted sequence.
5. **Verify**: Read the file to ensure the order is correct and the rest of the document structure is preserved.

## Target File
- `math_21_century.tex`
