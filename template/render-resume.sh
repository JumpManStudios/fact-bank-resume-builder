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

# This repo is used from macOS, Windows (Git Bash), and the Claude Code mobile app,
# so neither pandoc nor Python can be assumed to live under a fixed name or path.
# Both lookups below probe by CAPABILITY (does the candidate actually run / import
# what we need?) rather than trusting a name to mean what it says. On Windows in
# particular, the python3.exe / python.exe entries under WindowsApps are Microsoft
# Store app-execution alias stubs: they appear on PATH but do not execute, and the
# only working interpreter is the `py` launcher.
PY_CANDIDATES="python3 python py"

# Find a Python 3 that actually runs. fix-bullet-spacing.py is standard-library
# only (zipfile + xml.etree), so no third-party module is required here.
PY=""
for cand in $PY_CANDIDATES; do
  if [ -z "$PY" ] && command -v "$cand" >/dev/null 2>&1 \
     && "$cand" -c 'import sys, zipfile; assert sys.version_info[0] == 3' >/dev/null 2>&1; then
    PY="$cand"
  fi
done

# Find pandoc. Prefer a system install (may be a newer brew build); otherwise
# fall back to the pandoc bundled by pypandoc_binary (pip install -r requirements.txt).
# The pypandoc fallback is probed across every interpreter, not just $PY, since the
# one holding pypandoc need not be the one that runs the spacing script.
PANDOC="$(command -v pandoc || true)"
for cand in /opt/homebrew/bin/pandoc /usr/local/bin/pandoc; do
  [ -z "$PANDOC" ] && [ -x "$cand" ] && PANDOC="$cand"
done
for cand in $PY_CANDIDATES; do
  if [ -z "$PANDOC" ] && command -v "$cand" >/dev/null 2>&1; then
    PANDOC="$("$cand" -c 'import pypandoc; print(pypandoc.get_pandoc_path())' 2>/dev/null || true)"
  fi
done
[ -z "$PANDOC" ] && {
  echo "pandoc not found. Install either:" >&2
  echo "  pip install -r requirements.txt   (bundled pandoc, no system install)" >&2
  echo "  brew install pandoc               (system install)" >&2
  exit 1
}

"$PANDOC" "$IN" --reference-doc "$HERE/reference.docx" -o "$OUT"
[ -z "$PY" ] && {
  echo "No working Python 3 found (tried: $PY_CANDIDATES)." >&2
  echo "fix-bullet-spacing.py did not run, so '$OUT' is NOT SHIPPABLE:" >&2
  echo "  * Microsoft Word will refuse to open it (\"file appears to be" >&2
  echo "    corrupted\") because pandoc drops the .ttf content-type declaration" >&2
  echo "    that reference.docx's embedded fonts depend on." >&2
  echo "  * It also still has pandoc's loose bullet spacing." >&2
  echo "Install Python 3, or run the cleanup by hand before sending the file:" >&2
  echo "  <your-python> template/fix-bullet-spacing.py \"$OUT\"" >&2
  exit 1
}
"$PY" "$HERE/fix-bullet-spacing.py" "$OUT"
echo "[render-resume] wrote: $OUT"
