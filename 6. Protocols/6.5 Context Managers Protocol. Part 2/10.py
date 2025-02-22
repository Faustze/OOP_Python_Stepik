import time


class AdvancedTimer:
    def __init__(self):
        self.last_run = None
        self.runs = []
        self.min = None
        self.max = None
    
    def __enter__(self):
        self.last_run = time.perf_counter()
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        end_time = time.perf_counter()
        self.last_run = end_time - self.last_run
        self.runs.append(self.last_run)
        self.min, self.max = min(self.runs), max(self.runs)
        return True