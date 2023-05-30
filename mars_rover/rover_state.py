from dataclasses import dataclass, field


@dataclass(frozen=True)
class Position:
    x: int
    y: int
        
    def __add__(self, other):
        x = self.x + other.x
        y = self.y + other.y
        return Position(x, y)

P = Position
@dataclass(frozen=True)
class Direction:
    direction_str: str
    
    def delta(self, command):
        deltas = {
            'f' :  {'N' : P(0,1), 'S' : P(0,-1), 'W' : P(-1, 0), 'E': P(1, 0)},
            'b' :  {'N' : P(0,-1), 'S' : P(0,1), 'W' : P(1, 0), 'E': P(-1, 0)}
        }
        delta = deltas[command][self.direction_str]
        return delta

    def turn(self, command):
        pass


@dataclass(frozen=False)
class RoverState:
    pos: Position
    direction: str
    direction_new: Direction = field(init=False)
    def __post_init__(self):
        self.direction_new = Direction(self.direction)

    def __repr__(self) -> str:
        return f"RS({self.pos.x},{self.pos.y},'{self.direction}')"

    def delta(self, command):
        return self.direction_new.delta(command)

    def get_direction(self):
        return self.direction_new

# shorthand factory for RoverState:
def RS(x,y,d):
    return RoverState(Position(x,y),d)
