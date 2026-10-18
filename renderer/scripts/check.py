"""Mechanical checks on a rendered resume / cover letter folder.

Usage:
    python renderer/scripts/check.py custom_resumes/acme-corp_backend-engineer
    python renderer/scripts/check.py custom_resumes/acme-corp_backend-engineer --max-pages 1
    python renderer/scripts/check.py master --max-pages 0      # master has no page limit

Checks:
  - PDF page count, text layer present, name + email readable (what a parser sees)
  - Required resume sections present
  - Cover letter fits one page and 250-400 body words (warn outside 200-450)
  - Fact trace: every number and employer in the tailored files exists in master/
  - Keyword coverage against keywords.txt (warn only: a missing keyword may be an honest gap)

Exit code 1 when any FAIL is reported.
"""

from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
NUMBER = re.compile(r"(?<![\w.])\$?\d[\d,]*(?:\.\d+)?\s?(?:%|x|k|m|b|\+)?(?![\w])", re.IGNORECASE)
LETTER_DATE = re.compile(
    r"^(january|february|march|april|may|june|july|august|september|october|november|december)\s+\d{1,2},\s+\d{4}$",
    re.IGNORECASE,
)
EMAIL = re.compile(r"[\w.+-]+@[\w-]+\.[\w.-]+")
REQUIRED_SECTIONS = ("experience", "education")


class Report:
    def __init__(self) -> None:
        self.rows: list[tuple[str, str]] = []

    def add(self, level: str, message: str) -> None:
        self.rows.append((level, message))

    @property
    def failed(self) -> bool:
        return any(level == "FAIL" for level, _ in self.rows)

    def print(self) -> None:
        for level, message in self.rows:
            print(f"{level:<5} {message}")
        print("\nRESULT:", "FAIL" if self.failed else "PASS")


def strip_comments(text: str) -> str:
    return re.sub(r"<!--.*?-->", "", text, flags=re.DOTALL)


def body_lines(md_text: str) -> list[str]:
    """Markdown lines after the 3-line header block."""
    lines = strip_comments(md_text).strip().splitlines()
    i = 0
    while i < len(lines) and lines[i].strip():
        i += 1
    return lines[i:]


def norm_number(token: str) -> str:
    return re.sub(r"[\s,]", "", token.lower())


def numbers_in(lines: list[str]) -> set[str]:
    found = set()
    for line in lines:
        if LETTER_DATE.match(line.strip()):
            continue
        line = re.sub(r"\]\([^)]*\)", "]", line)
        found |= {norm_number(m.group(0)) for m in NUMBER.finditer(line)}
    return found


def employers_in(md_text: str) -> set[str]:
    employers, in_experience = set(), False
    for line in strip_comments(md_text).splitlines():
        if line.startswith("## "):
            in_experience = "experience" in line.lower()
        elif in_experience and line.startswith("### ") and "|" in line:
            cells = [c.strip() for c in line[4:].split("|")]
            if len(cells) > 1:
                employers.add(cells[1])
    return employers


NOT_FACTS = {"open_questions.md", "review.md", "README.md"}


def master_text(master_dir: Path) -> str:
    parts = [p.read_text(encoding="utf-8") for p in sorted(master_dir.glob("*.md")) if p.name not in NOT_FACTS]
    return strip_comments("\n".join(parts))


def fact_trace(md_path: Path, master: str, report: Report) -> None:
    text = md_path.read_text(encoding="utf-8")
    master_numbers = numbers_in(master.splitlines())
    missing = sorted(numbers_in(body_lines(text)) - master_numbers)
    if missing:
        report.add("FAIL", f"{md_path.name}: numbers not found in master/: {', '.join(missing)}")
    else:
        report.add("OK", f"{md_path.name}: every number traces to master/")

    lower_master = master.lower()
    unknown = sorted(e for e in employers_in(text) if e.lower() not in lower_master)
    if unknown:
        report.add("FAIL", f"{md_path.name}: employers not in master/: {', '.join(unknown)}")


