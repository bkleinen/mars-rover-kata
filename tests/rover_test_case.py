from lib.base import RS, RoverState
from dataclasses import dataclass
from lib.world import World
from lib.planet import Planet

@dataclass
class RoverTestCase:
    world: type 
    dimension: int
    init: RoverState
    command: str
    expected: RoverState
    note: str = ""
    xfail: bool = False

