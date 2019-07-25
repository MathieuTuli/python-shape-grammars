import pytest
from python_shape_grammars.components import FloorPlanStatus
from python_shape_grammars.floor_plan import FloorPlan


def fail_if(boolean):
    if boolean:
        pytest.fail()


def test_floor_plan():
    name = 'test'
    status = FloorPlanStatus('start')
    fp = FloorPlan(name, status)
    fail_if(fp.name != name)
    print(fp.status)
    print(status)
    fail_if(fp.status != status)
