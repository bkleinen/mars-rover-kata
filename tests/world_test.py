import pytest
from mars_rover import Rover, World, RS, ObstacleEncountered

def test_world_to_str_1():
    world = World(10, 1)
    world_rep = """
..........
"""
    assert str(world) == world_rep

def test_world_to_str_10():
    world = World(10, 10)
    world_rep = """
..........
..........
..........
..........
..........
..........
..........
..........
..........
..........
"""
    assert str(world) == world_rep

def test_world_to_str_5():
    world = World(10, 5)
    world_rep = """
..........
..........
..........
..........
..........
"""
    assert str(world) == world_rep

def test_world_to_str_5_obstacle_1():
    world = World(10, 5)
    world.add_obstacle(0,0)
    world_rep = """
..........
..........
..........
..........
o.........
"""
    assert str(world) == world_rep

def test_world_to_str_5_obstacle_2():
    world = World(10, 5)
    world.add_obstacle(0,0)
    world.add_obstacle(1,3)
    world_rep = """
..........
.o........
..........
..........
o.........
"""
    assert str(world) == world_rep


def test_world_to_str_5_obstacle_3():
    world = World(10, 5)
    world.add_obstacle(0,0)
    world.add_obstacle(1,3)
    world.add_obstacle(4,4)
    world_rep = """
....o.....
.o........
..........
..........
o.........
"""
    assert str(world) == world_rep

def test_world_from_str_1():
    world_rep = """
o.........
"""
    world = World.from_str(world_rep)
    assert str(world) == world_rep


def test_world_from_str_2():
    world_rep = """
....o.....
.o........
..........
..........
o.........
"""
    world = World.from_str(world_rep)
    assert str(world) == world_rep

def test_rover_obstacles_1():
    world_rep = """
....o.....
.o........
..........
..........
....o.....
"""
    world = World.from_str(world_rep)
    assert str(world) == world_rep
    rover = Rover(RS(2,0,'N'), world)
    with pytest.raises(ObstacleEncountered):
        rover.execute('rffffff')
    assert RS(3,0,'E') == rover.position()


def test_rover_obstacles_2():
    world_rep = """
....o.....
.o........
..........
..........
....o.....
"""
    world = World.from_str(world_rep)
    assert str(world) == world_rep
    rover = Rover(RS(1,0,'N'), world)
    with pytest.raises(ObstacleEncountered):
        rover.execute('ffff')
    assert RS(1,2,'N') == rover.position()


def test_rover_obstacles_more():
    world_rep = """
....o.....
.o........
..........
..........
....o.....
"""
    world = World.from_str(world_rep)
    assert str(world) == world_rep
    rover = Rover(RS(1,0,'N'), world)
    with pytest.raises(ObstacleEncountered):
        rover.execute('ffffrffff')
    assert RS(1,2,'N') == rover.position()