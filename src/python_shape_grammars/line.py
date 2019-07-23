'''Line shape
'''
from typing import Optional

from .vector import Vector


class Line:
    def __init__(self, vector_a: Vector, vector_b: Vector,
                 thickness: int) -> None:
        self.vector_a: Vector = vector_a
        self.vector_b: Vector = vector_b

        ret = vector_a.left_of(vector_b)
        self.left_node: Optional[Vector] = None if ret == - \
            1 else vector_a if ret else vector_b
        self.right_node: Optional[Vector] = None if ret == - \
            1 else vector_b if ret else vector_a
        self.is_horizontal: bool = ret == -1

        ret = vector_a.beneath(vector_b)
        self.bottom_node: Optional[Vector] = None if ret == - \
            1 else vector_a if ret else vector_b
        self.upper_node: Optional[Vector] = None if ret == - \
            1 else vector_b if ret else vector_a
        self.is_vertical: bool = ret == -1

        # defining equation
        self.m: float = (vector_b.y - vector_a.y) / (vector_b.x - vector_a.x)
        self.b: float = vector_a.y - (self.m * vector_a.x)

        self.midpoint: Vector = vector_a.linear_combination(
            vector_b, value=0.5)

    def __str__(self) -> str:
        return f"{type(self).__name__} from {self.vector_a} to {self.vector_b}"

    def __len__(self) -> float:
        return self.vector_a.distance_to(self.vector_b)

    def __eq__(self, other: 'Line') -> bool:
        return False if not isinstance(other, Line) else \
            self.vector_a == self.vector_b and \
            type(self).__name__ == type(other).__name__

    def contains(self, vector: Vector, threshold: float) -> bool:
        '''Threshold is used because the points we used are floats, so we might
        not fall exactlly on the line
        '''
        if not isinstance(vector, Vector):
            raise ValueError(f"Passed in vector is not of type {type(Vector)}")
        return \
            vector.y <= (((self.m * vector.x) + self.b) + threshold) and \
            vector.y >= (((self.m * vector.x) + self.b) - threshold)

    def is_on_midpoint(self, vector: Vector, threshold: float) -> bool:
        '''Threshold is used because the points we used are floats, so we might
        not fall exactlly on the line
        '''
        if not isinstance(vector, Vector):
            raise ValueError(f"Passed in vector is not of type {type(Vector)}")
        return \
            (vector.x <= self.midpoint.x + threshold) and \
            (vector.x >= self.midpoint.x - threshold)
