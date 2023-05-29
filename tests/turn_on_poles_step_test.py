import pytest
from lib.rover import Rover
from lib.planet import Planet
from lib.base import RS
from tests.rover_test_case import RoverTestCase as T

# assert RS(0,2,'N') == RS(2,2,'N')
# assert RS(1,2,'N') == RS(3,2,'N')
# assert RS(2,2,'N') == RS(0,2,'N')
# assert RS(3,2,'N') == RS(1,2,'N')
# assert RS(0,1,'S') == RS(2,1,'S')
# assert RS(1,1,'S') == RS(3,1,'S')
# assert RS(2,1,'S') == RS(0,1,'S')
# assert RS(3,1,'S') == RS(1,1,'S')
testcases = [
    T(Planet,4,RS(0,2,'N'), 'ff', RS(2,2,'S')),  # RS(0,2,'N') == RS(2,2,'N')
    T(Planet,4,RS(1,2,'N'), 'ff', RS(3,2,'S')),  # RS(1,2,'N') == RS(3,2,'N')
    T(Planet,4,RS(2,2,'N'), 'ff', RS(0,2,'S')),  # RS(2,2,'N') == RS(0,2,'N')
    T(Planet,4,RS(3,2,'N'), 'ff', RS(1,2,'S')),  # RS(3,2,'N') == RS(1,2,'N')

  #  T(Planet,4,RS(0,2,'S'), 'b', RS(0,3,'S')),
  #  T(Planet,4,RS(0,3,'S'), 'b', RS(2,2,'N'), 'moving backwards over pole',xfail=True),
  #  T(Planet,4,RS(1,2,'S'), 'bb', RS(3,2,'S'),'moving backwards over pole',xfail=True),
  #  T(Planet,4,RS(2,2,'S'), 'bb', RS(0,2,'S'),'moving backwards over pole',xfail=True),
  #  T(Planet,4,RS(3,2,'S'), 'bb', RS(1,2,'S'),'moving backwards over pole',xfail=True),

    T(Planet,4,RS(0,2,'N'), 'frf', RS(1,2,'S')),
    T(Planet,4,RS(1,2,'N'), 'frf', RS(2,2,'S')),
    T(Planet,4,RS(2,2,'N'), 'frf', RS(3,2,'S')),
    T(Planet,4,RS(3,2,'N'), 'frf', RS(0,2,'S')),

    T(Planet,4,RS(0,2,'N'), 'flf', RS(3,2,'S')),
    T(Planet,4,RS(1,2,'N'), 'flf', RS(0,2,'S')),
    T(Planet,4,RS(2,2,'N'), 'flf', RS(1,2,'S')),
    T(Planet,4,RS(3,2,'N'), 'flf', RS(2,2,'S')),

   
    T(Planet,4,RS(0,1,'S'), 'ff', RS(2,1,'N')),
    T(Planet,4,RS(1,1,'S'), 'ff', RS(3,1,'N')),
    T(Planet,4,RS(2,1,'S'), 'ff', RS(0,1,'N')),
    T(Planet,4,RS(3,1,'S'), 'ff', RS(1,1,'N')),

    T(Planet,4,RS(0,1,'S'), 'f', RS(0,0,'S')), # step1
    T(Planet,4,RS(0,0,'S'), 'r', RS(0,0,'W')), # step2
    T(Planet,4,RS(0,0,'W'), 'f', RS(3,1,'N')), # step3 of the next:

    T(Planet,4,RS(0,1,'S'), 'frf', RS(3,1,'N')),
    T(Planet,4,RS(1,1,'S'), 'frf', RS(0,1,'N')),
    T(Planet,4,RS(2,1,'S'), 'frf', RS(1,1,'N')),
    T(Planet,4,RS(3,1,'S'), 'frf', RS(2,1,'N')),

    T(Planet,4,RS(0,1,'S'), 'flf', RS(1,1,'N')),
    T(Planet,4,RS(1,1,'S'), 'flf', RS(2,1,'N')),
    T(Planet,4,RS(2,1,'S'), 'flf', RS(3,1,'N')),
    T(Planet,4,RS(3,1,'S'), 'flf', RS(0,1,'N')),
                    
]
      


