import os
import tempfile

PUB_VAR = 0
DATA = ''
DATA_ARRAY = ()
WAIT = False
END_CODE = "\n"
DEBUG = False

def dbg(*args, **kwargs):
    if DEBUG:
        print(*args, **kwargs)  # forwards everything to print

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