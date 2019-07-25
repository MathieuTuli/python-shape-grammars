import pytest

from python_shape_grammars.vector import Vector
from python_shape_grammars.line import Line


def fail_if(boolean):
    if boolean:
        pytest.fail()


def test_line():
    vector = Vector(0, 0)
    vector2 = Vector(2, 2)
    vector3 = Vector(0, 1)
    line = Line(vector, vector2, 2)
    line2 = Line(vector, vector3, 2)

    fail_if(line.midpoint != Vector(1, 1))
    fail_if(line.midpoint != vector.linear_combination(vector2, 0.5))
    fail_if(line.left_vector != vector)
    fail_if(line.right_vector != vector2)
    fail_if(line.upper_vector != vector2)
    fail_if(line.bottom_vector != vector)
    fail_if(line.is_horizontal)
    fail_if(line.is_vertical)
    fail_if(line.m != 1.0)
    fail_if(line.b != 0.0)
    fail_if(abs(line2) != 1.0)

    fail_if(line2.left_vector is not None)
    fail_if(line2.right_vector is not None)
    fail_if(line2.upper_vector != vector3)
    fail_if(line2.bottom_vector != vector)
    fail_if(line2.is_horizontal)
    fail_if(not line2.is_vertical)
    fail_if(line2.m != float('Inf'))
    fail_if(line2.b != float('Inf'))

    fail_if(not line.contains(vector, 0))
    fail_if(not line.contains(vector, 10))

    fail_if(not line.is_on_midpoint(Vector(1, 1), 0))
    fail_if(not line.is_on_midpoint(Vector(1, 1), 10))
    fail_if(line.is_on_midpoint(Vector(1, 2), 0))
    fail_if(not line.is_on_midpoint(Vector(1, 2), 1))
