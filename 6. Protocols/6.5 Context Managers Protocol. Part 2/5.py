class Reloopable:
    def __init__(self, file):
        self.file = file

    def __enter__(self):
        return self.file.readlines()

    def __exit__(self, *args, **kwargs):
        self.file.close()