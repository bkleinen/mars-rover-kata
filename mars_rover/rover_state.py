from dataclasses import dataclass, field
from enum import Enum

@dataclass(frozen=True)
class Position:
    x: int
    y: int
        
    def __add__(self, other):
        x = self.x + other.x
        y = self.y + other.y
        return Position(x, y)

P = Position

class Orientation(Enum):
    N = 0
    E = 1
    S = 2
    W = 3

    @classmethod
    def for_number(cls, i):
        return Orientation(i % 4)

    def turn(self, turns):
        return self.__class__.for_number(self.value + turns)
    
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


    directions = ["N", "E", "S", "W"]
    turns = {'r' : 1, 'l': -1}

    def turn(self, command):
        i = self.directions.index(self.direction_str)
        delta_i = self.turns[command]
        new_index = (i + delta_i) % len(self.directions)
        new_direction = self.directions[new_index]
        return new_direction
        return Direction(new_direction)
    
    pole_quarter_turns = { 'N' : {
            'f': {'E': 1, 'N' : 2, 'W': 3, 'S': 0},
            'b': {'E': 3, 'N' : 0, 'W': 1, 'S': 2}},
              'S' : {
            'f': {'E': 1, 'N' : 0, 'W': 3, 'S': 2},
            'b': {'E': 3, 'N' : 2, 'W': 1, 'S': 0}}
            }
    def quarter_turns_for_on(self, command, pole):
        return self.pole_quarter_turns[pole][command][self.direction_str]


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
