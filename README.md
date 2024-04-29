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
python obsidian_autodoc.py
```
## .env
```
VAULT_DIRECTORY=C:\path-to-your-obsidian-vault
OPENAI_API_KEY=your-apikey
```

