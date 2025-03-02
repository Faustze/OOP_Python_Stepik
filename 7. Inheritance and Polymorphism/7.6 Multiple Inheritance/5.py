class MROHelper:
    @staticmethod
    def len(any_class) -> int:
        return len(any_class.mro())
    
    @staticmethod
    def class_by_index(any_class, n: int=0):
        return any_class.mro()[n]
    
    @staticmethod
    def index_by_class(child, parent):
        return child.mro().index(parent)