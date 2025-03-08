import re


def snake_case(attrs=False):
    def decorator(cls):
        def to_snake_case(name):
            return re.sub(r'(?<!^)([A-Z])', r'_\1', name).lower()
        
        for name in dir(cls):
            if not name.startswith('__') and not name.endswith('__'):
                attr = getattr(cls, name)
                if callable(attr) or (attrs and not callable(attr)):
                    new_name = to_snake_case(name)
                    if new_name != name:
                        setattr(cls, new_name, attr)
                        delattr(cls, name)
                
        return cls
    
    return decorator