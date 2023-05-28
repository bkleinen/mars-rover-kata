import pytest
from lib.rover import Rover
from lib.planet import Planet
from lib.base import RS

    
        
def test_world_width_must_be_multiple_of_four():
    with pytest.raises(AttributeError):
        rover = Rover(RS(1,0,"S"), Planet(10,10))