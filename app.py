import coderunner
from utils import CODE_FILES, dbg
import utils
import runcode
import thread_runner
import threadc
from coderunner import run_block
import os

def wait(threads_list):
    dbg('[Waiting] for threads to finish...')
    for t in threads_list:
        t.join()
    dbg("[Ends] Threaded Code")

    dbg(f"\n[Running] End code")
    run_block(utils.END_CODE)
    dbg("[Ends] End code")

    dbg("[Cleaning]")
    for FILE in CODE_FILES:
        dbg("Removing:", FILE)
        os.remove(FILE)
        
        threads_list.clear()

import processcode

def main(paths: str):
    with open(paths, "r") as file:
        data_array = file.read().splitlines()

    data = "\n".join(data_array)
    utils.DATA = data
    utils.DATA_ARRAY = data_array
    utils.WAIT = data.endswith('wait')

    # --- Extract pub_var ---
    processcode.extract_pub_vars_from_module(data_array)
    
    # --- Threads and code setup ---
    threads = int(threadc.threads(data))
    nums, code = runcode.main(data)

    lines = data_array
    lang = lines[1].strip() if len(lines) > 1 else ''
    threads_list = []

    dbg("[Running] Threaded Code")

    # --- Launch threads in batches ---
    full_batches, remainder = divmod(nums, threads)

    for batch in range(full_batches):
        dbg(f"(Batch {batch+1}) launching {threads} threads")
        threads_list.extend(thread_runner.run_in_process(code, lang) for _ in range(threads))

    if remainder:
        dbg(f"(Batch {full_batches+1}) launching {remainder} threads")
        threads_list.extend(thread_runner.run_in_process(code, lang) for _ in range(remainder))
    # --- Wait for threads if needed ---
    if utils.WAIT:
        wait(threads_list)


if __name__ == "__main__":
    main("app.crs")