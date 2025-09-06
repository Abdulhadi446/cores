# Cores

There are many topics that we can covert but Start with simplecity. Get on the first line on the first line there are.

## First Line:

Supported values:

- "max" / "maxc" -> cpu_count \* 4
- "min" / "minc" -> 4
- "default" / "defaultc" -> cpu_count
- "Nc" -> N \* 4 (e.g., "2c" -> 8)
- integer -> exact number

So What are these values. they are Max threads.

## Second Line:

Supported values:

- "py": ["python", "-c"], # Python
- "js": ["node", "-e"], # JavaScript (Node.js)
- "rb": ["ruby", "-e"], # Ruby
- "pl": ["perl", "-e"], # Perl
- "php": ["php", "-r"], # PHP
- "r": ["R", "-e"], # R
- "lua": ["lua", "-e"], # Lua
- ### Shells
- "bash": ["bash", "-c"], # Bash
- "sh": ["sh", "-c"], # POSIX sh
- "cmd": ["cmd", "/C"], # Windows Command Prompt
- "ps": ["powershell", "-Command"], # Windows PowerShell

But we also Support custom values like

```
py,python
```

In this example `py` is the extension that file is gonna have and python is the executable.

So for this example the program run creates a temp file name
`python-tempfile.py` then run it like

```
python "~/../temp/python-tempfile.py"
```

So will get the output.

## DO Block.

It is meant for preperation before all the threads.
It will start with `do:` and then `{}` example:

```
do: {
    print("Hello, World!")
}
```

So it will output `Hello, World`

## Variables

We only have a single block wise variable declared like `pub_var={value}` before `DO:` block.
We can use it like

#### Use

```
print("PUB_VAR")
```

#### increasion

```
pub_var = PUB_VAR + 2
```

#### For Strings.

```
pub_var = "Hello, World"
```

## TIMES BLOCK

This is the main block that uses multiple threads. in
This we have example structure like

```
times: (9) {
    print("Hello, World")
}
```

It will print `Hello, World` 9 times.
It can also use the `PUB_VAR` and asign `pub_var` just like `DO:` block but also have other variables.
Like:

- THREAD-NAME: Threads Name Like (Thread-{Thread-N} (thread_main)),
- THREAD-NUMBER': Thread Number the Number of Threa
- THREAD-NATIVE-ID: UID to do something with the thread If you want. Inside from it.
- THREAD-IS-ALIVE: Is thread alive (Mostly returns `True`)
- THREAD-DAEMON: Is the Thread has a `DEAMON` (True Bu deafult But can be changed).
- THREAD-IDENT: Code Level UID.

## `WAIT` keyword

It is supposed to be at the end of the file.
If the WAIT keyword is present so the program waits for all the threads in times block to END.

NOTE: Alway Keep it at the end of the file/code.

## END BLOCK

Only run at the end of all threads so it will not run if we dont wait for threads to end with `wait` keyword
It just does every thing `DO:` does but after all the threads ENDs like cleanup before stop.

## DEBUG

So there are two types of output modes that you can chose.

- DEBUG
- NOT DEBUG

So to set `DEBUG` or other setting you are supposed to go on utils.py to change them.

- `DEBUG = True` (Default) to
- `DEBUG = False`.

I love DEBUG false personally.

## WHOLE LANGUAGE

So after learning the basics There are two code snippets to check you compiler.

#### Minimal Test

```
max
py,python

do: {
    print("Hello!")
}

times: (5) {
    print("Doing somework!")
}

end: {
    print("Bye!")
}

wait
```

output:

#### With Debug

