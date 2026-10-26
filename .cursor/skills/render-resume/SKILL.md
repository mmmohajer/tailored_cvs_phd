---
name: render-resume
description: >-
  Render academic CV and statement Markdown to HTML and PDF and run the
  mechanical checks. Use when the user says render, export PDF, make the PDF,
  or change style.
---

# Render

Read `rules/06_render.md`.

1. `python renderer/scripts/render.py <file-or-folder> [--style classic|minimal]`
2. `python renderer/scripts/check.py <folder> --max-pages <limit>` (`--max-pages 0` for `master`).
3. On a WeasyPrint import error, point the person to the setup section in `README.md` (`brew install pango` on macOS).

Report PDF paths and the check result. Don't edit content unless asked.
