'''A floor plan layout
'''
from typing import List, Optional, Tuple

from .edge import Edge
from .node import Node
from .room import Room


class FloorPlan:
    def __init__(self,
                 name: str,
                 status: str,
                 starting_nodes: List[Node],
                 starting_rooms: List[Room] = list()) -> None:
        self.name = name
        self.status = status
        self.rooms: List[Room] = starting_rooms
        self.nodes: List[Node] = starting_nodes

    def __str__(self) -> str:
        return f"{type(self).__name__} {self.name} in {self.status}"

    def add_room(self, room: Room) -> None:
        if not isinstance(room, Room):
            raise ValueError(f"Cannot add room not of type {type(Room)}")
        self.rooms.append(room)

    def remove_room(self, room: Room) -> bool:
        if not isinstance(room, Room):
            raise ValueError(f"Cannot remove room not of type {type(Room)}")
        try:
            self.rooms.remove(room)
            return True
        except ValueError:
            return False

    def room_exists(self, room: Room) -> bool:
        if not isinstance(room, Room):
            raise ValueError(
                f"Cannot search for room not of type {type(Room)}")
        try:
            self.rooms.index(room)
            return True
        except ValueError:
            return False

    def get_room_by_name(self, name: str) -> Optional[Room]:
        for room in self.rooms:
            if room.label_node.name == name:
                return room
        return None

    def rooms_exist(self, rooms: List[Room]) -> Tuple[Optional[Room], bool]:
        '''Will optionally return the room it could not find
            - the first one it can't find
        '''
        if not isinstance(rooms, list):
            raise ValueError(f"Cannot search rooms: not a list.")
        for room in rooms:
            if not isinstance(room, Room):
                raise ValueError(
                    f"Cannot search for room not of type {type(Room)}")
            if not self.room_exists(room):
                return room, False
        return None, True

    def add_node(self, node: Node) -> None:
        if not isinstance(node, Room):
            raise ValueError(f"Cannot add node not of type {type(Node)}")
        self.nodes.append(node)

    def remove_node(self, node: Node) -> bool:
        if not isinstance(node, Node):
            raise ValueError(f"Cannot remove node not of type {type(Node)}")
        try:
            self.node.remove(node)
            return True
        except ValueError:
            return False

    def node_exists(self, node: Node) -> bool:
        if not isinstance(node, Node):
            raise ValueError(
                f"Cannot search for node not of type {type(Node)}")
        try:
            self.node.index(node)
            return True
        except ValueError:
            return False

    def nodes_exist(self, nodes: List[Node]) -> Tuple[Optional[Node], bool]:
        '''Will optionally return the room it could not find
            - the first one it can't find
        '''
        if not isinstance(nodes, list):
            raise ValueError(f"Cannot search rooms: not a list.")
        for node in nodes:
            if not isinstance(node, Node):
                raise ValueError(
                    f"Cannot search for node not of type {type(Node)}")
            if not self.node_exists(node):
                return node, False
        return None, True

    def get_node_by_name(self, name: str) -> Optional[Node]:
        for node in self.nodes:
            if node.name == name:
                return node
        return None

    def add_edge(self, edge: Edge) -> None:
        if not isinstance(edge, Edge):
            raise ValueError(f"Cannot add edge not of type {type(Edge)}")
        self.edges.append(edge)

    def remove_edge(self, edge: Edge) -> bool:
        if not isinstance(edge, Edge):
            raise ValueError(f"Cannot remove edge not of type {type(Edge)}")
        try:
            self.edges.remove(edge)
            return True
        except ValueError:
            return False

    def edge_exists(self, edge: Edge) -> bool:
        if not isinstance(edge, Edge):
            raise ValueError(
                f"Cannot search for edge not of type {type(Edge)}")
        try:
            self.edges.index(edge)
            return True
        except ValueError:
            return False

    def edges_exist(self, edges: List[Edge]) -> Tuple[Optional[Edge], bool]:
        '''Will optionally return the room it could not find
            - the first one it can't find
        '''
        if not isinstance(edges, list):
            raise ValueError(f"Cannot search rooms: not a list.")
        for edge in edges:
            if not isinstance(edge, Edge):
                raise ValueError(
                    f"Cannot search for edge not of type {type(Edge)}")
            if not self.edge_exists(edge):
                return edge, False
        return None, True

    def get_edge_by_name(self, name: str) -> Optional[Edge]:
        for edge in self.edges:
            if edge.name == name:
                return edge
        return None
