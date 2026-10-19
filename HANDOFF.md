# Handoff: CS-Based Mathematics Curriculum Textbooks

Written 2026-10-18 at the end of a claude.ai session. This file is the complete context needed
to keep going in Claude Code. Read it top to bottom once; after that, CLAUDE.md is the short
version.

## 1. What this project is

The owner (Lalo) is a senior frontend developer teaching himself the mathematics behind
computer science from Algebra 1 upward. The project has two layers:

1. **The curriculum**: nine courses, Algebra 1 through electives, each with topic tables, a
   programming Build, an exit check and resources. Canonical copy is a Claude Doc (link below);
   `curriculum/curriculum.md` mirrors it.
2. **One textbook per course**, written for self-study by someone who already codes. Each book
   teaches the math first, has exercises to solve by hand, then programming exercises that reuse
   the hand exercises as test cases, then a course project, an exit review and an answer key.
   Books are typeset in LaTeX to look like an academic textbook (Palatino, boxed formulas,
   numbered examples with a left rule, two-column exercise sets, running heads, answer key at
   the back). The PDFs are the deliverable.

Pedagogical stance that every chapter must keep: programming is the vehicle, never the subject.
Standard-library Python only (plus matplotlib, canvas or SVG for drawing). Every concept is
implemented from scratch; NumPy, SymPy and engine vector classes are off limits in exercises.

## 2. State at handoff

| Course | Status | Pages | Source | PDF |
|---|---|---|---|---|
| 1. Algebra 1 | Done, reviewed page by page | 36 | `course-01-algebra-1/` | `pdf/Algebra-1-A-Programmers-Introduction.pdf` |
| 2. Geometry and Intro Trig | Done, reviewed page by page | 40 | `course-02-geometry/` | `pdf/Geometry-and-Introductory-Trigonometry-A-Programmers-Introduction.pdf` |
| 3. Algebra 2 and Precalculus | Not started (next) | | | |
| 4 to 9 | Not started | | | |

Both builds compile with zero LaTeX errors and zero overfull lines wider than 5pt.

Claude Docs from the chat session (editable, with comments):

- Curriculum: https://claude.ai/code/artifact/e287fbbc-246b-47ce-8b44-b55a7f80da5e
- Course 1 textbook, prose version with Unicode superscripts (predates the LaTeX; the LaTeX
  source is now canonical): https://claude.ai/code/artifact/9c62a7af-be2c-4c9b-877b-0680b70d3ae0

Course 2 exists only as LaTeX; no doc version was made. If the owner wants doc versions of
later books, generate them from the LaTeX after the PDF is final, not before.

## 3. Repo layout and build

```
cs-math-curriculum/
  CLAUDE.md               short instructions Claude Code reads automatically
  HANDOFF.md              this file
  build.sh                builds one or all courses, copies PDFs to pdf/
  curriculum/curriculum.md course map and topic tables (source for chapter lists)
  course-01-algebra-1/    main.tex ch01..ch11.tex exit.tex answers.tex
  course-02-geometry/     same layout
  pdf/                    built PDFs
```

Build: `./build.sh` or `./build.sh course-02-geometry`. Needs TeX Live with `latexmk` and
`poppler-utils` (`pdfinfo`, `pdftoppm`, `pdftotext`). LaTeX packages used: mathpazo, txfonts
(for the `txtt` monospace), microtype, amsmath, amssymb, geometry, xcolor, tcolorbox (skins,
breakable), titlesec, fancyhdr, multicol, enumitem, booktabs, tabularx, array, float, pifont,
tikz, listings, hyperref. On Debian/Ubuntu, `texlive-full` covers all of it; a smaller set is
`texlive-latex-extra texlive-fonts-recommended texlive-pictures texlive-science`.

The script exits non-zero on any `!` line in `main.log` and prints the count of overfull lines
wider than 5pt. Treat a nonzero count as a bug: find it with
`grep -B2 -A3 'Overfull' course-NN/main.log` and reword the sentence (see section 6).

To start a new course: copy `course-02-geometry/main.tex` (not course 1; course 2 has the
extra helper macros), change `pdftitle`, the title page lines, and the preface wording that
names the course and the code file prefix. Then write the chapters.

