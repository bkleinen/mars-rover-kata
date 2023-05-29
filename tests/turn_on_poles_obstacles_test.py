import pytest
from lib.rover import Rover
from lib.planet import Planet
from lib.rover_state import RS, ObstacleEncountered, Position as P


planet_string = """
....
...o
.o..
....
"""


testcases_planet = [
    (RS(1,2,"N"), "ff", RS(1,3,"N")), # stops in front of obstacle
    (RS(3,1,"S"), "ff", RS(3,0,"S")),
    (RS(2,1,"S"), "frf", RS(2,0,"W")),
    (RS(0,1,"S"), "flf", RS(0,0,"E")),             
]

@pytest.mark.parametrize("init,command,expected", testcases_planet)
def test_rover_turn_on_pole_4_4_obstacles_invalid(init, command, expected):
    planet = Planet.from_str(planet_string)
    rover = Rover(init, planet)
    with pytest.raises(ObstacleEncountered):
        rover.execute(command)
    assert rover.position() == expected

planet_string = """
oooo
....
....
..o.
"""

# its possible to build a semi-permeable pole now:

testcases_planet = [
    (RS(3,1,"S"), "ff", RS(3,0,"S")),
    (RS(0,1,"S"), "flf", RS(0,0,"E")),             
]

@pytest.mark.parametrize("init,command,expected", testcases_planet)
def test_rover_turn_on_pole_4_4_obstacles_invalid(init, command, expected):
    planet = Planet.from_str(planet_string)
    rover = Rover(init, planet)
    rover.execute(command)
    assert rover.position() == expected


testcases_planet = [
    (RS(1,2,"N"), "f", RS(1,2,"N")), # stops in front of obstacle
    (RS(2,1,"S"), "frf", RS(2,1,"S")),
   ]

@pytest.mark.parametrize("init,command,expected", testcases_planet)
def test_rover_turn_on_pole_4_4_obstacles_invalid(init, command, expected):
    planet = Planet.from_str(planet_string)
    rover = Rover(init, planet)
    with pytest.raises(ObstacleEncountered):
        rover.execute(command)
    assert rover.position() == expected


# thus, the planet should look like this if an 
# obstacle is set to the pole:
planet_string = """
oooo
..o.
.o..
oooo
"""

def test_obstacle_covers_pole():
    planet = Planet(4,4)
    planet.add_obstacle(0,0)
    planet.add_obstacle(1,1)
    planet.add_obstacle(2,2)
    planet.add_obstacle(3,3)
    assert str(planet) == planet_string




