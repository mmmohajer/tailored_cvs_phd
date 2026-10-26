# Render

## Commands

```bash
# Master CV
python renderer/scripts/render.py master/master_resume.md

# Tailored CV and the four documents in one folder
python renderer/scripts/render.py custom_resumes/<slug>

# Other style, or HTML only for a quick look
python renderer/scripts/render.py custom_resumes/<slug> --style minimal
python renderer/scripts/render.py custom_resumes/<slug> --html-only
```

Each `name.md` produces `name.html` and `name.pdf` beside it. `cv.md` and `master_resume.md` render as the CV. `cover_letter.md`, `professor_email.md`, and `follow_up.md` render as prose. `statement.md` is rendered only when that position asked for a statement of purpose.

## Markdown contract

`render.py` relies on the format in `renderer/templates/resume.md` and `cover_letter.md`:

- Line 1 `# Full Name`, line 2 headline, line 3 contact items separated by ` | `. A blank line ends the header.
- `## Heading` starts a section.
- `### Title | Org | Location | Dates` becomes one entry line. The last cell is right-aligned when it looks like a date (has a year, "Present," or "Expected").
- Statements keep single line breaks (address block, sign-off).
- No tables, images, columns, or raw HTML layout.

## Styles

`renderer/styles/classic.css` (navy accent) and `minimal.css` (black). Letter size, Roboto. To add a style, create `renderer/styles/<name>.css` that `@import "classic.css";` and overrides the CSS variables.

The page footer shows the name and page numbers automatically.

## After rendering

Run `check.py` (`05_review.md`). Open the PDF and look at page breaks. Cover letters target one page. The position's own length limit overrides the script's warning.
