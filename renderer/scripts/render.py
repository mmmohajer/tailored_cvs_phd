"""Render a resume or cover letter from Markdown to HTML and PDF.

Usage:
    python renderer/scripts/render.py master/master_resume.md
    python renderer/scripts/render.py custom_resumes/acme/resume.md --style minimal
    python renderer/scripts/render.py custom_resumes/acme            # every .md resume/cover letter in the folder

Writes <name>.html and <name>.pdf next to each Markdown file.
"""

from __future__ import annotations

import argparse
import html
import os
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
TEMPLATES = ROOT / "renderer" / "templates"
STYLES = ROOT / "renderer" / "styles"

RENDERABLE = ("resume", "cover_letter", "master_resume")
DATE_HINT = re.compile(r"(\d{4}|present|current|expected)", re.IGNORECASE)


def detect_kind(md_path: Path) -> str:
    return "cover_letter" if "cover" in md_path.stem.lower() else "resume"


def split_header(text: str) -> tuple[list[str], str]:
    """Return (header lines, rest). Header = '# Name' plus the lines before the first blank line."""
    text = re.sub(r"<!--.*?-->", "", text, flags=re.DOTALL).strip("\n")
    lines = text.splitlines()
    if not lines or not lines[0].startswith("# "):
        raise ValueError("First line must be '# Full Name'.")
    header = []
    i = 0
    while i < len(lines) and lines[i].strip():
        header.append(lines[i].strip())
        i += 1
    return header, "\n".join(lines[i:]).strip("\n")


def inline_md(text: str) -> str:
    import markdown

    out = markdown.markdown(text, extensions=["extra"])
    return re.sub(r"^<p>(.*)</p>$", r"\1", out.strip(), flags=re.DOTALL)


def render_header(lines: list[str]) -> str:
    name = html.escape(lines[0][2:].strip())
    parts = [f"<h1>{name}</h1>"]
    if len(lines) > 1:
        parts.append(f'<p class="headline">{inline_md(lines[1])}</p>')
    if len(lines) > 2:
        contact = " | ".join(inline_md(c.strip()) for c in " | ".join(lines[2:]).split("|") if c.strip())
        parts.append(f'<p class="contact">{contact}</p>')
    return '<header class="doc-header">\n' + "\n".join(parts) + "\n</header>"


def render_entry(match: re.Match) -> str:
    raw = match.group(1)
    if "|" not in raw:
        return match.group(0)
    cells = [c.strip() for c in raw.split("|") if c.strip()]
    title, rest = cells[0], cells[1:]
    date = ""
    if rest and DATE_HINT.search(re.sub(r"<[^>]+>", "", rest[-1])):
        date = rest.pop()
    meta = " · ".join(rest)
    out = f'<h3 class="entry"><span><span class="entry-title">{title}</span>'
    if meta:
        out += f'<span class="entry-meta"> · {meta}</span>'
    out += "</span>"
    if date:
        out += f'<span class="entry-date">{date}</span>'
    return out + "</h3>"


def slug(text: str) -> str:
    return re.sub(r"[^a-z0-9]+", "-", re.sub(r"<[^>]+>", "", text).lower()).strip("-")


def wrap_sections(body_html: str) -> str:
    chunks = re.split(r"(?=<h2>)", body_html)
    out = []
    for chunk in chunks:
        m = re.match(r"<h2>(.*?)</h2>", chunk)
        if m:
            out.append(f'<section class="{slug(m.group(1))}">\n{chunk.strip()}\n</section>')
        elif chunk.strip():
            out.append(chunk.strip())
    return "\n".join(out)


def markdown_to_html(text: str, kind: str) -> tuple[str, str, str]:
    """Return (title, header_html, body_html)."""
    import markdown

    header_lines, rest = split_header(text)
    extensions = ["extra", "sane_lists"]
    if kind == "cover_letter":
        extensions.append("nl2br")
    body = markdown.markdown(rest, extensions=extensions)
    body = re.sub(r"<h3>(.*?)</h3>", render_entry, body)
    body = wrap_sections(body)
    title = header_lines[0][2:].strip()
    return title, render_header(header_lines), body


def build_html(md_path: Path, style: str) -> Path:
    kind = detect_kind(md_path)
    title, header_html, body_html = markdown_to_html(md_path.read_text(encoding="utf-8"), kind)
    css = STYLES / f"{style}.css"
    if not css.exists():
        raise SystemExit(f"Unknown style '{style}'. Available: {', '.join(p.stem for p in STYLES.glob('*.css'))}")
    doc_title = f"{title} | {'Cover Letter' if kind == 'cover_letter' else 'Resume'}"
    template = (TEMPLATES / "document.html").read_text(encoding="utf-8")
    page = (
        template.replace("{{title}}", html.escape(doc_title))
        .replace("{{stylesheet}}", os.path.relpath(css, md_path.parent))
        .replace("{{kind}}", kind)
        .replace("{{header}}", header_html)
        .replace("{{body}}", body_html)
    )
    out = md_path.with_suffix(".html")
    out.write_text(page, encoding="utf-8")
    return out


def build_pdf(html_path: Path) -> Path:
    from weasyprint import HTML

    out = html_path.with_suffix(".pdf")
    HTML(filename=str(html_path)).write_pdf(str(out))
    return out


def targets(path: Path) -> list[Path]:
    if path.is_file():
        return [path]
    found = sorted(p for p in path.glob("*.md") if any(k in p.stem for k in RENDERABLE))
    if not found:
        raise SystemExit(f"No resume/cover letter Markdown files in {path}")
    return found


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("path", type=Path, help="A .md file or a folder containing resume.md / cover_letter.md")
    parser.add_argument("--style", default="classic", help="Stylesheet name in renderer/styles (default: classic)")
    parser.add_argument("--html-only", action="store_true", help="Skip PDF output")
    args = parser.parse_args(argv)

    for md in targets(args.path.resolve()):
        html_path = build_html(md, args.style)
        print(f"html  {html_path.relative_to(ROOT) if html_path.is_relative_to(ROOT) else html_path}")
        if not args.html_only:
            pdf = build_pdf(html_path)
            print(f"pdf   {pdf.relative_to(ROOT) if pdf.is_relative_to(ROOT) else pdf}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
