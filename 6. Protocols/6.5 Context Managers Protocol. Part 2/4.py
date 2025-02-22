class ReadableTextFile:
    def __init__(self, filename):
        self.filename = filename

    def __enter__(self):
        self.file = open(self.filename, mode='r', encoding='utf-8')
        return (line.strip() for line in self.file)
    
    def __exit__(self, *args, **kwargs):
        self.file.close()