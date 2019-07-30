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


def test_floor_plan_rooms():
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
    try:
        fail_if(fp.remove_room(0))
        pytest.fail()
    except ValueError:
        pass

    fp.add_room(room)
    fail_if(fp.rooms['name'] != room)
    fail_if(not fp.room_exists(room))
    fail_if(not fp.room_exists('name'))
    try:
        fail_if(fp.room_exists(0))
        pytest.fail()
    except ValueError:
        pass

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


def test_floor_plan_nodes():
    name = 'test'
    status = FloorPlanStatus.start
    fp = FloorPlan(name, status)

    vector_orig = Vector(0, 0)
    node = Node(vector_orig)
    fp.add_node(node)
    vector2 = Vector(0, 1)
    try:
        fp.add_node(vector2)
        pytest.fail()
    except ValueError:
        pass
    fail_if(fp.nodes[str(vector_orig)] != node)

    # can't add a duplicate node/vector location
    fail_if(fp.add_node(node))

    try:
        fp.remove_node(Vector(0, 0))
        pytest.fail()
    except ValueError:
        pass
    fail_if(not fp.remove_node(node))
    # doesn't exist
    fail_if(fp.remove_node(Node(Vector(0, 100))))

    fp.add_node(node)
    fail_if(fp.get_node(vector_orig) is None)
    fail_if(fp.get_node(Vector(0, 100)) is not None)
    try:
        fp.get_node((0, 0))
        pytest.fail()
    except ValueError:
        pass

    fail_if(not fp.node_exists(node))
    fail_if(not fp.node_exists(vector_orig))
    try:
        fp.node_exists((0, 0))
        pytest.fail()
    except ValueError:
        pass
    _, exists = fp.nodes_exist([node])
    fail_if(not exists)
    _, exists = fp.nodes_exist([node, vector_orig])
    fail_if(not exists)
    _, exists = fp.nodes_exist([node, Vector(0, 100)])
    fail_if(exists)
    try:
        fp.nodes_exist([node, (0, 0)])
        pytest.fail()
    except ValueError:
        pass
    try:
        fp.nodes_exist((0, 0))
        pytest.fail()
    except ValueError:
        pass
    try:
        fp.nodes_exist(node)
        pytest.fail()
    except ValueError:
        pass

    # test update
    node, ret = fp.update_node_vector(node, vector2)
    fail_if(not ret)
    fail_if(node.vector == vector_orig)
    fail_if(node.vector != vector2)
    fail_if(str(vector_orig) in fp.nodes)
    fail_if(not str(vector2) in fp.nodes)
    fail_if(fp.get_node(vector2) != node)
    fail_if(fp.nodes[str(vector2)].vector != vector2)
    fail_if(len(fp.nodes) != 1)
    try:
        fp.update_node_vector(node, (0, 0))
        pytest.fail()
    except ValueError:
        pass
    fail_if(fp.update_node_vector(Node(Vector(0, 100)), Vector(0, 300)))


def test_floor_plan_edges():
    name = 'test'
    status = FloorPlanStatus.start
    fp = FloorPlan(name, status)

    node = Node(Vector(0, 1))
    node_b = Node(Vector(0, 2))
    fp.add_node(node)
    fp.add_node(node_b)
    edge = Edge(edge_type=EdgeType.wall, node_a=node, node_b=node_b)
    node.add_edge(edge)
    node_b.add_edge(edge)

    fail_if(fp.get_node(Vector(0, 1)).neighbour_edges[0] != edge)
    fail_if(fp.get_node(Vector(0, 1)).neighbour_edges[0].upper_node != node_b)
    fail_if(fp.get_node(Vector(0, 1)).neighbour_edges[0].bottom_node != node)

    fp.add_edge(edge)
    fail_if(fp.edges[f'{node}_{node.get_direction_to(node_b)}'] != edge)
    fail_if(fp.edges[f'{node_b}_{node_b.get_direction_to(node)}'] != edge)
    fail_if(fp.edges[str(edge)] != edge)

    try:
        fp.add_edge(0)
        pytest.fail()
    except ValueError:
        pass

    try:
        fp.remove_edge(0)
        pytest.fail()
    except ValueError:
        pass

    fail_if(not fp.remove_edge(edge))
    fp.add_edge(edge)
    node_3 = Node(Vector(0, 10))
    node_4 = Node(Vector(0, 30))
    edge2 = Edge(EdgeType.wall, node_a=node_3, node_b=node_4)
    fail_if(fp.remove_edge(edge2))
    fp.add_edge(edge2)
    fail_if(len(fp.edges) != 2)
    fail_if(fp.edges[f'{node}_{node.get_direction_to(node_b)}'] != edge)
    fail_if(fp.edges[f'{node_b}_{node_b.get_direction_to(node)}'] != edge)
    fail_if(fp.edges[str(edge)] != edge)
    fail_if(fp.edges[f'{node_3}_{node_3.get_direction_to(node_4)}'] == edge)
    fail_if(fp.edges[f'{node_3}_{node_3.get_direction_to(node_4)}'] != edge2)
    fail_if(fp.edges[f'{node_4}_{node_4.get_direction_to(node_3)}'] != edge2)
    fail_if(fp.edges[str(edge2)] != edge2)

    fail_if(not fp.edge_exists(edge))
    fail_if(not fp.edge_exists(edge2))
    edge3 = Edge(EdgeType.wall, node_a=node, node_b=node_4)
    fail_if(fp.edge_exists(edge3))
    try:
        fp.edge_exists(0)
        pytest.fail()
    except ValueError:
        pass
    _, ret = fp.edges_exist([edge, edge2])
    fail_if(not ret)
    edge_ret, ret = fp.edges_exist([edge, edge2, edge3])
    fail_if(ret)
    fail_if(edge_ret != edge3)
    try:
        _, ret = fp.edges_exist([edge, edge2, 0])
        pytest.fail()
    except ValueError:
        pass
    try:
        _, ret = fp.edges_exist(edge)
        pytest.fail()
    except ValueError:
        pass

    node_4 = Node(Vector(0, -10))
    edge = Edge(EdgeType.wall, node_a=node, node_b=node_4)
    fail_if(node.neighbour_edges[node.get_direction_to(node_4).integer_value]
            is not None)
    fp.add_edge(edge)
    node.add_edge(edge)
    node_4.add_edge(edge)
    fail_if(node.neighbour_edges[node.get_direction_to(
        node_4).integer_value] is None)
    print(fp.nodes)
    fail_if(fp.nodes[str(node.vector)].neighbour_edges[
        node.get_direction_to(node_4).integer_value] != edge)
