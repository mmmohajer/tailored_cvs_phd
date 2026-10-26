"""Turn every input file in a folder into plain text the agent can read.

Usage:
    python renderer/scripts/extract.py profile
    python renderer/scripts/extract.py positions/university_program

Supports .pdf, .docx, .txt, .md, .html/.htm, and (on macOS, via textutil) .doc/.rtf/.pages.
Writes <folder>/_extracted/<file>.txt plus <folder>/_extracted/_index.md.
Scanned PDFs (images, no text layer) are reported so the user can supply a text version.
"""

from __future__ import annotations

import argparse
import html
import re
import shutil
import subprocess
import sys
from pathlib import Path

SKIP_NAMES = {"README.md", ".gitkeep", ".DS_Store"}
TEXTUTIL_TYPES = {".doc", ".rtf", ".pages", ".odt"}
MIN_CHARS = 40


def read_pdf(path: Path) -> str:
    from pypdf import PdfReader

    reader = PdfReader(str(path))
    return "\n\n".join((page.extract_text() or "") for page in reader.pages)


def read_docx(path: Path) -> str:
    import docx

    document = docx.Document(str(path))
    parts = [p.text for p in document.paragraphs]
    for table in document.tables:
        for row in table.rows:
            parts.append(" | ".join(cell.text.strip() for cell in row.cells))
    return "\n".join(parts)


def read_html(path: Path) -> str:
    raw = path.read_text(encoding="utf-8", errors="replace")
    raw = re.sub(r"<(script|style)[^>]*>.*?</\1>", "", raw, flags=re.DOTALL | re.IGNORECASE)
    raw = re.sub(r"<br\s*/?>|</(p|div|li|h\d|tr)>", "\n", raw, flags=re.IGNORECASE)
    return html.unescape(re.sub(r"<[^>]+>", "", raw))


def read_textutil(path: Path) -> str:
    if not shutil.which("textutil"):
        raise RuntimeError("textutil not available; save the file as .docx or .pdf")
    result = subprocess.run(
        ["textutil", "-convert", "txt", "-stdout", str(path)], capture_output=True, text=True, check=True
    )
    return result.stdout


def extract(path: Path) -> str:
    suffix = path.suffix.lower()
    if suffix == ".pdf":
        return read_pdf(path)
    if suffix == ".docx":
        return read_docx(path)
    if suffix in {".html", ".htm"}:
        return read_html(path)
    if suffix in TEXTUTIL_TYPES:
        return read_textutil(path)
    return path.read_text(encoding="utf-8", errors="replace")


def clean(text: str) -> str:
    text = text.replace("\r\n", "\n").replace("\u00a0", " ")
    text = re.sub(r"[ \t]+\n", "\n", text)
    return re.sub(r"\n{3,}", "\n\n", text).strip() + "\n"


def input_files(folder: Path) -> list[Path]:
    return sorted(
        p
        for p in folder.rglob("*")
        if p.is_file()
        and "_extracted" not in p.parts
        and p.name not in SKIP_NAMES
        and not p.name.startswith(".")
    )


def run(folder: Path) -> list[tuple[str, str, int]]:
    out_dir = folder / "_extracted"
    out_dir.mkdir(exist_ok=True)
    rows: list[tuple[str, str, int]] = []
    for src in input_files(folder):
        rel = src.relative_to(folder)
        target = out_dir / (str(rel).replace("/", "__") + ".txt")
        try:
            text = clean(extract(src))
        except Exception as exc:  # noqa: BLE001 - report every failure, keep going
            rows.append((str(rel), f"FAILED: {exc}", 0))
            continue
        target.write_text(text, encoding="utf-8")
        status = "ok" if len(text.strip()) >= MIN_CHARS else "EMPTY: likely a scanned image, needs a text version"
        rows.append((str(rel), status, len(text)))

    lines = ["# Extracted inputs", "", "| Source | Status | Characters |", "|---|---|---|"]
    lines += [f"| {name} | {status} | {chars} |" for name, status, chars in rows]
    (out_dir / "_index.md").write_text("\n".join(lines) + "\n", encoding="utf-8")
    return rows


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("folder", type=Path)
    args = parser.parse_args(argv)
    folder = args.folder.resolve()
    if not folder.is_dir():
        raise SystemExit(f"Not a folder: {folder}")

    rows = run(folder)
    if not rows:
        print(f"No input files in {folder}")
        return 1
    for name, status, chars in rows:
        print(f"{status:<10.60} {chars:>7}  {name}")
    print(f"\nIndex: {folder / '_extracted' / '_index.md'}")
    return 0 if all(status == "ok" for _, status, _ in rows) else 2


if __name__ == "__main__":
    sys.exit(main())
