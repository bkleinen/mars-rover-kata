import pytest
from lib.rover import Rover, World
from lib.base import ObstacleEncountered
from lib.base import RoverState, Position, RS

testcases = [
    (RS(0,0,"N"), "f", RS(0,1,"N")),
    (RS(0,1,"N"), "b", RS(0,0,"N")),
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
    rover = Rover(init)
    rover.execute(command)
    assert rover.position() == expected

def test_rover_throws_exception_on_unknown_command():
    init = RS(3,3,"N")
    command = "x"
    rover = Rover(init)
    with pytest.raises(AttributeError):
        rover.execute(command)

def test_rover_rolls_over_world_10x10_n():
    init = RS(2,8,"N")
    command = "ff"
    rover = Rover(init)
    rover.execute(command)
    expected = RS(2,0,"N")
    assert rover.position() == expected

def test_rover_rolls_over_world_10x10_e():
    init = RS(8,2,"N")
    command = "rff"
    rover = Rover(init)
    rover.execute(command)
    expected = RS(0,2,"E")
    assert rover.position() == expected

def test_rover_rolls_over_world_10x10_both():
    init = RS(8,8,"N")
    command = "ffrff"
    rover = Rover(init)
    rover.execute(command)
    expected = RS(0,0,"E")
    assert rover.position() == expected


def test_rover_rolls_over_both_world_size():
    world = World(5,7)
    init = RS(4,5,"N")
    command = "ffrff"
    rover = Rover(init, world)
    rover.execute(command)
    expected = RS(1,0,"E")
    assert rover.position() == expected
