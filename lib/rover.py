from dataclasses import dataclass
import dataclasses
from lib.rover_helper import string_to_matrix, matrix_to_string


@dataclass(frozen=False)
class World:
    width: int
    height: int
    field: list = None
    def __post_init__(self):
        if self.field is None:
            self.field = [['.' for i in list(range(0,self.width))] for j in  list(range(0,self.height))]
 
    @classmethod
    def from_str(cls, world_rep):
        field = string_to_matrix(world_rep)
        height = (len(field))
        width = len(field[0])
        return World(width, height, field)

    def __str__(self):
        rows = [ ''.join(r) for r in self.field ]
        rows.reverse()
        world_str = '\n' + '\n'.join(rows) + '\n'
        return world_str
    
    def add_obstacle(self, x, y):
        self.set(x,y,'o')       

    def is_free(self, x, y):
        return self.get(x, y) == '.' 
    
    def get(self, x, y):
        return self.field[y][x]
    
    def set(self, x, y, value):
        self.field[y][x] = value

class ObstacleEncountered(Exception):
    pass


class Rover:
    def __init__(self, rover_state, world = World(10,10)):
        self.state = rover_state
        self.world = world

    def execute(self, input):
        commands = [Command.for_str(c) for c in list(input)]
        for command in commands: 
            self.state = command.execute(self.state, self.world)
          
    def position(self):
        return self.state
    
class Command:
    @classmethod
    def for_str(cls, input, rover_state = None):
        if input in ['f', 'b']:
            return  MoveCommand(input)
        if input in ['l', 'r']:
            return  TurnCommand(input)
        raise AttributeError(f"no command for:{input}, {type(input)} {list(input)}")
        
class MoveCommand(Command):
    def __init__(self, input, rover_state = None):
        self.command = input
        self.state = rover_state
        
    
    def execute(self, state, world):
        deltas = {
            'f' :  {'N' : P(0,1), 'S' : P(0,-1), 'W' : P(-1, 0), 'E': P(1, 0)},
            'b' :  {'N' : P(0,-1), 'S' : P(0,1), 'W' : P(1, 0), 'E': P(-1, 0)}
        }
        delta = deltas[self.command][state.direction]
        new_pos = state.pos + delta
        new_x = new_pos.x % world.width
        new_y = new_pos.y % world.height
        new_pos2 = P(new_x,new_y)
        if not world.is_free(new_x, new_y):
            raise ObstacleEncountered(f' obstacle at {new_x}, {new_y}: {world.get(new_x, new_y)}')
        
        return dataclasses.replace(state, pos=new_pos2)
        

class TurnCommand(Command):
    
    def __init__(self, input):
        self.command = input
    
    def execute(self, state, _world):
        new_direction = self.get_new_direction(state.direction, self.command)
        return dataclasses.replace(state, direction=new_direction)

    directions = ["N", "E", "S", "W"]
    turns = {'r' : 1, 'l': -1}
    def get_new_direction(self, direction, command):
        i = self.directions.index(direction)
        d = self.turns[command]
        new_index = (i + d) % len(self.directions)
        new_direction = self.directions[new_index]
        return new_direction
  
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




