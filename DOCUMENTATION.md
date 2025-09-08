# Cores – Harness the Full Power of Your CPU

**Cores** is a lightweight experimental programming language inspired by **CUDA** concepts but designed to run directly on CPU threads. It is built for experimenting with **parallel execution**, **thread variables**, and **low-level concurrency** using a simple, Python-like syntax.

---

## Features

- Thread-Oriented Execution Model: `times:` block for automatic threading.
- Global Variables: `pub_var`, `PUB_VAR`, and other shared variables.
- Minimal Syntax: `do`, `times`, `end`, `wait` blocks.
- Built-In Thread Metadata:

  - `THREAD-NAME`
  - `THREAD-NUMBER`
  - `THREAD-NATIVE-ID`
  - `THREAD-IS-ALIVE`
  - `THREAD-DAEMON`
  - `THREAD-IDENT`

- Pub Variables and Placeholders:

  - `pub_var`, `pub_bool`, `pub_int`, `pub_float`, `pub_str`, `pub_array`, `pub_json`
  - Corresponding placeholders: `PUB_VAR`, `PUB_BOOL`, `PUB_INT`, `PUB_FLOAT`, `PUB_STR`, `PUB_ARRAY`, `PUB_JSON`

- Line Keywords:

  - `ASSIGN` – executes the line and updates variables.
  - `RM-LINE` – removes the line after execution.

---

## Language Overview

Cores has a simple, Python-like syntax with special keywords and blocks:

### Blocks

- `do:` – standard code block executed sequentially.
- `times: (N)` – runs the block in parallel across N threads.
- `end:` – defines a block to run after all `do:` and `times:` blocks.
- `wait` – waits for all threads to finish.

### PUB\_\* Variables

- `pub_var`, `pub_bool`, `pub_int`, `pub_float`, `pub_str`, `pub_array`, `pub_json` are global variables.
- Can be referenced in code via `PUB_VAR`, `PUB_BOOL`, etc.
- Automatically updated when assigned.

### Line Keywords

- `ASSIGN` – executes the line in the current context and updates utils variables.
- `RM-LINE` – removes the line after execution to keep DSL code clean.

### Thread Special Variables

Within `times:` blocks, each thread can access metadata:

- `THREAD-NAME` – the thread's name.
- `THREAD-NUMBER` – the index number of the thread.
- `THREAD-NATIVE-ID` – the OS-native thread ID.
- `THREAD-IS-ALIVE` – whether the thread is alive.
- `THREAD-DAEMON` – thread daemon status.
- `THREAD-IDENT` – internal Python thread ID.

### Example

```cores
mystr = "Hello, World" # ASSIGN
pub_str = mystr + PUB_STR # ASSIGN
print(PUB_STR) # RM-LINE
```

- This will execute assignments and update `PUB_STR` before printing, then remove the print line if `RM-LINE` is used.

---

## Example Code

```cores
max py

pub_var = 0

do: {
  pub_var = 1
  print("Hello!")
}

times: (9) {
  print("\n")
  pub_var = PUB_VAR + 1
  print("PUB-VAR: ", PUB_VAR)
  print("Info About me:")
  Name = "THREAD-NAME"
  Number = "THREAD-NUMBER"
  NativeNumber = "THREAD-NATIVE-ID"
  AmIAlive = "THREAD-IS-ALIVE"
  deamon = "THREAD-DAEMON"
  MyID = "THREAD-IDENT"
  PublicVar = "PUB_VAR"
  print(Name, Number, NativeNumber, AmIAlive, deamon, MyID, PublicVar)
  print("\n")
}

end: {
  print("Bye!")
}

wait
```

---

## Example Output

```
Hello!
PUB-VAR: 1
Info About me:
Thread-3 (thread_main) 3 32860 True True 32860 1
...
Bye!
```

---

## Keywords

- `do:`
- `times: (N)`
- `end:`
- `wait`
- `ASSIGN`
- `RM-LINE`
- `pub_var`, `pub_bool`, `pub_int`, `pub_float`, `pub_str`, `pub_array`, `pub_json`
- `PUB_VAR`, `PUB_BOOL`, `PUB_INT`, `PUB_FLOAT`, `PUB_STR`, `PUB_ARRAY`, `PUB_JSON`
- Thread Special Variables: `THREAD-NAME`, `THREAD-NUMBER`, `THREAD-NATIVE-ID`, `THREAD-IS-ALIVE`, `THREAD-DAEMON`, `THREAD-IDENT`
