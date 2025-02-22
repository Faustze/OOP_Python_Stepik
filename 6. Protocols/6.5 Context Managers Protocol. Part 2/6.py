class Suppress:
    def __init__(self, *args):
        self.args = args
        self.exception = None

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        if exc_type in self.args:
            self.exception = exc_value
            return True