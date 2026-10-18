"""Create the paired input/output folders for one job application.

Usage:
    python renderer/scripts/new_application.py "Acme Corp"
    python renderer/scripts/new_application.py "Acme Corp" "Backend Engineer"

Creates jobs/<slug>/ (drop the job description here) and custom_resumes/<slug>/ (outputs land here).
Slug: company, or company_role when a role is given.
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
    parser.add_argument("company")
    parser.add_argument("role", nargs="?")
    args = parser.parse_args(argv)

    slug = application_slug(args.company, args.role)
    for base in ("jobs", "custom_resumes"):
        (ROOT / base / slug).mkdir(parents=True, exist_ok=True)
        print(f"{base}/{slug}/")
    print(f"\nNext: put the job description in jobs/{slug}/ (txt, md, pdf, or docx).")
    return 0


if __name__ == "__main__":
    sys.exit(main())
