import psutil

def threads(thread: str) -> int:
    """
    Convert the first line of a string into a number of worker threads.

    Supported values:
      - "max"  / "maxc" -> cpu_count * 4
      - "min"  / "minc" -> 4
      - "Nc"            -> N * 4  (e.g., "2c" -> 8)
      - integer string  -> exact number
    """
    first_line = thread.lstrip().splitlines()[0].lower()

    if first_line in ("max", "maxc"):
        return psutil.cpu_count(logical=True) * 4

    if first_line in ("min", "minc"):
        return 4

    if first_line.endswith("c"):
        n = first_line[:-1]
        if n.isdigit():
            return int(n) * 4
        raise ValueError(f"Invalid thread format: {first_line}")

    if first_line.isdigit():
        return int(first_line)

    raise ValueError(f"Invalid thread value: {first_line}")
