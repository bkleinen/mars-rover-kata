
from dataclasses import dataclass
from mars_rover import RoverState

@dataclass
class RoverTestCase:
    world: type 
    dimension: int
    init: RoverState
    command: str
    expected: RoverState
    note: str = ""
    xfail: bool = False

