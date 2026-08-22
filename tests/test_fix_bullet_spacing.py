import xml.etree.ElementTree as ET

from conftest import load_fix_bullet_spacing
from docx_fixtures import (
    bullet_paragraph,
    build_docx,
    plain_paragraph,
    read_content_types,
    read_document_xml,
    W_NS,
)

fbs = load_fix_bullet_spacing()


def _spacing_after(doc_xml, index):
    """Return the w:after value (or None) of the index'th <w:p> in document.xml."""
    root = ET.fromstring(doc_xml)
    paras = root.find(fbs.w("body")).findall(fbs.w("p"))
    pPr = paras[index].find(fbs.w("pPr"))
    if pPr is None:
        return None
    sp = pPr.find(fbs.w("spacing"))
    if sp is None:
        return None
    return sp.get(fbs.w("after"))


def test_tightens_all_but_last_bullet_in_a_group(tmp_path):
    path = tmp_path / "resume.docx"
    build_docx(
        path,
        [
            bullet_paragraph("first"),
            bullet_paragraph("second"),
            bullet_paragraph("third"),
            plain_paragraph("Next Section"),
        ],
    )

    changed, added_ct = fbs.process_docx(str(path))
    assert changed == 2
    assert added_ct == []

    doc_xml = read_document_xml(path)
    assert _spacing_after(doc_xml, 0) == "0"
    assert _spacing_after(doc_xml, 1) == "0"
    assert _spacing_after(doc_xml, 2) is None  # last bullet keeps inherited gap
    assert _spacing_after(doc_xml, 3) is None  # non-bullet paragraph untouched


def test_single_bullet_group_is_untouched(tmp_path):
    path = tmp_path / "resume.docx"
    build_docx(
        path,
        [
            plain_paragraph("Heading"),
            bullet_paragraph("only bullet"),
            plain_paragraph("Next Section"),
        ],
    )

    changed, added_ct = fbs.process_docx(str(path))
    assert changed == 0
    assert added_ct == []

    doc_xml = read_document_xml(path)
    assert _spacing_after(doc_xml, 1) is None


def test_two_separate_groups_each_tighten_independently(tmp_path):
    path = tmp_path / "resume.docx"
    build_docx(
        path,
        [
            bullet_paragraph("a1"),
            bullet_paragraph("a2"),
            plain_paragraph("Sub-header"),
            bullet_paragraph("b1"),
            bullet_paragraph("b2"),
            bullet_paragraph("b3"),
        ],
    )

    changed, added_ct = fbs.process_docx(str(path))
    assert changed == 3  # a1, b1, b2 (a2 and b3 are each their group's last)
    assert added_ct == []

    doc_xml = read_document_xml(path)
    assert _spacing_after(doc_xml, 0) == "0"  # a1
    assert _spacing_after(doc_xml, 1) is None  # a2 (last of group)
    assert _spacing_after(doc_xml, 3) == "0"  # b1
    assert _spacing_after(doc_xml, 4) == "0"  # b2
    assert _spacing_after(doc_xml, 5) is None  # b3 (last of group)


def test_idempotent_second_run_makes_no_changes(tmp_path):
    path = tmp_path / "resume.docx"
    build_docx(
        path,
        [
            bullet_paragraph("first"),
            bullet_paragraph("second"),
        ],
    )

    first_run, _ = fbs.process_docx(str(path))
    second_run, _ = fbs.process_docx(str(path))

    assert first_run == 1
    assert second_run == 0


def test_existing_after_value_is_overwritten_to_zero(tmp_path):
    path = tmp_path / "resume.docx"
    build_docx(
        path,
        [
            bullet_paragraph("first", existing_spacing_after="160"),
            bullet_paragraph("second"),
        ],
    )

    changed, added_ct = fbs.process_docx(str(path))
    assert changed == 1
    assert added_ct == []

    doc_xml = read_document_xml(path)
    assert _spacing_after(doc_xml, 0) == "0"


def test_other_zip_parts_are_preserved(tmp_path):
    path = tmp_path / "resume.docx"
    build_docx(path, [bullet_paragraph("first"), bullet_paragraph("second")])

    import zipfile

    with zipfile.ZipFile(path) as z:
        before = z.read("[Content_Types].xml")

    fbs.process_docx(str(path))

    with zipfile.ZipFile(path) as z:
        after = z.read("[Content_Types].xml")
        names = set(z.namelist())

    assert before == after
    assert "word/document.xml" in names
    assert "_rels/.rels" in names


