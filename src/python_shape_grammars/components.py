# from collections import dataclass

import enum


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
        return self.value

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


EdgeType = enum.Enum(
    'EdgeType', ['wall', 'empty', 'label'])

RoomType = enum.Enum(
    'RoomType', ['kitchen', 'hallway', 'dining', 'living', 'other', 'bed',
                 'bath', 'closet', 'garage', 'staircase'])

FloorPlanStatus = enum.Enum(
    'FloorPlanStatus', ['start', 'generating', 'done'])
