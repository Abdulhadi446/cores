import utils
from utils import dbg, createTemp
import subprocess
import ast
import tempfile
import os
import platform

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

def run_block(code: str):
    new_lines = []
    code = code.replace("PUB_VAR", str(utils.PUB_VAR))

    for line in code.splitlines():
        if line.startswith("pub_var"):
            # Update PUB_VAR
            dbg("Asining PUB-VAR: ", str(line))
            try:
                key, value = line.split("=", 1)
                utils.PUB_VAR = ast.literal_eval(value.strip())
            except Exception:
                utils.PUB_VAR = eval(value.strip())
            dbg(f"[PUB-VAR]: {utils.PUB_VAR}")
            continue  # skip this line (remove it)
        new_lines.append(line)

    # Join remaining lines
    code = "\n".join(new_lines)

    # Determine runtime
    lines = utils.DATA.splitlines()
    second_line = lines[1].strip() if len(lines) > 1 else ''
    dbg("Language:", second_line)
    if ',' in  second_line:
        langs = second_line.split(',')
        path = createTemp(f"{langs[1]}-tempfile.{langs[0]}", code)
        binary = langs[1]
        cmd = [f'{binary}',f'{path}']
        dbg("Running", cmd)
        subprocess.run(cmd)
        
    elif second_line in ('c', 'cpp'):
        run_cpp_code_fully(code, second_line)
    else:
        cmd = utils.RUNTIMES.get(second_line) + [code]
        dbg("Running", cmd)
        subprocess.run(cmd)