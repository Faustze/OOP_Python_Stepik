from dataclasses import dataclass, field

    
@dataclass
class Point:
    x: float = 0.0
    y: float = 0.0
    quadrant: int = field(init=False)

    def __post_init__(self):
        self.quadrant = self.calculate_quadrant(self.x, self.y)
    
    @staticmethod
    def calculate_quadrant(x: float, y: float) -> int:
        if x > 0 and y > 0:
            return 1
        elif x > 0 and y < 0:
            return 4
        elif x < 0 and y > 0:
            return 2
        elif x < 0 and y < 0:
            return 3
        else:
            return 0
        
    def symmetric_x(self):
        return self.__class__(self.x, -self.y)
    
    def symmetric_y(self):
        return self.__class__(-self.x, self.y)