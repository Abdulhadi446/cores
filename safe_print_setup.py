# safe_print_setup.py
import sys, threading, atexit, io

_shutdown = False
_print_lock = threading.Lock()

def _mark_shutdown():
    global _shutdown
    _shutdown = True
    try:
        sys.__stdout__.flush()
        sys.__stderr__.flush()
    except Exception:
        pass

atexit.register(_mark_shutdown)

class SafeStream(io.TextIOBase):
    def __init__(self, stream):
        self._stream = stream

    def write(self, data):
        global _shutdown
        if not data:
            return
        if _shutdown:
            try:
                sys.__stdout__.write(data)
                sys.__stdout__.flush()
            except Exception:
                pass
        else:
            with _print_lock:
                try:
                    self._stream.write(data)
                    self._stream.flush()
                except Exception:
                    pass
        return len(data)

    def flush(self):
        global _shutdown
        if _shutdown:
            return
        try:
            self._stream.flush()
        except Exception:
            pass

    def isatty(self):
        return self._stream.isatty()

    def fileno(self):
        return self._stream.fileno()

    def close(self):
        try:
            self._stream.close()
        except Exception:
            pass

    @property
    def encoding(self):
        return getattr(self._stream, "encoding", None)

    def __getattr__(self, name):
        return getattr(self._stream, name)

# Replace global stdout/stderr
sys.stdout = SafeStream(sys.stdout)
sys.stderr = SafeStream(sys.stderr)
