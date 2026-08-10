#!/usr/bin/env bash
#
# Render a resume / cover-letter .md to .docx in the house style, then apply the
# bullet-spacing cleanup so drafts ship pre-tightened (no manual editor pass).
#
# Every render path (/tailor-resume, /cover-letter, re-renders, the review loop)
# should go through this wrapper instead of calling pandoc directly.
#
# Usage: template/render-resume.sh <input.md> <output.docx>
set -euo pipefail

IN="${1:?usage: render-resume.sh <input.md> <output.docx>}"
OUT="${2:?usage: render-resume.sh <input.md> <output.docx>}"
HERE="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"

# Find pandoc. Prefer a system install (may be a newer brew build); otherwise
# fall back to the pandoc bundled by pypandoc_binary (pip install -r requirements.txt).
PANDOC="$(command -v pandoc || true)"
for cand in /opt/homebrew/bin/pandoc /usr/local/bin/pandoc; do
  [ -z "$PANDOC" ] && [ -x "$cand" ] && PANDOC="$cand"
done
if [ -z "$PANDOC" ]; then
  PANDOC="$(python3 -c 'import pypandoc; print(pypandoc.get_pandoc_path())' 2>/dev/null || true)"
fi
[ -z "$PANDOC" ] && {
  echo "pandoc not found. Install either:" >&2
  echo "  pip install -r requirements.txt   (bundled pandoc, no system install)" >&2
  echo "  brew install pandoc               (system install)" >&2
  exit 1
}

"$PANDOC" "$IN" --reference-doc "$HERE/reference.docx" -o "$OUT"
python3 "$HERE/fix-bullet-spacing.py" "$OUT"
echo "[render-resume] wrote: $OUT"
