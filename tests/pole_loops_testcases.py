import pytest
from mars_rover import Planet, RS
from tests.rover_test_case import RoverTestCase as T


testcases = [
    T(Planet,4,RS(0,2,"N"), "frfrfr", RS(0,2,"N")),
    T(Planet,4,RS(0,1,"S"), "frfrfr", RS(0,1,"S")),
   # T(Planet,4,RS(1,1,"S"), "frfffrff", RS(1,1,"S")),
          
]
      


