from mars_rover.rover import World
from mars_rover.rover_state import Position as P
from dataclasses import replace


class Planet(World):
    def __post_init__(self):
        if self.width % 4 != 0:
            raise AttributeError('width must be multiple of 4')
        super().__post_init__()

    def next_state(self, rover_state, command): 
        if not self.on_pole(rover_state.pos):
            return super().next_state(rover_state, command)
        
        return self.next_on_pole(rover_state, command)

    northpole_turns = {
            'f': {'E': 1, 'N' : 2, 'W': 3, 'S': 0},
            'b': {'E': 3, 'N' : 0, 'W': 1, 'S': 2}}
    southpole_turns = {
            'f': {'E': 1, 'N' : 0, 'W': 3, 'S': 2},
            'b': {'E': 3, 'N' : 2, 'W': 1, 'S': 0}}
        
    def next_on_pole(self, rover_state, command): 
        if self.on_north_pole(rover_state.pos):
            turns = self.northpole_turns[command]
            new_y = self.height-2
            new_direction = 'S' if command == 'f' else 'N'
        else:
            turns = self.southpole_turns[command]
            new_y = 1
            new_direction = 'N' if command == 'f' else 'S'
        
        new_x = self.turn(rover_state.pos.x,turns[rover_state.direction])   
        return replace(rover_state, pos=P(new_x, new_y), direction=new_direction)

    def on_pole(self, pos):
        return self.on_north_pole(pos) or self.on_south_pole(pos)
    
    def on_north_pole(self, pos):
        return pos.y == self.height-1

    def on_south_pole(self, pos):
        return pos.y == 0
    
    def turn(self, x, quarters):
        quarter = self.width/4
        return int((x + quarters * quarter) % self.width)
    
    def add_obstacle(self, x, y):
        if not self.on_pole(P(x,y)):
            super().add_obstacle(x,y)
            return
         
        for x in range(self.width):
            super().add_obstacle(x,y)