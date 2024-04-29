# AutoDocs
 Automatic tool for work documentation and reporting with [Obsidian Notebook](https://obsidian.md/). This tool can process your daily software work notes on obsidian and generate a quick latex report and git commit summary. In order to start you have to simply:
- Configure env vars (OpenAI api key, Obsidian vault path and output language)
- Run Autodocs
- Write a note on obsidian and name it for example "My programming note"
- Autodocs will ask for the **note name**. Insert "My programming note" and then wait for the generation
- After generation, checkout the generated documentation in the **output directory**.
## Quick start
```
python -venv env
```
- activate env linux
```
source env/bin/activate
```
- activate env windows
```
.\env\Scripts\activate
```
```
pip install -e .
```
```
cd src
```
```
python autodocs.py
```
## .env
```
VAULT_DIRECTORY=C:\path-to-your-obsidian-vault
OPENAI_API_KEY=your-apikey
LANGUAGE=english
```
- **VAULT_DIRECTORY**: path of your obsidian vault
- **OPENAI_API_KEY**: your valid openai api key for generating documentation
- **LANGUAGE**: output documentation language. It can be for example: italian, english, spanish...

#### build exe
- install requirements.txt
```
pip install -r requirements.txt
```
```
cd src
```
```
python build.py
```
- checkout dist folder
- if there are any problems try to copy manually .env file into dist/Autodocs folder.