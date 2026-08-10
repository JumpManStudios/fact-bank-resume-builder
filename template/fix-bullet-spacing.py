#!/usr/bin/env python3
"""
Post-render bullet-spacing cleanup for pandoc-generated resume/cover-letter .docx.

Why this exists
---------------
Pandoc renders every bullet as the "Compact" style with no explicit paragraph
spacing, so each bullet inherits docDefaults `after=160` (8pt). That puts a gap
after *every* bullet — including the last one in a group — leaving lists spread
out. The human editor always tightens the same way: bullets inside a group sit
flush, and the only gap is after the LAST bullet of each group, separating it
from the next section or sub-header.

This reproduces that automatically so first drafts ship pre-cleaned:
for every bullet that is NOT the last in its contiguous run, stamp an explicit
`w:spacing w:after="0"`. The last bullet of each run is left untouched, so it
keeps the inherited gap. Non-bullet paragraphs are never touched.

Notes
-----
- A "group" is a maximal run of consecutive list paragraphs. In these resumes
  every group is separated by a heading or a bold sub-header, so consecutive-run
  detection matches one visual bullet list.
- A single-bullet group keeps the gap (its only bullet is also its last), which
  is the consistent behavior across sections.
- Idempotent: re-running makes no further changes.

Usage: fix-bullet-spacing.py <file.docx> [more.docx ...]
"""
import os
import re
import sys
import zipfile
import xml.etree.ElementTree as ET

W = "http://schemas.openxmlformats.org/wordprocessingml/2006/main"


def w(tag):
    return f"{{{W}}}{tag}"


def register_ns(xml_bytes):
    """Preserve every xmlns prefix declared on the root so ET round-trips cleanly."""
    head = xml_bytes[:8000].decode("utf-8", "replace")
    for prefix, uri in re.findall(r'xmlns:([A-Za-z0-9]+)="([^"]+)"', head):
        try:
            ET.register_namespace(prefix, uri)
        except ValueError:
            pass
    m = re.search(r'xmlns="([^"]+)"', head)
    if m:
        ET.register_namespace("", m.group(1))


def is_bullet(p):
    pPr = p.find(w("pPr"))
    return pPr is not None and pPr.find(w("numPr")) is not None


def tighten(p):
    """Force `after=0` on this paragraph. Returns True if it changed anything."""
    pPr = p.find(w("pPr"))
    if pPr is None:
        return False
    sp = pPr.find(w("spacing"))
    if sp is None:
        sp = ET.Element(w("spacing"))
        # w:spacing must follow w:numPr / w:pStyle in the pPr child order.
        numPr = pPr.find(w("numPr"))
        anchor = numPr if numPr is not None else pPr.find(w("pStyle"))
        idx = list(pPr).index(anchor) + 1 if anchor is not None else 0
        pPr.insert(idx, sp)
    if sp.get(w("after")) == "0":
        return False
    sp.set(w("after"), "0")
    return True


def process_docx(path):
    with zipfile.ZipFile(path) as z:
        doc = z.read("word/document.xml")
    register_ns(doc)
    root = ET.fromstring(doc)
    paras = root.find(w("body")).findall(w("p"))

    changed = 0
    i, n = 0, len(paras)
    while i < n:
        if is_bullet(paras[i]):
            j = i
            while j < n and is_bullet(paras[j]):
                j += 1
            for k in range(i, j - 1):  # every bullet in the run except the last
                if tighten(paras[k]):
                    changed += 1
            i = j
        else:
            i += 1

    body_xml = ET.tostring(root, encoding="unicode")
    new_doc = (
        '<?xml version="1.0" encoding="UTF-8" standalone="yes"?>\r\n' + body_xml
    ).encode("utf-8")

    tmp = path + ".tmp"
    with zipfile.ZipFile(path) as zin, zipfile.ZipFile(
        tmp, "w", zipfile.ZIP_DEFLATED
    ) as zout:
        for item in zin.infolist():
            data = new_doc if item.filename == "word/document.xml" else zin.read(item.filename)
            zout.writestr(item, data)
    os.replace(tmp, path)
    return changed


def main(argv):
    files = argv[1:]
    if not files:
        print("usage: fix-bullet-spacing.py <file.docx> ...", file=sys.stderr)
        return 2
    for f in files:
        changed = process_docx(f)
        print(f"[fix-bullet-spacing] {os.path.basename(f)}: tightened {changed} bullet(s)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv))
