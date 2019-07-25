import math

import pytest

from python_shape_grammars.floor_plan_elements import Node, Edge, RoomNode, \
    CornerNode, WallNode, Rectangle, Window, Door, Staircase
from python_shape_grammars.components import EdgeType, EdgeDirection, RoomType
from python_shape_grammars.vector import Vector


def fail_if(boolean):
    if boolean:
        pytest.fail()


def test_vector():
    vector = Vector(0, 0)
    fail_if(vector.x != 0)
    fail_if(vector.y != 0)
    fail_if(vector != Vector(0, 0))

    fail_if(vector.left_of(Vector(-1, 0)) != 0)
    fail_if(vector.left_of(Vector(1, 0)) != 1)
    fail_if(vector.left_of(Vector(0, 1)) != -1)
    try:
        vector.left_of((0, 0))
        pytest.fail()
    except ValueError:
        pass
    try:
        vector.right_of((0, 0))
        pytest.fail()
    except ValueError:
        pass
    try:
        vector.above((0, 0))
        pytest.fail()
    except ValueError:
        pass
    try:
        vector.beneath((0, 0))
        pytest.fail()
    except ValueError:
        pass

    fail_if(vector.right_of(Vector(-1, 0)) != 1)
    fail_if(vector.right_of(Vector(1, 0)) != 0)
    fail_if(vector.right_of(Vector(0, -1)) != -1)

    fail_if(vector.beneath(Vector(0, 1)) != 1)
    fail_if(vector.beneath(Vector(0, -1)) != 0)
    fail_if(vector.beneath(Vector(1, 0)) != -1)

    fail_if(vector.above(Vector(0, 1)) != 0)
    fail_if(vector.above(Vector(0, -1)) != 1)
    fail_if(vector.above(Vector(-1, 0)) != -1)

    vector2 = Vector(1, 1)
    fail_if(vector.distance_to(vector2) != math.sqrt(2))
    try:
        vector.distance_to((0, 0))
        pytest.fail()
    except ValueError:
        pass

    lc = vector.linear_combination(vector2, 2)
    fail_if(lc != Vector(2, 2))

    lc = vector2.linear_combination(vector2, 2, 3)
    fail_if(lc != Vector(5, 5))
    try:
        vector.linear_combination((0, 0), 1)
        pytest.fail()
    except ValueError:
        pass

    fail_if(vector2 + vector2 != Vector(2, 2))
    fail_if(vector2 + vector2 == Vector(3, 2))
    try:
        vector2 + (0, 0)
        pytest.fail()
    except ValueError:
        pass
