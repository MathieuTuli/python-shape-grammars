import pytest

from python_shape_grammars.components import EdgeDirection, EdgeType, RoomType, FloorPlanStatus


def fail_if(boolean):
    if boolean:
        pytest.fail()


def test_edge_direction():
    N = EdgeDirection('N')
    NE = EdgeDirection('NE')
    E = EdgeDirection('E')
    SE = EdgeDirection('SE')
    S = EdgeDirection('S')
    SW = EdgeDirection('SW')
    W = EdgeDirection('W')
    NW = EdgeDirection('NW')

    fail_if(N.value != 'N')
    fail_if(N.integer_value != 0)
    fail_if(NE.value != 'NE')
    fail_if(NE.integer_value != 1)
    fail_if(E.value != 'E')
    fail_if(E.integer_value != 2)
    fail_if(SE.value != 'SE')
    fail_if(SE.integer_value != 3)
    fail_if(S.value != 'S')
    fail_if(S.integer_value != 4)
    fail_if(SW.value != 'SW')
    fail_if(SW.integer_value != 5)
    fail_if(W.value != 'W')
    fail_if(W.integer_value != 6)
    fail_if(NW.value != 'NW')
    fail_if(NW.integer_value != 7)

    fail_if(N.reverse() != EdgeDirection('S'))
    fail_if(NE.reverse() != EdgeDirection('SW'))
    fail_if(E.reverse() != EdgeDirection('W'))
    fail_if(SE.reverse() != EdgeDirection('NW'))
    fail_if(S.reverse() != EdgeDirection('N'))
    fail_if(SW.reverse() != EdgeDirection('NE'))
    fail_if(W.reverse() != EdgeDirection('E'))
    fail_if(NW.reverse() != EdgeDirection('SE'))

    try:
        EdgeDirection('s')
        pytest.fail()
    except ValueError:
        pass

    fail_if(str(N) != "EdgeDirection | N or 0")


def test_edge_type():
    edge_type = EdgeType('wall')
    edge_type2 = EdgeType('empty')
    edge_type3 = EdgeType('label')

    fail_if(edge_type.value != 'wall')
    fail_if(edge_type2.value != 'empty')
    fail_if(edge_type3.value != 'label')

    try:
        edge_type_ = EdgeType('')
        pytest.fail()
    except ValueError:
        pass

    edge_type2 = EdgeType('wall')
    fail_if(edge_type != edge_type2)
    fail_if(edge_type == edge_type3)


def test_room_type():
    room_type = RoomType('kitchen')
    room_type2 = RoomType('hallway')
    room_type3 = RoomType('dining room')
    room_type4 = RoomType('living room')

    fail_if(room_type.value != 'kitchen')
    fail_if(room_type2.value != 'hallway')
    fail_if(room_type3.value != 'dining room')
    fail_if(room_type4.value != 'living room')

    try:
        room_type_ = RoomType('')
        pytest.fail()
    except ValueError:
        pass

    room_type2 = RoomType('kitchen')
    fail_if(room_type != room_type2)
    fail_if(room_type == room_type3)


def test_floor_plan_status():
    status = FloorPlanStatus('start')
    status2 = FloorPlanStatus('generating')
    status3 = FloorPlanStatus('done')

    fail_if(status.value != 'start')
    fail_if(status2.value != 'generating')
    fail_if(status3.value != 'done')

    try:
        status_ = FloorPlanStatus('')
        pytest.faili()
    except ValueError:
        pass

    status2 = FloorPlanStatus('start')
    fail_if(status != status2)
    fail_if(status == status3)
