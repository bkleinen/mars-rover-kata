import pytest
from lib.rover import Rover
from lib.planet import Planet
from lib.base import RS

    
def test_world_width_must_be_multiple_of_four():
    with pytest.raises(AttributeError):
        rover = Rover(RS(1,0,"S"), Planet(10,10))


def test_turn_on_north_pole():
    pass

testcases_planet = [(RS(0,2,"N"), "ff", RS(2,2,"S"))
             ]

new_tests = [(RS(0,2,"N"), "ff", RS(2,2,"S"))]

new_tests = [pytest.param(*t,marks=pytest.mark.xfail) for t in new_tests]

testcases_planet.extend(new_tests)       
 # pytest.param(
   #     RS(1,0,"S"), "f", RS(11,1,"N"),
   #     marks=pytest.mark.xfail), # passing over North Pole
@pytest.mark.skip
@pytest.mark.parametrize("init,command,expected", testcases_planet)
def test_rover_turn_on_pole_4_4(init, command, expected):
    rover = Rover(init, Planet(4,4))
    rover.execute(command)
    assert rover.position() == expected


                      
testcases_planet_8 = [
            
             ]
new_tests_8 = [(RS(0,7,"N"), "f", RS(4,6,"S")),(RS(0,6,"N"), "ff", RS(4,6,"S"))]

new_tests_8 = [pytest.param(*t,marks=pytest.mark.xfail) for t in new_tests]

testcases_planet_8.extend(new_tests_8)       
 # pytest.param(
   #     RS(1,0,"S"), "f", RS(11,1,"N"),
   #     marks=pytest.mark.xfail), # passing over North Pole
@pytest.mark.skip
@pytest.mark.parametrize("init,command,expected", testcases_planet)
def test_rover_turn_on_pole_8_8(init, command, expected):
    rover = Rover(init, Planet(8,8))
    rover.execute(command)
    assert rover.position() == expected