## 4. The chapter template (do not deviate)

`main.tex` defines everything; chapters only use these:

```latex
\chapter{Title In Title Case}
\chapterintro{One paragraph, large italic grey, stating why this topic matters to a programmer.}

\section{Core Ideas}
\paragraph{Run-in heading} One short paragraph per idea. Definitions, rules, and the CS reason.
% a boxed formula when there is a key formula:
\begin{keybox}{Title of the box}
\[ formula \]
\end{keybox}
% optional figure, always [H]:
\begin{figure}[H] ... tikz ... \caption{...} \label{fig:...} \end{figure}

\section{Worked Examples}
\begin{example}
Problem statement.
\solution The solution, with every step shown.
\end{example}
% three examples per chapter

\section{Exercises}
\begin{multicols}{2}
\begin{exercises}
\item ...            % auto-numbered N.1, N.2 ...; 10 to 13 per chapter
\item \textbf{(proof)} ...   % one or two proof exercises from Course 2 onward
\end{exercises}
\end{multicols}

\section{Programming Exercises}
\begin{codeexercises}
\item Write \lstinline!function_name(args)! that ... Test with Exercises~N.3 and N.4.
\end{codeexercises}   % 4 to 5 per chapter, each naming the hand exercises it reuses as tests
```

Chapter 11 is always the course project: `\chapterintro`, one paragraph of rules, then
`\section{The Six Stages}` with a `tabularx` table (Stage, Build, Reuses, Done when), split into
two tables if it does not fit on the opener page, then `\section{Acceptance Checklist}` using
the `checklist` list, then `\section{Stretch Goals}`.

`exit.tex`: `\chapter*{Exit Review}` with 12 problems in `reviewexercises` inside `multicols`,
then the curriculum's exit check as a `checklist`. Answers are not in the key.

`answers.tex`: `\chapter*{Answers to Exercises}`, `multicols{2}`, `\small`, a `\subsection*`
per chapter, one `\answer{N.k}{...}` per non-proof exercise.

Available macros beyond the environments above: `\lerp`, `\clamp`, `\vv{x, y}` (angle-bracket
vector), `\abs{x}`, `\degs` (degree sign, use as `90\degs`), `\proj`.

## 5. Writing and style rules

- **No em dashes, ever.** Not in prose, captions, comments or code strings. The owner's style
  does not use them. Use a comma, colon, semicolon or two sentences. Check with
  `grep -rnP '(*UTF8)\x{2014}|---' course-*/` before committing (there should be no hits; `--` en dashes
  are also avoided in favor of "to", as in "pages 3 to 7").
- Lead sentences carry the point. Short sentences, under about 25 words. No filler, no "note
  that", no "it is important to".
- Every variable, number in a formula, and expression is in math mode: `$3x^2 - 5x + 7$`.
  Plain prose numbers like "10 exercises" stay in text. Currency is `\$20`, percent is `5\%`.
- Big numbers use `{,}` thin-space commas inside math: `$4{,}294{,}967{,}296$`.
- Each core idea paragraph should say what the thing is, the rule, and why a programmer cares,
  in that order. The CS tie-in is mandatory, not decorative.
- Exercises escalate: skills first, then word problems, then one or two that are explicitly
  about code or screens (pixels, bits, sprites), then proofs last.
- Programming exercises name the function signature exactly, say what to test it against
  (specific exercise numbers), and never ask for a library the book forbids. Function names are
  the API later chapters import; keep them stable (the Course 2 project reuses `to_screen`,
  `dilate`, `signed_area`, `circle_line_intersections`, `dot`, `wrap_pi`, `shortest_turn`).
- Answer keys are the most error-prone part. Every numeric answer was computed by hand and
  cross-checked during the session. Keep that bar: compute, then verify with a two-line Python
  check, then write it. Exact forms first (`$6\sqrt{2}$`), decimals second.
- Cross-course references use the curriculum's numbering: "Course 6", "Chapter 9", "Exercise
  C5.4".

## 6. LaTeX pitfalls already hit (so you do not hit them again)

