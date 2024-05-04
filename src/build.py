import os

# runs the following command with os, produces the executable in dist folder

name = "Autodocs"

os.system(f"pyinstaller autodocs.py --onefile --icon=wordart.ico --name={name} -y")

os.system(f"copy generation_prompt.txt dist\{name}")

os.system(f"copy config.json dist\{name}")

