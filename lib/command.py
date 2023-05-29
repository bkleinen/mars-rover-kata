import dataclasses
from lib.base import Position as P

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
        new_direction = self.get_new_direction(state.direction, self.command)
        return dataclasses.replace(state, direction=new_direction)

    directions = ["N", "E", "S", "W"]
    turn = {'r' : 1, 'l': -1}
    def get_new_direction(self, direction, command):
        i = self.directions.index(direction)
        delta = self.turn[command]
        new_index = (i + delta) % len(self.directions)
        new_direction = self.directions[new_index]
        return new_direction
