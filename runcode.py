import re
import textwrap
from utils import dbg
import utils
from coderunner import run_block

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
# Main
# -----------------------------
def main(code):
    dbg(f"[Running] Do code")

    do_code = extract_do_block(code)
    do_output = run_block(do_code) if do_code else None
    if do_output:
        print(do_output)

    dbg(f"[Ends] Do code\n")

    # Extract END block
    utils.END_CODE = extract_end_block(code)

    # Extract TIMES block
    times_number, times_code = extract_times_block(code)
    return times_number, times_code
