import pytest
from lib.rover import Rover
from lib.planet import Planet
from lib.base import RS

planet_string = """
....
...o
....
....
"""

testcases_planet = [
    (RS(0,2,"N"), "ff", RS(2,2,"S")),
  # (RS(1,2,"N"), "ff", RS(3,2,"S")),
   # (RS(2,2,"N"), "ff", RS(0,3,"S")), # stops in front of obstacle
  # (RS(3,2,"N"), "ff", RS(1,2,"S")),

  # (RS(0,2,"N"), "frf", RS(1,2,"S")),
  # (RS(1,2,"N"), "frf", RS(2,2,"S")),
  # (RS(2,2,"N"), "frf", RS(3,2,"S")),
  # (RS(3,2,"N"), "frf", RS(0,2,"S")),

  # (RS(0,2,"N"), "flf", RS(3,2,"S")),
  # (RS(1,2,"N"), "flf", RS(0,2,"S")),
  # (RS(2,2,"N"), "flf", RS(1,2,"S")),
  # (RS(3,2,"N"), "flf", RS(2,2,"S")),

  #
  # (RS(0,1,"S"), "ff", RS(2,1,"N")),
  # (RS(1,1,"S"), "ff", RS(3,1,"N")),
  # (RS(2,1,"S"), "ff", RS(0,1,"N")),
  # (RS(3,1,"S"), "ff", RS(1,1,"N")),

  # (RS(0,1,"S"), "frf", RS(3,1,"N")),
  # (RS(1,1,"S"), "frf", RS(0,1,"N")),
  # (RS(2,1,"S"), "frf", RS(1,1,"N")),
  # (RS(3,1,"S"), "frf", RS(2,1,"N")),

    (RS(0,1,"S"), "flf", RS(1,1,"N")),
    (RS(1,1,"S"), "flf", RS(2,1,"N")),
    (RS(2,1,"S"), "flf", RS(3,1,"N")),
    (RS(3,1,"S"), "flf", RS(0,1,"N")),
                    
]
      
@pytest.mark.parametrize("init,command,expected", testcases_planet)
def test_rover_turn_on_pole_4_4(init, command, expected):
    planet = Planet.from_str(planet_string)
    assert str(type(planet)) == "<class 'lib.planet.Planet'>"
    rover = Rover(init, planet)
    
    rover.execute(command)
    assert rover.position() == expected

