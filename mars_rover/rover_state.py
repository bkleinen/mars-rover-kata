from dataclasses import dataclass, field, replace as dataclasses_replace
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

    def reverse(self):
        return self.__class__.for_number(self.value + 2)
    
    def turn(self, command):
        turns = {'r' : 1, 'l': -1}[command] 
        return self.__class__.for_number(self.value + turns)
    
    @classmethod
    def deltas(cls):
        return {
            'f' :  {cls.N : P(0,1), cls.S : P(0,-1), cls.W : P(-1, 0), cls.E : P(1, 0)},
            'b' :  {cls.N : P(0,-1), cls.S : P(0,1), cls.W : P(1, 0),  cls.E : P(-1, 0)}
        }
    def delta(self, command): 
        delta = self.deltas()[command][self]
        return delta
    
    @classmethod
    def pole_quarter_turns(cls):
        return { cls.N : {'f': {cls.E : 1, cls.N : 2, cls.W : 3, cls.S : 0},
                          'b': {cls.E : 3, cls.N : 0, cls.W : 1, cls.S : 2}},
                 cls.S : {'f': {cls.E : 1, cls.N : 0, cls.W : 3, cls.S : 2},
                          'b': {cls.E : 3, cls.N : 2, cls.W : 1, cls.S : 0}}
            }
    def quarter_turns_for_on(self, command, pole):
        return self.pole_quarter_turns()[pole][command][self]


@dataclass(frozen=False)
class RoverState:
    pos: Position
    orientation: Orientation

    def __repr__(self) -> str:
        return f"RS({self.pos.x},{self.pos.y},'{self.orientation.name}')"
    
    def replace(self, **kwargs):
        return dataclasses_replace(self, **kwargs)
    

# shorthand factory for RoverState:
def RS(x,y,d):
    return RoverState(Position(x,y),Orientation[d])
