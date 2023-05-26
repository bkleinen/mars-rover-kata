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

testcases = []
@pytest.mark.parametrize("init,command,expected", testcases)
def test_rover(init, command, expected):
    pass


    
