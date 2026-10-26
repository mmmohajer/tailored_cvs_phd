# positions/

One folder per PhD position you might apply to. Gitignored except this README.

A position is any specific place you would send an application. That can be:

- an advertised vacancy or funded studentship
- a doctoral program you apply to as a cohort
- a supervisor and research group you are asking to host you

Your own history stays in `profile/` and `master/`. This folder holds only the other side: what they asked for.

## What goes in `positions/<slug>/`

Save the whole call, not a summary. Any of `.txt`, `.md`, `.pdf`, or `.docx`.

- The admissions page or the vacancy text
- Faculty or lab pages for the people you would name
- Essay prompts, word limits, and required documents
- Deadline, funding rules, and test policy
- A note if a supervisor must agree before you can apply

Create the folder (and the matching output folder) with:

```bash
python renderer/scripts/new_application.py "University of Toronto" "Computer Science"
# → positions/university-of-toronto_computer-science/
# → custom_resumes/university-of-toronto_computer-science/
```

The same slug is used in `custom_resumes/`, which later holds the custom CV, cover letter, professor email, and follow-up plan. Do not draft those files in here.

Nothing is added until you choose a real position. One university can have several folders if the projects differ.
