import pytest
from lib.rover import Rover
from lib.rover import RoverState as RS

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
             ]
@pytest.mark.parametrize("init,command,expected", testcases)
def test_rover_move(init, command, expected):
    rover = Rover(init)
    rover.execute(command)
    assert rover.position() == expected



    
