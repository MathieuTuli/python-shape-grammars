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

from multi_key_dict import multi_key_dict as MKDict

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
                 node_a: 'Node',
                 node_b: 'Node',
                 doors: List['Door'] = None,
                 windows: List['Window'] = None,
                 thickness: int = 1) -> None:
        # something weird with inheritance so check like this
        if not isinstance(edge_type, EdgeType):
            raise ValueError(f"edge_type {edge_type} is of incorrect type."
                             + " Need EdgeType")
        if not isinstance(node_a, Node) or not isinstance(node_b, Node):
            raise ValueError("Incompatible nodes for an edge")
        if node_a == node_b or node_a.vector == node_b.vector:
            raise ValueError("Incompatible nodes for an edge")
        self.type: str = edge_type
        self.direction = node_a.get_direction_to(node_b)
        self.node_a: Node = node_a
        self.node_b: Node = node_b
        self.line: Line = Line(node_a.vector, node_b.vector, thickness)
        self.upper_node = node_a if node_a.vector == self.line.upper_vector \
            else node_b
        self.bottom_node = node_a if self.upper_node != node_a else node_b
        self.doors: List[Door] = doors
        self.windows: List[Window] = windows
        self.edge_count: int = Edge.edge_counter
        self.midpoint = self.line.midpoint
        Edge.edge_counter += 1

    def __str__(self) -> str:
        return (f"{type(self).__name__} {self.edge_count} -"
                + f" {self.type} connected by {self.node_a} and {self.node_b}")

    def __abs__(self) -> float:
        return abs(self.line)

    def __eq__(self, other: 'Edge') -> bool:
        return False if not isinstance(other, Edge) else \
            self.node_a == other.node_a and \
            self.node_b == other.node_b and \
            self.type == other.type and \
            self.doors == other.doors and \
            self.windows == other.windows and \
            self.edge_count == other.edge_count and \
            type(self).__name__ == type(other).__name__

    def get_left_node(self) -> Optional['Node']:
        left_vector = self.line.left_vector
        return None if left_vector is None else \
            self.node_a if self.node_a.vector == left_vector else \
            self.node_b

    def get_right_node(self) -> Optional['Node']:
        right_vector = self.line.right_vector
        return None if right_vector is None else \
            self.node_a if self.node_a.vector == right_vector else \
            self.node_b

    def get_bottom_node(self) -> Optional['Node']:
        bottom_vector = self.line.bottom_vector
        return None if bottom_vector is None else \
            self.node_a if self.node_a.vector == bottom_vector else \
            self.node_b

    def get_upper_node(self) -> Optional['Node']:
        upper_vector = self.line.upper_vector
        return None if upper_vector is None else \
            self.node_a if self.node_a.vector == upper_vector else \
            self.node_b

    def get_other_node(self, current_node: 'Node') -> Optional['Node']:
        return self.node_b if self.node_a == current_node else self.node_a

    def is_horizontal(self) -> bool:
        return self.line.is_horizontal

    def is_vertical(self) -> bool:
        return self.line.is_vertical

    # TODO
    def get_left_door_point(self) -> Vector:
        '''this one doesn't really make sense
        '''
        raise NotImplementedError

    # TODO
    def get_right_door_point(self) -> Vector:
        '''this one doesn't really make sense
        '''
        raise NotImplementedError

    # TODO
    def does_intersect(self, rectangle: 'Rectangle') -> Optional[bool]:
        '''Tests whether or not a rectangle intersects this edge or not
        This is used to determine whether or nota door/window belongs to this
        edge
        '''
        if not isinstance(rectangle, Rectangle):
            raise ValueError(
                f"Rectangle passed in not of type Rectangle")
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
    --|----|---|----|---|----|---|---
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

    def __init__(self, vector: Vector,) -> None:
        # The following initializes the empty neighbour array
        if not isinstance(vector, Vector):
            raise ValueError("Argument * vector * must be of type Vector")
        self.neighbour_edges: MKDict = MKDict()
        self.neighbour_edges[0, 'N'] = None
        self.neighbour_edges[1, 'NE'] = None
        self.neighbour_edges[2, 'E'] = None
        self.neighbour_edges[3, 'SE'] = None
        self.neighbour_edges[4, 'S'] = None
        self.neighbour_edges[5, 'SW'] = None
        self.neighbour_edges[6, 'W'] = None
        self.neighbour_edges[7, 'NW'] = None
        self.vector: Vector = vector
        self.node_count: int = Node.node_counter
        Node.node_counter += 1

    def __str__(self) -> str:
        return (f"{type(self).__name__} {self.node_count} -" +
                f" @ {self.vector}")

    def __eq__(self, other: 'Node') -> bool:
        return False if not isinstance(other, Node) else \
            self.neighbour_edges == other.neighbour_edges and \
            self.vector == other.vector and \
            self.node_count == other.node_count and \
            type(self).__name__ == type(other).__name__

    def get_direction_to(self, other: 'Node') -> EdgeDirection:
        '''
            N | NE | E | SE | S | SW | W | NW
            --|----|---|----|---|----|---|---
            0 | 1  | 2 | 3  | 4 | 5  | 6 | 7
        '''
        if self.left_of(other) == -1 and self.beneath(other) == 1:
            return EdgeDirection('N')

        if self.left_of(other) == 1 and self.beneath(other) == 1:
            return EdgeDirection('NE')

        if self.left_of(other) == 1 and self.beneath(other) == -1:
            return EdgeDirection('E')

        if self.left_of(other) == 1 and self.above(other) == 1:
            return EdgeDirection('SE')

        if self.left_of(other) == -1 and self.above(other) == 1:
            return EdgeDirection('S')

        if self.right_of(other) == 1 and self.above(other) == 1:
            return EdgeDirection('SW')

        if self.right_of(other) == 1 and self.above(other) == -1:
            return EdgeDirection('W')

        if self.right_of(other) == 1 and self.beneath(other) == 1:
            return EdgeDirection('NW')

    def left_of(self, other: 'Node') -> bool:
        return self.vector.left_of(other.vector)

    def right_of(self, other: 'Node') -> bool:
        return self.vector.right_of(other.vector)

    def above(self, other: 'Node') -> bool:
        return self.vector.above(other.vector)

    def beneath(self, other: 'Node') -> bool:
        return self.vector.beneath(other.vector)

    def add_edge(self,
                 edge: Edge,
                 transformation: Optional[Transformation] = None) -> None:
        if not isinstance(edge, Edge):
            raise ValueError(
                f"Passed in edge is not of type Edge")
        direction = edge.direction if self == edge.node_a else \
            edge.direction.reverse()
        if self.neighbour_edges[direction.value] is not None:
            raise ValueError(
                f"For {str(self)} -" +
                f" There already exists an edge at {direction}")
        if transformation is not None and not isinstance(transformation,
                                                         Transformation):
            raise ValueError(
                "Passed in transformation is not of " +
                f"type Transformation")
        if transformation:
            self.neighbour_edges[direction.integer_value,
                                 direction.value] = transformation(
                edge)
        else:
            self.neighbour_edges[direction.integer_value,
                                 direction.value] = edge

    def get_neighbour_edge(
            self,
            direction: EdgeDirection,
            transformation: Optional[Transformation] = None) -> \
            Optional['Edge']:
        if not isinstance(direction, EdgeDirection):
            raise ValueError(
                f"Passed in direction is not of type EdgeDirection")
        if transformation is not None and not isinstance(transformation,
                                                         Transformation):
            raise ValueError(
                "Passed in transformation is not of type Transformation")
        neighbour_edge = self.neighbour_edges[direction.integer_value]
        return None if neighbour_edge is None else \
            transformation(neighbour_edge) if transformation is not None else \
            neighbour_edge

    def get_neighbour_node(
            self,
            direction: EdgeDirection,
            transformation: Optional[Transformation] = None) -> \
            Optional['Node']:
        if not isinstance(direction, EdgeDirection):
            raise ValueError(
                f"Passed in direction is not of type EdgeDirection")
        if transformation is not None and \
                not isinstance(transformation, Transformation):
            raise ValueError(
                "Passed in transformation is not of type Transformation")
        neighbour_edge = self.neighbour_edges[direction.integer_value]
        return None if neighbour_edge is None else \
            transformation(neighbour_edge.get_other_node(self)) if \
            transformation is not None else \
            neighbour_edge.get_other_node(self)


