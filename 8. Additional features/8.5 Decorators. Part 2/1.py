import functools


def track_instances(cls):
    cls.instances = []
    old_init = cls.__init__

    @functools.wraps(cls)
    def new_init(self, *args, **kwargs):
        old_init(self, *args, **kwargs)
        self.instances.append(self)
    
    cls.__init__ = new_init
    return cls