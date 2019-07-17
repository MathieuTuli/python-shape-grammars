from typing import List

from .rectangle import Rectangle
from .node import Node


class Staircase(Rectangle):
    def __init__(self, corners: List[Node]):
        Rectangle.__init__(corners)
