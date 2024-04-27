import obsidiantools.api as otools
from dotenv import load_dotenv
from wasabi import msg
from datetime import datetime
import os
import openai

load_dotenv()

GPT3_MODEL = "gpt-3.5-turbo"
GPT4_MODEL = "gpt-4-1106-preview"

def get_completion_from_messages(messages, model=GPT4_MODEL, temperature=0.15):
    response = openai.ChatCompletion.create(
        model=model,
        messages=messages,
        temperature=temperature, # this is the degree of randomness of the model's output
    )
    return response.choices[0].message["content"]

def generate_documentation(obsidian_text, sys_prompt, model=GPT4_MODEL, temperature=0.15):
    prompt = f"""
    Genera documentazione e git commit dai seguenti appunti presi durante lo sviluppo software:
    {obsidian_text}
    """
    messages = [
        {"role": "system", "content": sys_prompt},
        {"role": "user", "content": prompt}
    ]
    return get_completion_from_messages(messages, model, temperature)

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
VAULT_DIRECTORY = os.getenv("VAULT_DIRECTORY")

def check_env():
    if OPENAI_API_KEY is None:
        msg.fail("OPENAI_API_KEY non è stato trovato. Assicurati di averlo settato nel file .env")
        return False
    else:
        msg.good("OPENAI_API_KEY env set.")
    if VAULT_DIRECTORY is None:
        msg.fail("VAULT_DIRECTORY non è stato trovato. Assicurati di averlo settato nel file .env")
        return False
    else:
        msg.good("VAULT_DIRECTORY env set.")
    return True

title = """
                _        _____                 
     /\        | |      |  __ \                
    /  \  _   _| |_ ___ | |  | | ___   ___ ___ 
   / /\ \| | | | __/ _ \| |  | |/ _ \ / __/ __|
  / ____ \ |_| | || (_) | |__| | (_) | (__\__ \\
 /_/    \_\__,_|\__\___/|_____/ \___/ \___|___/
                                               
                                               
"""
vault = otools.Vault(VAULT_DIRECTORY).connect().gather()
print(title)

# check if exists directory .obsidian VAULT_DIRECTORY/.obsidian

if not os.path.exists(f"{VAULT_DIRECTORY}/.obsidian"):
    msg.fail(f"Vault non trovato in {VAULT_DIRECTORY}. Assicurati di aver settato il percorso corretto nel file .env")
    exit()
else:
    msg.good(f"Vault obsidian set.")

if not check_env():
    exit()

openai.api_key = OPENAI_API_KEY

# leggi generation_prompt.txt
if not os.path.exists("generation_prompt.txt"):
    msg.fail("Il file generation_prompt.txt non è stato trovato. Assicurati di averlo creato.")
    exit()
with open("generation_prompt.txt", "r") as f:
    generation_prompt = f.read()

msg.good(f"Prompt set.")

while True:
    print("Inserisci il nome dell'obsidian file:")
    obsidian_file = input()
    try:
        src_txt = vault.get_source_text(obsidian_file)
        text = vault.get_readable_text(obsidian_file)
        msg.good("File trovato.")
        msg.info("Generazione della documentazione in corso...")

        output = generate_documentation(text, generation_prompt)
        filename = datetime.now().strftime("%Y-%m-%d-%H-%M-%S")
        # log in outputs/
        if not os.path.exists("outputs"):
            os.makedirs("outputs")
        output_filename = f"outputs/{filename}.md"
        with open(output_filename, "w",encoding="utf-8") as f:
            f.write(output)
        
        current_dir = os.getcwd()
        msg.good(f"Documentazione generata in {current_dir}/{output_filename}")
        

        
    except Exception as e:
        msg.fail(f"Il file '{obsidian_file}' non esiste nel vault. Riprova.")