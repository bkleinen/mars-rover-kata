from dataclasses import dataclass
import dataclasses


@dataclass(frozen=False)
class World:
    width: int
    height: int
    field: list = None
    def __post_init__(self):
        self.field = [['.' for i in list(range(0,self.width))] for j in  list(range(0,self.height))]
 

    def __str__(self):
        rows = [ ''.join(r) for r in self.field ]
        rows.reverse()
        world_str = '\n' + '\n'.join(rows) + '\n'
        return world_str
    
    def add_obstacle(self, x, y):
        self.field[x][y] = 'o'        


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
        if state is not None:
            self.state = state
        state = self.state
        deltas = {
            'f' :  {'N' : (0,1), 'S' : (0,-1), 'W' : (-1, 0), 'E': (1, 0)},
            'b' :  {'N' : (0,-1), 'S' : (0,1), 'W' : (1, 0), 'E': (-1, 0)}
        }
        delta = deltas[self.command][state.direction]
        new_y = (state.y + delta[1]) % world.height
        new_x = (state.x + delta[0]) % world.width
        return dataclasses.replace(state, x=new_x, y=new_y)

class TurnCommand(Command):
    
    def __init__(self, input):
        self.command = input
    
    directions = ["N", "E", "S", "W"]
    def execute(self, state, _world):
        i = self.directions.index(state.direction)
        d = 0
        if "r" == self.command:
            d = 1
        elif "l" == self.command: 
            d = -1
        new_index = (i + d) % len(self.directions)
        new_direction = self.directions[new_index]
        return dataclasses.replace(state, direction=new_direction)
  

@dataclass(frozen=False)
class RoverState:
    x: int
    y: int
    direction: str



