# CORES Programming Language

**CORES** is a lightweight experimental programming language inspired by **CUDA** concepts but designed to run directly on CPU threads.  
It is built for experimenting with **parallel execution**, **thread variables**, and **low-level concurrency** using a simple, Python-like syntax.

---

## ✨ Features
- **Thread-oriented execution model** – every `times:` block spawns threads automatically.  
- **Global variables** with live updates across threads (`pub_var`, `PUB_VAR`).  
- **Minimal syntax** with `do`, `times`, `end`, and `wait` blocks.  
- **Built-in thread metadata** for debugging and introspection:  
  - `THREAD-NAME`  
  - `THREAD-NUMBER`  
  - `THREAD-NATIVE-ID`  
  - `THREAD-IS-ALIVE`  
  - `THREAD-DAEMON`  
  - `THREAD-IDENT`  
  - `PUB_VAR`  

---

## 🔧 Syntax

```
max
py
pub_var=0

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

▶️ Example Output

When the above code runs, the threads will execute concurrently and output will look like:

```
Hello!


PUB-VAR:  1
Info About me:
Thread-3 (thread_main) 3 32860 True True 32860 1


PUB-VAR:  1
Info About me:
Thread-6 (thread_main) 6 19612 True True 19612 1


PUB-VAR:  1
Info About me:
Thread-1 (thread_main) 1 20720 True True 20720 1


PUB-VAR:  1
Info About me:
Thread-4 (thread_main) 4 15716 True True 15716 1


PUB-VAR:  1
Info About me:
Thread-2 (thread_main) 2 1324 True True 1324 1


PUB-VAR:  1
Info About me:
Thread-5 (thread_main) 5 8092 True True 8092 1


PUB-VAR:  1
Info About me:
Thread-7 (thread_main) 7 26424 True True 26424 1


PUB-VAR:  1
Info About me:
Thread-8 (thread_main) 8 15868 True True 15868 1


PUB-VAR:  1
Info About me:
Thread-9 (thread_main) 9 27796 True True 27796 1


Bye!
```

⚠️ Note: Because threads run concurrently, the order of output is not guaranteed. Each run may produce slightly different interleaving of lines.
🧩 Keywords

    do: → Defines an initialization block (runs once before threading).

    times: (N) → Spawns N threads that run the block concurrently.

    end: → Defines a cleanup block (runs once after threading).

    wait → Ensures the main process waits for all threads to finish.

🚀 Future Goals

    Add support for async do blocks.

    Shared memory handling beyond PUB_VAR.

    File I/O and networking inside thread blocks.

    GPU-like parallel kernel simulation.

📜 License (MIT)

MIT License

Copyright (c) 2025 Abdul Hadi

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.


---
