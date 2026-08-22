#!/usr/bin/env python3
"""
Post-render repairs for pandoc-generated resume/cover-letter .docx.

Two passes run over every rendered file: bullet-spacing cleanup (the original
reason this script exists) and a content-type repair that keeps Word able to
open the result at all. The filename predates the second pass.

Why the bullet-spacing pass exists
----------------------------------
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

Why the content-type pass exists
--------------------------------
`template/reference.docx` is a Google Docs export, and it embeds its fonts as
plain `.ttf` parts declared by `<Default Extension="ttf" .../>`. Pandoc copies
those font parts into its output but rebuilds `[Content_Types].xml` from its own
template, which has no `ttf` entry. The rendered package therefore contains five
font parts that no content type declares — an OPC violation. Word refuses the
whole document with "The file appears to be corrupted," while Google Docs,
LibreOffice, `pdftotext` and most ATS parsers read it without complaint, so the
breakage is invisible unless someone opens the .docx in Word.

The pass below restores any missing `<Default>` entry. It only ever adds
declarations for extensions actually present in the package, never removes or
rewrites existing ones, and is idempotent.

Usage: fix-bullet-spacing.py <file.docx> [more.docx ...]
"""
import os
import re
import sys
import zipfile
import xml.etree.ElementTree as ET

W = "http://schemas.openxmlformats.org/wordprocessingml/2006/main"
CONTENT_TYPES = "[Content_Types].xml"

# Content types for the binary parts pandoc may copy out of a --reference-doc
# without carrying over their <Default> declaration. Fonts are the ones that
# actually bite here; the image entries are cheap insurance for the same class
# of bug if a reference doc ever carries embedded images.
EXT_CONTENT_TYPES = {
    "ttf": "application/x-font-ttf",
    "otf": "application/x-font-otf",
    "odttf": "application/vnd.openxmlformats-officedocument.obfuscatedFont",
    "png": "image/png",
    "jpeg": "image/jpeg",
    "jpg": "image/jpeg",
    "gif": "image/gif",
    "emf": "image/x-emf",
    "wmf": "image/x-wmf",
}


def w(tag):
    return f"{{{W}}}{tag}"


def repair_content_types(names, ct_xml):
    """Declare any part extension the package uses but never declares.

    Returns (new_bytes, [extensions_added]). Purely additive: existing Default
    and Override entries are left exactly as they are.
    """
    text = ct_xml.decode("utf-8")
    declared = {e.lower() for e in re.findall(r'<Default[^>]*Extension="([^"]+)"', text)}
    overridden = {
        p.lstrip("/").lower()
        for p in re.findall(r'<Override[^>]*PartName="([^"]+)"', text)
    }

    added = []
    for name in names:
        if name.endswith("/") or name.lower() in overridden or "." not in name:
            continue
        ext = name.rsplit(".", 1)[-1].lower()
        if ext in declared:
            continue
        ct = EXT_CONTENT_TYPES.get(ext)
        if ct is None:
            continue
        declared.add(ext)
        added.append(ext)
        text = text.replace(
            "</Types>", f'<Default Extension="{ext}" ContentType="{ct}"/></Types>', 1
        )
    return text.encode("utf-8"), added


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
        names = z.namelist()
        ct_xml = z.read(CONTENT_TYPES) if CONTENT_TYPES in names else None
    new_ct, added_ct = (
        repair_content_types(names, ct_xml) if ct_xml is not None else (None, [])
    )
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
            if item.filename == "word/document.xml":
                data = new_doc
            elif item.filename == CONTENT_TYPES and new_ct is not None:
                data = new_ct
            else:
                data = zin.read(item.filename)
            zout.writestr(item, data)
    os.replace(tmp, path)
    return changed, added_ct


def main(argv):
    files = argv[1:]
    if not files:
        print("usage: fix-bullet-spacing.py <file.docx> ...", file=sys.stderr)
        return 2
    for f in files:
        changed, added_ct = process_docx(f)
        note = ""
        if added_ct:
            note = f"; declared missing content type(s): {', '.join(added_ct)}"
        print(
            f"[fix-bullet-spacing] {os.path.basename(f)}: "
            f"tightened {changed} bullet(s){note}"
        )
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv))
