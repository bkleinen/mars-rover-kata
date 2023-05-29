import dataclasses
from mars_rover.rover_state import RS

def backward_testcase(rover_test_case):
    rtc = rover_test_case

    init = rover_test_case.init
    reverse = {'N': 'S','S': 'N', 'W':'E', 'E':'W'}
    flipped_init = RS(init.pos.x, init.pos.y, reverse[init.direction])

    command = rover_test_case.command
    flipped_command = command.replace('f','B').replace('b','f').replace('B','b')
    expected = rover_test_case.expected
    flipped_expect = dataclasses.replace(expected, direction=reverse[expected.direction])
    return dataclasses.replace(rover_test_case, init=flipped_init, command=flipped_command, expected = flipped_expect)
   