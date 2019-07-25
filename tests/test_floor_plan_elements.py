import math

import pytest

from python_shape_grammars.floor_plan_elements import Node, Edge, RoomNode, \
    CornerNode, WallNode, Rectangle, Window, Door, Staircase
from python_shape_grammars.components import EdgeType, EdgeDirection, RoomType
from python_shape_grammars.vector import Vector


def fail_if(boolean):
    if boolean:
        pytest.fail()


def test_node_and_edge():
    vector = Vector(0, 0)
    node = Node(vector)

    fail_if(len(node.neighbour_edges) != 8)
    # fail_if(sum([arg is not None for arg in node.neighbour_edges]) != 0)
    fail_if(node.vector != vector)
    fail_if(node.node_count != 0)
    fail_if(Node.node_counter != 1)
    fail_if(str(node) != f"Node 0 - @ {str(vector)}")
    # that this shouldn't be allowed when building the graph, but ok for now
    node2 = Node(vector)
    fail_if(node2.node_count != 1)
    fail_if(Node.node_counter != 2)

    fail_if(node != node)
    fail_if(node2 != node2)

    fail_if(node.vector != node2.vector)

    try:
        Node(0, 0)
        pytest.fail()
    except Exception:
        pass

    # directions
    fail_if(node.left_of(Node(Vector(-1, 0))))
    fail_if(not node.left_of(Node(Vector(1, 1))))
    fail_if(node.right_of(Node(Vector(1, 0))))
    fail_if(not node.right_of(Node(Vector(-1, 0))))
    fail_if(node.above(Node(Vector(1, 1))))
    fail_if(not node.above(Node(Vector(1, -1))))
    fail_if(node.beneath(Node(Vector(0, -1))))
    fail_if(not node.beneath(Node(Vector(0, 1))))

    # direction to
    fail_if(node.get_direction_to(Node(Vector(0, 1))) != EdgeDirection('N'))
    fail_if(node.get_direction_to(Node(Vector(1, 0))) != EdgeDirection('E'))
    fail_if(node.get_direction_to(Node(Vector(1, 1))) != EdgeDirection('NE'))
    fail_if(node.get_direction_to(Node(Vector(0, -1))) != EdgeDirection('S'))
    fail_if(node.get_direction_to(Node(Vector(-1, 0))) != EdgeDirection('W'))
    fail_if(node.get_direction_to(Node(Vector(-1, -1))) != EdgeDirection('SW'))
    fail_if(node.get_direction_to(Node(Vector(-1, 1))) != EdgeDirection('NW'))
    fail_if(node.get_direction_to(Node(Vector(1, -1))) != EdgeDirection('SE'))

    # SOME EDGE STUFF
    node2 = Node(Vector(0, 1))
    direction = EdgeDirection('N')
    to = node.get_direction_to(node2)
    fail_if(to != direction)
    fail_if(direction.reverse() != EdgeDirection('S'))
    fail_if(node2.get_direction_to(node) != direction.reverse())
    et = EdgeType('wall')
    edge = Edge(edge_type=et, node_a=node, node_b=node2)
    node.add_edge(edge)
    node2.add_edge(edge)
    try:
        node.add_edge(edge)
        pytest.fail()
    except ValueError:
        pass
    try:
        node.add_edge(0)
        pytest.fail()
    except ValueError:
        pass

    fail_if(edge.midpoint != Vector(0, 0.5))
    fail_if(node.neighbour_edges[0] != edge)
    fail_if(node2.neighbour_edges[4] != edge)
    fail_if(node.neighbour_edges['N'] != edge)
    fail_if(node2.neighbour_edges['S'] != edge)

    fail_if(edge.get_other_node(node) != node2)
    fail_if(edge.get_other_node(node2) != node)

    fail_if(edge.get_upper_node() != node2)
    fail_if(edge.get_bottom_node() != node)
    fail_if(edge.get_right_node() is not None)
    fail_if(edge.get_left_node() is not None)
    fail_if(edge.is_horizontal())
    fail_if(not edge.is_vertical())

    fail_if(node.get_neighbour_edge(EdgeDirection('N')) != edge)
    fail_if(node.get_neighbour_node(EdgeDirection('N')) != node2)

    try:
        node.get_neighbour_edge('N')
        pytest.fail()
    except ValueError:
        pass
    try:
        node.get_neighbour_node('N')
        pytest.fail()
    except ValueError:
        pass

    try:
        Edge(edge_type='N', node_a=node, node_b=node)
        pytest.fail()
    except ValueError:
        pass
    try:
        str(edge)
    except Exception:
        pytest.fail()

    fail_if(abs(edge) != 1.0)


def test_room_node():
    rn = RoomNode(vector=Vector(0, 0), room_type=RoomType('kitchen'))
    fail_if(
        str(rn) != f"RoomNode {Node.node_counter - 1} - kitchen - " +
        f"{Vector(0,0)}")
    rn2 = RoomNode(vector=Vector(0, 0), room_type=RoomType('kitchen'))
    fail_if(rn != rn)
    fail_if(rn == rn2)


def test_corner_node():
    cn = CornerNode(vector=Vector(0, 0))
    fail_if(
        str(cn) != f"CornerNode {Node.node_counter - 1} - " +
        f"@ {Vector(0,0)}")
    cn2 = CornerNode(vector=Vector(0, 0))
    fail_if(cn != cn)
    fail_if(cn == cn2)


def test_wall_node():
    wn = WallNode(vector=Vector(0, 0))
    fail_if(
        str(wn) != f"WallNode {Node.node_counter - 1} - " +
        f"@ {Vector(0,0)}")
    wn2 = WallNode(vector=Vector(0, 0))
    fail_if(wn != wn)
    fail_if(wn == wn2)
