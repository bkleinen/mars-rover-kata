from dataclasses import dataclass

@dataclass(frozen=True)
class Position:
    x: int
    y: int
        
    def __add__(self, other):
        x = self.x + other.x
        y = self.y + other.y
        return Position(x, y)

P = Position

@dataclass(frozen=False)
class RoverState:
    pos: Position
    direction: str

class ObstacleEncountered(Exception):
    pass