1. **fancyhdr wipes headers.** A global `\pagestyle{plain}` executes the redefined plain style,
   whose `\fancyhf{}` clears the fancy fields for every later page. Fixed by defining the body
   headers as a named style `\fancypagestyle{body}{...}` and calling `\pagestyle{body}` after
   `\mainmatter` and after `\backmatter`. Do not touch this.
2. **`\titlerule` only works inside titlesec formats.** The title page uses
   `\rule{0.6\textwidth}{1.2pt}` followed by `\par`.
3. **`\frontmatter` must precede the title page** or hyperref complains about duplicate page
   anchors.
4. **`\lstinline` inside `tabularx` breaks** (the cell is re-read as an argument). Use
   `\texttt{}` with `\textasciicircum{}`, `\_`, `\{`, `\}` in table cells.
5. **tcolorbox titles with commas** need braces; the `keybox` macro already uses `title={#1}`.
6. **Floats drifting off the chapter opener.** All figures and tables use `[H]` (package
   `float`). When a `[H]` table is taller than the remaining page, it moves whole and leaves a
   gap; split it into two tables.
7. **Overfull lines from inline code.** `\lstinline` content cannot break. When a line is
   overfull, move the code span earlier or later in the sentence, shorten the function name, or
   replace a code span with math (`$\text{lo} \le \clamp(x, \text{lo}, \text{hi}) \le \text{hi}$`).
   `\emergencystretch` is already 2.5em.
8. **Unbreakable math sets** in two-column exercises: write `$\{(1, 2)$, $(2, 3)$, $(1, 4)\}$`
   so TeX can break at the commas.
9. **Unicode in source.** Avoid it entirely except in comments; use `\times`, `\div`, `\le`,
   `\ge`, `\circ`, `\cup`, `\infty`, `\pm`, `\degs`.

## 7. Review process that was used (repeat it per book)

1. `./build.sh course-NN-slug`; zero errors, zero overfull over 5pt.
2. `cd course-NN-slug && pdftoppm -r 80 -png main.pdf pg` then view: the title page, the TOC,
   one chapter opener, every page with a figure, the Chapter 11 table page, the exit review,
   the first answer-key page. Look for: headers present on body pages, figures not overlapping
   their labels, tables on the intended page, examples not split awkwardly.
3. `pdftotext` a few pages and grep for the dash character to confirm none slipped in.
4. Spot-check five answers against a Python one-liner.

## 8. Next steps, in order

1. **Course 3: Algebra 2 and Precalculus** (12 weeks, 11 topics; see `curriculum/curriculum.md`).
   Chapters: Functions in Depth; Polynomial Functions; Rational Functions; Radicals and Rational
   Exponents; Exponential and Logarithmic Functions; Sequences and Series; Complex Numbers;
   Matrices; Trigonometry Beyond Right Triangles; Conic Sections; Counting Preview. That is
   eleven topic chapters, so the project becomes Chapter 12 (adjust `main.tex` inputs and the
   preface sentence "ends with the course project"). Project: Mandelbrot renderer with an
   own complex type, sequence explorer with partial sums, 3x3 matrix calculator; six stages
   like the earlier books. Keyboxes to include: log laws, change of base, arithmetic and
   geometric sum formulas, De Moivre's formula, 2x2 and 3x3 determinant, law of sines and
   cosines, the Pythagorean and double-angle identities. Figures worth drawing in TikZ: a
   log-scale plot, a Mandelbrot thumbnail is not feasible in TikZ (describe it instead), the
   unit-circle derivation of the law of cosines, the four conics as sections of a cone (or
   just their standard graphs).
2. Courses 4 through 8 in curriculum order, then the electives as shorter books.
3. Nice-to-haves the owner has not asked for yet: an author line on the title page (ask
   first), a combined single PDF, a GitHub Actions workflow running `./build.sh`, a
   `solutions/` folder with reference Python implementations of every programming exercise
   (would also serve as the answer-key verifier), and doc versions of Courses 2 and up.

## 9. Things to ask the owner before deciding

- Whether later books should also exist as Claude Docs, or PDF only.
- Whether to put his name on the title pages.
- Whether Course 3 should include a short review chapter of Courses 1 and 2 (currently the
  books assume the earlier course and move on).
- Whether to write the reference solutions in Python only or also in TypeScript.
