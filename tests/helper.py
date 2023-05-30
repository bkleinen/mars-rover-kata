import dataclasses
from mars_rover import RS, Orientation as Rose

def backward_testcase(rover_test_case):
    rtc = rover_test_case

    init = rover_test_case.init
    reverse = {'N': 'S','S': 'N', 'W':'E', 'E':'W'}

    reverse = {Rose.N: Rose.S, Rose.S: Rose.N, Rose.W: Rose.E, Rose.E: Rose.W}
    flipped_init = RS(init.pos.x, init.pos.y, init.orientation.reverse().name)

    command = rover_test_case.command
    flipped_command = command.replace('f','B').replace('b','f').replace('B','b')
    expected = rover_test_case.expected
    flipped_expect = dataclasses.replace(expected, orientation=expected.orientation.reverse())
    return dataclasses.replace(rover_test_case, init=flipped_init, command=flipped_command, expected = flipped_expect)
   