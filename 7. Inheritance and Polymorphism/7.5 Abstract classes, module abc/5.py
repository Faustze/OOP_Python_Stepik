from collections.abc import Sequence


class CustomRange(Sequence):
    def __init__(self, *args):
        self.args = []
        for arg in args:
            if isinstance(arg, int):
                self.args.append(arg)
            elif isinstance(arg, str):
                start, end = map(int, arg.split('-'))
                self.args.extend(range(start, end + 1))

    def __len__(self):
        return len(self.args)
    
    def __getitem__(self, item):
        if isinstance(item, (int, slice)):
            return self.args[item]
        return NotImplemented