# AutoDocs
 Automatic tool for work documentation and reporting
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