from lib.rover import World
from lib.base import Position as P
from dataclasses import replace


class Planet(World):
    def __post_init__(self):
        if self.width % 4 != 0:
            raise AttributeError('width must be multiple of 4')
        super().__post_init__()

    def next(self, rover_state, command):
        if self.on_north_pole(rover_state):
            new_x = self.opposite_longitude(rover_state.pos.x)
            new_y = self.height-2
            return replace(rover_state, pos=P(new_x, new_y), direction="S")
        elif self.on_south_pole(rover_state):
            if rover_state.direction == 'E':
                new_x = self.width - rover_state.pos.x
            new_x = self.opposite_longitude(rover_state.pos.x)
            new_y = 1
            return replace(rover_state, pos=P(new_x, new_y), direction="N")
        return super().next(rover_state, command)
    
    def on_north_pole(self, rover_state):
        return rover_state.pos.y == self.height-1

    def on_south_pole(self, rover_state):
        return rover_state.pos.y == 0

    def opposite_longitude(self, x):
        half = self.width/2
        return (x + half) % self.width