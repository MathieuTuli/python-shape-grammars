import pytest
from python_shape_grammars.floor_plan_elements import Rectangle, Node, Window, \
    Door, Staircase
from python_shape_grammars.vector import Vector


def fail_if(boolean):
    if boolean:
        pytest.fail()


def test_rectangle():
    bl = Node(Vector(0, 0))
    tl = Node(Vector(0, 1))
    br = Node(Vector(1, 0))
    tr = Node(Vector(1, 1))

    try:
        Rectangle([bl, tl])
        pytest.fail()
    except ValueError:
        pass
    try:
        Rectangle([bl, tl, tr, 0])
        pytest.fail()
    except ValueError:
        pass
    try:
        Rectangle([bl, tl, tr, tl])
        pytest.fail()
    except ValueError:
        pass
    rectangle = Rectangle([tl, bl, tr, br])

    fail_if(rectangle.NE != tr)
    fail_if(rectangle.SE != br)
    fail_if(rectangle.SW != bl)
    fail_if(rectangle.NW != tl)
    fail_if(rectangle.NE.vector.x != rectangle.SE.vector.x or
            rectangle.NW.vector.x != rectangle.SW.vector.x or
            rectangle.NE.vector.y != rectangle.NW.vector.y or
            rectangle.SE.vector.y != rectangle.SW.vector.y)

    fail_if(rectangle.width != 1)
    fail_if(rectangle.height != 1)

    fail_if(rectangle.is_vertical)
    fail_if(rectangle.is_horizontal)
    fail_if(not rectangle.is_square)

    bl = Node(Vector(0, 0))
    tl = Node(Vector(0, 2))
    br = Node(Vector(1, 0))
    tr = Node(Vector(1, 2))
    rectangle2 = Rectangle([tl, bl, tr, br])
    fail_if(not rectangle2.is_vertical)
    fail_if(rectangle2.is_horizontal)
    fail_if(rectangle2.is_square)
    fail_if(rectangle2.width != 1)
    fail_if(rectangle2.height != 2)

    bl = Node(Vector(0, 0))
    tl = Node(Vector(0, 1))
    br = Node(Vector(2, 0))
    tr = Node(Vector(2, 1))
    rectangle3 = Rectangle([tl, bl, tr, br])
    fail_if(rectangle3.is_vertical)
    fail_if(not rectangle3.is_horizontal)
    fail_if(rectangle3.is_square)
    fail_if(rectangle3.width != 2)
    fail_if(rectangle3.height != 1)

    fail_if(rectangle != rectangle)
    fail_if(rectangle == rectangle3)

    # check overlap
    bl = Node(Vector(0, 0))
    tl = Node(Vector(0, 10))
    br = Node(Vector(10, 0))
    tr = Node(Vector(10, 10))
    rectangle = Rectangle([tl, bl, tr, br])
    bl = Node(Vector(5, 5))
    tl = Node(Vector(5, 15))
    br = Node(Vector(15, 5))
    tr = Node(Vector(15, 15))
    rectangle2 = Rectangle([tl, bl, tr, br])
    bl = Node(Vector(-5, -5))
    tl = Node(Vector(-5, 5))
    br = Node(Vector(5, -5))
    tr = Node(Vector(5, 5))
    rectangle3 = Rectangle([tl, bl, tr, br])
    bl = Node(Vector(5, 5))
    tl = Node(Vector(5, 15))
    br = Node(Vector(15, 5))
    tr = Node(Vector(15, 15))
    rectangle4 = Rectangle([tl, bl, tr, br])
    bl = Node(Vector(5, -5))
    tl = Node(Vector(5, 1))
    br = Node(Vector(10, -5))
    tr = Node(Vector(10, 1))
    rectangle5 = Rectangle([tl, bl, tr, br])
    bl = Node(Vector(100, 100))
    tl = Node(Vector(100, 110))
    br = Node(Vector(110, 100))
    tr = Node(Vector(110, 110))
    rectangle6 = Rectangle([tl, bl, tr, br])

    fail_if(not rectangle.overlap_with(rectangle))
    fail_if(not rectangle.overlap_with(rectangle2))
    fail_if(not rectangle.overlap_with(rectangle3))
    fail_if(not rectangle.overlap_with(rectangle4))
    fail_if(not rectangle.overlap_with(rectangle5))
    fail_if(rectangle.overlap_with(rectangle6))


def test_window():
    bl = Node(Vector(0.0, 0.0))
    tl = Node(Vector(0.0, 1.0))
    br = Node(Vector(1.0, 0.0))
    tr = Node(Vector(1.0, 1.0))
    window = Window([bl, tl, br, tr])
    fail_if(str(window) != "Window defined by"
            + f" [NE: (1.0, 1.0)"
            + f", SE: (1.0, 0.0)"
            + f", SW: (0.0, 0.0)"
            + f", NW: (0.0, 1.0)]")


def test_door():
    bl = Node(Vector(0.0, 0.0))
    tl = Node(Vector(0.0, 1.0))
    br = Node(Vector(1.0, 0.0))
    tr = Node(Vector(1.0, 1.0))
    door = Door([bl, tl, br, tr])
    fail_if(str(door) != "Door defined by"
            + f" [NE: (1.0, 1.0)"
            + f", SE: (1.0, 0.0)"
            + f", SW: (0.0, 0.0)"
            + f", NW: (0.0, 1.0)]")


def test_staircase():
    bl = Node(Vector(0.0, 0.0))
    tl = Node(Vector(0.0, 1.0))
    br = Node(Vector(1.0, 0.0))
    tr = Node(Vector(1.0, 1.0))
    stairs = Staircase([bl, tl, br, tr])
    fail_if(str(stairs) != "Staircase defined by"
            + f" [NE: (1.0, 1.0)"
            + f", SE: (1.0, 0.0)"
            + f", SW: (0.0, 0.0)"
            + f", NW: (0.0, 1.0)]")
