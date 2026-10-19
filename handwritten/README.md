# Handwritten Work

The curriculum's rule is "do it by hand first, then automate it." This folder holds the by-hand
half: exercise solutions, proofs, scratch work and notes, written on paper or a tablet and
saved here as scans or exports.

## Layout

```
handwritten/
  mistake-log.md            every error you make, and the rule it broke
  course-01-algebra-1/
    ch01/ .. ch11/          one folder per chapter (ch11 is the course project)
    project/                design sketches and math for the course Build
    exit-review/            the exit review, done cold, before moving on
```

## Naming

Use `chNN-<what>-<n>.<ext>` so files sort in reading order:

- `ch04-exercises-1.pdf`, `ch04-exercises-2.pdf` for Exercises 4.1 to 4.13
- `ch04-examples.pdf` for reworking the three worked examples without looking
- `ch04-notes.pdf` for your own summary of the Core Ideas
- `ch04-proof-4.12.pdf` for a proof exercise, one proof per file

PDF is preferred (one file per session, many pages). JPG or PNG is fine for a single page.
Keep scans under about 2 MB each; 150 to 200 dpi grayscale is plenty for handwriting. If the
folder grows past a few hundred MB, move images to Git LFS (`git lfs track "handwritten/**/*.jpg"`).

## Workflow per chapter

1. Read the chapter in `pdf/` and rework the worked examples on paper.
2. Do every exercise by hand. Write the answer in a box so it is easy to find.
3. Check against the answer key at the back of the book. Mark each one right or wrong.
4. Log every wrong answer in `mistake-log.md`, then redo it.
5. Scan the pages into this chapter's folder and commit.
6. Move to the programming exercises in `python/`, using your hand answers as test cases.

Proofs (marked "(proof)" in the book) have no key. Write them in full sentences, then check
them against the chapter's worked examples, or revisit them a week later with fresh eyes.
