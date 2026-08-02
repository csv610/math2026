# 21st Century Mathematics

A comprehensive textbook covering landmark mathematical results proven in the 21st century.

## Objectives

This book has three interrelated goals:

1. **Demystify modern breakthroughs.** The research papers behind results like the Poincaré Conjecture, Fermat's Last Theorem, and the Kakeya conjecture are technically impenetrable to most readers. This book bridges the gap between research papers and textbooks, making the core ideas and proof strategies accessible to advanced undergraduates and beginning graduate students.

2. **Teach the proof, not just the statement.** Every chapter presents a complete, rigorous proof with no hand-waving. The "Solution" section in each chapter walks through the argument step by step, explaining the intuition, the key insights, and the technical machinery that makes the proof work. Where gaps exist in the literature, they are identified and filled.

3. **Connect across fields.** The 30 chapters span number theory, algebra, geometry, analysis, combinatorics, and mathematical physics. The book makes explicit the unexpected bridges between them---the modular connection behind Fermat's Last Theorem, the topological methods that unlocked the Poincaré Conjecture, the Fourier analytic tools behind the Green-Tao theorem. Readers should finish with a sense of how modern mathematics is woven together.

The book is designed for:
- Graduate students encountering these results for the first time
- Researchers in adjacent fields who want a self-contained overview
- Mathematically mature readers who want to understand how some of the greatest theorems of the 21st century were proved

## Overview

| Detail | Value |
|--------|-------|
| Author | Chaman Singh Verma |
| Year | 2026 |
| Chapters | 30 |
| Source | 7,479 lines of LaTeX |
| PDF | ~279 pages |
| Bibliography | 135 entries |
| Repository | [github.com/csv610/math21century](https://github.com/csv610/math21century) |

## Structure

Each chapter follows a consistent pedagogical format:

- **The Problem** -- Informal motivation, formal statement, historical context, simplified version
- **Mathematical Theory** -- Prerequisites, key theorems, definitions, lemmas
- **Solution** -- Step-by-step proof with intuition, gap analysis, student-friendly explanations
- **Why This Matters** -- Connections to other fields and real-world applications
- **After the Proof** -- Consequences, open questions, further reading
- **Computational Verification** -- Numerical or algorithmic confirmation (Tier 1 chapters)

## Chapters

| # | Chapter | Year | Prize |
|---|---------|------|-------|
| 1 | AKS Primality Test | 2002 | -- |
| 2 | Bounded Gaps Between Primes | 2013 | -- |
| 3 | Cap Sets (Elitzur-Sheffield-Bloom) | 2016 | -- |
| 4 | Catalan Conjecture | 2002 | -- |
| 5 | Classification of Finite Simple Groups | 2004 | -- |
| 6 | Erdős Discrepancy Problem | 2015 | -- |
| 7 | Erdős Distinct Distances | 2019 | -- |
| 8 | Fermat's Last Theorem / Modularity | 1995/2001 | \* |
| 9 | Fundamental Lemma | 2007 (Ngô) | Fields |
| 10 | Geometric Langlands | 2024 | -- |
| 11 | Green-Tao Theorem | 2004/2016 | -- |
| 12 | Jacob-Tsimerman (Andree-Oort) | 2016 | -- |
| 13 | John Pardon (Knot Distortion) | 2020 | -- |
| 14 | Kadison-Singer Conjecture | 2013 | -- |
| 15 | Kakeya Conjecture | -- | -- |
| 16 | Kepler Conjecture | 2005 | -- |
| 17 | Kervaire Invariant One | 2009 | -- |
| 18 | Lawson Conjecture | 2012 | -- |
| 19 | Mirzakhani (Hyperbolic Geometry) | 2007-2014 | Fields |
| 20 | Perfectoid Spaces | 2010 | -- |
| 21 | Poincaré Conjecture | 2003 | Fields |
| 22 | Random Matrices (Universality) | -- | -- |
| 23 | Sato-Tate Conjecture | 2008 | -- |
| 24 | Sensitivity Conjecture | 2019 | -- |
| 25 | Sphere Packings (High Dimensions) | 2016/2017 | Fields |
| 26 | Sunflowers / Delta-Systems | -- | -- |
| 27 | Virtual Haken Conjecture | 2012 | -- |
| 28 | Weak Goldbach Conjecture | 2013 | -- |
| 29 | Willmore Conjecture | 2012 | -- |
| 30 | Yu-Deng (Navier-Stokes Regularity) | 2024 | -- |

\* Awarded for completed proof; result proven earlier.

## File Layout

```
Math21Century/
  math_21_century.tex           # Master document
  bibliography.tex              # Bibliography (thebibliography environment)
  bibliography_full.tex         # Full bibliography (with all citations)
  chapters/
    aks_primality.tex
    bounded_gaps_primes.tex
    ... (28 more chapters)
    appendix_figures.tex        # Figure index/descriptions
  figures/                      # Generated illustrations
  figure_prompts.csv            # Image generation prompts (28 entries)
```

## Building

Compile with standard LaTeX:

```bash
pdflatex math_21_century.tex
bibtex math_21_century
pdflatex math_21_century.tex
pdflatex math_21_century.tex
```

Or use `latexmk` for automatic round management:

```bash
latexmk -pdf math_21_century.tex
```

The book compiles cleanly: **0 errors, 0 warnings, 0 overfull boxes**.

## Dependencies

- LaTeX (pdfTeX)
- `amsmath`, `amssymb`, `amsthm`
- `geometry`, `xcolor`, `hyperref`
- `enumitem`, `booktabs`, `tabularx`, `graphicx`
- `fancyhdr`

No external package managers or Python dependencies required.

## Citations

All 135 bibliographic entries resolve to their in-text citations with zero missing references. Key sources include arXiv preprints and peer-reviewed journal articles from Annals of Mathematics, Inventiones Mathematicae, Journal of the AMS, and ICM proceedings.

## License

Personal academic project. All mathematical content is original exposition; source material attributed to original authors.
