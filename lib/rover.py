from dataclasses import dataclass
class Rover:
    def __init__(self, rover_state):
        self.state = rover_state
        self.x = rover_state.x
        self.y = rover_state.y

    def execute(self, input):
        command_chars = list(input)
        commands = [Command.for_str(c) for c in command_chars]
        for command in commands: 
            command.execute(self.state)
        for command in command_chars:
            if "f" == command:
                self.state = Command.for_str(command).execute(self.state)
            elif "b" == command:
                 self.state = Command.for_str(command).execute(self.state)
            elif "r" == command:
                i = RoverState.directions.index(self.state.direction)
                i = (i + 1) % len(RoverState.directions)
                self.state.direction = RoverState.directions[i]
            elif "l" == command: 
                i = RoverState.directions.index(self.state.direction)
                i = (i - 1) % len(RoverState.directions)
                self.state.direction = RoverState.directions[i]
        

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
    
    def execute(self, state):
        if "r" == self.command:
            i = RoverState.directions.index(state.direction)
            i = (i + 1) % len(RoverState.directions)
            new_direction = RoverState.directions[i]
        elif "l" == self.command: 
            i = RoverState.directions.index(state.direction)
            i = (i - 1) % len(RoverState.directions)
            new_direction = RoverState.directions[i]
        return RoverState(state.x, state.y, direction= new_direction)
    

@dataclass(frozen=False)
class RoverState:
    x: int
    y: int
    direction: str
    directions = ["N", "E", "S", "W"]