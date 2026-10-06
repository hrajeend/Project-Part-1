# INTEG 275 — Technical Setup Exercise: Dimension Reduction

Welcome! This is a short warm-up exercise to get your VS Code,
Python, and GitHub Copilot environment working before the Final
Challenge. By the end, you will have written a small script that
loads a real dataset, reduces it to two dimensions with Principal
Component Analysis (PCA), and saves a plot, and you'll have pushed
that work to your own GitHub repository.

No prior coding experience is assumed. Take your time on the setup
steps below; they matter more than they might seem.

## What's in this repository

data/
  penguins.csv          the dataset (see "About the data" below)
src/
  warmup_fix_me.py       a tiny script with an intentional bug — fix
                          this first, as practice reading error messages
  pca_exercise.py         the main exercise, with TODOs for you to
                          fill in with Copilot's help
outputs/                 your generated plot goes here
docs/
  expected_output_example.png   roughly what a correct plot looks like
AGENTS.md                 instructions Copilot reads automatically
                          to help it match this course's expectations
requirements.txt          the Python packages this project needs


## Step 1: Install the tools

1. Install [VS Code](https://code.visualstudio.com/) if you don't
   already have it.
2. Install [Python](https://www.python.org/downloads/) (3.14 or
   newer). On Windows, check the box that says "Add python.exe to
   PATH" during installation.
3. Open VS Code, go to the Extensions panel (the icon that looks
   like four squares on the left sidebar, or Ctrl+Shift+X /
   Cmd+Shift+X), and install:
   - **Python** (by Microsoft)
   - **GitHub Copilot Chat** (by GitHub)
4. Sign in to GitHub Copilot with your GitHub account. If your
   Copilot access is through the GitHub Student Developer Pack,
   make sure that's activated first at
   https://education.github.com/pack (it can take a little while to
   process, so do this well before the deadline).

## Step 2: Get your own copy of this repository

Your instructor will share this repository as a **GitHub template**.

1. On the repository's GitHub page, click the green **"Use this
   template"** button, then **"Create a new repository"**. This
   creates your own private copy under your own GitHub account; it
   does not affect the original.
2. On your new repository's page, click the green **Code** button
   and copy the HTTPS URL.
3. In VS Code, open the Command Palette (Ctrl+Shift+P / Cmd+Shift+P),
   type "Git: Clone", paste the URL, and choose a folder on your
   computer to save it in.
4. Once it's cloned, open the folder in VS Code (File > Open
   Folder...).

## Step 3: Set up your Python environment

Open the repository folder in VS Code, then open a terminal in VS Code
(Terminal > New Terminal). The terminal must be at the top level of the
repository — the folder that contains `requirements.txt`, `src`, and
`README.md` — before running the commands below. If you opened a larger
parent folder in VS Code, right-click `INTEG275_PCA_Starter_Repo` in the
Explorer and choose **Open in Integrated Terminal** instead.

On Windows, you can verify the location with:
```
Get-Location
Test-Path .\requirements.txt
```

The second command should print `True`. If it prints `False`, change to
the repository folder before continuing, or reopen that folder in VS Code.

Then run for **Windows (PowerShell)**:
```
python -m venv .venv
.venv\Scripts\Activate.ps1
python -m pip install -r requirements.txt
```

Or run for **macOS / Linux**:
```
python3 -m venv .venv
source .venv/bin/activate
python3 -m pip install -r requirements.txt
```

If VS Code asks whether to use this environment as your workspace's
Python interpreter, say yes. You'll know the virtual environment is
active if you see `(.venv)` at the start of your terminal prompt.

## Step 4: Warm up — fix the bug

Open `src/warmup_fix_me.py` and run it:
```
python src/warmup_fix_me.py
```

It will fail. Read the error message that appears in the terminal
(the last line usually tells you the actual problem), then ask
Copilot Chat to help you understand and fix it. Once it runs
successfully and prints some penguin statistics, move on to Step 5.

## Step 5: Complete the PCA exercise

Open `src/pca_exercise.py`. It contains ten numbered `TODO`
comments walking you through the task, each with a suggested
Copilot prompt to get you started. Work through them in order,
using Copilot's inline suggestions (just start typing) or Copilot
Chat (select a TODO block and ask Copilot to help) to write the
code for each step.

Run the script as you go to check your progress:
```
python src/pca_exercise.py
```

When it finishes without errors, check `outputs/` for
`pca_scatter.png`. Compare it loosely to
`docs/expected_output_example.png`. Your exact styling can differ;
what matters is that the three species are visible and at least
partially separated in the plot.

## Step 6: Commit and push your work

These commands save your completed work to your GitHub repository.
First, `git add .` prepares all changed files in this repository,
including your scripts and plot. The next two commands let you check
which files are prepared. Then `git commit` records a snapshot of
those files, and `git push` uploads the commit to GitHub.

In the VS Code terminal:
```
git add .

git status
git diff --cached --name-status

git commit -m "Complete PCA dimension reduction exercise"
git push
```

If this is your first time pushing from this machine, Git may ask
you to sign in to GitHub; follow the prompts.

## Step 7: Submit

Copy your repository's URL from GitHub and submit it as instructed
on Crowdmark. Please ensure that your repository is set to Public. 
You can change this setting under the Settings tab in GitHub.

## About the data

This exercise uses the Palmer Penguins dataset: body measurements
for 344 Adélie, Chinstrap, and Gentoo penguins from the Palmer
Archipelago, Antarctica.

- Data collected by Dr. Kristen Gorman and the Palmer Station
  Antarctica Long Term Ecological Research (LTER) Program.
- Gorman, K. B., Williams, T. D., & Fraser, W. R. (2014). Ecological
  Sexual Dimorphism and Environmental Variability within a
  Community of Antarctic Penguins (Genus Pygoscelis). PLOS ONE.
  https://doi.org/10.1371/journal.pone.0090081
- Packaged for teaching by Horst, A. M., Hill, A. P., & Gorman, K. B.
  (2020). palmerpenguins R package, CC0 licence.
  https://allisonhorst.github.io/palmerpenguins/

## Using Copilot well

Copilot works best when you describe what you want in plain
language, one step at a time, rather than asking it to write the
whole script at once. If a suggestion looks confusing, ask Copilot
Chat to explain it line by line before accepting it; you're
responsible for understanding code that ends up in your submission,
not just for getting it to run.

This repository includes an `AGENTS.md` file, which Copilot reads
automatically to understand the constraints of this exercise (for
example, sticking to the packages already listed in
`requirements.txt`). You don't need to do anything with it, but
feel free to open it if you're curious what Copilot "sees" before
you even ask it a question.
