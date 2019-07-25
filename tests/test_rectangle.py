import pytest
from python_shape_grammars.floor_plan_elements import Rectangle, Node
from python_shape_grammars.vector import Vector


def fail_if(boolean):
    if boolean:
        pytest.fail()


def test_rectangle():
    bl = Node(Vector(0, 0))
    tl = Node(Vector(0, 1))
    br = Node(Vector(1, 0))
    tr = Node(Vector(1, 1))

    rectangle = Rectangle([tl, bl, tr, br])

    print(rectangle)
    fail_if(rectangle.NE != tr)
    fail_if(rectangle.SE != br)
    fail_if(rectangle.SW != bl)
    fail_if(rectangle.NW != tl)

    fail_if(rectangle.width != 1)
    fail_if(rectangle.height != 1)

    fail_if(rectangle.is_vertical)
    fail_if(rectangle.is_horizontal)
    fail_if(not rectangle.is_square)

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
