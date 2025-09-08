# utils.py
import os
import tempfile


EXEC_CONTEXT = {}
DATA = ''
DATA_ARRAY = ()
WAIT = False
END_CODE = "\n"
DEBUG = True
CODE_FILES = []

# PUBLIC variables
PUB_VAR = None
PUB_BOOL = False
PUB_INT = 0
PUB_STR = ''
PUB_FLOAT = 0.0
PUB_ARRAY = []
PUB_JSON = '{}'

import builtins

def safe_print(*args, **kwargs):
    """Print safely even during interpreter shutdown (ignore stdout errors)."""
    try:
        builtins.print(*args, **kwargs)
    except Exception:
        pass

def dbg(*args, **kwargs):
    if DEBUG:
        safe_print(*args, **kwargs)  # forwards everything to print

def createTemp(name: str, content: str) -> str:
    # Create a temporary directory
    tmpdir = tempfile.mkdtemp()
    filepath = os.path.join(tmpdir, name)
    
    # Write content to the file
    with open(filepath, "w", encoding="utf-8") as f:
        f.write(content)
    
    return filepath

RUNTIMES = {
    "py": ["python", "-c"],             # Python
    "js": ["node", "-e"],               # JavaScript (Node.js)
    "rb": ["ruby", "-e"],               # Ruby
    "pl": ["perl", "-e"],               # Perl
    "php": ["php", "-r"],               # PHP
    "r": ["R", "-e"],                   # R
    "lua": ["lua", "-e"],               # Lua
    
    # Shells
    "bash": ["bash", "-c"],             # Bash
    "sh": ["sh", "-c"],                 # POSIX sh
    "cmd": ["cmd", "/C"],               # Windows Command Prompt
    "ps": ["powershell", "-Command"],   # Windows PowerShell
}