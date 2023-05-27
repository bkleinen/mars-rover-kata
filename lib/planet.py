from lib.rover import World
from lib.base import Position as P
from dataclasses import replace


class Planet(World):
    def next(self, rover_state, command):
        if not self.on_pole(rover_state):
            return super().next(rover_state, command)
        new_x = self.width - rover_state.pos.x
        new_y = self.height-2
        return replace(rover_state, pos=P(new_x, new_y), direction="S")
    
    def on_pole(self, rover_state):
        return rover_state.pos.y == self.height-1
