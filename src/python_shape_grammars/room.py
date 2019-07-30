'''A Room in 2D coordinate vectors

extends the Rectangle class
'''
from typing import List

from .floor_plan_elements import RoomNode, Node, Rectangle, Staircase


class Room(Rectangle):
    '''Rectangle Class
    '''
    room_counter = 0

    def __init__(self, corners: List[Node],
                 name: str,
                 room_node: RoomNode,) -> None:
        if not isinstance(name, str):
            raise ValueError("Must use a unique string for the name")
        Rectangle.__init__(self, corners)
        if room_node.vector != self.midpoint:
            raise ValueError(
                f"For {str(self)} -" +
                " The room_node is not in the midpoint of the rectangle")
        self.name = name
        self.room_node = room_node
        self.room_count = Room.room_counter
        Room.room_counter += 1

    def __eq__(self, other: 'Room') -> bool:
        return False if not isinstance(other, Room) else \
            self.NE == other.NE and \
            self.SE == other.SE and \
            self.SW == other.SW and \
            self.NW == other.NW and \
            self.name == other.name and \
            self.room_node == other.room_node and \
            self.room_count == other.room_count and \
            type(self).__name__ == type(other).__name__

    def __str__(self) -> str:
        return (f"{type(self).__name__} defined by"
                + f" [({self.NE.vector.x}, {self.NE.vector.y})"
                + f", ({self.SE.vector.x}, {self.SE.vector.y})"
                + f", ({self.SW.vector.x}, {self.SW.vector.y})"
                + f", ({self.NW.vector.x}, {self.NW.vector.y})]"
                + f" labelled: {self.room_node.room_type}"
                + f" name: {self.name}"
                + f" | count: {self.room_count}")
