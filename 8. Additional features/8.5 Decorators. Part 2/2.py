import functools

def add_attr_to_class(cls):
    cls.instances = []
    old_init = cls.__init__

    @functools.wraps(old_init)
    def new_init(self, *args, **kwargs):
        old_init(self, *args, **kwargs)
        self.instances.append(self)
        
    cls.__init__ = new_init
    return cls