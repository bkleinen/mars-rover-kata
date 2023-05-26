from dataclasses import dataclass
class Rover:
    def __init__(self, rover_state):
        self.x = rover_state.x
        self.y = rover_state.y

    def execute(self, command):
        if "f" == command:
            self.y += 1
        else:
            self.y -= 1
        pass

    def position(self):
        return RoverState(self.x, self.y, "N")
    
@dataclass
class RoverState:
    x: int
    y: int
    direction: str