"""Create the paired input/output folders for one PhD application.

Usage:
    python renderer/scripts/new_application.py "University of Toronto"
    python renderer/scripts/new_application.py "University of Toronto" "Computer Science"

Creates positions/<slug>/ (drop the position page and prompts here) and
custom_resumes/<slug>/ (custom CV, cover letter, professor email, and follow-up plan land here).
Slug: university, or university_program when a program is given.
"""

from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]


def slugify(text: str) -> str:
    return re.sub(r"[^a-z0-9]+", "-", text.lower()).strip("-")


def application_slug(company: str, role: str | None = None) -> str:
    return slugify(company) + (f"_{slugify(role)}" if role else "")


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("institution", help="University or department name")
    parser.add_argument("program", nargs="?", help="Program or field, optional")
    args = parser.parse_args(argv)

    slug = application_slug(args.institution, args.program)
    for base in ("positions", "custom_resumes"):
        (ROOT / base / slug).mkdir(parents=True, exist_ok=True)
        print(f"{base}/{slug}/")
    print(f"\nNext: put the position page and prompts in positions/{slug}/ (txt, md, pdf, or docx).")
    return 0


if __name__ == "__main__":
    sys.exit(main())
