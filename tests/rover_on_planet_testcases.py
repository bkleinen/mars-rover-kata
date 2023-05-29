import pytest
from lib.rover import Rover, World
from lib.base import RS
from lib.planet import Planet
from tests.rover_test_case import RoverTestCase as T

testcases = [
    T(Planet,12,RS(1,1,"N"), "f", RS(1,2,"N")),
    T(Planet,12,RS(2,2,"N"), "b", RS(2,1,"N")),
    T(Planet,12,RS(5,5,"N"), "f", RS(5,6,"N")),
    T(Planet,12,RS(1,1,"N"), "r", RS(1,1,"E")),
    T(Planet,12,RS(1,2,"E"), "r", RS(1,2,"S")),
    T(Planet,12,RS(1,3,"S"), "r", RS(1,3,"W")),
    T(Planet,12,RS(1,4,"W"), "r", RS(1,4,"N")),
    T(Planet,12,RS(2,2,"N"), "l", RS(2,2,"W")),
    T(Planet,12,RS(3,3,"N"), "rr", RS(3,3,"S")),
    T(Planet,12,RS(3,3,"N"), "ffr", RS(3,5,"E")),
    T(Planet,12,RS(3,3,"N"), "rf", RS(4,3,"E")),
    T(Planet,12,RS(3,3,"N"), "ffrfflf", RS(5,6,"N")),

    T(Planet,12,RS(1,10,"N"), "f", RS(1,11,"N")),
    T(Planet,12,RS(1,11,"N"), "f", RS(7,10,"S")),
    T(Planet,12,RS(4,11,"N"), "f", RS(10,10,"S")),
    T(Planet,12,RS(6,10,"N"), "ff", RS(0,10,"S")),
    T(Planet,12,RS(0,10,"N"), "ff", RS(6,10,"S")),
    T(Planet,12,RS(1,1,"S"), "f", RS(1,0,"S")),
    T(Planet,12,RS(1,0,"S"), "f", RS(7,1,"N")),
    T(Planet,12,RS(2,0,"S"), "f", RS(8,1,"N")),
    T(Planet,12,RS(11,0,"S"), "f", RS(5,1,"N")),
     
             ]
