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
                self.state.y += 1
            elif "b" == command:
                self.state.y -= 1
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
    def from_str(cls, input):
        if input in ['l', 'r']:
            return  TurnCommand(input)
        pass
    pass
class TurnCommand(Command):
    def __init__(self, input):
        pass
    pass
@dataclass
class RoverState:
    x: int
    y: int
    direction: str
    directions = ["N", "E", "S", "W"]