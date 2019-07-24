import pytest

from python_shape_grammars.vector import Vector
from python_shape_grammars.line import Line


def fail_if(boolean):
    if boolean:
        pytest.fail()


def test_line():
    vector = Vector(0, 0)
    vector2 = Vector(2, 2)
    line = Line(vector, vector2, 2)
