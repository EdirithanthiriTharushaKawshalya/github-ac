import os
import datetime

# File to update (README.md or any dummy file)
FILE = "README.md"

# Add current time to README
with open(FILE, "a") as f:
    f.write(f"\nUpdated on {datetime.datetime.now()}\n")

# Git commands
os.system("git add .")
os.system(f'git commit -m "Auto commit: {datetime.datetime.now()}"')
os.system("git push origin main")
