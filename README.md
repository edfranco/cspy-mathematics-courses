# CS-Based Mathematics

Self-study mathematics from Algebra 1 upward, learned two ways at once: by hand on paper, then
in Python. Nine courses are mapped in [`curriculum/curriculum.md`](curriculum/curriculum.md);
each gets its own textbook, written for someone who already codes.

## Layout

| Path | What it is |
|---|---|
| `pdf/` | The textbooks. Start here. |
| `handwritten/` | Your paper work: scanned exercises, proofs, notes, and the [mistake log](handwritten/mistake-log.md). See [its README](handwritten/README.md). |
| `python/` | Your code: one module per chapter with stubs for every programming exercise. |
| `progress.md` | Chapter-by-chapter tracker for reading, hand work and code. |
| `course-NN-slug/` | LaTeX source for each textbook. |
| `curriculum/` | The course map, topics, builds and exit checks. |
| `tools/scaffold.py` | Generates `python/` stubs and `handwritten/` folders from the LaTeX. |

Courses 1 (Algebra 1) and 2 (Geometry and Introductory Trigonometry) are written. Course 3 is next.

## The loop for each chapter

1. **Read** the chapter and rework the three worked examples on paper.
2. **Hand exercises.** Do them all on paper, check against the answer key, log mistakes, scan
   into `handwritten/course-NN-slug/chNN/`.
3. **Programming exercises.** Open `python/courseNN_slug/chNN.py`. Each exercise has its text
   as a comment, function stubs that raise `NotImplementedError`, and a `test_` function that
   is skipped. Implement the function, then replace the skip with asserts built from your hand
   answers. Standard library only (matplotlib is allowed for plots); NumPy and SymPy are off
   limits because the point is to build each idea yourself.
4. **Mark it** in `progress.md`.

Chapter 11 of each book is the course project, which reuses the functions from earlier
chapters. Import them, for example `from course02_geometry.ch04 import to_screen`.

## Python setup

Python 3.9 or newer. Only pytest is needed to run the tests.

```bash
python -m venv .venv
```

```bash
.venv/Scripts/python -m pip install pytest matplotlib
```

```bash
.venv/Scripts/python -m pytest
```

On macOS or Linux use `.venv/bin/python`. The summary lists every skipped test, which doubles
as the list of programming exercises still to do. Run one chapter with
`pytest python/course01_algebra_1/ch04.py`.

## Building the textbooks

Needs TeX Live (`latexmk`) and poppler-utils; on Windows, run from Git Bash or WSL.

```bash
./build.sh course-02-geometry
```

Run `./check-dashes.sh` before committing book changes. After a new course's LaTeX is written,
generate its workspace with `python tools/scaffold.py course-NN-slug` (it never overwrites
existing files). See [`HANDOFF.md`](HANDOFF.md) for the full authoring guide.
