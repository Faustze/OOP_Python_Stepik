import contextlib
import os

@contextlib.contextmanager
def safe_write(filename: str):
    backup = None
    if os.path.exists(filename):
        with open(filename, 'r', encoding='utf-8') as f:
            backup = f.read()

    try:
        with open(filename, 'w', encoding='utf-8') as file:
            yield file
    except Exception as e:
        if backup is not None:
            with open(filename, 'w', encoding='utf-8') as f:
                f.write(backup)
        print(f'Во время записи в файл было возбуждено исключение {type(e).__name__}')