from pathlib import Path

import pytest

import render

RESUME = """# Ada Example
Backend Engineer | Python
Toronto, ON | ada@example.com | [github.com/ada](https://github.com/ada)

## Experience

### Engineer | Acme | Remote | Jan 2022 – Present

- Cut latency from 900 ms to 250 ms.

## Projects

### Tool | Python | [github.com/ada/tool](https://github.com/ada/tool)

- Did a thing.
"""


def test_header_is_split_into_name_headline_contact():
    _, header, _ = render.markdown_to_html(RESUME, "resume")
    assert "<h1>Ada Example</h1>" in header
    assert '<p class="headline">Backend Engineer | Python</p>' in header
    assert 'href="https://github.com/ada"' in header


def test_entry_with_date_is_right_aligned():
    _, _, body = render.markdown_to_html(RESUME, "resume")
    assert '<span class="entry-title">Engineer</span>' in body
    assert '<span class="entry-meta"> · Acme · Remote</span>' in body
    assert '<span class="entry-date">Jan 2022 – Present</span>' in body


def test_entry_without_date_keeps_link_as_meta():
    _, _, body = render.markdown_to_html(RESUME, "resume")
    assert "entry-date" not in body.split('class="projects"')[1]
    assert 'href="https://github.com/ada/tool"' in body


def test_sections_are_wrapped_with_slug_class():
    _, _, body = render.markdown_to_html(RESUME, "resume")
    assert '<section class="experience">' in body
    assert '<section class="projects">' in body


def test_cover_letter_keeps_single_line_breaks():
    letter = "# Ada Example\nEngineer\nada@example.com\n\nHiring Team\nAcme\n\nDear Team,\n"
    _, _, body = render.markdown_to_html(letter, "cover_letter")
    assert "Hiring Team<br />" in body


def test_missing_name_line_is_rejected():
    with pytest.raises(ValueError):
        render.markdown_to_html("Ada\n\n## Experience\n", "resume")


def test_detect_kind():
    assert render.detect_kind(Path("cover_letter.md")) == "cover_letter"
    assert render.detect_kind(Path("resume.md")) == "resume"


def test_build_html_links_stylesheet_relatively(tmp_path):
    md = tmp_path / "resume.md"
    md.write_text(RESUME, encoding="utf-8")
    out = render.build_html(md, "classic")
    html = out.read_text(encoding="utf-8")
    assert 'rel="stylesheet"' in html and "classic.css" in html
    assert '<body class="resume">' in html
