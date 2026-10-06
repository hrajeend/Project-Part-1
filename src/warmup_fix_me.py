"""
Warm-up exercise: fix the bug!

Before starting the main PCA task, run this script exactly as it is.
It will fail with an error message. Your job is to:

  1. Read the error message in the terminal carefully (start from the
     bottom line, it usually tells you the actual problem).
  2. Ask GitHub Copilot Chat to explain what the error means and how
     to fix it (select the error text or paste it into the chat).
  3. Make the fix yourself in this file.
  4. Run the script again to confirm it works.

This script is meant to break on purpose. That is normal, and it is
exactly the kind of error you will run into constantly once you start
writing your own code, so it is worth getting comfortable with it now.

How to run this script:
  Open a terminal in VS Code (Terminal > New Terminal), make sure your
  virtual environment is active and your directory end with 
  "INTEG275_PCA_Starter_Repo>", then run:

      python src/warmup_fix_me.py

Or click on the "Run Python File" button in VS Code (triangle at the top right).
"""

penguins = pd.read_csv("data/penguins.csv", na_values="NA")

print("Loaded", len(penguins), "penguin records.")
print("Species found:", penguins["species"].unique())
print("Average body mass (g):", penguins["body_mass_g"].mean())
