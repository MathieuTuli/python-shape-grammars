#!/user/bin/env python3
import pytest

from python_shape_grammars.helper import check_argument_uniqueness


def test_check_argument_uniqueness() -> None:
    class Test1:
        def __init__(self):
            return

    class Test2:
        def __init__(self):
            return

    class Test3:
        def __init__(self):
            return
    a = Test1()
    b = Test2()
    c = Test3()
    try:
        result = check_argument_uniqueness(a, b, c)
        pytest.fail()
    except ValueError:
        pass

    a = None
    b = Test2()
    c = Test3()
    try:
        result = check_argument_uniqueness(a, b, c)
        pytest.fail()
    except ValueError:
        pass

    a = None
    b = None
    c = Test3()
    try:
        result = check_argument_uniqueness(a, b, c)
        if result != c:
            pytest.fail()
    except ValueError:
        pytest.fail()

    a = Test1()
    b = None
    c = None
    try:
        result = check_argument_uniqueness(a, b, c)
        if result == c:
            pytest.fail()
        if result == b:
            pytest.fail()
    except ValueError:
        pytest.fail()
