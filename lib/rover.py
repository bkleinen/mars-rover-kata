from dataclasses import dataclass
class Rover:
    def __init__(self, rover_state):
        self.state = rover_state
        self.x = rover_state.x
        self.y = rover_state.y

    def execute(self, input):
        commands = list(input)
        for command in commands:
            if "f" == command:
                self.state = Command.for_str(input,self.state).execute()
            elif "b" == command:
                 self.state = Command.for_str(input,self.state).execute()
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
            return  MoveCommand(input, rover_state)
        if input in ['l', 'r']:
            return  TurnCommand(input, rover_state)
        
    pass
class MoveCommand(Command):
    def __init__(self, input, rover_state):
        self.command = input
        self.state = rover_state
        
    
    def execute(self, state = None):
        if state is not None:
            self.state = state
        if "f" == self.command:
            y = self.state.y + 1
        elif "b" == self.command:
            y = self.state.y - 1
        return RoverState(self.state.x, y, self.state.direction)
    pass
class TurnCommand(Command):
    def __init__(self, input, rover_state):
        self.command = input
        self.state = rover_state
    

@dataclass(frozen=False)
class RoverState:
    x: int
    y: int
    direction: str
    directions = ["N", "E", "S", "W"]