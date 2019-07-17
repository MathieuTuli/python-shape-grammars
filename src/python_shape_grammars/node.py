'''Graph Node

@credit KuiYue - Code is based on his work from "Estimating the Interior
    Layout of Buildings Using a Shape Grammar to Capture Building Style"
@link https://ascelibrary.org/doi/10.1061/%28ASCE%29CP.1943-5487.0000129
'''
from typing import List, Optional

from .components import EdgeDirection, RoomType
from .transformations import Transformation
from .vector import Vector
from .edge import Edge


class Node:
    '''Node Class

    To avoid to complexity of programming with shape grammars, a graph
    structure is only ever able to represent rectangular-based shapes.

    As such, a shape node will only ever have at most 8 neighbours, defined
    by a simple grid structure. A neighbour may be NORTH, NORTHEAST, EAST,
    SOUTHEAST, SOUTH, SOUTHWEST, WEST, NORTHWEST. These directions are
    respresented as follows:

    N | NE | E | SE | S | SW | W | NW
    --|----|---|----|---|--------|---
    0 | 1  | 2 | 3  | 4 | 5  | 6 | 7

    You might be wondering why NE, SE, SW, and NW are valid neighbours for
    a rectangular based shape grammar. Well, a shape holds a label, and labels
    are indicated by centerpoint nodes as follows:

    N = Node
    L = Node
    N-----N
    |\   /|
    | \ / |
    |  L  |
    | / \ |
    |/   \|
    N-----N

    Evidently, in order to encapsulate labels, nodes need the diagonal edges
    '''
    node_counter = 0

    def __init__(self, vector: Vector) -> None:
        # The following initializes the empty neighbour array
        self.neighbour_edges: List[Edge] = [None] * 8
        self.vector: Vector = vector
        self.node_count: int = Node.node_counter
        Node.node_counter += 1
        pass

    def __str__(self) -> str:
        return (f"{type(self).__name } {self.node_count} -" +
                " {self.id} @ {self.point}")

    def __eq__(self, other: 'Node') -> bool:
        return False if not isinstance(other, Node) else \
            self.neighbour_edges == other.neighbour_edges and \
            self.vector == other.vector and \
            self.node_counter == other.node_count

    def add_edge(self,
                 direction: EdgeDirection,
                 edge: Edge,
                 transformation: Optional[Transformation] = None) -> None:
        if len(self.neighbour_edges) == 8:
            raise ValueError("Already have 8 edges")
        if not isinstance(direction, EdgeDirection):
            raise ValueError(
                f"Passed in direction is not of type {type(EdgeDirection)}")
        if not isinstance(edge, Edge):
            raise ValueError(
                f"Passed in edge is not of type {type(Edge)}")
        if not isinstance(transformation, Transformation):
            raise ValueError(
                "Passed in transformation is not of type " +
                f"{type(Transformation)}")
        if transformation:
            self.neighbour_edges[direction.integer_value] = transformation(
                edge)
        else:
            self.neighbour_edges[direction.integer_value] = edge

    def get_neighbour_edge(
            self,
            direction: EdgeDirection,
            transformation: Optional[Transformation] = None) -> \
            Optional['Edge']:
        if not isinstance(direction, EdgeDirection):
            raise ValueError(
                f"Passed in direction is not of type {type(EdgeDirection)}")
        if not isinstance(transformation, Transformation):
            raise ValueError(
                "Passed in transformation is not of type " +
                f"{type(Transformation)}")
        neighbour_edge = self.neighbour_edges[direction.integer_value]
        if neighbour_edge:
            if transformation:
                return transformation(neighbour_edge)
        return neighbour_edge

    def get_neighbour_node(
            self,
            direction: EdgeDirection,
            transformation: Optional[Transformation] = None) -> \
            Optional['Node']:
        if not isinstance(direction, EdgeDirection):
            raise ValueError(
                f"Passed in direction is not of type {type(EdgeDirection)}")
        if not isinstance(transformation, Transformation):
            raise ValueError(
                "Passed in transformation is not of type " +
                f"{type(Transformation)}")
        neighbour_edge = self.neighbour_edges[direction.integer_value]
        if neighbour_edge:
            if transformation:
                return transformation(
                    neighbour_edge.get_other_node(self.node_counter))
            return neighbour_edge.get_other_node(self.node_counter)
        return


class RoomNode(Node):
    '''Extends Node, just mostly for typing reasons'''

    def __init__(self, vector: Vector,
                 room_type: RoomType = RoomType()) -> None:
        Node.__init__(vector)
        self.room_type = room_type

    def __str__(self) -> str:
        return (f"{type(self).__name__} {self.node_count} - {self.room_type}"
                + " - {self.id} @ {self.point}")

    def __eq__(self, other: 'Node') -> bool:
        return False if not isinstance(other, Node) else \
            self.neighbour_edges == other.neighbour_edges and \
            self.vector == other.vector and \
            self.node_counter == other.node_count and \
            self.room_type == other.room_type
