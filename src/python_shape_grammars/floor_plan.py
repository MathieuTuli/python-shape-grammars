'''A floor plan layout
'''
from typing import List

from .room import Room


class FloorPlan:
    def __init__(self,
                 name: str,
                 status: str,
                 starting_rooms: List[Room] = list()) -> None:
        self.name = name
        self.status = status
        self.rooms: List[Room] = starting_rooms

    def __str__(self) -> str:
        return f"{type(self).__name__} {self.name} in {self.status}"

    def add_room(self, room: Room) -> None:
        if not isinstance(room, Room):
            raise ValueError(f"Cannot add room not of type {type(Room)}")
        self.rooms.append(room)

    def remove_room(self, room: Room) -> None:
        if not isinstance(room, Room):
            raise ValueError(f"Cannot add room not of type {type(Room)}")
        raise NotImplementedError

    def rooms_exists(self, rooms: Room) -> bool:
        if not isinstance(rooms, List):
            raise ValueError(f"Cannot parse rooms, not a list")
        for room in rooms:
            if not isinstance(room, Room):
                raise ValueError(f"Cannot add room not of type {type(Room)}")
            raise NotImplementedError
