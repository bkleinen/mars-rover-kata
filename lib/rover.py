from dataclasses import dataclass
import dataclasses
from lib.rover_helper import string_to_matrix, matrix_to_string, create_field


@dataclass(frozen=False)
class World:
    width: int
    height: int
    field: list = None
    def __post_init__(self):
        if self.field is None:
            self.field = create_field(self.width, self.height)
 
    @classmethod
    def from_str(cls, world_rep):
        field = string_to_matrix(world_rep)
        height = (len(field))
        width = len(field[0])
        return World(width, height, field)

    def __str__(self):
        world_str = matrix_to_string(self.field)
        return world_str

    def add_obstacle(self, x, y):
        self.set(x,y,'o')       

    def is_free(self, x, y):
        return self.get(x, y) == '.' 
    
    def get(self, x, y):
        return self.field[y][x]
    
    def set(self, x, y, value):
        self.field[y][x] = value

    def wrap(self, pos):
        new_x = pos.x % self.width
        new_y = pos.y % self.height
        return Position(new_x, new_y)


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
        new_pos = world.wrap(state.pos + delta)
        if not world.is_free(new_pos.x, new_pos.y):
            raise ObstacleEncountered(f' obstacle at {new_pos.x}, {new_pos.y}: {world.get(new_pos.x, new_pos.y)}')
        
        return dataclasses.replace(state, pos=new_pos)
        

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




