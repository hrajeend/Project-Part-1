# AGENTS.md — INTEG 275 Technical Setup Exercise

## Audience note 
These instructions are written for GitHub Copilot
(or any AI coding assistant) working in this repository. They tell
you how to behave when helping a student — what to check, what to
ask permission for, and what NOT to do for the student, so that the
learning exercise stays intact. Where a rule describes a goal for the
student (e.g., "the student should be able to explain their code"),
your job is to act in ways that support that goal (e.g., explain your suggestion in
steps rather than pasting a finished block).

## Context
This is a student exercise for an introductory AI-for-Science course
(INTEG 275, University of Waterloo). Most students are new to Python,
VS Code, and GitHub Copilot; some have only used Jupyter Notebooks, MATLAB, 
or other platforms and coding languages. Prioritize clear, readable, 
well-commented code over compact or clever code. When suggesting code, 
briefly explain what it does in plain language, not just what the syntax means.

## Confirm the project folder
- Before running project commands, confirm that the terminal is open at the
  repository root—the folder containing README.md, requirements.txt, and src/.
- If a command reports that a file cannot be found, check the current folder
  before changing the code.

## Environment
- Python 3.14+, managed in a local virtual environment (.venv).
- After creating the virtual environment, activate it before running
  project Python commands or installing packages. Confirm that the terminal
  prompt begins with `(.venv)`.
- Use the project's .venv environment for all work.
- In VS Code, select the interpreter located inside the project's .venv folder.
- If asked to help with Git, do not stage or commit the .venv/ directory, secrets, or machine-specific files.
- The `.venv/` directory should remain local and should not be uploaded.
- When running or suggesting install commands, use python -m pip, not a bare pip command.
- Approved libraries for this exercise: pandas, matplotlib,
  scikit-learn (listed in requirements.txt).
- Do not introduce deep learning frameworks (PyTorch, TensorFlow,
  Keras) or other new dependencies for this exercise. If a task
  later on genuinely seems to need something outside this list, say
  so and explain why, rather than installing it silently.
- Prefer `pathlib.Path` for file paths instead of hard-coded absolute paths.
- Do not assume that the project is located in a particular user's home
  directory.
- Run project commands from the repository root unless the README explicitly
  says otherwise.

## File-edit permission
- Ask for permission before applying edits to project files.
  Users may create expected outputs by following the assignment instructions. 
- Before asking for permission, describe the proposed change, identify the
  file or files affected, and explain where in each file the change would be
  made. Do not make the change until the user explicitly approves it.
- Reading files, analyzing problems, suggesting changes, and displaying
  proposed patches are allowed without permission; applying those changes
  is not.
- Before making substantial changes, ask the user to save or commit their
  current work if it has not already been saved.

## Explain errors before fixing them
- When a script raises an error (debugging), reproduce the error and read
  the complete traceback. Explain the file, line number, exception type, and
  likely cause in plain language to the user before proposing a fix.
- Make one focused change at a time, then run the script again.
- Do not hide errors with broad try/except blocks or by deleting failing code.

## Preserve the learning exercise
- Explain concepts, interpret error messages, and suggest
  small examples.
- When explaining Python code, define unfamiliar terms such as variable,
  function, argument, method, module, exception, and DataFrame in context.
- Prefer one small working example over a large abstract explanation.
- Clearly distinguish Python syntax errors, runtime errors, and incorrect
  results.
- Do not complete the entire exercise in one step, even if asked. Offer one TODO at a time and prompt the student to try before you supply a full solution.
- Keep the numbered TODOs in the exercise unless the user explicitly asks
  to remove or reorganize them.

## Workflow rules
- Before adding any new package, explain why it's needed and
  whether an already-approved library (pandas, matplotlib,
  scikit-learn) could do the job instead.
- If a new package is genuinely needed and the student agrees to
  it: add it to requirements.txt, and add one line under "Tools
  used" below with a short reason.
- Keep functions short. Add a one-line comment above any block of
  code that isn't self-explanatory.
- After changing a script, run it from the repository root using the command
  shown in README.md.
- Save generated figures to the outputs/ folder as PNG files with
  descriptive filenames (e.g., outputs/pca_scatter.png).

- Do not fabricate or invent data values. If a data file is missing
  or a path looks wrong, say so rather than generating placeholder
  numbers to make the script run.


## Tools used
(Log new packages here as they're added during the project, with a
one-line reason. Do not remove earlier entries — this is a running
record of what the project ended up using and why.)
