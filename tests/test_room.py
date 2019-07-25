import pytest
from python_shape_grammars.room import Room


def fail_if(boolean):
    if boolean:
        pytest.fail()