```
[Running] Do code
Language: py,python
Running ['python', 'C:\\Users\\(user-name)\\AppData\\Local\\Temp\\tmp6jf4814_\\python-tempfile.py']
Hello!
[Ends] Do code

[Running] Threaded Code
(Batch 1) launching 5 threads
[2025-09-06 20:59:12.021209] [Thread-1 (thread_main)] starting execution...
Language: py,python
[2025-09-06 20:59:12.022802] [Thread-2 (thread_main)] starting execution...
Language: py,python
[2025-09-06 20:59:12.024128] [Thread-3 (thread_main)] starting execution...
Language: py,python
[2025-09-06 20:59:12.024709] [Thread-4 (thread_main)] starting execution...
Running ['python', 'C:\\Users\\(user-name)\\AppData\\Local\\Temp\\tmpx9_xxjrm\\python-tempfile.py']
Language: py,python
[2025-09-06 20:59:12.032203] [Thread-5 (thread_main)] starting execution...
waiting for threads to finish...
Running ['python', 'C:\\Users\\(user-name)\\AppData\\Local\\Temp\\tmpk1u8sqme\\python-tempfile.py']
Running ['python', 'C:\\Users\\(user-name)\\AppData\\Local\\Temp\\tmpncnzg3yd\\python-tempfile.py']
Language: py,python
Running ['python', 'C:\\Users\\(user-name)\\AppData\\Local\\Temp\\tmpgt9fgbla\\python-tempfile.py']
Running ['python', 'C:\\Users\\(user-name)\\AppData\\Local\\Temp\\tmp7qvydlpy\\python-tempfile.py']
Doing somework!
Doing somework!
Doing somework!
Doing somework!
Doing somework!
[2025-09-06 20:59:12.252187] [Thread-2 (thread_main)] finished execution.
[2025-09-06 20:59:12.259700] [Thread-3 (thread_main)] finished execution.
[2025-09-06 20:59:12.262048] [Thread-1 (thread_main)] finished execution.
[2025-09-06 20:59:12.264936] [Thread-4 (thread_main)] finished execution.
[2025-09-06 20:59:12.265962] [Thread-5 (thread_main)] finished execution.
[Ends] Threaded Code

[Running] End code
Language: py,python
Running ['python', 'C:\\Users\\(user-name)\\AppData\\Local\\Temp\\tmpvvn3xo4m\\python-tempfile.py']
Bye!
[Ends] End code
```

#### Without Debug

```
Hello!
Doing somework!
Doing somework!
Doing somework!
Doing somework!
Doing somework!
Bye!
```

#### Full Test

```
8
py

pub_var = 0

do: {
    pub_var = 1
    print("Hello!")
}

times: (5) {
    pub_var = PUB_VAR + 1
    print("THREAD NAME:", 'THREAD-NAME')
    print("THREAD NUMBER:", 'THREAD-NUMBER')
    print("THREAD NATIVE ID", 'THREAD-NATIVE-ID')
    print("THREAD IS ALIVE", 'THREAD-IS-ALIVE')
    print("THREAD DAEMON", 'THREAD-DAEMON')
    print("THREAD IDENT", 'THREAD-IDENT')
    print("PUB VAR", 'PUB_VAR')
}

end: {
    print('PUB_VAR')
    print("Bye!")
}
```

#### With Debug

