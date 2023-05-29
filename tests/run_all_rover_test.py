import pytest
from lib.planet import Planet
from lib.rover import Rover
from tests.rover_simple_movement_testcases import testcases as simple_tc

testcases = []
testcases.extend(simple_tc)


def pytest_testcase(rtc):
    testtuple = (rtc.note, rtc.dimension, rtc.init, rtc.command, rtc.expected)
    if rtc.xfail:
        return pytest.param(*testtuple,marks=pytest.mark.xfail) 
    else:
        return testtuple

testcases = [pytest_testcase(testcase) for testcase in testcases]

@pytest.mark.parametrize("note,dimension,init,command,expected", testcases)
def test_rover_move_on_planet(note,dimension, init, command, expected):
    rover = Rover(init, Planet(dimension,dimension))
    rover.execute(command)
    assert rover.position() == expected