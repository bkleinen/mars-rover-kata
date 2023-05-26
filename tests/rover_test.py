import pytest
from lib.rover import Rover
from lib.rover import RoverState as RS

def test_rover():
    rover = Rover(0,0,"N")

import pytest
from lib.rover import Rover


testcases = [
    (RS(0,0,"N"), "f", RS(0,1,"N")),
    (RS(0,1,"N"), "b", RS(0,0,"N")),
    (RS(5,5,"N"), "f", RS(5,6,"N")),
    (RS(3,3,"N"), "r", RS(3,3,"E")),
    (RS(0,0,"N"), "l", RS(0,0,"W")),
             ]
@pytest.mark.parametrize("init,command,expected", testcases)
def test_rover(init, command, expected):
    rover = Rover(init)
    rover.execute(command)
    assert rover.position() == expected



    
