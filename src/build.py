import os
from dotenv import load_dotenv

load_dotenv()
# runs the following command with os, produces the executable in dist folder

name = "Autodocs"

os.system(f"pyinstaller autodocs.py --icon=Clippit.ico --name={name} -y")

os.system(f"copy generation_prompt.txt dist\{name}")

# create a .env with all env variables

with open(f"dist/{name}/.env", "w") as f:
    pass

for env_var in ["OPENAI_API_KEY", "VAULT_DIRECTORY", "LANGUAGE"]:
    with open(f"dist/{name}/.env", "a") as f:
        f.write(f"{env_var}={os.getenv(env_var)}\n")