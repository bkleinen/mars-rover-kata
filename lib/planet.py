from lib.rover import World
from lib.base import Position as P
from dataclasses import replace


class Planet(World):
    def __post_init__(self):
        if self.width % 4 != 0:
            raise AttributeError('width must be multiple of 4')
        super().__post_init__()

   # def next_state(self, rover_state, command): 
   #     if self.not_on_pole(rover_state):
   #         return super().next_position(rover_state, command)
   #     return self.next_on_pole(rover_state)

    def next_state(self, rover_state, command): 
        if self.not_on_pole(rover_state.pos):
            return super().next_state(rover_state, command)
        
        return self.next_on_pole(rover_state)

    def next_on_pole(self, rover_state): 
        if self.on_north_pole(rover_state.pos):
            turns = {'E': 1, 'N' : 2, 'W': 3, 'S': 4}
            new_y = self.height-2
            new_direction = 'S'
        else:
            turns = {'E': 1, 'N' : 4, 'W': 3, 'S': 2}
            new_y = 1
            new_direction = 'N'
        
        new_x = self.turn(rover_state.pos.x,turns[rover_state.direction])   
        return replace(rover_state, pos=P(new_x, new_y), direction=new_direction)

    def not_on_pole(self, pos):
        return not self.on_north_pole(pos) and not self.on_south_pole(pos)
    
    def on_north_pole(self, pos):
        return pos.y == self.height-1

    def on_south_pole(self, pos):
        return pos.y == 0
    
    def turn(self, x, quarters):
        quarter = self.width/4
        return int((x + quarters * quarter) % self.width)
    
    def add_obstacle(self, x, y):
        if self.not_on_pole(P(x,y)):
            super().add_obstacle(x,y) 
    
        for x in range(self.width):
            super().add_obstacle(x,y)