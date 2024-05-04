
from dotenv import load_dotenv
from wasabi import msg
from datetime import datetime
import os,json
import openai

load_dotenv()


DEFAULT_CONFIG = {
    "language": "ITALIANO",
    "vault_directory": ""
}



def save_config(config):
    with open("config.json", "w") as f:
        json.dump(config, f)

    
def load_config():
    if not os.path.exists("config.json"):
        save_config(DEFAULT_CONFIG)
    with open("config.json", "r") as f:
        return json.load(f)


config = load_config()

LANGUAGE = config["language"]
VAULT_DIRECTORY = config["vault_directory"]
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")



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
    global LANGUAGE
    prompt = f"""
    Ecco gli appunti presi durante lo sviluppo software:
    {obsidian_text}
    Genera documentazione e git commit dai seguenti in LINGUAGGIO {LANGUAGE.upper()}:
    """
    messages = [
        {"role": "system", "content": sys_prompt},
        {"role": "user", "content": prompt}
    ]
    return get_completion_from_messages(messages, model, temperature)



def check_env():
    if OPENAI_API_KEY is None:
        msg.fail("OPENAI_API_KEY not found. Make sure to set it in the file .env")
        return False
    else:
        msg.good("OPENAI_API_KEY env set.")
    return True

TITLE = """
                _        _____                 
     /\        | |      |  __ \                
    /  \  _   _| |_ ___ | |  | | ___   ___ ___ 
   / /\ \| | | | __/ _ \| |  | |/ _ \ / __/ __|
  / ____ \ |_| | || (_) | |__| | (_) | (__\__ \\
 /_/    \_\__,_|\__\___/|_____/ \___/ \___|___/
                                               
                                               
"""

print(TITLE)
msg.info(f"Output Language set to {LANGUAGE.upper()}")
# check if exists directory VAULT_DIRECTORY/.obsidian

if os.path.exists(VAULT_DIRECTORY):
    msg.good(f"Directory '{VAULT_DIRECTORY}' found, please edit the config.json file")
else:
    msg.fail(f"Directory '{VAULT_DIRECTORY}' not found")
    input("Press Enter to exit...")
    exit()

if not check_env():
    input("Press Enter to exit...")
    exit()

openai.api_key = OPENAI_API_KEY

# leggi generation_prompt.txt
if not os.path.exists("generation_prompt.txt"):
    msg.fail("File generation_prompt.txt not found.")
    input("Press Enter to exit...")
    exit()
with open("generation_prompt.txt", "r") as f:
    generation_prompt = f.read()

msg.good(f"Prompt set.")

while True:
    print("Insert the name of the obsidian note that you want to process:")
    obsidian_file = input()
    try:
        with open(f"{VAULT_DIRECTORY}/{obsidian_file}.md", "r",encoding="utf-8") as f:
            text = f.read()
        msg.good("Note found!")
        msg.info("Generating documentation and git commit...")
    except:
        msg.fail(f"File '{obsidian_file}' not found :( try again.")
        continue
    try:
        output = generate_documentation(text, generation_prompt)
        filename = datetime.now().strftime("%Y-%m-%d-%H-%M-%S")
        # log in outputs/
        if not os.path.exists("outputs"):
            os.makedirs("outputs")
        output_filename = f"outputs/{filename}.md"
        with open(output_filename, "w",encoding="utf-8") as f:
            f.write(output)
        
        current_dir = os.getcwd()
        msg.good(f"Docs generated! Output Path: {current_dir}/{output_filename}")
        

        
    except Exception as e:
        msg.fail(f"Unexpected Error: {e}, please report it to the developer.")