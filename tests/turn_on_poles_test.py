import pytest
from lib.rover import Rover
from lib.planet import Planet
from lib.base import RS

    
def test_world_width_must_be_multiple_of_four():
    with pytest.raises(AttributeError):
        rover = Rover(RS(1,0,"S"), Planet(10,10))


def test_turn_on_north_pole():
    pass

testcases_planet = [(RS(0,2,"N"), "ff", RS(2,2,"S")),
                    (RS(0,3,"N"), "f", RS(2,2,"S")),
                    (RS(0,3,"N"), "rf", RS(1,2,"S")),
                    (RS(0,3,"N"), "lf", RS(3,2,"S")),
                    (RS(1,3,"N"), "llf", RS(1,2,"S")),

                    (RS(1,3,"N"), "rrf",  RS(1,2,"S")),
                    (RS(1,3,"N"), "rrff",  RS(1,1,"S")),

                    (RS(0,3,"N"), "f", RS(2,2,"S")),
                    (RS(0,3,"S"), "f",  RS(0,2,"S")), # on pole, with direction S -> two turns were there!

                    (RS(1,2,"S"), "f",  RS(1,1,"S")),
                    (RS(1,3,"S"), "ff", RS(1,1,"S")), # this is on north pole and fails
                    (RS(0,0,"S"), "f",  RS(2,1,"N")),
               #     (RS(1,2,"S"), "frf", RS(0,2,"N")),
]
      
@pytest.mark.parametrize("init,command,expected", testcases_planet)
def test_rover_turn_on_pole_4_4(init, command, expected):
    rover = Rover(init, Planet(4,4))
    rover.execute(command)
    assert rover.position() == expected


                      
testcases_planet_8 = [
    (RS(0,7,"N"), "f", RS(4,6,"S")),
    (RS(0,6,"N"), "ff", RS(4,6,"S")),
    (RS(0,7,"N"), "rf", RS(2,6,"S")),
    (RS(0,7,"N"), "rrf", RS(0,6,"S")),
    (RS(0,7,"N"), "lf", RS(6,6,"S")),
    (RS(0,6,"N"), "frrf", RS(0,6,"S")),

]
@pytest.mark.parametrize("init,command,expected", testcases_planet_8)
def test_rover_turn_on_pole_8_8(init, command, expected):
    rover = Rover(init, Planet(8,8))
    rover.execute(command)
    assert rover.position() == expected