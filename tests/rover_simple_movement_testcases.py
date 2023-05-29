from lib.base import RS, RoverState
from dataclasses import dataclass

@dataclass
class RoverTestCase:
    dimension: int
    init: RoverState
    command: str
    expected: RoverState
    note: str = "RoverTestCase"
    xfail: bool = False

T = RoverTestCase

testcases = [
    T(12,RS(1,1,"N"), "f", RS(1,2,"N")),
    T(12,RS(2,2,"N"), "b", RS(2,1,"N")),
    T(12,RS(5,5,"N"), "f", RS(5,6,"N")),
    T(12,RS(1,1,"N"), "r", RS(1,1,"E")),
    T(12,RS(1,2,"E"), "r", RS(1,2,"S")),
    T(12,RS(1,3,"S"), "r", RS(1,3,"W")),
    T(12,RS(1,4,"W"), "r", RS(1,4,"N")),
    T(12,RS(2,2,"N"), "l", RS(2,2,"W")),
    T(12,RS(3,3,"N"), "rr", RS(3,3,"S")),
    T(12,RS(3,3,"N"), "ffr", RS(3,5,"E")),
    T(12,RS(3,3,"N"), "rf", RS(4,3,"E")),
    T(12,RS(3,3,"N"), "ffrfflf", RS(5,6,"N")),
    T(12,RS(1,11,"N"), "f", RS(1,2,"N"), xfail=True),
             ]

testcases2 = [
    T(12,RS(1,1,"N"), "f", RS(1,2,"N"))
]