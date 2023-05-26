from dataclasses import dataclass
class Rover:
    def __init__(self, rover_state):
        self.state = rover_state
        self.x = rover_state.x
        self.y = rover_state.y

    def execute(self, command):
        if "f" == command:
            self.state.y += 1
        else:
            self.state.y -= 1
        pass

    def position(self):
        return self.state
    
@dataclass
class RoverState:
    x: int
    y: int
    direction: str