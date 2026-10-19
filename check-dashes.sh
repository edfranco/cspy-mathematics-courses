#!/usr/bin/env bash
# Fails if any em dash (U+2014) or LaTeX '---' appears in sources or docs.
set -u
cd "$(dirname "$0")"
bad=0
hits=$(python3 -c "import pathlib;print('\n'.join(str(p) for p in pathlib.Path('.').rglob('*') if p.suffix in ('.tex','.md','.sh') and '.git' not in p.parts and '\u2014' in p.read_text(errors='ignore')))")
if [ -n "$hits" ]; then echo "em dash found in:"; echo "$hits"; bad=1; fi
if grep -rn --include='*.tex' -e '---' . >/dev/null; then echo "LaTeX '---' found:"; grep -rn --include='*.tex' -e '---' .; bad=1; fi
[ $bad -eq 0 ] && echo "no em dashes"
exit $bad
