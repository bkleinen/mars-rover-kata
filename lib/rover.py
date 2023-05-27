from dataclasses import dataclass
import dataclasses


@dataclass(frozen=False)
class World:
    width: int
    height: int
    field: list = None
    def __post_init__(self):
        if self.field is None:
            self.field = [['.' for i in list(range(0,self.width))] for j in  list(range(0,self.height))]
 
    @classmethod
    def from_str(cls, world_rep):
        rows = world_rep.strip().split('\n')
        field = [list(row) for row in rows]
        field.reverse()
        height = (len(field))
        width = len(field[0])
        return World(width, height, field)

    def __str__(self):
        rows = [ ''.join(r) for r in self.field ]
        rows.reverse()
        world_str = '\n' + '\n'.join(rows) + '\n'
        return world_str
    
    def add_obstacle(self, x, y):
        self.set(x,y,'o')       

    def is_free(self, x, y):
        return self.get(x, y) == '.' 
    
    def get(self, x, y):
        return self.field[y][x]
    
    def set(self, x, y, value):
        self.field[y][x] = value

class ObstacleEncountered(Exception):
    pass


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
        deltas = {
            'f' :  {'N' : (0,1), 'S' : (0,-1), 'W' : (-1, 0), 'E': (1, 0)},
            'b' :  {'N' : (0,-1), 'S' : (0,1), 'W' : (1, 0), 'E': (-1, 0)}
        }
        delta = deltas[self.command][state.direction]
        new_y = (state.y + delta[1]) % world.height
        new_x = (state.x + delta[0]) % world.width
        if not world.is_free(new_x, new_y):
            raise ObstacleEncountered(f' obstacle at {new_x}, {new_y}: {world.get(new_x, new_y)}')
        
        return dataclasses.replace(state, x=new_x, y=new_y)
        

class TurnCommand(Command):
    
    def __init__(self, input):
        self.command = input
    
    def execute(self, state, _world):
        new_direction = self.get_new_direction(state.direction, self.command)
        return dataclasses.replace(state, direction=new_direction)

    directions = ["N", "E", "S", "W"]
    turns = {'r' : 1, 'l': -1}
    def get_new_direction(self, direction, command):
        i = self.directions.index(direction)
        d = self.turns[command]
        new_index = (i + d) % len(self.directions)
        new_direction = self.directions[new_index]
        return new_direction
  

@dataclass(frozen=True)
class RoverState:
    x: int
    y: int
    direction: str



