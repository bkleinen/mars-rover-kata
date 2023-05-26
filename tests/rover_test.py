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


    
