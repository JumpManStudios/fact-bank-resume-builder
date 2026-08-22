from conftest import load_review_docx
from docx_fixtures import W_NS, build_docx, comments_part

rd = load_review_docx()


def tracked_change_paragraph():
    """A paragraph with plain text, an accepted insertion, and a rejected-looking
    deletion, mimicking a Word tracked-changes round."""
    return (
        "<w:p>"
        '<w:r><w:t xml:space="preserve">Led the </w:t></w:r>'
        '<w:ins w:id="1" w:author="Editor">'
        '<w:r><w:t xml:space="preserve">cross-functional </w:t></w:r>'
        "</w:ins>"
        '<w:del w:id="2" w:author="Editor">'
        '<w:r><w:delText xml:space="preserve">small </w:delText></w:r>'
        "</w:del>"
        '<w:r><w:t xml:space="preserve">migration effort.</w:t></w:r>'
        "</w:p>"
    )


def plain_text_paragraph(text):
    return f'<w:p><w:r><w:t xml:space="preserve">{text}</w:t></w:r></w:p>'


def blank_paragraph():
    return "<w:p><w:pPr/></w:p>"


def test_final_paragraphs_accepts_insertions_and_drops_deletions(tmp_path):
    path = tmp_path / "returned.docx"
    build_docx(path, [tracked_change_paragraph()])

    paras = rd.final_paragraphs(str(path))

    assert paras == ["Led the cross-functional migration effort."]


def test_final_paragraphs_drops_blank_paragraphs(tmp_path):
    path = tmp_path / "returned.docx"
    build_docx(path, [plain_text_paragraph("Summary line."), blank_paragraph()])

    paras = rd.final_paragraphs(str(path))

    assert paras == ["Summary line."]


def test_comments_parses_author_and_text(tmp_path):
    path = tmp_path / "returned.docx"
    build_docx(
        path,
        [plain_text_paragraph("Bullet.")],
        comments_xml=comments_part(
            [("0", "Editor", "Tighten this."), ("1", "Editor", "Good metric.")]
        ),
    )

    result = rd.comments(str(path))

    assert result == [
        ("0", "Editor", "Tighten this."),
        ("1", "Editor", "Good metric."),
    ]


def test_comments_returns_empty_list_when_no_comments_part(tmp_path):
    path = tmp_path / "returned.docx"
    build_docx(path, [plain_text_paragraph("Bullet.")])

    assert rd.comments(str(path)) == []


def test_norm_folds_curly_quotes_and_dashes_and_collapses_whitespace():
    assert rd._norm("“Quoted”  text here—now") == '"Quoted" text here-now'
    assert rd._norm("a  \n  b") == "a b"


def test_cmd_diff_identical_after_normalization(tmp_path, capsys):
    a = tmp_path / "a.docx"
    b = tmp_path / "b.docx"
    build_docx(a, [plain_text_paragraph("Led the team—building tools.")])
    build_docx(b, [plain_text_paragraph('Led the team-building tools.')])

    exit_code = rd.cmd_diff(str(a), str(b))

    assert exit_code == 0
    assert "CONTENT IDENTICAL" in capsys.readouterr().out


def test_cmd_diff_reports_wording_differences(tmp_path, capsys):
    a = tmp_path / "a.docx"
    b = tmp_path / "b.docx"
    build_docx(a, [plain_text_paragraph("Led the small migration.")])
    build_docx(b, [plain_text_paragraph("Led the enterprise migration.")])

    exit_code = rd.cmd_diff(str(a), str(b))
    out = capsys.readouterr().out

    assert exit_code == 1
    assert "small" in out
    assert "enterprise" in out
