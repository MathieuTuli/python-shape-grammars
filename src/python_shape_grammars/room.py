'''A Room in 2D coordinate vectors

extends the Rectangle class
'''
from typing import List

from .graph_elements import RoomNode, Node, Rectangle, Staircase


class Room(Rectangle):
    '''Rectangle Class
    '''

    def __init__(self, corners: List[Node],
                 label_node: RoomNode,
                 staircase: Staircase) -> None:
        Rectangle.__init__(corners)
        if label_node.x != (self.NE.x - self.NW.x) and \
                label_node.y != (self.NE.y - self.SE.y):
            raise ValueError(
                "The label_node is not in the midpoint of the rectangle")
        self.label_node = label_node
        self.staircase = staircase

    def __eq__(self, other: 'Room') -> bool:
        return False if not isinstance(other, Room) else \
            self.NE == other.NE and \
            self.SE == other.SE and \
            self.SW == other.SW and \
            self.NW == other.NW and \
            self.label_node == other.label_node

    def __str__(self) -> str:
        return (f"{type(self).__name__} defined by"
                + " [({self.NE.vector.x}, {self.NE.vector.y})"
                + ", ({self.SE.vector.x}, {self.SE.vector.y})"
                + ", ({self.SW.vector.x}, {self.SW.vector.y})"
                + ", ({self.NW.vector.x}, {self.NW.vector.y})]"
                + " labelled: {self.label_node.type}")
