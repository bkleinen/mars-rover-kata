import pytest
from lib.planet import Planet
from lib.rover import Rover
from tests.example_testcases import testcases as example_tc
from tests.rover_in_flat_world_test import testcases as flat_world_tc
testcases = []

testcases.extend(example_tc)
testcases.extend(flat_world_tc)


def pytest_testcase(rtc):
    testtuple = (rtc.note, rtc.world, rtc.dimension, rtc.init, rtc.command, rtc.expected)
    if rtc.xfail:
        return pytest.param(*testtuple,marks=pytest.mark.xfail) 
    else:
        return testtuple

testcases = [pytest_testcase(testcase) for testcase in testcases]

@pytest.mark.parametrize("note,world,dimension,init,command,expected", testcases)
def test_rover_move_on_planet(note, world, dimension, init, command, expected):
    rover = Rover(init, world(dimension,dimension))
    rover.execute(command)
    assert rover.position() == expected