"""Mechanical checks on a rendered CV / statement folder.

Usage:
    python renderer/scripts/check.py custom_resumes/university_program
    python renderer/scripts/check.py custom_resumes/university_program --max-pages 2
    python renderer/scripts/check.py master --max-pages 0      # master CV has no page limit

Checks:
  - PDF page count, text layer present, name + email readable
  - CV has Education and Research (or Experience)
  - Cover letter, email, and follow-up length (warn outside the targets in cover_letter_words)
  - Fact trace: every number and organization in the tailored files exists in master/
  - Keyword coverage against keywords.txt (warn only: a missing term may be an honest gap)

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


def is_application_md(path: Path) -> bool:
    stem = path.stem.lower()
    if stem in {"cv", "statement"}:
        return True
    return any(token in stem for token in ("resume", "cover", "statement", "proposal", "motivation", "email", "follow_up"))


def kind_of(path: Path) -> str:
    stem = path.stem.lower()
    if any(token in stem for token in ("cover", "statement", "proposal", "motivation", "email", "follow_up")):
        return "cover_letter"
    return "resume"


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
            heading = line.lower()
            in_experience = "experience" in heading or "research" in heading
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
    if "follow" in md_path.stem.lower():
        report.add("OK", f"{md_path.name}: timing plan, not a source of new facts")
    else:
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
    limit = max_pages
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
    if "follow" not in pdf.stem.lower() and not EMAIL.search(text):
        report.add("FAIL", f"{pdf.name}: no email address readable in PDF text")
    if kind == "resume":
        if "education" not in flat:
            report.add("FAIL", f"{pdf.name}: missing 'Education' section")
        if "experience" not in flat and "research" not in flat:
            report.add("FAIL", f"{pdf.name}: missing 'Research' or 'Experience' section")


def cover_letter_words(md_path: Path, report: Report) -> None:
    words = len(re.findall(r"[A-Za-z0-9'’-]+", "\n".join(body_lines(md_path.read_text(encoding="utf-8")))))
    stem = md_path.stem.lower()
    if "follow" in stem:
        if words < 40:
            report.add("WARN", f"{md_path.name}: {words} words (a follow-up plan needs the send, the one reminder, and the stop)")
        else:
            report.add("OK", f"{md_path.name}: {words} words")
        return
    if "email" in stem:
        low, high, target = 80, 220, "120-180"
    elif "proposal" in stem:
        low, high, target = 400, 3000, "1000-1500 unless the position sets a limit"
    elif "motivation" in stem:
        low, high, target = 300, 900, "400-700 (often 1-2 pages)"
    elif "cover" in stem:
        low, high, target = 180, 550, "250-400, one page, unless the position sets a limit"
    else:
        low, high, target = 500, 1200, "700-1000 unless the position sets a limit"
    if words < low or words > high:
        report.add("WARN", f"{md_path.name}: {words} words (target {target})")
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
    report.add(level, f"keywords: {covered}/{len(keywords)} in {resume_md.name}" + (f"; missing: {', '.join(missing)}" if missing else ""))


def person_name(md_path: Path) -> str:
    first = strip_comments(md_path.read_text(encoding="utf-8")).strip().splitlines()[0]
    return first[2:].strip() if first.startswith("# ") else ""


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("folder", type=Path)
    parser.add_argument("--master", type=Path, default=ROOT / "master")
    parser.add_argument("--max-pages", type=int, default=2, help="Page limit for the CV and statement; 0 = no limit")
    args = parser.parse_args(argv)

    folder = args.folder.resolve()
    master_dir = args.master.resolve()
    report = Report()
    is_master = folder == master_dir

    mds = sorted(p for p in folder.glob("*.md") if is_application_md(p))
    if not mds:
        raise SystemExit(f"No CV or statement Markdown in {folder}")

    master = master_text(master_dir) if master_dir.exists() else ""
    if not is_master and not master:
        report.add("FAIL", f"No master files in {master_dir}; build the master first")

    for md in mds:
        kind = kind_of(md)
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
