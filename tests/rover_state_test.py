
from lib.base import RS, RoverState

def test_str_rep():
    rover_state = RS(3,4,'E')
    assert str(rover_state) == "RS(3,4,'E')"
    