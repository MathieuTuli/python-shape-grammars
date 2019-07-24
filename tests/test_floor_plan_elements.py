import math

import pytest

from python_shape_grammars.floor_plan_elements import Node, Edge, RoomNode, \
    CornerNode, WallNode, Rectangle, Window, Door, Staircase
from python_shape_grammars.components import EdgeType, EdgeDirection
from python_shape_grammars.vector import Vector


def fail_if(boolean):
    if boolean:
        pytest.fail()


def test_vector():
    vector = Vector(0, 0)
    fail_if(vector.x != 0)
    fail_if(vector.y != 0)
    fail_if(vector != Vector(0, 0))

    fail_if(vector.left_of(Vector(-1, 0)) != 0)
    fail_if(vector.left_of(Vector(1, 0)) != 1)
    fail_if(vector.left_of(Vector(0, 1)) != -1)

    fail_if(vector.right_of(Vector(-1, 0)) != 1)
    fail_if(vector.right_of(Vector(1, 0)) != 0)
    fail_if(vector.right_of(Vector(0, -1)) != -1)

    fail_if(vector.beneath(Vector(0, 1)) != 1)
    fail_if(vector.beneath(Vector(0, -1)) != 0)
    fail_if(vector.beneath(Vector(1, 0)) != -1)

    fail_if(vector.above(Vector(0, 1)) != 0)
    fail_if(vector.above(Vector(0, -1)) != 1)
    fail_if(vector.above(Vector(-1, 0)) != -1)

    vector2 = Vector(1, 1)
    fail_if(vector.distance_to(vector2) != math.sqrt(2))

    lc = vector.linear_combination(vector2, 2)
    fail_if(lc != Vector(2, 2))

    lc = vector2.linear_combination(vector2, 2, 3)
    fail_if(lc != Vector(5, 5))


def test_node_and_edge():
    vector = Vector(0, 0)
    node = Node(vector)
    fail_if(len(node.neighbour_edges) != 8)
    # fail_if(sum([arg is not None for arg in node.neighbour_edges]) != 0)
    fail_if(node.vector != vector)
    fail_if(node.node_count != 0)
    fail_if(Node.node_counter != 1)
    fail_if(f"{type(node).__name__} {node.node_count} - @ {node.vector}" !=
            f"Node 0 - @ {str(vector)}")
    # that this shouldn't be allowed when building the graph, but ok for now
    node2 = Node(vector)
    fail_if(node2.node_count != 1)
    fail_if(Node.node_counter != 2)

    fail_if(node != node)
    fail_if(node2 != node2)

    fail_if(node.vector != node2.vector)

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

def test_rectangle():
    pass
