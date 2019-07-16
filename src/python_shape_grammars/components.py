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


class NodeType:
    pass


class EdgeType:
    pass


class Window:
    pass


class Door:
    pass


class Rectangle
