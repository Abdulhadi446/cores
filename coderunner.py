from glm import e
import utils
from utils import dbg, createTemp
import subprocess
import ast
import tempfile
import os
import platform

# print

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
        
        utils.CODE_FILES.append(src_file)
        utils.CODE_FILES.append(exe_file)
        
        # Write code to file
        with open(src_file, "w") as f:
            f.write(cpp_code)
        
        # Compile
        compile_process = subprocess.run([compiler, src_file, "-o", exe_file])
        if compile_process.returncode != 0:
            dbg("[Compilation failed.]")
            return
        
        # Run executable with console I/O
        run_cmd = [exe_file] if platform.system() != "Windows" else [exe_file]
        try:
            subprocess.run(run_cmd, check=True)
        except subprocess.CalledProcessError:
            dbg("[Execution failed.]")


import processcode

def run_block(code: str):
    code = processcode.process_code(code)

    # Determine runtime
    lines = utils.DATA.splitlines()
    second_line = lines[1].strip() if len(lines) > 1 else ''
    dbg("[Language]", second_line)
    if ',' in  second_line:
        langs = second_line.split(',')
        path = createTemp(f"{langs[1]}-tempfile.{langs[0]}", code)
        utils.CODE_FILES.append(path)
        binary = langs[1]
        cmd = [f'{binary}',f'{path}']
        dbg("[Running]", cmd)
        subprocess.run(cmd)
        
    elif second_line in ('c', 'cpp'):
        run_cpp_code_fully(code, second_line)
    else:
        cmd = utils.RUNTIMES.get(second_line) + [code]
        dbg("[Running]", cmd)
        subprocess.run(cmd)