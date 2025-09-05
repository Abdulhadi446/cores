import re
import textwrap
import subprocess
import ast
from utils import RUNTIMES, run_cpp_code_fully, PUB_VAR, DEBUG, DATA, END_CODE
import utils

# -----------------------------
# Regex patterns for extraction
# -----------------------------
DO_BLOCK_RE = re.compile(r'do:\s*\{([\s\S]*?)\}', re.MULTILINE)
END_BLOCK_RE = re.compile(r'end:\s*\{([\s\S]*?)\}', re.MULTILINE)
TIMES_BLOCK_RE = re.compile(r'times:\s*\((\d+)\)\s*\{([\s\S]*?)\}', re.MULTILINE)

# -----------------------------
# Extraction functions
# -----------------------------
def extract_do_block(text):
    match = DO_BLOCK_RE.search(text)
    return textwrap.dedent(match.group(1)).strip() if match else None

def extract_end_block(text):
    match = END_BLOCK_RE.search(text)
    return textwrap.dedent(match.group(1)).strip() if match else None

def extract_times_block(text):
    match = TIMES_BLOCK_RE.search(text)
    if not match:
        return None, None
    return int(match.group(1)), textwrap.dedent(match.group(2)).strip()

# -----------------------------
# Run block
# -----------------------------

def run_block(code: str):
    new_lines = []

    for line in code.splitlines():
        if line.startswith("pub_var"):
            # Update PUB_VAR
            try:
                key, value = line.split("=", 1)
                utils.PUB_VAR = ast.literal_eval(value.strip())
            except Exception:
                utils.PUB_VAR = eval(value.strip())
            if utils.DEBUG:
                print(f"[PUB-VAR]: {utils.PUB_VAR}")
            continue  # skip this line (remove it)
        new_lines.append(line)

    # Join remaining lines
    code = "\n".join(new_lines)

    # Replace PUB_VAR placeholders with current value
    code = code.replace("PUB_VAR", str(utils.PUB_VAR))
        

    # Determine runtime
    lines = utils.DATA.splitlines()
    second_line = lines[1].strip() if len(lines) > 1 else ''
    if utils.DEBUG:
        print("Language:", second_line)


    if second_line in ('c', 'cpp'):
        run_cpp_code_fully(code, second_line)
    else:
        subprocess.run(RUNTIMES.get(second_line, ['python', '-c']) + [code])

# -----------------------------
# Main
# -----------------------------
def main(code):
    if utils.DEBUG:
        print(f"[Running] Do code")

    do_code = extract_do_block(code)
    do_output = run_block(do_code) if do_code else None
    if do_output:
        print(do_output)

    if utils.DEBUG:
        print(f"[Ends] Do code\n")

    # Extract END block
    utils.END_CODE = extract_end_block(code)

    # Extract TIMES block
    times_number, times_code = extract_times_block(code)
    return times_number, times_code
