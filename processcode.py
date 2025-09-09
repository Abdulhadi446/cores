import ast

import utils
from utils import dbg

def extract_pub_vars_from_module(data_array, rm_line=True):
    """
    Extract all pub_* variables from data_array, assign them to utils.py module,
    optionally remove the lines, and return the edited code as a string.

    Parameters:
        data_array: list of strings, each line from DSL
        dbg: optional debug function
        rm_line: if True, remove lines that set pub_* variables

    Returns:
        Edited DSL code as a single string.
    """
    pub_vars = ["pub_var", "pub_bool", "pub_int", "pub_str", "pub_float", "pub_array", "pub_json"]
    
    # Track indices of lines to remove
    lines_to_remove = set()
    
    for i, line in enumerate(data_array):
        line_strip = line.strip()
        for pub_name in pub_vars:
            if line_strip.startswith(pub_name):
                try:
                    key, value = line_strip.split("=", 1)
                    value = value.strip()
                    
                    # Evaluate it in the current Python context
                    # parsed_value = eval(value, globals(), locals())  # safer: maybe restrict locals/globals

                    # Safe parsing
                    try:
                        parsed_value = ast.literal_eval(value)
                    except Exception:
                        try:
                            parsed_value = eval(value, utils.EXEC_CONTEXT, utils.EXEC_CONTEXT)
                        except Exception as e:
                            dbg(f"[Error] {value}")
                            parsed_value = value

                    # Assign to utils
                    setattr(utils, key.upper(), parsed_value)
                                
                    # Assign to utils
                    setattr(utils, pub_name.upper(), parsed_value)
                    dbg(f"[{pub_name.upper()}]: {parsed_value}")
                    
                    if rm_line:
                        lines_to_remove.add(i)

                except Exception as e:
                    dbg(f"[ERROR parsing {pub_name}]: {e}")
                break  # stop checking other pub_* for this line

    # Remove lines in reverse order to not mess up indices
    if rm_line:
        for index in sorted(lines_to_remove, reverse=True):
            data_array.pop(index)

    # Return edited code as single string
    return "\n".join(data_array)

import utils
from utils import dbg
import ast

def process_code(code: str):
    """
    Process DSL code in correct order:
    1. Execute all ASSIGN lines and extract pub_* variables
    2. Replace all PUB_* placeholders in remaining lines
    3. Remove RM-LINE lines
    Returns cleaned DSL code ready for execution.
    """
    lines = code.splitlines()
    final_lines = []

    pub_vars_lower = ["pub_var", "pub_bool", "pub_int", "pub_str",
                      "pub_float", "pub_array", "pub_json"]
    pub_vars_upper = ["PUB_VAR", "PUB_BOOL", "PUB_INT", "PUB_STR",
                      "PUB_FLOAT", "PUB_ARRAY", "PUB_JSON"]

    # Step 1: Assign pub_* variables and execute ASSIGN lines
    for raw_line in lines:
        line = raw_line.strip()

        # Handle pub_* assignments
        for pub_name in pub_vars_lower:
            if line.startswith(pub_name):
                try:
                    key, value = line.split("=", 1)
                    value = value.strip()
                    # Try safe literal_eval first
                    try:
                        parsed_value = ast.literal_eval(value)
                    except:
                        # fallback to EXEC_CONTEXT eval
                        parsed_value = eval(value, utils.EXEC_CONTEXT, utils.EXEC_CONTEXT)
                    # Assign to utils
                    setattr(utils, key.upper(), parsed_value)
                    setattr(utils, pub_name.upper(), parsed_value)
                    dbg(f"[{pub_name.upper()}]: {parsed_value}")
                except Exception as e:
                    dbg(f"[Error parsing {pub_name}]: {e}")
                break  # only one pub_* per line

        # Execute ASSIGN lines
        if "ASSIGN" in line:
            try:
                dbg(f"[Executing] {line}")
                exec(line, utils.EXEC_CONTEXT, utils.EXEC_CONTEXT)
            except Exception as e:
                dbg(f"[Error] {e} \n[Line] {line}")

    # Step 2: Replace PUB_* placeholders in all lines
    processed_lines = []
    for raw_line in lines:
        line = raw_line.strip()
        for pub_name in pub_vars_upper:
            if hasattr(utils, pub_name):
                pub_val = getattr(utils, pub_name)
                line = line.replace(pub_name, repr(pub_val))
        processed_lines.append(line)

    # Step 3: Remove RM-LINE lines
    for line in processed_lines:
        if "RM-LINE" in line:
            dbg("[Removing]", line)
            continue
        final_lines.append(line)

    # Return the final code
    return "\n".join(final_lines)

def assign_debug(is_debug: str):
    """Set utils.DEBUG based on input or fallback to utils.DATA_ARRAY."""
    is_debug = (is_debug or "").strip().lower()

    if is_debug == "on":
        utils.DEBUG = True
    elif is_debug == "off":
        utils.DEBUG = False
    else:
        # fallback: check utils.DATA_ARRAY
        for line in utils.DATA_ARRAY:
            line = line.strip().lower()
            if line == "debug on":
                utils.DEBUG = True
                break
            elif line == "debug off":
                utils.DEBUG = False
                break