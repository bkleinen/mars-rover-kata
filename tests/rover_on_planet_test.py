import pytest
from lib.rover import Rover, World
from lib.base import RoverState, Position
from lib.planet import Planet

def RS(x,y,d):
    return RoverState(Position(x,y),d)
testcases = [
    (RS(1,1,"N"), "f", RS(1,2,"N")),
    (RS(2,2,"N"), "b", RS(2,1,"N")),
    (RS(5,5,"N"), "f", RS(5,6,"N")),
    (RS(1,1,"N"), "r", RS(1,1,"E")),
    (RS(1,2,"E"), "r", RS(1,2,"S")),
    (RS(1,3,"S"), "r", RS(1,3,"W")),
    (RS(1,4,"W"), "r", RS(1,4,"N")),
    (RS(2,2,"N"), "l", RS(2,2,"W")),
    (RS(3,3,"N"), "rr", RS(3,3,"S")),
    (RS(3,3,"N"), "ffr", RS(3,5,"E")),
    (RS(3,3,"N"), "rf", RS(4,3,"E")),
    (RS(3,3,"N"), "ffrfflf", RS(5,6,"N")),
             ]
@pytest.mark.parametrize("init,command,expected", testcases)
def test_rover_move(init, command, expected):
    rover = Rover(init, Planet(10,10))
    rover.execute(command)
    assert rover.position() == expected

testcases_planet = [
    (RS(1,8,"N"), "f", RS(1,9,"N")),
    #(RS(1,9,"N"), "f", RS(9,8,"S")),
    pytest.param(
        RS(1,9,"N"), "f", RS(9,8,"S"),
        marks=pytest.mark.xfail), # passing over North Pole

             ]

@pytest.mark.parametrize("init,command,expected", testcases_planet)
def test_rover_move_on_planet(init, command, expected):
    rover = Rover(init, Planet(10,10))
    rover.execute(command)
    assert rover.position() == expected

