from dataclasses import dataclass
from lib.rover_helper import string_to_matrix, matrix_to_string, create_field
from lib.base import Position

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
    
    def next(self, position, command):
        pass

