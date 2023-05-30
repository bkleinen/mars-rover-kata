import dataclasses
from mars_rover.rover_state import Position as P

class Command:
    @classmethod
    def for_str(cls, input):
        if input in ['f', 'b']:
            return  MoveCommand(input)
        if input in ['l', 'r']:
            return  TurnCommand(input)
        raise AttributeError(f"no command for:{input}, {type(input)} {list(input)}")
        

class MoveCommand(Command):
    def __init__(self, input):
        self.command = input
         
    def execute(self, state, world):
        return world.next(state, self.command)
        

class TurnCommand(Command):
    
    def __init__(self, input):
        self.command = input
    
    def execute(self, state, _world):
        new_direction = state.get_orientation().turn(self.command)
        return state.replace(orientation=new_direction)

