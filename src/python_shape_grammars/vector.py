'''2D Vector for grid-based alignment of the Graph
'''
import math


class Vector:
    def __init__(self, x: float, y: float) -> None:
        self.x: float = float(x)
        self.y: float = float(y)

    def __str__(self) -> str:
        return f"{type(self).__name__} ({self.x},{self.y})"

    def __add__(self, other: 'Vector') -> 'Vector':
        pass

    def __eq__(self, other: 'Vector') -> bool:
        return False if not isinstance(other, Vector) else \
            True if self.x == other.x and self.y == other.y else False

    def left_of(self, other: 'Vector') -> int:
        '''Returns int whether or not the vector is the left of the other

        @return 0 if not the left vector
        @return 1 if the left vector
        @return -1 if the vectors are on the same horizontal line
        '''
        if not isinstance(other, Vector):
            raise ValueError(f"Passed in vector is not of type {type(Vector)}")
        return 1 if self.x < other.x else 0 if self.x > other.x else -1

    def right_of(self, other: 'Vector') -> int:
        '''Returns int whether or not the vector is the right of the other

        @return 0 if not the right vector
        @return 1 if the right vector
        @return -1 if the vectors are on the same horizontal line
        '''
        if not isinstance(other, Vector):
            raise ValueError(f"Passed in vector is not of type {type(Vector)}")
        return 1 if self.x > other.x else 0 if self.x < other.x else -1

    def beneath(self, other: 'Vector') -> int:
        '''Returns int whether or not the vector is beneath the other

        @return 0 if not beneath the vector
        @return 1 if beneath the vector
        @return -1 if the vectors are on the same vertical line
        '''
        if not isinstance(other, Vector):
            raise ValueError(f"Passed in vector is not of type {type(Vector)}")
        return 1 if self.y < other.y else 0 if self.y > other.y else -1

    def above(self, other: 'Vector') -> int:
        '''Returns int whether or not the vector is above the other

        @return 0 if not above the vector
        @return 1 if above the vector
        @return -1 if the vectors are on the same vertical line
        '''
        if not isinstance(other, Vector):
            raise ValueError(f"Passed in vector is not of type {type(Vector)}")
        return 1 if self.y > other.y else 0 if self.y < other.y else -1

    def distance_to(self, other: 'Vector') -> float:
        if not isinstance(other, Vector):
            raise ValueError(f"Passed in vector is not of type {type(Vector)}")
        return math.sqrt((self.x - other.x) ^ 2 + (self.y - other.y) ^ 2)

    def linear_combination(self, other: 'Vector',
                           value: float, self_value: float = None) -> 'Vector':
        if not isinstance(other, Vector):
            raise ValueError(f"Passed in vector is not of type {type(Vector)}")
        self_value = value if self_value is None else self_value
        return Vector(x=((self.x * self_value) + (other.x * value)),
                      y=((self.y * self_value) + (other.y * value)))
