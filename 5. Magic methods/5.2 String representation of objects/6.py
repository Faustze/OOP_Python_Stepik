class AnyClass:
    def __init__(self, **kwargs):
        for k, v in kwargs.items():
            setattr(self, k, v)

    def __repr__(self, **kwargs):
        return f"{self.__class__.__name__}({', '.join(self._attrs())})"

    def __str__(self, **kwargs):
        return f"{self.__class__.__name__}: {', '.join(self._attrs())}"

    def _attrs(self):
        return [f'{k}={repr(v)}' for (k, v) in self.__dict__.items()]