'''Graph Edge

@credit KuiYue - Code is based on his work from "Estimating the Interior
    Layout of Buildings Using a Shape Grammar to Capture Building Style"
@link https://ascelibrary.org/doi/10.1061/%28ASCE%29CP.1943-5487.0000129
'''
from typing import List, Optional

from .components import EdgeType, Door, Window, Rectangle
from .vector import Vector
from .line import Line
from .node import Node


class Edge:
    '''Edge Class
    '''
    edge_counter = 0

    def __init__(self,
                 edge_type: EdgeType,
                 node_a: Node,
                 node_b: Node,
                 doors: List[Door] = None,
                 windows: List[Window] = None,
                 thickness: int = 1) -> None:
        self.type: str = edge_type
        self.node_a: Node = node_a
        self.node_b: Node = node_b
        self.line: Line = Line(node_a.vector, node_b.vector, thickness)
        self.doors: List[Door] = doors
        self.windows: List[Window] = windows
        self.edge_count: int = Edge.edge_counter
        Edge.edge_counter += 1

    def __str__(self) -> str:
        return (f"Edge {self.edge_count} {self.type} connected by"
                + " {self.node_a} and {self.node_b}")

    def __len__(self) -> float:
        return len(self.line)

    def __eq__(self, other: 'Edge') -> bool:
        return True if self.node_a == other.node_a and \
            self.node_b == other.node_b and \
            self.type == other.type and \
            self.doors == other.doors and \
            self.windows == other.windows and \
            self.edge_count == other.edge_count else False

    def get_left_node(self) -> Optional[Node]:
        return self.line.left_node

    def get_right_node(self) -> Optional[Node]:
        return self.line.right_node

    def get_bottom_node(self) -> Optional[Node]:
        return self.line.bottom_node

    def get_upper_node(self) -> Optional[Node]:
        return self.line.upper_node

    def get_other_node(self, current_node: Node) -> Optional[Node]:
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

    def does_intersect(self, rectangle: Rectangle) -> Optional[bool]:
        '''Tests whether or not a rectangle intersects this edge or not
        This is used to determine whether or nota door/window belongs to this
        edge
        '''
        return self.line.intersects(rectangle)
