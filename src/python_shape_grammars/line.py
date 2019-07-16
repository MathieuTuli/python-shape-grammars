'''Line shape
'''
from .vector import Vector
from .shape import Shape


class Line(Shape):
    def __init__(self, vector_a: Vector, vector_b: Vector) -> None:
        self.vector_a = vector_a
        self.vector_b = vector_b

        ret = vector_a.left_of(vector_b)
        self.left_node = None if ret == -1 else vector_a if ret else vector_b
        self.right_node = None if ret == -1 else vector_b if ret else vector_a
        self.is_horizontal = True if ret == -1 else False

        ret = vector_a.beneath(vector_b)
        self.bottom_node = None if ret == -1 else vector_a if ret else vector_b
        self.upper_node = None if ret == -1 else vector_b if ret else vector_a
        self.is_vertical = True if ret == -1 else False

    def __str__(self) -> str:
        return f"Line from {self.vector_a} to {self.vector_b}"

    def __len__(self) -> float:
        return self.vector_a.distance_to(self.vector_b)
