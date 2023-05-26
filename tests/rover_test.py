import pytest
from lib.rover import Rover
from lib.rover import RoverState as RS

def test_rover():
    rover = Rover(0,0,"N")

import pytest
from lib.rover import Rover


testcases = [(RS(0,0,"N"), "f", RS(0,1,"N")),
             ]
@pytest.mark.parametrize("init,command,expected", testcases)
def test_rover(init, command, expected):
    rover = Rover(init)
    rover.execute(command)
    assert rover.position() == expected



    
