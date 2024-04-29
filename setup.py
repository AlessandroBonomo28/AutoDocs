import os
import shutil
import sys
from cx_Freeze import setup, Executable
from setuptools import find_packages

__version__ = '1.0.0'
base = None
if sys.platform == 'win32':
    base = 'Win32GUI'

include_files = ['src/generation_prompt.txt', '.env']
includes = ['src']
excludes = []


packages = find_packages(include=include_files)
install_packages = [
    "aiohttp==3.9.5",
    "aiosignal==1.3.1",
    "altgraph==0.17.4",
    "attrs==23.2.0",
    "beautifulsoup4==4.12.3",
    "bleach==6.1.0",
    "certifi==2024.2.2",
    "charset-normalizer==3.3.2",
    "colorama==0.4.6",
    "frozenlist==1.4.1",
    "html2text==2024.2.26",
    "idna==3.7",
    "lxml==5.2.1",
    "Markdown==3.6",
    "multidict==6.0.5",
    "networkx==3.3",
    "numpy==1.26.4",
    "obsidiantools==0.10.0",
    "openai==0.27.9",
    "packaging==24.0",
    "pandas==2.2.2",
    "pefile==2023.2.7",
    "pyinstaller-hooks-contrib==2024.5",
    "pymdown-extensions==10.8",
    "python-dateutil==2.9.0.post0",
    "python-dotenv==1.0.1",
    "python-frontmatter==1.1.0",
    "pytz==2024.1",
    "pywin32-ctypes==0.2.2",
    "PyYAML==6.0.1",
    "requests==2.31.0",
    "six==1.16.0",
    "soupsieve==2.5",
    "tqdm==4.66.2",
    "tzdata==2024.1",
    "urllib3==2.2.1",
    "wasabi==1.1.2",
    "webencodings==0.5.1",
    "yarl==1.9.4",
]

setup(
    name='Autodocs',
    description='Autodocs',
    version=__version__,
    executables=[Executable('src/autodocs.py', base=base)],
    options = {'build_exe': {
        'packages': packages,
        'includes': includes,
        'include_files': include_files,
        'include_msvcr': True,
        'excludes': excludes,
    }},
    install_requires=install_packages
)