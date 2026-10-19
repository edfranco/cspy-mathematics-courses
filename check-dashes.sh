#!/usr/bin/env bash
# Fails if any em dash (U+2014) or LaTeX '---' appears in sources or docs.
set -u
cd "$(dirname "$0")"
bad=0
py=python3
python3 -c '' 2>/dev/null || py=python
hits=$($py -c "import pathlib;print('\n'.join(str(p) for p in pathlib.Path('.').rglob('*') if p.suffix in ('.tex','.md','.sh','.py') and not {'.git','.venv'} & set(p.parts) and '\u2014' in p.read_text(encoding='utf-8', errors='ignore')))") || { echo "python failed; dash check did not run"; exit 2; }
if [ -n "$hits" ]; then echo "em dash found in:"; echo "$hits"; bad=1; fi
if grep -rn --include='*.tex' -e '---' . >/dev/null; then echo "LaTeX '---' found:"; grep -rn --include='*.tex' -e '---' .; bad=1; fi
[ $bad -eq 0 ] && echo "no em dashes"
exit $bad
