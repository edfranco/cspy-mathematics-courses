"""Generate Python exercise stubs and handwritten folders from the LaTeX chapters.

Usage: python tools/scaffold.py            (all courses)
       python tools/scaffold.py course-03-algebra-2-precalculus

Existing files are never overwritten, so it is safe to rerun after adding a course.
"""

import ast
import re
import sys
import textwrap
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
PY_ROOT = ROOT / "python"
HAND_ROOT = ROOT / "handwritten"

SIGNATURE = re.compile(r"\\lstinline!([A-Za-z_]\w*)\(([^!]*)\)!")
NOT_STUBS = {"print", "round", "range", "len", "abs", "int", "float", "str", "sum",
             "min", "max", "sorted", "math", "assert", "isinstance", "pow", "divmod"}

LATEX_SUBS = [
    (r"\\lstinline!([^!]*)!", r"`\1`"),
    (r"\\texttt\{([^{}]*)\}", r"`\1`"),
    (r"\\(?:textbf|emph|textit|text|mathrm)\{([^{}]*)\}", r"\1"),
    (r"\\[td]?frac\{(\w+)\}\{(\w+)\}", r"\1/\2"),
    (r"\\[td]?frac\{([^{}]*)\}\{([^{}]*)\}", r"(\1)/(\2)"),
    (r"\\sqrt\{([^{}]*)\}", r"sqrt(\1)"),
    (r"\\vv\{([^{}]*)\}", r"<\1>"),
    (r"\\abs\{([^{}]*)\}", r"|\1|"),
    (r"\\times", "*"), (r"\\cdot", "*"), (r"\\div", "/"),
    (r"\\le(?:q)?\b", "<="), (r"\\ge(?:q)?\b", ">="), (r"\\ne(?:q)?\b", "!="),
    (r"\\pm", "+/-"), (r"\\infty", "inf"), (r"\\degs", " deg"), (r"\\approx", "~"),
    (r"\\pi\b", "pi"), (r"\\theta\b", "theta"), (r"\\\{", "{"), (r"\\\}", "}"),
    (r"\\%", "%"), (r"\\\$", "$"), (r"\{,\}", ","), (r"\\[,;!]", " "), (r"~", " "),
    (r"\\(?:mathrel|operatorname)\{([^{}]*)\}", r"\1"),
    (r"\\[Bb]ig[lr]?", ""), (r"\\(?:left|right)\b", ""),
    (r"\\ref\{fig:([^{}]*)\}", r"(\1 figure in the book)"), (r"\\ref\{[^{}]*\}", "(see book)"),
    (r"_\{([^{}]*)\}", r"_\1"),
    (r"\\([A-Za-z]+)", r"\1"),
    (r"\$", ""),
]


def to_plain(latex):
    text = " ".join(latex.split())
    for _ in range(3):
        for pattern, repl in LATEX_SUBS:
            text = re.sub(pattern, repl, text)
    return text


def module_name(course_dir):
    return course_dir.name.replace("course-", "course", 1).replace("-", "_")


def code_exercises(tex):
    block = re.search(r"\\begin\{codeexercises\}(.*?)\\end\{codeexercises\}", tex, re.S)
    if not block:
        return []
    items = re.split(r"\\item\b", block.group(1))
    return [item.strip() for item in items if item.strip()]


def valid_args(name, args):
    try:
        ast.parse(f"def {name}({args}):\n    pass\n")
        return args
    except SyntaxError:
        return "*args"


def render_chapter(course_mod, chapter, title, exercises, known):
    lines = [f'"""Chapter {chapter}: {title}. Programming exercises C{chapter}.1 to '
             f'C{chapter}.{len(exercises)}.', "",
             "Solve the hand exercises first (see handwritten/), then implement each",
             "function and turn its test into real asserts using those answers.",
             "Standard library only; matplotlib is allowed for plots.", '"""', ""]
    imports, body = [], []
    for k, item in enumerate(exercises, 1):
        label = f"C{chapter}.{k}"
        wrapped = textwrap.wrap(to_plain(item), 84)
        body += ["", "", f"# {label}"] + [f"# {line}" for line in wrapped]
        for name, args in SIGNATURE.findall(item):
            if name in NOT_STUBS or name in known.get(course_mod + f".ch{chapter:02d}", {}):
                continue
            owner = next((mod for mod, names in known.items()
                          if mod.startswith(course_mod + ".") and name in names), None)
            if owner:
                imports.append(f"from {owner} import {name}  # noqa: F401")
                continue
            known.setdefault(f"{course_mod}.ch{chapter:02d}", set()).add(name)
            body += ["", "", f"def {name}({valid_args(name, args)}):",
                     f'    raise NotImplementedError("{label}")']
        body += ["", "", f"def test_{label.lower().replace('.', '_')}():",
                 f'    pytest.skip("{label}: write asserts from the hand exercises")']
    head = ["import pytest"] + sorted(set(imports))
    return "\n".join(lines + head + body) + "\n"


def scaffold(course_dir, known):
    course_mod = module_name(course_dir)
    pkg = PY_ROOT / course_mod
    pkg.mkdir(parents=True, exist_ok=True)
    (pkg / "__init__.py").touch()
    hand = HAND_ROOT / course_dir.name
    for tex_path in sorted(course_dir.glob("ch[0-9][0-9].tex")):
        chapter = int(tex_path.stem[2:])
        tex = tex_path.read_text(encoding="utf-8")
        title = re.search(r"\\chapter\{([^}]*)\}", tex).group(1)
        (hand / tex_path.stem).mkdir(parents=True, exist_ok=True)
        (hand / tex_path.stem / ".gitkeep").touch()
        exercises = code_exercises(tex)
        target = pkg / f"{tex_path.stem}.py"
        if not exercises:
            continue
        source = render_chapter(course_mod, chapter, title, exercises, known)
        if target.exists():
            print(f"   keep  {target.relative_to(ROOT)}")
            continue
        target.write_text(source, encoding="utf-8")
        print(f"   wrote {target.relative_to(ROOT)}")
    for extra in ("project", "exit-review"):
        (hand / extra).mkdir(parents=True, exist_ok=True)
        (hand / extra / ".gitkeep").touch()


def main(names):
    all_courses = sorted(p for p in ROOT.glob("course-*") if p.is_dir())
    wanted = {n.rstrip("/\\") for n in names}
    for course_dir in all_courses:
        if wanted and course_dir.name not in wanted:
            continue
        print(f"== {course_dir.name}")
        scaffold(course_dir, {})


if __name__ == "__main__":
    main(sys.argv[1:])
