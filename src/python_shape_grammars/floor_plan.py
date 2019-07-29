'''A floor plan layout
'''
from typing import List, Optional, Tuple, Union, Dict

from multi_key_dict import multi_key_dict as MKDict

from .floor_plan_elements import Edge, Node
from .components import FloorPlanStatus, EdgeType
# from .database import Database
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

    def remove_room(self, identifier: Union[Room, str]) -> bool:
        if isinstance(identifier, Room):
            identifier = identifier.name
        if not isinstance(identifier, str):
            raise ValueError("Identifier to remove room is of wrong type")
        if identifier not in self.rooms:
            return False
        del self.rooms[identifier]
        return True

    def room_exists(self, identifier: Union[Room, str]) -> bool:
        if isinstance(identifier, Room):
            identifier = identifier.name
        if not isinstance(identifier, str):
            raise ValueError("Identifier to remove room is of wrong type")
        return identifier in self.rooms

    def rooms_exist(self,
                    rooms: List[Union[str, Room]]) -> Tuple[Optional[Room],
                                                            bool]:
        '''Will optionally return the room it could not find
            - the first one it can't find
        '''
        if not isinstance(rooms, list):
            raise ValueError(f"Cannot search rooms: not a list.")
        for room in rooms:
            if not isinstance(room, Room) and not isinstance(room, str):
                raise ValueError(
                    f"Cannot search for room not of type Room or str")
            if not self.room_exists(room):
                return room, False
        return None, True

    def add_node(self,
                 node: Node,) -> bool:
        if isinstance(node, Node):
            if str(node.vector) in self.nodes:
                return False
        else:
            raise ValueError(f"Cannot add node. Incorrect identifiers.")
        self.nodes[str(node.vector)] = node
        return True

    # TODO propogate to edges
    def remove_node(self,
                    node: Node,) -> bool:
        if isinstance(node, Node):
            if str(node.vector) in self.nodes:
                del self.nodes[str(node.vector)]
                return True
            return False
        else:
            raise ValueError(f"Cannot remove node, incorrect identifier.")

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
                    identifier: Union[Vector, Node]) -> bool:
        if isinstance(identifier, Vector):
            if str(identifier) in self.nodes:
                return self.nodes[str(identifier)] is not None
        elif isinstance(identifier, Node):
            for keys, existing_node in self.nodes.items():
                return identifier == existing_node
        else:
            raise ValueError(f"Cannot look for node, incorrect identifier.")

    def nodes_exist(self,
                    nodes: List[Union[Node, str, Vector]]) -> \
            Tuple[Optional[Union[Node, Vector]], bool]:
        '''Will optionally return the identifier for the node it could not find
            - the first one it can't find
        '''
        if not isinstance(nodes, list):
            raise ValueError(f"Cannot search nodes: not a list.")
        for node in nodes:
            ret = self.node_exists(node)
            if not ret:
                return node, False
        return None, True

    # TODO propogate this change to edges/rooms and even check validity
    def update_node_vector(self, node: Node,
                           vector: Vector) -> Tuple[Node, bool]:
        if not isinstance(node, Node) or not isinstance(vector, Vector):
            raise ValueError(
                "Cannot update node when node and vector not specified " +
                "with proper types")
        if not self.node_exists(node):
            return False
        del self.nodes[str(node.vector)]
        node.vector = vector
        self.add_node(node)
        return node, True

    # TODO add nodes of edge if not in graph
    def add_edge(self, edge: Edge) -> None:
        if not isinstance(edge, Edge):
            raise ValueError(f"Cannot add edge not of type {type(Edge)}")
        self.edges[f"{edge.node_a}_{edge.direction}",
                   f"{edge.node_b}_{edge.direction}",
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
                "Cannot search for edge not of type Edge."
                f"\n{edge} is not valid")
        return str(edge) in self.edges

    def edges_exist(self, edges: List[Edge]) -> Tuple[Optional[Edge], bool]:
        '''Will optionally return the room it could not find
            - the first one it can't find
        '''
        if not isinstance(edges, list):
            raise ValueError(f"Cannot search rooms: not a list.")
        for edge in edges:
            if not self.edge_exists(edge):
                return edge, False
        return None, True
