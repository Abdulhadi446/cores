from utils import DATA, DATA_ARRAY, WAIT, PUB_VAR, DEBUG, END_CODE
import utils
import time
import runcode
import thread_runner
import threadc
import ast

# --- Helper for debug printing ---
def dbg(msg):
    if utils.DEBUG:
        print(msg)

# --- Read file once and split into lines ---
with open("app.crs", "r") as file:
    data_array = file.read().splitlines()

data = "\n".join(data_array)
utils.DATA = data
utils.DATA_ARRAY = data_array
utils.WAIT = data.endswith('wait')

# --- Extract pub_var ---
for line in data_array:
    if line.startswith("pub_var"):
        key, value = line.split("=", 1)
        try:
            utils.PUB_VAR = ast.literal_eval(value.strip())
        except Exception:
            utils.PUB_VAR = eval(value.strip())  # fallback if complex expression
        dbg(f"[PUB-VAR]: {utils.PUB_VAR}")
        break

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
    threads_list.extend(thread_runner.run_in_thread(code, lang) for _ in range(threads))

if remainder:
    dbg(f"(Batch {full_batches+1}) launching {remainder} threads")
    threads_list.extend(thread_runner.run_in_thread(code, lang) for _ in range(remainder))

# --- Wait for threads if needed ---
if utils.WAIT:
    dbg('waiting for threads to finish...')
    for t in threads_list:
        t.join()
    dbg("[Ends] Threaded Code")

    dbg(f"\n[Running] End code")
    runcode.run_block(utils.END_CODE)
    dbg("[Ends] End code")
    threads_list.clear()
