'''Graph Edge

@credit KuiYue - Code is based on his work from "Estimating the Interior
    Layout of Buildings Using a Shape Grammar to Capture Building Style"
@link https://ascelibrary.org/doi/10.1061/%28ASCE%29CP.1943-5487.0000129

Graph Node

@credit KuiYue - Code is based on his work from "Estimating the Interior
    Layout of Buildings Using a Shape Grammar to Capture Building Style"
@link https://ascelibrary.org/doi/10.1061/%28ASCE%29CP.1943-5487.0000129

Rectangle

A rectangle in 2D coordinate vectors

Note that rectangles rely on the assmption that coordinates, although floats,
are grid based, and hence th NE and SE corners will have the exact same x
vector value
'''
from typing import List, Tuple, Optional
from .components import EdgeDirection, RoomType, EdgeType
from .transformations import Transformation
from .vector import Vector
from .line import Line


class Edge:
    '''Edge Class
    '''
    edge_counter = 0

    def __init__(self,
                 edge_type: EdgeType,
                 name: str,
                 node_a: 'Node',
                 node_b: 'Node',
                 doors: List['Door'] = None,
                 windows: List['Window'] = None,
                 thickness: int = 1) -> None:
        self.name = name
        self.type: str = edge_type.value
        self.node_a: Node = node_a
        self.node_b: Node = node_b
        self.line: Line = Line(node_a.vector, node_b.vector, thickness)
        self.doors: List[Door] = doors
        self.windows: List[Window] = windows
        self.edge_count: int = Edge.edge_counter
        Edge.edge_counter += 1

    def __str__(self) -> str:
        return (f"{type(self).__name__} {self.edge_count} - {self.name} -"
                + " {self.type} connected by {self.node_a} and {self.node_b}")

    def __len__(self) -> float:
        return len(self.line)

    def __eq__(self, other: 'Edge') -> bool:
        return False if not isinstance(other, Edge) else \
            self.node_a == other.node_a and \
            self.node_b == other.node_b and \
            self.type == other.type and \
            self.doors == other.doors and \
            self.windows == other.windows and \
            self.edge_count == other.edge_count and \
            self.name == other.name and \
            type(self).__name__ == type(other).__name__

    def get_left_node(self) -> Optional['Node']:
        return self.line.left_node

    def get_right_node(self) -> Optional['Node']:
        return self.line.right_node

    def get_bottom_node(self) -> Optional['Node']:
        return self.line.bottom_node

    def get_upper_node(self) -> Optional['Node']:
        return self.line.upper_node

    def get_other_node(self, current_node: 'Node') -> Optional['Node']:
        return self.node_b if self.node_a == current_node else self.node_a

    def is_horizontal(self) -> bool:
        return self.line.is_horizontal

    def is_vertical(self) -> bool:
        return self.line.is_vertical

    def length(self) -> float:
        return len(self)

    def get_midpoint(self) -> Vector:
        return self.node_a.linear_combination(self.node_b, value=0.5)

    def get_left_door_point(self) -> Vector:
        '''this one doesn't really make sense
        '''
        raise NotImplementedError

    def get_right_door_point(self) -> Vector:
        '''this one doesn't really make sense
        '''
        raise NotImplementedError

    def does_intersect(self, rectangle: 'Rectangle') -> Optional[bool]:
        '''Tests whether or not a rectangle intersects this edge or not
        This is used to determine whether or nota door/window belongs to this
        edge
        '''
        if not isinstance(rectangle, Rectangle):
            raise ValueError(
                f"Rectangle passed in not of type {type(Rectangle)}")
        return self.line.intersects(rectangle)


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

    def __init__(self, vector: Vector, name: str) -> None:
        # The following initializes the empty neighbour array
        self.name = name
        self.neighbour_edges: List[Edge] = [None] * 8
        self.vector: Vector = vector
        self.node_count: int = Node.node_counter
        Node.node_counter += 1

    def __str__(self) -> str:
        return (f"{type(self).__name } {self.node_count} - {self.name}" +
                " {self.id} @ {self.point}")

    def __eq__(self, other: 'Node') -> bool:
        return False if not isinstance(other, Node) else \
            self.neighbour_edges == other.neighbour_edges and \
            self.vector == other.vector and \
            self.node_counter == other.node_count and \
            self.name == other.name and \
            type(self).__name__ == type(other).__name__

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
                 name: str,
                 room_type: RoomType) -> None:
        Node.__init__(vector, name)
        self.room_type = room_type.value

    def __str__(self) -> str:
        return (f"{type(self).__name__} {self.node_count} - {self.name} -"
                + " {self.room_type} - {self.id} @ {self.point}")

    def __eq__(self, other: 'Node') -> bool:
        return False if not isinstance(other, Node) else \
            self.neighbour_edges == other.neighbour_edges and \
            self.vector == other.vector and \
            self.node_counter == other.node_count and \
            self.room_type == other.room_type and \
            self.name == other.name and \
            type(self).__name__ == type(other).__name__


