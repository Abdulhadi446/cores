# Cores Documentation

**Cores** – _"CUDA for CPUs"_ – _"Harness the full power of your CPU"_

Cores is a lightweight scripting framework for high-performance CPU-based code execution. It provides a Python-like DSL for rapid development, threaded execution, and runtime variable management.

---

## Core Concepts

### 🔹 ASSIGN

- **Purpose:** Execute a line immediately.
- **Example:**

```cores
mystr = "Hello, World" # ASSIGN
pub_str = mystr + PUB_STR # ASSIGN
```

- **Notes:**

  - Executes in the `utils.EXEC_CONTEXT` environment.
  - Can be combined with `RM-LINE`.

### 🔹 RM-LINE

- **Purpose:** Remove the line from final execution/output.
- **Example:**

```cores
print(PUB_STR) # RM-LINE
```

### 🔹 ASSIGN + RM-LINE

- **Purpose:** Execute the line but remove it from the output.
- **Example:**

```cores
mystr = "Hello" # ASSIGN RM-LINE
pub_str = mystr + PUB_STR # ASSIGN RM-LINE
```

- **Processing Order:**

  1. `ASSIGN` runs and updates variables.
  2. `RM-LINE` removes the line from the final code.

### 🔹 PUB\_\* Variables

These are global placeholders available throughout your code.

| Variable  | Example              |
| --------- | -------------------- |
| PUB_VAR   | `{'x': 10, 'y': 20}` |
| PUB_JSON  | `{"score": 0}`       |
| PUB_ARRAY | `[1,2,3,4,5]`        |
| PUB_BOOL  | `True`               |
| PUB_INT   | `42`                 |
| PUB_FLOAT | `3.14`               |
| PUB_STR   | `'Hello DSL'`        |

- **Usage:** Can be referenced in any line and will be replaced dynamically during processing.
- **Note:** Always assign pub\_\* variables at the start of the script.

### 🔹 Blocks

Cores supports structured blocks:

#### `do:`

- Executes code in a contained block.
- Example:

```cores
do: {
    var = PUB_VAR
    print(str(var))
    print(PUB_STR) # RM-LINE
}
```

#### `times:`

- Repeat a block a specified number of times.
- Example:

```cores
times: (3) {
    print(PUB_STR)
}
```

#### `end:`

- Optional cleanup or final block after loops.

### 🔹 wait

- Pauses execution if used in a thread or synchronous code.
- Syntax: `wait`

### 🔹 Thread Special Keywords

Access thread metadata during execution:

| Keyword          | Description                |
| ---------------- | -------------------------- |
| THREAD-NAME      | Thread name                |
| THREAD-NUMBER    | Index number of thread     |
| THREAD-NATIVE-ID | OS native ID               |
| THREAD-IS-ALIVE  | Boolean if thread is alive |
| THREAD-DAEMON    | Boolean if daemon thread   |
| THREAD-IDENT     | Thread identifier          |

- Example:

```cores
print(THREAD-NAME)
print(THREAD-IS-ALIVE)
```

### 🔹 Debugging

Use `dbg()` for logging internal states:

```cores
dbg("[Debug] Current PUB_STR:", PUB_STR)
```

### 🔹 Execution Flow

1. \*_Assign pub\__ variables\*\*
2. \*_Replace PUB\__ placeholders\*\*
3. **Handle ASSIGN and RM-LINE directives**
4. **Process blocks (`do:`, `times:`, `end:`)**
5. **Evaluate threaded or sequential code**

### 🔹 Notes

- Lines with multiple directives (e.g., `ASSIGN RM-LINE`) are processed in order.
- Always replace PUB\_\* variables first in a line to avoid runtime errors.
- Thread keywords allow dynamic inspection inside threaded execution blocks.

---

**Tagline:** _"Cores – Unlocking the full potential of your CPU"_
