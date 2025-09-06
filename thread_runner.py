# thread_runner.py
import threading
import subprocess
from datetime import datetime
import re
import ast
import utils
from utils import RUNTIMES, run_cpp_code_fully, DEBUG
from coderunner import run_block

# Lock to prevent console output from multiple threads mixing
print_lock = threading.Lock()

def run_in_thread(code: str, lang: str):
    """Run code in a separate thread with placeholders, PUB_VAR handling, and debug logging."""

    def thread_main(code: str, lang: str):
        t = threading.current_thread()

        # Local debug function
        def dbg(msg):
            if DEBUG:
                with print_lock:
                    print(msg)

        # Extract thread number from thread name
        thread_number_match = re.search(r'Thread-(\d+)', t.name)
        thread_number = int(thread_number_match.group(1)) if thread_number_match else 0

        # Replace placeholders
        placeholders = {
            'THREAD-NAME': t.name,
            'THREAD-NUMBER': thread_number,
            'THREAD-NATIVE-ID': t.native_id,
            'THREAD-IS-ALIVE': t.is_alive(),
            'THREAD-DAEMON': t.daemon,
            'THREAD-IDENT': t.ident,
            "PUB_VAR": utils.PUB_VAR
        }
        pattern = re.compile('|'.join(re.escape(k) for k in placeholders))
        code = pattern.sub(lambda m: str(placeholders[m.group(0)]), code)

        dbg(f"[{datetime.now()}] [{t.name}] starting execution...")

        try:
            run_block(code)
        except Exception as e:
            with print_lock:
                print(f"[Thread Error] {e}")

        dbg(f"[{datetime.now()}] [{t.name}] finished execution.")

    # Start thread
    t = threading.Thread(target=thread_main, args=(code, lang), daemon=True)
    t.start()
    return t