class CornerNode(Node):
    '''Extends Node, just mostly for typing reasons'''

    def __init__(self, vector: Vector,
                 name: str,) -> None:
        Node.__init__(vector, name)


class WallNode(Node):
    '''Extends Node, just mostly for typing reasons'''

    def __init__(self, vector: Vector,
                 name: str,) -> None:
        Node.__init__(vector, name)


class Rectangle:
    '''Rectangle Class
    '''

    def __init__(self, corners: List[Node]) -> None:
        if len(corners) != 4:
            raise ValueError(
                "Rectangle was initialized with list of corners != 4")
        NE, SE, SW, NW = self.sort_nodes(corners)
        self.NE: Node = NE
        self.SE: Node = SE
        self.NW: Node = SW
        self.SW: Node = NW
        self.corners: List[Node] = [self.NE, self.SE, self.NW, self.SW]
        self.width: float = NE.x - NW.x
        self.height: float = NE.y - SE.y

        # TODO need to define allowable labels
        self.is_horizontal: bool = self.width > self.height
        self.is_vertical: bool = self.width < self.height
        self.is_square: bool = self.width == self.height

    def __str__(self) -> str:
        return (f"{type(self).__name__} defined by"
                + " [({self.NE.vector.x}, {self.NE.vector.y})"
                + ", ({self.SE.vector.x}, {self.SE.vector.y})"
                + ", ({self.SW.vector.x}, {self.SW.vector.y})"
                + ", ({self.NW.vector.x}, {self.NW.vector.y})]")

    def __eq__(self, other: 'Rectangle') -> bool:
        return False if not isinstance(other, Rectangle) else \
            self.NE == other.NE and \
            self.SE == other.SE and \
            self.SW == other.SW and \
            self.NW == other.NW and \
            type(self).__name__ == type(other).__name__

    def sort_nodes(self, nodes: List[Node]) -> Tuple[Node]:
        for node in nodes:
            if not isinstance(node, Node):
                raise ValueError(
                    f"One of the corners is not of type {type(Node)}")
        a, b, c, d = nodes
        min_x = min(a.x, b.x, c.x, d.x)
        max_x = max(a.x, b.x, c.x, d.x)
        min_y = min(a.y, b.y, c.y, d.y)
        max_y = max(a.y, b.y, c.y, d.y)
        NE = [node for node in nodes if node.x == max_x and node.y == max_y][0]
        SE = [node for node in nodes if node.x == max_x and node.y == min_y][0]
        SW = [node for node in nodes if node.x == min_x and node.y == max_y][0]
        NW = [node for node in nodes if node.x == min_x and node.y == max_y][0]
        if NE.x != SE.x or NW.x != SW.x or NE.y != NW.y or SE.y != SW.y:
            raise ValueError(
                "The rectangular corners did not match up" +
                f"\nNE: ({NE.x}, {NE.y})" +
                f"\nSE: ({SE.x}, {SE.y})" +
                f"\nSW: ({SW.x}, {SW.y})" +
                f"\nNW: ({NW.x}, {NW.y})")
        return (NE, SE, SW, NW)

    def overlap_with(self, other: 'Rectangle') -> bool:
        '''Checks if this rectangle overlaps with another
        '''
        if self.NW.x > other.SE.x or other.NW.x > self.SE.x or \
                self.NW.y < other.SE.y or other.NW.y < self.SE.y:
            return False
        return True


class Window(Rectangle):
    def __init__(self, corners: List[Node]):
        Rectangle.__init__(corners)


class Door(Rectangle):
    def __init__(self, corners: List[Node]):
        Rectangle.__init__(corners)


class Staircase(Rectangle):
    def __init__(self, corners: List[Node]):
        Rectangle.__init__(corners)
