import pytest
from python_shape_grammars.floor_plan_elements import Node, RoomNode
from python_shape_grammars.components import RoomType
from python_shape_grammars.vector import Vector
from python_shape_grammars.room import Room


def fail_if(boolean):
    if boolean:
        pytest.fail()


def test_room():
    bl = Node(Vector(0, 0))
    tl = Node(Vector(0, 1))
    br = Node(Vector(1, 0))
    tr = Node(Vector(1, 1))
    room_node = RoomNode(Vector(0.5, 0.5), RoomType('kitchen'))
    room = Room(corners=[tl, bl, tr, br], room_node=room_node)

    fail_if(room != room)
    fail_if(room.room_count != 0)
    fail_if(Room.room_counter != 1)

    fail_if(str(room) != f"Room defined by"
            + f" [(1.0, 1.0)"
            + f", (1.0, 0.0)"
            + f", (0.0, 0.0)"
            + f", (0.0, 1.0)]"
            + f" labelled: {RoomType('kitchen').value}"
            + f" | count: 0")

    try:
        Room(corners=[tl, bl, tr, br], room_node=tl)
        pytest.fail()
    except ValueError:
        pass
