'''A floor plan layout
'''
from typing import List

from .room import Room
from .node import Node
from .edge import Edge


class FloorPlan:
    def __init__(self,
                 name: str,
                 status: str,
                 starting_nodes: List[Node] = list(),
                 starting_edges: List[Edge] = list()) -> None:
        self.name = name
        self.status = status
        self.nodes: List[Node] = starting_nodes
        self.edges: List[Edge] = starting_edges

    def __str__(self) -> str:
        return f"FloorPlan {self.name} in {self.status}"

    def add_room(self, room: Room):
        pass