```
PS E:\aSodeom\cores> & C:/Users/TECHNOSELLERS/AppData/Local/Microsoft/WindowsApps/python3.13.exe e:/aSodeom/cores/app.py
[PUB-VAR]: 0
[Running] Do code
Asining PUB-VAR:  pub_var = 1
[PUB-VAR]: 1
Language: py
Running ['python', '-c', 'print("Hello!")']
Hello!
[Ends] Do code

[Running] Threaded Code
(Batch 1) launching 5 threads
[2025-09-06 21:35:29.997298] [Thread-1 (thread_main)] starting execution...
Asining PUB-VAR:  pub_var = 1 + 1
[2025-09-06 21:35:29.999849] [Thread-2 (thread_main)] starting execution...
[PUB-VAR]: 2
[2025-09-06 21:35:30.000895] [Thread-3 (thread_main)] starting execution...
Asining PUB-VAR:  pub_var = 2 + 1
Asining PUB-VAR:  pub_var = 1 + 1
[PUB-VAR]: 3
Language: py
[2025-09-06 21:35:30.002089] [Thread-4 (thread_main)] starting execution...
[PUB-VAR]: 2
Running ['python', '-c', 'print("THREAD NAME:", \'Thread-1 (thread_main)\')\nprint("THREAD NUMBER:", \'1\')\nprint("THREAD NATIVE ID", \'3752\')\nprint("THREAD IS ALIVE", \'True\')\nprint("THREAD DAEMON", \'True\')\nprint("THREAD IDENT", \'3752\')\nprint("PUB VAR", \'1\')']
Asining PUB-VAR:  pub_var = 3 + 1
[2025-09-06 21:35:30.003110] [Thread-5 (thread_main)] starting execution...
Language: py
[PUB-VAR]: 4
Asining PUB-VAR:  pub_var = 2 + 1
Running ['python', '-c', 'print("THREAD NAME:", \'Thread-3 (thread_main)\')\nprint("THREAD NUMBER:", \'3\')\nprint("THREAD NATIVE ID", \'14960\')\nprint("THREAD IS ALIVE", \'True\')\nprint("THREAD DAEMON", \'True\')\nprint("THREAD IDENT", \'14960\')\nprint("PUB VAR", \'2\')']
Language: py
Running ['python', '-c', 'print("THREAD NAME:", \'Thread-4 (thread_main)\')\nprint("THREAD NUMBER:", \'4\')\nprint("THREAD NATIVE ID", \'17540\')\nprint("THREAD IS ALIVE", \'True\')\nprint("THREAD DAEMON", \'True\')\nprint("THREAD IDENT", \'17540\')\nprint("PUB VAR", \'3\')']
PS E:\aSodeom\cores> THREAD NAME: Thread-1 (thread_main)
THREAD NUMBER: 1
THREAD NATIVE ID 3752
THREAD IS ALIVE True
THREAD DAEMON True
THREAD IDENT 3752
PUB VAR 1
THREAD NAME: Thread-3 (thread_main)
THREAD NUMBER: 3
THREAD NATIVE ID 14960
THREAD IS ALIVE True
THREAD DAEMON True
THREAD IDENT 14960
PUB VAR 2
THREAD NAME: Thread-4 (thread_main)
THREAD NUMBER: 4
THREAD NATIVE ID 17540
THREAD IS ALIVE True
THREAD DAEMON True
THREAD IDENT 17540
PUB VAR 3
```

#### Without Debug

```
PS E:\aSodeom\cores> & C:/Users/TECHNOSELLERS/AppData/Local/Microsoft/WindowsApps/python3.13.exe e:/aSodeom/cores/app.py
Hello!
PS E:\aSodeom\cores> THREAD NAME: Thread-1 (thread_main)
THREAD NUMBER: 1
THREAD NATIVE ID 15492
THREAD IS ALIVE True
THREAD DAEMON True
THREAD IDENT 15492
PUB VAR 1
THREAD NAME: Thread-4 (thread_main)
THREAD NUMBER: 4
THREAD NATIVE ID 11064
THREAD IS ALIVE True
THREAD DAEMON True
THREAD IDENT 11064
PUB VAR 4
THREAD NAME: Thread-3 (thread_main)
THREAD NAME: Thread-2 (thread_main)
THREAD NUMBER: 3
THREAD NUMBER: 2
THREAD NATIVE ID 11248
THREAD IS ALIVE True
THREAD NATIVE ID 8168
THREAD DAEMON True
THREAD IDENT 11248
PUB VAR 3
THREAD IS ALIVE True
THREAD DAEMON True
THREAD IDENT 8168
PUB VAR 2
THREAD NAME: Thread-5 (thread_main)
THREAD NUMBER: 5
THREAD NATIVE ID 2496
THREAD IS ALIVE True
THREAD DAEMON True
THREAD IDENT 2496
PUB VAR 5
```