def test_is_bullet_distinguishes_list_from_plain_paragraphs():
    bullet_xml = f'<w:p xmlns:w="{W_NS}"><w:pPr><w:numPr/></w:pPr></w:p>'
    plain_xml = f'<w:p xmlns:w="{W_NS}"><w:pPr/></w:p>'
    no_ppr_xml = f'<w:p xmlns:w="{W_NS}"/>'

    assert fbs.is_bullet(ET.fromstring(bullet_xml)) is True
    assert fbs.is_bullet(ET.fromstring(plain_xml)) is False
    assert fbs.is_bullet(ET.fromstring(no_ppr_xml)) is False


CONTENT_TYPES_NO_TTF = (
    '<?xml version="1.0" encoding="UTF-8" standalone="yes"?>\r\n'
    '<Types xmlns="http://schemas.openxmlformats.org/package/2006/content-types">'
    '<Default Extension="xml" ContentType="application/xml"/>'
    "</Types>"
)


def test_content_types_repaired_for_undeclared_font_extension(tmp_path):
    path = tmp_path / "resume.docx"
    build_docx(
        path,
        [bullet_paragraph("first")],
        content_types=CONTENT_TYPES_NO_TTF,
        extra_parts={"word/fonts/font1.ttf": b"\x00fake-font-bytes"},
    )

    changed, added_ct = fbs.process_docx(str(path))

    assert added_ct == ["ttf"]
    ct_xml = read_content_types(path)
    assert 'Extension="ttf"' in ct_xml
    assert 'ContentType="application/x-font-ttf"' in ct_xml


def test_content_types_repair_is_purely_additive(tmp_path):
    path = tmp_path / "resume.docx"
    build_docx(
        path,
        [plain_paragraph("text")],
        content_types=CONTENT_TYPES_NO_TTF,
        extra_parts={"word/fonts/font1.ttf": b"\x00fake"},
    )

    fbs.process_docx(str(path))
    ct_xml = read_content_types(path)

    assert 'Extension="xml"' in ct_xml  # pre-existing declaration untouched
    assert 'Extension="ttf"' in ct_xml  # new declaration added


def test_content_types_repair_is_idempotent(tmp_path):
    path = tmp_path / "resume.docx"
    build_docx(
        path,
        [plain_paragraph("text")],
        content_types=CONTENT_TYPES_NO_TTF,
        extra_parts={"word/fonts/font1.ttf": b"\x00fake"},
    )

    _, first_added = fbs.process_docx(str(path))
    _, second_added = fbs.process_docx(str(path))

    assert first_added == ["ttf"]
    assert second_added == []


def test_content_types_skips_already_declared_extension(tmp_path):
    already_declared = (
        '<?xml version="1.0" encoding="UTF-8" standalone="yes"?>\r\n'
        '<Types xmlns="http://schemas.openxmlformats.org/package/2006/content-types">'
        '<Default Extension="xml" ContentType="application/xml"/>'
        '<Default Extension="ttf" ContentType="application/x-font-ttf"/>'
        "</Types>"
    )
    path = tmp_path / "resume.docx"
    build_docx(
        path,
        [plain_paragraph("text")],
        content_types=already_declared,
        extra_parts={"word/fonts/font1.ttf": b"\x00fake"},
    )

    changed, added_ct = fbs.process_docx(str(path))

    assert added_ct == []  # already declared, so nothing to add


def test_content_types_ignores_unmapped_extensions(tmp_path):
    path = tmp_path / "resume.docx"
    build_docx(
        path,
        [plain_paragraph("text")],
        content_types=CONTENT_TYPES_NO_TTF,
        extra_parts={"word/embeddings/data.bin": b"\x00fake"},
    )

    changed, added_ct = fbs.process_docx(str(path))

    assert added_ct == []  # "bin" isn't in EXT_CONTENT_TYPES, so nothing declared


def test_process_docx_without_content_types_part_does_not_crash(tmp_path):
    import zipfile

    path = tmp_path / "resume.docx"
    build_docx(path, [bullet_paragraph("first"), bullet_paragraph("second")])

    # Strip [Content_Types].xml out entirely to simulate a package missing the part.
    with zipfile.ZipFile(path) as zin:
        items = [(i, zin.read(i.filename)) for i in zin.infolist() if i.filename != "[Content_Types].xml"]
    with zipfile.ZipFile(path, "w", zipfile.ZIP_DEFLATED) as zout:
        for item, data in items:
            zout.writestr(item, data)

    changed, added_ct = fbs.process_docx(str(path))

    assert changed == 1
    assert added_ct == []
