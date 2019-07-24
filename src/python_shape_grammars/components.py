# from collections import dataclass

from .typed_tuple import TypedTuple
from .vector import Vector


class EdgeDirection:
    def __init__(self, direction: str):
        if direction == 'N':
            self.integer_value = 0
            self.value = direction
        elif direction == 'NE':
            self.integer_value = 1
            self.value = direction
        elif direction == 'E':
            self.integer_value = 2
            self.value = direction
        elif direction == 'SE':
            self.integer_value = 3
            self.value = direction
        elif direction == 'S':
            self.integer_value = 4
            self.value = direction
        elif direction == 'SW':
            self.integer_value = 5
            self.value = direction
        elif direction == 'W':
            self.integer_value = 6
            self.value = direction
        elif direction == 'NW':
            self.integer_value = 7
            self.value = direction
        else:
            raise ValueError(
                f"Direction {direction} is not a value direction. Please" +
                " choose from one of" +
                " ['N', 'NE', 'E', 'SE', 'S', 'SW', 'W', 'NW']")

    def __str__(self) -> str:
        return f"{type(self).__name__} | {self.value} or {self.integer_value}"

    def __eq__(self, other: 'EdgeDirection') -> bool:
        return False if not isinstance(other, EdgeDirection) else \
            self.value == other.value and \
            self.integer_value == other.integer_value

    def reverse(self):
        if self.value == 'N':
            return EdgeDirection('S')
        if self.value == 'NE':
            return EdgeDirection('SW')
        if self.value == 'E':
            return EdgeDirection('W')
        if self.value == 'SE':
            return EdgeDirection('NW')
        if self.value == 'S':
            return EdgeDirection('N')
        if self.value == 'SW':
            return EdgeDirection('NE')
        if self.value == 'W':
            return EdgeDirection('E')
        if self.value == 'NW':
            return EdgeDirection('SE')


class EdgeType(TypedTuple):
    value = str

    def _parse_value(value):
        values = ['wall', 'empty', 'label edge']
        if value not in values:
            raise ValueError(f"Edge Type must be one of {values}")
        return value


class RoomType(TypedTuple):
    '''Defining Room Types
    '''
    value = str

    def _parse_value(value):
        room_types = ['kitchen', 'hallway', 'dining room', 'living room']
        if value not in room_types:
            raise ValueError(f"Argument room_type must be one of {room_types}")
        return value


class FloorPlanStatus(TypedTuple):
    '''Defining Room Types
    '''
    value = str

    def _parse_value(value):
        status_types = ['start', 'generating', 'done']
        if value not in status_types:
            raise ValueError(
                f"Argument room_type must be one of {status_types}")
        return value
