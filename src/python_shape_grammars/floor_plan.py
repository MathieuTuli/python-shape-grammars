'''A floor plan layout
'''
from typing import List, Optional, Tuple, Union, Dict

from multi_key_dict import multi_key_dict as MKDict

from .floor_plan_elements import Edge, Node
from .components import FloorPlanStatus, EdgeType
# from .database import Database
from .helper import check_argument_uniqueness
from .vector import Vector
from .room import Room


class FloorPlan:
    def __init__(self,
                 name: str,
                 status: FloorPlanStatus,) -> None:
        self.name = name
        self.status = status
        self.nodes: dict = {}
        self.edges: MKDict = MKDict()
        self.rooms: dict = {}

    def __str__(self) -> str:
        return f"{type(self).__name__} {self.name} in {self.status}"

    def add_room(self, room: Room) -> None:
        if not isinstance(room, Room):
            raise ValueError(f"Cannot add room not of type Room")
        self.rooms[room.name] = room

    def remove_room(self, room: Room) -> bool:
        if not isinstance(room, Room):
            raise ValueError(f"Cannot remove room not of type Room")
        if room.name not in self.rooms:
            return False
        del self.rooms[room.name]

    def room_exists(self, room: Room) -> bool:
        if not isinstance(room, Room):
            raise ValueError(
                f"Cannot search for room not of type Room")
        return room.name in self.rooms

    def rooms_exist(self, rooms: List[Room]) -> Tuple[Optional[Room], bool]:
        '''Will optionally return the room it could not find
            - the first one it can't find
        '''
        if not isinstance(rooms, list):
            raise ValueError(f"Cannot search rooms: not a list.")
        for room in rooms:
            if not isinstance(room, Room):
                raise ValueError(
                    f"Cannot search for room not of type Room")
            if not self.room_exists(room):
                return room, False
        return None, True

    def add_node(self,
                 node: Optional[Node] = None,
                 vector: Optional[Vector] = None) -> bool:
        identifier = check_argument_uniqueness(node, vector)
        if isinstance(identifier, Node):
            if str(node.vector) in self.nodes:
                return False
        elif isinstance(identifier, Vector):
            node = Node(vector)
        else:
            raise ValueError(f"Cannot add node. Incorrect identifiers.")
        self.nodes[str(node.vector)] = node
        return True

    def remove_node(self,
                    node: Optional[Node] = None,
                    vector: Optional[Vector] = None,) -> bool:
        identifier = check_argument_uniqueness(node, vector)
        if isinstance(identifier, str):
            pass
        if isinstance(identifier, Node):
            self.node.remove(node)
        elif isinstance(identifier, Vector):
            pass
        else:
            raise ValueError(f"Cannot remove node, incorrect identifier.")
        return True

    def get_node(self,
                 vector: Vector) -> Optional[Node]:
        if isinstance(vector, Vector):
            if str(vector) not in self.nodes:
                return None
            else:
                return self.nodes[str(vector)]
        else:
            raise ValueError(
                f"Cannot search for node without specifying vector.")

    def get_nodes_by_type(self,
                          node_type) -> List[Optional[Node]]:
        raise NotImplementedError

    def node_exists(self,
                    node: Optional[Node] = None,
                    vector: Optional[Vector] = None,) -> bool:
        identifier = check_argument_uniqueness(node, vector)
        if isinstance(identifier, Vector):
            if str(vector) in self.nodes:
                return self.nodes[str(vector)] is not None
        if isinstance(identifier, Node):
            for keys, existing_node in self.nodes.items():
                return node == existing_node
        else:
            raise ValueError(f"Cannot remove node, incorrect identifier.")

    def nodes_exist(self,
                    nodes: List[Union[Node, str, Vector]]) -> \
            Tuple[Optional[Union[Node, Vector]], bool]:
        '''Will optionally return the identifier for the node it could not find
            - the first one it can't find
        '''
        if not isinstance(nodes, list):
            raise ValueError(f"Cannot search nodes: not a list.")
        for node in nodes:
            if isinstance(node, Node) or isinstance(node, Vector):
                ret = self.node_exists(node)
                if not ret:
                    return node, False
        return None, True

    def add_premade_edge(self, edge: Edge) -> None:
        if not isinstance(edge, Edge):
            raise ValueError(f"Cannot add edge not of type {type(Edge)}")
        self.edges[str(edge.node_a.vector), str(edge.node_b.vector),
                   str(edge)] = edge

    def add_new_edge(self, edge_type: EdgeType,
                     node_a: Node, node_b: Node,
                     doors: List['Door'] = None,
                     windows: List['Window'] = None,
                     thickness: int = 1) -> None:
        '''This is bad design, so is adding a new node. This graph should be
        independent of how nodes/edges are made, so to speak
        '''
        edge = Edge(EdgeType, node_a, node_b, doors, windows, thickness)
        self.edges[(str(edge.node_a.vector), str(edge.node_b.vector)),
                   str(edge)] = edge

    def remove_edge(self, edge: Edge) -> bool:
        if not isinstance(edge, Edge):
            raise ValueError("Cannot remove edge not of type Edge")
        if str(edge) in self.edges:
            del self.edges[str(edge)]
            return True
        return False

    def edge_exists(self, edge: Edge) -> bool:
        if not isinstance(edge, Edge):
            raise ValueError(
                "Cannot search for edge not of type Edge")
        return str(edge) in self.edges

    def edges_exist(self, edges: List[Edge]) -> Tuple[Optional[Edge], bool]:
        '''Will optionally return the room it could not find
            - the first one it can't find
        '''
        if not isinstance(edges, list):
            raise ValueError(f"Cannot search rooms: not a list.")
        for edge in edges:
            if not isinstance(edge, Edge):
                raise ValueError(
                    "Cannot search for edge not of type Edge")
            if not self.edge_exists(edge):
                return edge, False
        return None, True
