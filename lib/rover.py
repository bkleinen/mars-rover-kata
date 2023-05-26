from dataclasses import dataclass
class Rover:
    def __init__(self, rover_state):
        self.state = rover_state

    def execute(self, input):
        commands = [Command.for_str(c) for c in list(input)]
        for command in commands: 
            self.state = command.execute(self.state)
          
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
        
    pass
class MoveCommand(Command):
    def __init__(self, input, rover_state = None):
        self.command = input
        self.state = rover_state
        
    
    def execute(self, state = None):
        if state is not None:
            self.state = state
        state = self.state
        deltas = {
            'f' :  {'N' : (0,1), 'S' : (0,-1), 'W' : (-1, 0), 'E': (1, 0)},
            'b' :  {'N' : (0,-1), 'S' : (0,1), 'W' : (1, 0), 'E': (-1, 0)}
        }
        delta = deltas[self.command][state.direction]
        return RoverState(state.x + delta[0], state.y + delta[1], state.direction)

    pass
class TurnCommand(Command):
    
    def __init__(self, input, rover_state = None):
        self.command = input
        self.state = rover_state
    
    directions = ["N", "E", "S", "W"]
    def execute(self, state):
        i = self.directions.index(state.direction)
        d = 0
        if "r" == self.command:
            d = 1
        elif "l" == self.command: 
            d = -1
        new_index = (i + d) % len(self.directions)
        new_direction = self.directions[new_index]
        return RoverState(state.x, state.y, direction = new_direction)
    

@dataclass(frozen=False)
class RoverState:
    x: int
    y: int
    direction: str