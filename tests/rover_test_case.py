from mars_rover.rover_state import RS, RoverState
from dataclasses import dataclass
from mars_rover.world import World
from mars_rover.planet import Planet

@dataclass
class RoverTestCase:
    world: type 
    dimension: int
    init: RoverState
    command: str
    expected: RoverState
    note: str = ""
    xfail: bool = False

