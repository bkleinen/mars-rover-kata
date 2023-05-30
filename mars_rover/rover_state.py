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


    directions = ["N", "E", "S", "W"]
    turns = {'r' : 1, 'l': -1}
    def turn(self, command):
        pass
        i = self.directions.index(self.direction_str)
        delta_i = self.turns[command]
        new_index = (i + delta_i) % len(self.directions)
        new_direction = self.directions[new_index]
        return new_direction
    
    northpole_turns = {
            'f': {'E': 1, 'N' : 2, 'W': 3, 'S': 0},
            'b': {'E': 3, 'N' : 0, 'W': 1, 'S': 2}}
    southpole_turns = {
            'f': {'E': 1, 'N' : 0, 'W': 3, 'S': 2},
            'b': {'E': 3, 'N' : 2, 'W': 1, 'S': 0}}
   
    def next_x_on_pole(self, command):
        turns = self.northpole_turns[command]
        turns = self.southpole_turns[command]


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
    
    def next_on_pole(self, command,pole):
        pass

# shorthand factory for RoverState:
def RS(x,y,d):
    return RoverState(Position(x,y),d)
