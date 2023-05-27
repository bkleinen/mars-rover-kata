from lib.rover import World
from lib.base import Position as P


class Planet(World):
    def next(self, rover_state, command):
        if not self.on_pole(rover_state):
            return super().next(rover_state, command)
        new_x = self.width - rover_state.pos.x
        new_y = self.height-2
        return P(new_x, new_y)
    
    def on_pole(self, rover_state):
        return rover_state.pos.y == self.height-1
