from dataclasses import dataclass, replace
from lib.rover_helper import string_to_matrix, matrix_to_string, create_field
from lib.base import Position as P
from lib.base import ObstacleEncountered

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
        return cls(width, height, field)

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
        return P(new_x, new_y)
    
    def next(self, rover_state, command):
        deltas = {
            'f' :  {'N' : P(0,1), 'S' : P(0,-1), 'W' : P(-1, 0), 'E': P(1, 0)},
            'b' :  {'N' : P(0,-1), 'S' : P(0,1), 'W' : P(1, 0), 'E': P(-1, 0)}
        }
        delta = deltas[command][rover_state.direction]
        new_pos = self.wrap(rover_state.pos + delta)
        if not self.is_free(new_pos.x, new_pos.y):
            obstacle = self.get(new_pos.x, new_pos.y)
            raise ObstacleEncountered(f' obstacle at {new_pos.x}, {new_pos.y}: {obstacle}')
        return replace(rover_state, pos=new_pos)
    
      

