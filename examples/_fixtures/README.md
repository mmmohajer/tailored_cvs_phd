# Fixtures

`scanned_resume.pdf` is a fictional resume saved as a picture of text, the way a phone scan or a "print to image" export looks. It has no text layer, so `extract.py` reports it as `EMPTY`. Lesson 4.3 uses it to show that case and its fix: add a text version (paste the content into a `.txt` or `.md` file next to it).

It is not part of any example person's profile.

```bash
python renderer/scripts/extract.py examples/_fixtures
```
