'''A rectangle in 2D coordinate vectors

Note that rectangles rely on the assmption that coordinates, although floats,
are grid based, and hence th NE and SE corners will have the exact same x
vector value
'''
from typing import List, Tuple

from .node import Node


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
        self.is_horizontal: bool = True if self.width > self.height else False
        self.is_vertical: bool = True if self.width < self.height else False
        self.is_square: bool = True if self.width == self.height else False

    def __str__(self) -> str:
        return (f"Rectangle defined by"
                + " [({self.NE.vector.x}, {self.NE.vector.y})"
                + ", ({self.SE.vector.x}, {self.SE.vector.y})"
                + ", ({self.SW.vector.x}, {self.SW.vector.y})"
                + ", ({self.NW.vector.x}, {self.NW.vector.y})]")

    def sort_nodes(self, nodes: List[Node]) -> Tuple[Node]:
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
