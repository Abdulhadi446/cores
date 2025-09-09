# Cores Extended Documentation

[DOCUMENTATION](../DOCUMENTATION.md)

## Keypoints

- You might know Cores is made on python.
- It have a much of compatablity with it.
- When you do assign so we just run the line with python `exec` function and while evaluation
  PUB_Var's we also just use the python `eval` funtion
- Why am I saying this to you becuse If you use an other PL (Programing languge)
- On the assing lines you are supposed to use python code/syntax
  and same goes while assigning pub vars.
- We will auto remove the line assigning PUB_Vars so
  Keep in mind that this line wasnt going to be with you.

## PUB\_\*'s use

So when you use pub Var they are'nt like a normal variable instead we just replace PUB_Var's name with its value like

```
pub_str = 'Hello, World'
print(PUB_STR)
```

is conveted to

```
print('Hello, World')
```

Stay Aware.

## Assingning PUB\_\*'s

When you assign PUB_Vars like this

```
pub_json = {"ball_color": "red", "score": 0}
```

We will be just using Python's `eval` so for this example we will get the value `{"ball_color": "red", "score": 0}` but If you use non python syntax or local varaible's in you code. assigment dons'nt heppen.

So first assign your local variable before use.
And also use python syntax on the assign lines.

And one more thing.

Before while using variable like pub_json so use double or single quotes around them.
like this.

```
print("PUB_JSON")
```

or

```
a = str(PUB_JSON)
print(a)
```

## Notes

- Local varaible's will be diffrent accross block's or threads.
- We use in line code runner to executes code's for define language's

  ```
  ['python', '-c', 'print("Hello, World")']
  ```

- We are using temp files for C/CPP code and for undefine langauge like

  ```
  ['python', '~/temp-path/python-tempfile.py']
  ```

- Use `file-extension,executable` for temp file like

  ```
  py,python
  ```

  for python.

  So you get temperary file.

  temp file's are better and stable use them.

- Try to use indented code like this in blocks

  ```
    max
    py,python

    debug off

    do: {
        print("Hello, World")
    }

    times: (5) {
        print("Doing something")
    }

    end: {
        print("Bye")
    }

    wait

  ```

- Use debug off to get clean output.
