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
    old_rectangle = rectangle

    bl = Node(Vector(0, 0))
    tl = Node(Vector(0, 2))
    br = Node(Vector(1, 0))
    tr = Node(Vector(1, 2))
    rectangle = Rectangle([tl, bl, tr, br])
    fail_if(not rectangle.is_vertical)
    fail_if(rectangle.is_horizontal)
    fail_if(rectangle.is_square)
    fail_if(rectangle.width != 1)
    fail_if(rectangle.height != 2)

    bl = Node(Vector(0, 0))
    tl = Node(Vector(0, 1))
    br = Node(Vector(2, 0))
    tr = Node(Vector(2, 1))
    rectangle = Rectangle([tl, bl, tr, br])
    fail_if(rectangle.is_vertical)
    fail_if(not rectangle.is_horizontal)
    fail_if(rectangle.is_square)
    fail_if(rectangle.width != 2)
    fail_if(rectangle.height != 1)

    fail_if(rectangle != rectangle)
    fail_if(old_rectangle == rectangle)


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
