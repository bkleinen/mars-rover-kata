import pytest
from mars_rover import Rover
from tests.helper import backward_testcase
from tests.rover_in_flat_world_test import testcases as rover_in_flat_world_test
from tests.rover_on_planet_testcases import testcases as rover_on_planet_testcases
from tests.turn_on_poles_step_test import testcases as turn_on_poles_step_test
from tests.turn_on_poles_test import testcases as turn_on_poles_test
from tests.pole_loops_testcases import testcases as pole_loops_testcases

testcases = {}
testcases['rover_in_flat_world_test'] = rover_in_flat_world_test
testcases['rover_on_planet_testcases'] = rover_on_planet_testcases
testcases['turn_on_poles_test'] = turn_on_poles_test
testcases['turn_on_poles_step_test'] = turn_on_poles_step_test


backward_testcases = [backward_testcase(tc) for tc in rover_in_flat_world_test]
testcases['rover_in_flat_world_test'+'_backward'] = backward_testcases


backward_testcases = [backward_testcase(tc) for tc in rover_on_planet_testcases]
#backward_testcases = [dataclasses.replace(tc,xfail=True) for tc in backward_testcases]
testcases['rover_on_planet_testcases'+'_backward'] = backward_testcases

backward_testcases = [backward_testcase(tc) for tc in turn_on_poles_step_test]
#backward_testcases = [dataclasses.replace(tc,xfail=True) for tc in backward_testcases]
testcases['turn_on_poles_step_test'+'_backward'] = backward_testcases

backward_testcases = [backward_testcase(tc) for tc in turn_on_poles_test]
# backward_testcases = [dataclasses.replace(tc,xfail=True) for tc in backward_testcases]
testcases['turn_on_poles_test'+'_backward'] = backward_testcases


backward_testcases = [backward_testcase(tc) for tc in pole_loops_testcases]
# backward_testcases = [dataclasses.replace(tc,xfail=True) for tc in backward_testcases]
testcases['pole_loops_testcases'] = pole_loops_testcases
testcases['pole_loops_testcases'+'_backward'] = backward_testcases


def pytest_testcase(rtc, filename):
    filename_marked = f"file:{filename}.py"
    testcase_note = filename_marked if (rtc.note is None or rtc.note == "") else f"{filename_marked}-{rtc.note}"
    testtuple = (testcase_note, rtc.world, rtc.dimension, rtc.init, rtc.command, rtc.expected)
    if rtc.xfail:
        return pytest.param(*testtuple,marks=pytest.mark.xfail) 
    else:
        return testtuple
    
testcases_list = [pytest_testcase(testcase, filename) for filename in testcases.keys() for testcase in testcases[filename]]

@pytest.mark.parametrize("note,world,dimension,init,command,expected", testcases_list)
def test_rover(note, world, dimension, init, command, expected):
    rover = Rover(init, world(dimension,dimension))
    rover.execute(command)
    assert rover.position() == expected