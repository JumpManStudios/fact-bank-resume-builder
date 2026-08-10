#!/usr/bin/env python3
"""
Helpers for the /apply-review loop (folding an editor-reviewed .docx back into
its .md source).

Two modes:

  review-docx.py text <docx>
      Print the document's FINAL text, one paragraph per line, with Word tracked
      changes resolved (insertions accepted, deletions dropped). Then print any
      comments as `[author] text`. Use this to see exactly what the editor's
      returned copy says so you can mirror it into the .md.

      If the editor typed directly (no tracked changes, like some rounds), the
      final text is just the paragraph text — still correct.

      Comments are surfaced here and should be archived to a review-notes log by
      the caller; they are discussion, NOT content, and never go into the .md.

  review-docx.py diff <returned.docx> <rendered.docx>
      Normalized CONTENT diff between two docx (curly quotes, non-breaking
      spaces, en/em dashes and arrows folded; whitespace collapsed; blank
      paragraphs dropped). Formatting/spacing differences are intentionally
      invisible here — only wording differences show. Empty output => content
      identical.

Standard library only.
"""
import re
import sys
import zipfile
import difflib
import xml.etree.ElementTree as ET

W = "http://schemas.openxmlformats.org/wordprocessingml/2006/main"


def w(tag):
    return f"{{{W}}}{tag}"


def _read(docx, member):
    with zipfile.ZipFile(docx) as z:
        if member in z.namelist():
            return z.read(member)
    return None


def final_paragraphs(docx):
    """Paragraph text with tracked changes resolved to the accepted/final state."""
    root = ET.fromstring(_read(docx, "word/document.xml"))
    out = []
    for p in root.find(w("body")).findall(w("p")):
        parts = []
        for node in p.iter():
            tag = node.tag
            if tag == w("t"):
                # skip delText (handled below); w:t inside w:ins or plain runs = kept
                parts.append(node.text or "")
            elif tag == w("delText"):
                # a deletion — excluded from final text
                pass
        # w:t inside w:del does not exist (deletions use w:delText), and
        # w:t inside w:ins is normal w:t, so iterating w:t already yields the
        # final text (kept + inserted), excluding deletions. delText is ignored.
        text = "".join(parts)
        if text.strip():
            out.append(text)
    return out


def comments(docx):
    raw = _read(docx, "word/comments.xml")
    if not raw:
        return []
    root = ET.fromstring(raw)
    res = []
    for c in root.iter(w("comment")):
        author = c.get(w("author")) or "?"
        text = "".join(t.text or "" for t in c.iter(w("t")))
        res.append((c.get(w("id")), author, text.strip()))
    return res


def _norm(s):
    for a, b in [("’", "'"), ("‘", "'"), ("“", '"'), ("”", '"'),
                 ("\xa0", " "), ("–", "-"), ("—", "-"), ("→", "->")]:
        s = s.replace(a, b)
    return " ".join(s.split())


def cmd_text(docx):
    print("===== FINAL TEXT (tracked changes resolved) =====")
    for line in final_paragraphs(docx):
        print(line)
    cs = comments(docx)
    print(f"\n===== COMMENTS ({len(cs)}) =====")
    if not cs:
        print("(none)")
    for cid, author, text in cs:
        print(f"[{author}] {text}")


def cmd_diff(a, b):
    na = [_norm(x) for x in final_paragraphs(a)]
    nb = [_norm(x) for x in final_paragraphs(b)]
    diff = list(difflib.unified_diff(na, nb, fromfile=a, tofile=b, lineterm=""))
    if not diff:
        print("CONTENT IDENTICAL (formatting/spacing ignored)")
    else:
        print("\n".join(diff))
    return 1 if diff else 0


def main(argv):
    if len(argv) >= 3 and argv[1] == "text":
        cmd_text(argv[2])
        return 0
    if len(argv) >= 4 and argv[1] == "diff":
        return cmd_diff(argv[2], argv[3])
    print(__doc__.strip().splitlines()[0], file=sys.stderr)
    print("usage: review-docx.py text <docx> | diff <a.docx> <b.docx>", file=sys.stderr)
    return 2


if __name__ == "__main__":
    raise SystemExit(main(sys.argv))
