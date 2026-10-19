# CLAUDE.md

Self-study math textbooks for a 9-course CS-based mathematics curriculum, typeset in LaTeX.
Read HANDOFF.md before doing anything substantial. It has the full context, the chapter
template, the style rules and the next steps.

## Quick facts

- One directory per course: `course-NN-slug/` with `main.tex`, `ch01.tex` .. `ch11.tex`,
  `exit.tex`, `answers.tex`. Courses 1 and 2 are complete. Course 3 is next.
- Build: `./build.sh` (all courses) or `./build.sh course-02-geometry`. Output lands in `pdf/`.
  The script fails on LaTeX errors and reports overfull lines wider than 5pt; keep that at 0.
- `curriculum/curriculum.md` is the course map and topic lists. Do not invent topics; the
  chapters of each book are exactly the curriculum's topic rows, in order, plus a Chapter 11
  course project that is the curriculum's Build.
- Every chapter follows the template in HANDOFF.md section 4. Do not restructure it.

## Learner workspace

The repo is also where the owner works through the books.

- `python/courseNN_slug/chNN.py`: the owner's solutions to the programming exercises, generated
  as stubs by `tools/scaffold.py`. Tests live in the same file as `test_cN_k` functions; run
  `python -m pytest`. Do not fill in solutions unless asked; the owner is learning by writing them.
- `handwritten/course-NN-slug/chNN/`: scans of hand work. `handwritten/mistake-log.md` and
  `progress.md` are the owner's records; edit only when asked.
- After writing a new course's LaTeX, run `python tools/scaffold.py course-NN-slug` and add the
  course's chapters to `progress.md`. The scaffold never overwrites existing files.

## Hard rules

- Never use em dashes (the long dash) anywhere, in prose or in LaTeX source. Use commas,
  colons, semicolons or a new sentence. (Owner's writing style; this is non-negotiable.)
  Run `./check-dashes.sh` before every commit.
- Every math expression goes in math mode. Exponents are `x^2`, never Unicode superscripts.
- Inline code uses `\lstinline!...!`, except inside `tabularx` cells, where it must be
  `\texttt{...}` with `^`, `_`, `{`, `}` escaped (verbatim breaks inside table cells).
- `keybox` titles are wrapped in braces by the macro, so commas in titles are fine.
- Figures and tables use `[H]`. If a table pushes a chapter opener's content to the next page,
  split it into two tables rather than shrinking the font below `\footnotesize`.
- Answer keys contain every numeric or short answer; proof exercises (marked `\textbf{(proof)}`)
  are excluded from the key. Exit review answers are deliberately not in the key.
- Verify every answer by hand or with a quick Python check before it goes in `answers.tex`.
  A wrong answer key is worse than no answer key.
- After building, render a few pages (`pdftoppm -r 80 -png main.pdf pg`) and look at them:
  chapter opener, a figure page, the project table, the answer key. Fix overlaps and orphans.
