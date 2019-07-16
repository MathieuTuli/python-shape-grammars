'''Shape Rule definitions
'''
from .layout import Layout


class ShapeRule:
    '''ShapeRule Class
    '''

    def __init__(self, name: str) -> None:
        self.name = name

    def __str__(self) -> str:
        return f"ShapeRule {self.name}"

    def apply(self, layout: Layout) -> Layout:
        pass
