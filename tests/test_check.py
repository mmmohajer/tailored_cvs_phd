import check

MASTER = """# Ada Example
Engineer
ada@example.com

## Experience

### Engineer | Acme | Remote | Jan 2022 – Present

- Cut latency from 900 ms to 250 ms; 4+ years; served ~1,100 users; 18% fewer errors.
"""


def write(tmp_path, name, text):
    path = tmp_path / name
    path.write_text(text, encoding="utf-8")
    return path


def test_numbers_ignore_header_and_letter_date():
    text = "# Ada\nEngineer\n(555) 010-0199\n\nOctober 17, 2026\n\nI cut errors by 18%.\n"
    assert check.numbers_in(check.body_lines(text)) == {"18%"}


def test_numbers_normalize_commas_and_ignore_inside_words():
    assert check.numbers_in(["~1,100 users, p95 at 250 ms, $1.2M saved, 3x faster"]) == {"1100", "250", "$1.2m", "3x"}


def test_fact_trace_passes_when_numbers_exist(tmp_path):
    md = write(tmp_path, "resume.md", MASTER.replace("Cut latency", "Reduced latency"))
    report = check.Report()
    check.fact_trace(md, MASTER, report)
    assert not report.failed


def test_fact_trace_fails_on_invented_number(tmp_path):
    md = write(tmp_path, "resume.md", MASTER + "- Grew revenue 40%.\n")
    report = check.Report()
    check.fact_trace(md, MASTER, report)
    assert report.failed
    assert "40%" in report.rows[0][1]


def test_fact_trace_fails_on_unknown_employer(tmp_path):
    md = write(tmp_path, "resume.md", MASTER.replace("| Acme |", "| Globex |"))
    report = check.Report()
    check.fact_trace(md, MASTER, report)
    assert any("Globex" in msg for level, msg in report.rows if level == "FAIL")


def test_keyword_coverage_warns_on_missing(tmp_path):
    md = write(tmp_path, "resume.md", MASTER)
    write(tmp_path, "keywords.txt", "# comment\nlatency\nKafka\n")
    report = check.Report()
    check.keyword_coverage(tmp_path, md, report)
    assert report.rows == [("WARN", "keywords: 1/2 in resume.md; missing: Kafka")]


def test_master_text_skips_open_questions(tmp_path):
    write(tmp_path, "master_resume.md", "real 5 facts")
    write(tmp_path, "open_questions.md", "was it 99%?")
    assert "99%" not in check.master_text(tmp_path)
