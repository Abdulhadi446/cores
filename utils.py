import subprocess
import os
import tempfile
import platform

PUB_VAR = 0
DATA = ''
DATA_ARRAY = ()
WAIT = False
END_CODE = "\n"
DEBUG = True

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

def run_cpp_code_fully(cpp_code: str, language="cpp"):
    """
    Runs a C or C++ code string with full console interaction.
    language: "cpp" for C++, "c" for C
    """
    exe_ext = ".exe" if platform.system() == "Windows" else ""
    
    # Select file extension and compiler
    if language == "cpp":
        file_ext = ".cpp"
        compiler = "g++"
    elif language == "c":
        file_ext = ".c"
        compiler = "gcc"
    else:
        raise ValueError("language must be 'c' or 'cpp'")
    
    # Temporary directory
    with tempfile.TemporaryDirectory() as tmpdirname:
        src_file = os.path.join(tmpdirname, "temp" + file_ext)
        exe_file = os.path.join(tmpdirname, "temp" + exe_ext)
        
        # Write code to file
        with open(src_file, "w") as f:
            f.write(cpp_code)
        
        # Compile
        compile_process = subprocess.run([compiler, src_file, "-o", exe_file])
        if compile_process.returncode != 0:
            print("Compilation failed.")
            return
        
        # Run executable with console I/O
        run_cmd = [exe_file] if platform.system() != "Windows" else [exe_file]
        try:
            subprocess.run(run_cmd, check=True)
        except subprocess.CalledProcessError:
            print("Execution failed.")