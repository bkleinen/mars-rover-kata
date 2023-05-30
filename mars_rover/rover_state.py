from dataclasses import dataclass, field

@dataclass(frozen=True)
class Position:
    x: int
    y: int
        
    def __add__(self, other):
        x = self.x + other.x
        y = self.y + other.y
        return Position(x, y)

@dataclass(frozen=True)
class Direction:
    direction: str

@dataclass(frozen=False)
class RoverState:
    pos: Position
    direction: str
    direction_new: Direction = field(init=False)
    def __post_init__(self):
        self.direction_new = Direction(self.direction)



    def __repr__(self) -> str:
        return f"RS({self.pos.x},{self.pos.y},'{self.direction}')"

    def delta_square(self, command):
        return None
# shorthand factory for RoverState:
def RS(x,y,d):
    return RoverState(Position(x,y),d)
