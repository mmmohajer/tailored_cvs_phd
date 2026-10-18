import extract
import new_application


def test_extract_reads_text_markdown_html_and_skips_readme(tmp_path):
    (tmp_path / "README.md").write_text("ignore me", encoding="utf-8")
    (tmp_path / "notes.txt").write_text("Built a webhook integration handling many events a day.", encoding="utf-8")
    (tmp_path / "about.md").write_text("# About\nBackend engineer who likes reliable systems and tests.", encoding="utf-8")
    sub = tmp_path / "old"
    sub.mkdir()
    (sub / "cv.html").write_text("<p>Engineer at Acme</p><script>x()</script><p>Since 2022, building APIs</p>", encoding="utf-8")

    rows = extract.run(tmp_path)
    names = {name for name, _, _ in rows}
    assert names == {"notes.txt", "about.md", "old/cv.html"}
    html_text = (tmp_path / "_extracted" / "old__cv.html.txt").read_text(encoding="utf-8")
    assert "Engineer at Acme" in html_text and "x()" not in html_text
    assert (tmp_path / "_extracted" / "_index.md").exists()


def test_extract_flags_near_empty_files(tmp_path):
    (tmp_path / "scan.txt").write_text("  ", encoding="utf-8")
    rows = extract.run(tmp_path)
    assert rows[0][1].startswith("EMPTY")


def test_application_slug():
    assert new_application.application_slug("Acme Corp") == "acme-corp"
    assert new_application.application_slug("Lumen Pay", "Backend Engineer (Payments)") == "lumen-pay_backend-engineer-payments"
