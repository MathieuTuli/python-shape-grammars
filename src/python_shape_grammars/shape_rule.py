'''Shape Rule definitions
'''
from .layout import Layout


class ShapeRule:
    '''ShapeRule Class
    '''

    def __init__(self, name: str) -> None:
        self.name = name

    def __str__(self) -> str:
        return f"{type(self).__name__} {self.name}"

    def apply(self, layout: Layout) -> Layout:
        pass
