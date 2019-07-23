'''A floor plan layout
'''
from typing import List, Optional, Tuple, Union

from .components import FloorPlanStatus
from .floor_plan_elements import Edge, Node
from .helper import check_argument_uniqueness
from .vector import Vector
from .room import Room


class FloorPlan:
    def __init__(self,
                 name: str,
                 status: FloorPlanStatus,
                 starting_nodes: List[Node] = list(),
                 starting_edges: List[Edge] = list(),
                 starting_rooms: List[Room] = list()) -> None:
        self.name = name
        self.status = status.value
        self.nodes: List[Node] = starting_nodes
        self.edges: List[Edge] = starting_edges
        self.rooms: List[Room] = starting_rooms

    def __str__(self) -> str:
        return f"{type(self).__name__} {self.name} in {self.status}"

    def add_room(self, room: Room) -> None:
        if not isinstance(room, Room):
            raise ValueError(f"Cannot add room not of type {type(Room)}")
        for existing_room in self.rooms:
            if existing_room.label_node.name == room.label_node.name:
                raise ValueError("Trying to add a room with duplicate name")
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

    def add_node(self,
                 node: Optional[Union] = None,
                 vector: Optional[Vector] = None,
                 points: Optional[Tuple[float, float]] = None) -> bool:
        check_argument_uniqueness(node, vector, points)
        if node is not None and isinstance(node, Node):
            for existing_node in self.nodes:
                if existing_node.name == node.name:
                    return False

        elif vector is not None and isinstance(vector, Vector):
            node = Node(vector)
        elif points is not None and isinstance(points, tuple):
            node = Node(points)
        else:
            raise ValueError(f"Cannot add node not of type {type(Node)}")
        self.nodes.append(node)
        return True

    def remove_node(self,
                    name: Optional[str] = None,
                    node: Optional[Union] = None,
                    vector: Optional[Vector] = None,
                    points: Optional[Tuple[float, float]] = None) -> bool:
        check_argument_uniqueness(name, node, vector, points)
        if name is not None and isinstance(name, str):
            pass
        if node is not None and isinstance(node, Node):
            self.node.remove(node)
        elif vector is not None and isinstance(vector, Vector):
            pass
        elif points is not None and isinstance(points, tuple):
            pass
        else:
            raise ValueError(f"Cannot remove node not of type {type(Node)}")
        return True

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
        for existing_edge in self.edges:
            if existing_edge.name == edge.name:
                raise ValueError("Trying to add a edge with duplicate name")
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
