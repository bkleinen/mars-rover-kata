from lib.rover import Position as P

def test_position_equals():
    p1 = P(4,3)
    p2 = P(4,3)
    assert p1 == p2

def test_position_unequal():
    p1 = P(4,3)
    p2 = P(4,4)
    assert p1 != p2

def test_position_add():
    p1 = P(4,3)
    p2 = P(4,4)
    pos = p1 + p2
    assert P(8,7) == pos

def test_position_delta():
    p1 = P(4,3)
    delta = P(-1,0)
    pos = p1 + delta
    assert P(3,3) == pos