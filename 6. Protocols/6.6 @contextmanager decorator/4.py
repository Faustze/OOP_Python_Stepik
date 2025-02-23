import contextlib


@contextlib.contextmanager
def safe_open(filename, mode='r'):
    try:
        file = open(filename, mode=mode)
    except Exception as e:
        yield None, e
    else:
        try:
            yield file, None
        finally:
            file.close()