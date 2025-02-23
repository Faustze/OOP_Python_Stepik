import contextlib
import sys


@contextlib.contextmanager
def reversed_print():
    standart_output = sys.stdout

    class ReversedStdout:
        def write(self, text):
            standart_output.write(text[::-1])

        def flush(self):
            standart_output.flush()
    
    sys.stdout = ReversedStdout()
    yield
    sys.stdout = standart_output