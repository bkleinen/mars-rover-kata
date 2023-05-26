import pytest
from lib.rover import Rover

def test_rover():
    rover = Rover(0,0,"N")

import pytest
from lib.rover import Rover

def test_rover_forward():
    rover = Rover(0,0,"N")
    rover.execute('f')
    assert rover.position() == (0,1)

def test_rover_backward():
    rover = Rover(0,1,"N")
    rover.execute('b')
    assert rover.position() == (0,0)

testcases = [((0,0,"N"), "f", (0,1))]
@pytest.mark.parametrize("init,command,expected", testcases)
def test_rover_position(init, command, expected):
    rover = Rover(*init)
    rover.execute(command)
    assert rover.position() == expected


    
