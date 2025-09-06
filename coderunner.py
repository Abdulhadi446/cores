import utils
from utils import dbg, createTemp, run_cpp_code_fully
import subprocess
import ast

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