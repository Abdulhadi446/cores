# How to use Cores

[DOCUMENTATION](../DOCUMENTATION.md)

## How to use **Cores**

- To install cores you are going to be in release folders of Cores repo and install the latest release As cores dont upload unstable releases.

- Run it go on any system path folder like `C:\Windows\System32` on windows and place the cores file you can also add cores to system path so `System32` will be safe.
- Test it by using this example code

  ```
    max
    py,python

    debug off

    pub_var = {'x': 10, 'y': 20, 'vel_x': 3, 'vel_y': 2, 'width':800, 'height': 600}
    pub_json = {"ball_color": "red", "score": 0}
    pub_array = [1, 2, 3, 4, 5]
    pub_bool = True
    pub_int = 42
    pub_float = 3.14
    pub_str = 'Hello DSL'

    do: {
        print("PUB_VAR")
        print("PUB_JSON")
        print('PUB_ARRAY')
        print("PUB_BOOL")
        print("PUB_INT")
        print("PUB_FLOAT")
        print(PUB_STR) # RM-LINE
    }

    times: (1) {
        print("PUB_VAR")
        print("PUB_JSON")
        print('PUB_ARRAY')
        print("PUB_BOOL")
        print("PUB_INT")
        print("PUB_FLOAT")
        mystr = "Hello, World" # ASSIGN
        pub_str = mystr + PUB_STR
        print(PUB_STR)

    }

    end: {
        print("PUB_VAR")
        print("PUB_JSON")
        print('PUB_ARRAY')
        print("PUB_BOOL")
        print("PUB_INT")
        print("PUB_FLOAT")
        print(PUB_STR) # RM-LINE
    }

    wait
  ```

- then run it using this command

  ```
  cores yourfilename.crs
  ```

  or if you want full debug

  ```
  cores yourfilename.crs --debug on
  ```

  or if you want clean output use

  ```
  cores yourfilename.crs --debug off
  ```

  On is default.
