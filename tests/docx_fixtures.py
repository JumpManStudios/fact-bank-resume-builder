"""Minimal in-memory .docx builders for testing template/fix-bullet-spacing.py
and template/review-docx.py without a python-docx dependency.

Both scripts only read/write specific parts of the zip (word/document.xml,
word/comments.xml), so these fixtures only need to be valid enough for those
parts — not a fully spec-compliant Word package.
"""
import zipfile

W_NS = "http://schemas.openxmlformats.org/wordprocessingml/2006/main"

CONTENT_TYPES = (
    '<?xml version="1.0" encoding="UTF-8" standalone="yes"?>\r\n'
    '<Types xmlns="http://schemas.openxmlformats.org/package/2006/content-types">'
    '<Default Extension="xml" ContentType="application/xml"/>'
    "</Types>"
)

RELS = (
    '<?xml version="1.0" encoding="UTF-8" standalone="yes"?>\r\n'
    '<Relationships xmlns="http://schemas.openxmlformats.org/package/2006/relationships"/>'
)

DOCUMENT_WRAPPER = (
    '<?xml version="1.0" encoding="UTF-8" standalone="yes"?>\r\n'
    '<w:document xmlns:w="{ns}">'
    "<w:body>{body}</w:body>"
    "</w:document>"
).format(ns=W_NS, body="{body}")


def bullet_paragraph(text, existing_spacing_after=None):
    """A list-item paragraph (has w:numPr), optionally with an existing spacing elt."""
    spacing = (
        f'<w:spacing w:after="{existing_spacing_after}"/>'
        if existing_spacing_after is not None
        else ""
    )
    return (
        "<w:p><w:pPr>"
        '<w:pStyle w:val="ListParagraph"/>'
        '<w:numPr><w:ilvl w:val="0"/><w:numId w:val="1"/></w:numPr>'
        f"{spacing}"
        f'</w:pPr><w:r><w:t xml:space="preserve">{text}</w:t></w:r></w:p>'
    )


def plain_paragraph(text):
    """A non-bullet paragraph (heading/body text, no numPr)."""
    return f'<w:p><w:r><w:t xml:space="preserve">{text}</w:t></w:r></w:p>'


def build_docx(path, paragraphs_xml, comments_xml=None):
    """Write a minimal .docx to `path` with the given raw <w:p> XML fragments."""
    body = "".join(paragraphs_xml)
    document_xml = DOCUMENT_WRAPPER.format(body=body).encode("utf-8")

    with zipfile.ZipFile(path, "w", zipfile.ZIP_DEFLATED) as z:
        z.writestr("[Content_Types].xml", CONTENT_TYPES)
        z.writestr("_rels/.rels", RELS)
        z.writestr("word/document.xml", document_xml)
        if comments_xml is not None:
            z.writestr("word/comments.xml", comments_xml)
    return path


def comments_part(comments):
    """comments: list of (id, author, text) -> word/comments.xml bytes."""
    items = "".join(
        f'<w:comment w:id="{cid}" w:author="{author}">'
        f'<w:p><w:r><w:t xml:space="preserve">{text}</w:t></w:r></w:p>'
        "</w:comment>"
        for cid, author, text in comments
    )
    return (
        '<?xml version="1.0" encoding="UTF-8" standalone="yes"?>\r\n'
        f'<w:comments xmlns:w="{W_NS}">{items}</w:comments>'
    ).encode("utf-8")


def read_document_xml(path):
    with zipfile.ZipFile(path) as z:
        return z.read("word/document.xml")