class RoomNode(Node):
    '''Extends Node, just mostly for typing reasons'''

    def __init__(self, vector: Vector,
                 room_type: RoomType) -> None:
        Node.__init__(self, vector)
        self.room_type = room_type

    def __str__(self) -> str:
        return (f"{type(self).__name__} {self.node_count} -"
                + f" {self.room_type} - {self.vector}")

    def __eq__(self, other: 'RoomNode') -> bool:
        return False if not isinstance(other, RoomNode) else \
            self.neighbour_edges == other.neighbour_edges and \
            self.vector == other.vector and \
            self.node_count == other.node_count and \
            self.room_type == other.room_type and \
            type(self).__name__ == type(other).__name__


class CornerNode(Node):
    '''Extends Node, just mostly for typing reasons'''

    def __init__(self, vector: Vector) -> None:
        Node.__init__(self, vector)


class WallNode(Node):
    '''Extends Node, just mostly for typing reasons'''

    def __init__(self, vector: Vector) -> None:
        Node.__init__(self, vector)


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
        self.SW: Node = SW
        self.NW: Node = NW
        self.corners: List[Node] = [self.NE, self.SE, self.NW, self.SW]
        self.width: float = abs(NE.vector.x - NW.vector.x)
        self.height: float = abs(NE.vector.y - SE.vector.y)

        # TODO need to define allowable labels
        self.is_horizontal: bool = self.width > self.height
        self.is_vertical: bool = self.width < self.height
        self.is_square: bool = self.width == self.height
        self.midpoint = Vector(
            NW.vector.x + (self.width / 2), SW.vector.y + (self.height / 2))

    def __str__(self) -> str:
        return (f"{type(self).__name__} defined by"
                + f" [NE: ({self.NE.vector.x}, {self.NE.vector.y})"
                + f", SE: ({self.SE.vector.x}, {self.SE.vector.y})"
                + f", SW: ({self.SW.vector.x}, {self.SW.vector.y})"
                + f", NW: ({self.NW.vector.x}, {self.NW.vector.y})]")

    def __eq__(self, other: 'Rectangle') -> bool:
        return False if not isinstance(other, Rectangle) else \
            self.NE == other.NE and \
            self.SE == other.SE and \
            self.SW == other.SW and \
            self.NW == other.NW and \
            type(self).__name__ == type(other).__name__

    def sort_nodes(self, nodes: List[Node]) -> Tuple[Node]:
        for node in nodes:
            if not isinstance(node, Node) and not isinstance(node, CornerNode):
                raise ValueError(
                    f"One of the corners is not of type Node")
        a, b, c, d = nodes
        if a == b or a == c or a == d or b == c or b == d or c == d:
            raise ValueError("There are duplicates nodes in the list")
        min_x = min(a.vector.x, b.vector.x, c.vector.x, d.vector.x)
        max_x = max(a.vector.x, b.vector.x, c.vector.x, d.vector.x)
        min_y = min(a.vector.y, b.vector.y, c.vector.y, d.vector.y)
        max_y = max(a.vector.y, b.vector.y, c.vector.y, d.vector.y)
        NE = [node for node in nodes if node.vector.x ==
              max_x and node.vector.y == max_y][0]
        SE = [node for node in nodes if node.vector.x ==
              max_x and node.vector.y == min_y][0]
        SW = [node for node in nodes if node.vector.x ==
              min_x and node.vector.y == min_y][0]
        NW = [node for node in nodes if node.vector.x ==
              min_x and node.vector.y == max_y][0]
        return (NE, SE, SW, NW)

    def overlap_with(self, other: 'Rectangle') -> bool:
        '''Checks if this rectangle overlaps with another
        '''
        if not isinstance(other, Rectangle):
            raise ValueError("Cannot check overlap of none-Rectangle object")
        if self.NW.vector.x > other.SE.vector.x or \
                other.NW.vector.x > self.SE.vector.x or \
                self.NW.vector.y < other.SE.vector.y or \
                other.NW.vector.y < self.SE.vector.y:
            return False
        return True

    def contains_node(self, node: Node) -> bool:
        if not isinstance(node, Node):
            raise ValueError("Cannot check overlap of none-Node object")
        return node.vector.x <= self.NE.vector.x and \
            node.vector.x >= self.NW.vector.x and \
            node.vector.y <= self.NE.vector.y and \
            node.vector.y >= self.SE.vector.y


class Window(Line):
    def __init__(self, vector_a: Vector, vector_b: Vector):
        Line.__init__(self, vector_a, vector_b)


class Door(Line):
    def __init__(self, vector_a: Vector, vector_b: Vector):
        Line.__init__(self, vector_a, vector_b)


class Staircase(Rectangle):
    def __init__(self, corners: List[Node]):
        Rectangle.__init__(self, corners)
