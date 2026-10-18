# Render

## Commands

```bash
# One file
python renderer/scripts/render.py master/master_resume.md

# Every resume / cover letter Markdown in a folder
python renderer/scripts/render.py custom_resumes/<slug>

# Other style, or HTML only for a quick look
python renderer/scripts/render.py custom_resumes/<slug> --style minimal
python renderer/scripts/render.py custom_resumes/<slug> --html-only
```

Each `name.md` produces `name.html` and `name.pdf` beside it.

## Markdown contract

`render.py` relies on the format in `renderer/templates/resume.md` and `cover_letter.md`:

- Line 1 `# Full Name`, line 2 headline, line 3 contact items separated by ` | `. A blank line ends the header.
- `## Heading` starts a section.
- `### Title | Org | Location | Dates` becomes one entry line. The last cell is right-aligned when it looks like a date (has a year, "Present," or "Expected").
- Cover letters keep single line breaks (address block, sign-off).
- No tables, images, columns, or raw HTML layout.

## Styles

`renderer/styles/classic.css` (navy accent) and `minimal.css` (black). Letter size, Roboto. To add a style, create `renderer/styles/<name>.css` that `@import "classic.css";` and overrides the CSS variables.

The page footer shows the name and page numbers automatically.

## After rendering

Run `check.py` (`05_review.md`). Open the PDF and look at page breaks.
