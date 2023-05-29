import pytest
from lib.planet import Planet
from lib.rover import Rover
from tests.example_testcases import testcases as example_testcases
from tests.rover_in_flat_world_test import testcases as rover_in_flat_world_test
from tests.rover_on_planet_test import testcases as rover_on_planet_test

testcases = {}
testcases['example_testcases'] = example_testcases
testcases['rover_in_flat_world_test'] = rover_in_flat_world_test
testcases['rover_on_planet_test'] = rover_on_planet_test


def pytest_testcase(rtc, filename):
    filename_marked = f"file:{filename}.py"
    testcase_note = filename_marked if (rtc.note is None or rtc.note == "") else f"{filename_marked}-{rtc.note}"
    testtuple = (testcase_note, rtc.world, rtc.dimension, rtc.init, rtc.command, rtc.expected)
    if rtc.xfail:
        return pytest.param(*testtuple,marks=pytest.mark.xfail) 
    else:
        return testtuple
# [(key, value_item) for key in a_map.keys() for value_item in a_map[key]]
testcases = [pytest_testcase(testcase, filename) for filename in testcases.keys() for testcase in testcases[filename]]

@pytest.mark.parametrize("note,world,dimension,init,command,expected", testcases)
def test_rover(note, world, dimension, init, command, expected):
    rover = Rover(init, world(dimension,dimension))
    rover.execute(command)
    assert rover.position() == expected