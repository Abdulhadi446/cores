# Cores – Unlocking the Full Potential of Your CPU

**Cores** is an experimental, CPU-focused programming language inspired by **CUDA** concepts. It is designed to leverage **parallel execution**, **thread variables**, and **low-level concurrency** directly on your CPU, with a Python-like minimal syntax.

---

## Highlights

- **Threaded Execution:** Automatically run blocks in parallel using `times:`.
- **Shared Variables:** Use `pub_var`, `pub_json`, `pub_array`, `pub_bool`, `pub_int`, `pub_float`, `pub_str` and their uppercase PUB\_\* counterparts for global state.
- **Lightweight Syntax:** Minimal constructs like `do:`, `times:`, `end:`, and `wait` blocks.
- **Thread Metadata Access:** Inspect threads in runtime with variables such as:

  - `THREAD-NAME`
  - `THREAD-NUMBER`
  - `THREAD-NATIVE-ID`
  - `THREAD-IS-ALIVE`
  - `THREAD-DAEMON`
  - `THREAD-IDENT`
  - `PUB_VAR`

- **Dynamic Variable Assignments:** Use `ASSIGN` to evaluate and store expressions at runtime.
- **Line Management:** Use `RM-LINE` to remove lines after execution.
- **CPU Power Utilization:** Designed to maximize your CPU cores without the complexity of GPU programming.

---

## Core Concepts

1. **Blocks:**

   - `do:` — Defines a code block that runs immediately.
   - `times: (N)` — Executes the block N times in separate threads.
   - `end:` — Concludes a code block.
   - `wait` — Ensures all threads finish before continuing.

2. **Global Variables:**

   - Variables starting with `pub_` are automatically shared across threads.
   - The uppercase PUB\_\* versions can be used in expressions and prints.

3. **Special Keywords:**

   - `ASSIGN` — Marks a line to execute as a runtime assignment.
   - `RM-LINE` — Marks a line to be removed from the final code after execution.

4. **Thread Info:**

   - Access metadata for each thread, including name, ID, status, and daemon flag.

5. **Execution Flow:**

   - Replace PUB\_\* placeholders first.
   - Execute ASSIGN lines.
   - Extract and update pub\_\* variables.
   - Remove lines marked with RM-LINE.

---

## Version

- Current Stable: **v1.0**

---

## Tagline

**Cores – Unlocking the Full Potential of Your CPU**

[DOCUMENTATION](DOCUMENTATION.md)
