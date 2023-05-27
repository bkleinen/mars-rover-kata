from dataclasses import dataclass
import dataclasses
from lib.rover_helper import string_to_matrix, matrix_to_string, create_field
from lib.base import Position, P, RoverState
from lib.command import Command 
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
   


 