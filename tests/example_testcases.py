from mars_rover.rover_state import RS, RoverState
from dataclasses import dataclass
from mars_rover.planet import Planet
from mars_rover.world import World

from tests.rover_test_case import RoverTestCase as T

testcases = [
    T(Planet,12,RS(1,1,"N"), "f", RS(1,2,"N"), ),
    T(World,12,RS(1,11,"N"), "f", RS(1,0,"N"), xfail=False),
             ]
