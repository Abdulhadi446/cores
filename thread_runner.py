# thread_runner.py
import threading
import subprocess
from datetime import datetime
import re
import ast
import utils
from utils import RUNTIMES, run_cpp_code_fully, DEBUG

def run_in_thread(code: str, lang: str):
    """Run code in a separate thread with all placeholders and optimizations."""

    def thread_main(code, lang):
        # Local debug function
        def dbg(msg):
            if DEBUG:
                print(msg)

        # Current thread object
        t = threading.current_thread()

        thread_number_match = re.search(r'Thread-(\d+)', t.name)
        thread_number = int(thread_number_match.group(1)) if thread_number_match else 0

        # All placeholders preserved
        placeholders = {
            'THREAD-NAME': t.name,
            'THREAD-NUMBER': thread_number,
            'THREAD-NATIVE-ID': t.native_id,
            'THREAD-IS-ALIVE': t.is_alive(),
            'THREAD-DAEMON': t.daemon,
            'THREAD-IDENT': t.ident,
            'PUB_VAR': utils.PUB_VAR
        }


        # Batch placeholder replacement using regex
        pattern = re.compile('|'.join(re.escape(k) for k in placeholders))
        code = pattern.sub(lambda m: str(placeholders[m.group(0)]), code)

        # Extract pub_var assignment safely
        match = re.search(r'pub_var\s*=\s*(.+)', code)
        if match:
            try:
                utils.PUB_VAR = ast.literal_eval(match.group(1))
                dbg(f"[PUB-VAR]: {utils.PUB_VAR}")
            except Exception as e:
                dbg(f"[PUB-VAR Eval Error]: {e}")

        dbg(f"[{datetime.now()}] [{t.name}] starting execution...")

        try:
            if lang in ('c', 'cpp'):
                run_cpp_code_fully(code, lang)
            elif lang == 'python':
                exec(code, globals())
            else:
                subprocess.run(RUNTIMES[lang] + [code])
        except Exception as e:
            print(f"[Thread Error] {e}")

        dbg(f"[{datetime.now()}] [{t.name}] finished execution.")

    # Create and start thread
    t = threading.Thread(target=thread_main, args=(code, lang), daemon=True)
    t.start()
    return t