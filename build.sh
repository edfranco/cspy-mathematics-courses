#!/usr/bin/env bash
# Build one course (./build.sh course-02-geometry) or every course (./build.sh).
# Requires TeX Live with latexmk and poppler-utils; see HANDOFF.md for the package list.
set -euo pipefail
cd "$(dirname "$0")"
courses=("$@")
if [ ${#courses[@]} -eq 0 ]; then courses=(course-*/); fi
mkdir -p pdf
for c in "${courses[@]}"; do
  c="${c%/}"
  echo "== building $c"
  ( cd "$c" && latexmk -pdf -interaction=nonstopmode main.tex >/dev/null 2>&1 ) || true
  if grep -q '^!' "$c/main.log"; then
    echo "LaTeX errors in $c/main.log:"; grep -n -A6 '^!' "$c/main.log" | head -40; exit 1
  fi
  echo "   pages: $(pdfinfo "$c/main.pdf" | awk '/^Pages/{print $2}')"
  bad=$(grep -E 'Overfull \\hbox \([0-9.]+pt' "$c/main.log" | sed -E 's/.*\(([0-9.]+)pt.*/\1/' | awk '$1>5{n++} END{print n+0}')
  echo "   overfull lines wider than 5pt: $bad"
  title=$(grep -oP 'pdftitle=\{\K[^}]*' "$c/main.tex" | head -1 | sed "s/[:']//g" | tr ' ' '-')
  cp "$c/main.pdf" "pdf/${title}.pdf"
  echo "   -> pdf/${title}.pdf"
done
