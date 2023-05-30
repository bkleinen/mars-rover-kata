from mars_rover.rover import World
from mars_rover.rover_state import Position as P, Orientation as Rose
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

        
    def next_on_pole(self, rover_state, command):
        
        if self.on_north_pole(rover_state.pos):
            pole = Rose.N
            
            new_y = self.height-2
            new_orientation = Rose.S if command == 'f' else Rose.N
        else:
            pole = Rose.S
            new_y = 1
            new_orientation = Rose.N if command == 'f' else Rose.S
        
        quarter_turns = rover_state.orientation.quarter_turns_for_on(command, pole)
        new_x = self.quarter_turn(rover_state.pos.x, quarter_turns)   
        return rover_state.replace(pos=P(new_x, new_y), orientation=new_orientation)
    
    def on_pole(self, pos):
        return self.on_north_pole(pos) or self.on_south_pole(pos)
    
    def on_north_pole(self, pos):
        return pos.y == self.height-1

    def on_south_pole(self, pos):
        return pos.y == 0
    
    def quarter_turn(self, x, quarters):
        quarter = self.width/4
        return int((x + quarters * quarter) % self.width)
    
    def add_obstacle(self, x, y):
        if not self.on_pole(P(x,y)):
            super().add_obstacle(x,y)
            return
         
        for x in range(self.width):
            super().add_obstacle(x,y)