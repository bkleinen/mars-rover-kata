import pytest
from mars_rover import Planet, RS, Rover
from tests.rover_test_case import RoverTestCase as T


def test_planet_width_must_be_multiple_of_four():
    with pytest.raises(AttributeError):
        rover = Rover(RS(1, 0, "S"), Planet(10, 10))


testcases = [
   # T(Planet,12, RS(0, 0, "S"), "rf", RS(9,1,"N"),'turn on pole'),
    T(Planet, 4, RS(0, 2, "N"), "ff", RS(2, 2, "S")),
    T(Planet, 4, RS(0, 3, "N"), "f", RS(2, 2, "S")),
    T(Planet, 4, RS(0, 3, "N"), "rf", RS(1, 2, "S")),
    T(Planet, 4, RS(0, 3, "N"), "lf", RS(3, 2, "S")),
    T(Planet, 4, RS(1, 3, "N"), "llf", RS(1, 2, "S")),

    T(Planet, 4, RS(1, 3, "N"), "rrf",  RS(1, 2, "S")),
    T(Planet, 4, RS(1, 3, "N"), "rrff",  RS(1, 1, "S")),

    T(Planet, 4, RS(0, 3, "N"), "f", RS(2, 2, "S")),
    # on pole, with direction S -> two turns were there!
    T(Planet, 4, RS(0, 3, "S"), "f",  RS(0, 2, "S")),

    T(Planet, 4, RS(1, 2, "S"), "f",  RS(1, 1, "S")),
    # this is on north pole and fails
    T(Planet, 4, RS(1, 3, "S"), "ff", RS(1, 1, "S")),
    T(Planet, 4, RS(0, 0, "S"), "f",  RS(2, 1, "N")),
    T(Planet, 4, RS(1, 2, "N"), "frf", RS(2, 2, "S")),

    T(Planet, 4, RS(1, 1, "S"), "frf", RS(0, 1, "N")),
    T(Planet, 4, RS(2, 1, "N"),    "fflff", RS(1, 1, "S")),
    T(Planet, 4, RS(1, 1, "S"), "frfffrff", RS(1, 1, "S")),

    T(Planet, 8, RS(0, 7, "N"), "f", RS(4, 6, "S")),
    T(Planet, 8, RS(0, 6, "N"), "ff", RS(4, 6, "S")),
    T(Planet, 8, RS(0, 7, "N"), "rf", RS(2, 6, "S")),
    T(Planet, 8, RS(0, 7, "N"), "rrf", RS(0, 6, "S")),
    T(Planet, 8, RS(0, 7, "N"), "lf", RS(6, 6, "S")),
    T(Planet, 8, RS(0, 6, "N"), "frrf", RS(0, 6, "S")),

]