def pdf_checks(pdf: Path, max_pages: int, name: str, kind: str, report: Report) -> None:
    from pypdf import PdfReader

    reader = PdfReader(str(pdf))
    pages = len(reader.pages)
    text = "\n".join((p.extract_text() or "") for p in reader.pages)
    limit = 1 if kind == "cover_letter" else max_pages
    if limit and pages > limit:
        report.add("FAIL", f"{pdf.name}: {pages} pages (limit {limit})")
    else:
        report.add("OK", f"{pdf.name}: {pages} page(s)")
    if len(text.strip()) < 200:
        report.add("FAIL", f"{pdf.name}: almost no extractable text (parsers will see nothing)")
        return
    flat = re.sub(r"\s+", " ", text).lower()
    if name and name.lower() not in flat:
        report.add("FAIL", f"{pdf.name}: name '{name}' not readable in PDF text")
    if not EMAIL.search(text):
        report.add("FAIL", f"{pdf.name}: no email address readable in PDF text")
    if kind == "resume":
        for section in REQUIRED_SECTIONS:
            if section not in flat:
                report.add("FAIL", f"{pdf.name}: missing '{section.title()}' section")


def cover_letter_words(md_path: Path, report: Report) -> None:
    words = len(re.findall(r"[A-Za-z0-9'’-]+", "\n".join(body_lines(md_path.read_text(encoding="utf-8")))))
    if words < 200 or words > 450:
        report.add("WARN", f"{md_path.name}: {words} words (target 250-400)")
    else:
        report.add("OK", f"{md_path.name}: {words} words")


def keyword_coverage(folder: Path, resume_md: Path, report: Report) -> None:
    kw_file = folder / "keywords.txt"
    if not kw_file.exists():
        return
    keywords = [k.strip() for k in kw_file.read_text(encoding="utf-8").splitlines() if k.strip() and not k.startswith("#")]
    if not keywords:
        return
    text = strip_comments(resume_md.read_text(encoding="utf-8")).lower()
    missing = [k for k in keywords if not re.search(r"(?<!\w)" + re.escape(k.lower()) + r"(?!\w)", text)]
    covered = len(keywords) - len(missing)
    level = "OK" if not missing else "WARN"
    report.add(level, f"keywords: {covered}/{len(keywords)} in resume.md" + (f"; missing: {', '.join(missing)}" if missing else ""))


def person_name(md_path: Path) -> str:
    first = strip_comments(md_path.read_text(encoding="utf-8")).strip().splitlines()[0]
    return first[2:].strip() if first.startswith("# ") else ""


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("folder", type=Path)
    parser.add_argument("--master", type=Path, default=ROOT / "master")
    parser.add_argument("--max-pages", type=int, default=2, help="Resume page limit; 0 = no limit")
    args = parser.parse_args(argv)

    folder = args.folder.resolve()
    master_dir = args.master.resolve()
    report = Report()
    is_master = folder == master_dir

    mds = sorted(p for p in folder.glob("*.md") if "resume" in p.stem or "cover" in p.stem)
    if not mds:
        raise SystemExit(f"No resume/cover letter Markdown in {folder}")

    master = master_text(master_dir) if master_dir.exists() else ""
    if not is_master and not master:
        report.add("FAIL", f"No master files in {master_dir}; build the master first")

    for md in mds:
        kind = "cover_letter" if "cover" in md.stem else "resume"
        pdf = md.with_suffix(".pdf")
        if pdf.exists():
            pdf_checks(pdf, args.max_pages, person_name(md), kind, report)
        else:
            report.add("FAIL", f"{pdf.name} missing; run render.py first")
        if kind == "cover_letter":
            cover_letter_words(md, report)
        if not is_master and master:
            fact_trace(md, master, report)
        if kind == "resume" and not is_master:
            keyword_coverage(folder, md, report)

    report.print()
    return 1 if report.failed else 0


if __name__ == "__main__":
    sys.exit(main())
