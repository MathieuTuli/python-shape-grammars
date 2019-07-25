import pytest

from python_shape_grammars.floor_plan_elements import Node, Edge, RoomNode, \
    CornerNode, WallNode, Rectangle, Window, Door, Staircase
from python_shape_grammars.components import EdgeType, EdgeDirection, \
    RoomType, FloorPlanStatus
from python_shape_grammars.floor_plan import FloorPlan
from python_shape_grammars.vector import Vector
from python_shape_grammars.room import Room


def fail_if(boolean):
    if boolean:
        pytest.fail()


def test_floor_plan():
    name = 'test'
    status = FloorPlanStatus.start
    fp = FloorPlan(name, status)
    fail_if(fp.name != name)
    fail_if(fp.status != status)

    str(fp)

    bl = CornerNode(Vector(0, 0))
    tl = CornerNode(Vector(0, 1))
    tr = CornerNode(Vector(1, 1))
    br = CornerNode(Vector(1, 0))
    room_node = RoomNode(Vector(0.5, 0.5), RoomType.kitchen)
    room = Room(name='name', corners=[bl, tl, tr, br], room_node=room_node)
    try:
        fp.add_room(0)
        pytest.fail()
    except ValueError:
        pass
    fp.add_room(room)
    fail_if(fp.rooms != {room.name: room})

    fail_if(not fp.remove_room('name'))
    fp.add_room(room)
    fail_if(not fp.remove_room(room))

    fp.add_room(room)
    fail_if(fp.rooms['name'] != room)
    fail_if(not fp.room_exists(room))
    fail_if(not fp.room_exists('name'))

    room_, ret = fp.rooms_exist(['name', room])
    fail_if(not ret)
    fail_if(fp.remove_room('test'))
    room_, ret = fp.rooms_exist(['ame', room])
    fail_if(ret)
    fail_if(room_ != 'ame')
    try:
        fp.rooms_exist('name')
        pytest.fail()
    except ValueError:
        pass
    try:
        fp.rooms_exist([0])
        pytest.fail()
    except ValueError:
        pass

    node = Node(Vector(0, 0))
