'''Shape Rule definitions
'''
from .layout import Layout


class ShapeRule:
    '''ShapeRule Class
    '''

    def __init__(self, name: str) -> None:
        self.name = name

    def __str__(self) -> str:
        return f"{type(self).__name__} - {self.name}"

    def apply(self, layout: Layout) -> Layout:
        '''This is where a rule's logic would go
        '''
        raise NotImplementedError("This method is meant to be overwritten")


class TemplateRule(ShapeRule):
    def __init__(self, name: str) -> None:
        ShapeRule.__init__(self, name)

    def apply(self, layout: Layout) -> Layout:
        pass


class NoOverlappingRooms(ShapeRule):
    def __init__(self, name: str) -> None:
        ShapeRule.__init__(self, name)

    def apply(self, layout: Layout) -> Layout:
        raise NotImplementedError


class WindowRoomBind(ShapeRule):
    def __init__(self, name: str) -> None:
        ShapeRule.__init__(self, name)

    def apply(self, layout: Layout) -> Layout:
        raise NotImplementedError


class HallwayToRoom(ShapeRule):
    def __init__(self, name: str) -> None:
        ShapeRule.__init__(self, name)

    def apply(self, layout: Layout) -> Layout:
        raise NotImplementedError


class MinimumRoomDimensions(ShapeRule):
    def __init__(self, name: str) -> None:
        ShapeRule.__init__(self, name)

    def apply(self, layout: Layout) -> Layout:
        raise NotImplementedError


class MultFloorStaircase(ShapeRule):
    def __init__(self, name: str) -> None:
        ShapeRule.__init__(self, name)

    def apply(self, layout: Layout) -> Layout:
        raise NotImplementedError


class WindowIndependence(ShapeRule):
    def __init__(self, name: str) -> None:
        ShapeRule.__init__(self, name)

    def apply(self, layout: Layout) -> Layout:
        raise NotImplementedError


class DoorIndependence(ShapeRule):
    def __init__(self, name: str) -> None:
        ShapeRule.__init__(self, name)

    def apply(self, layout: Layout) -> Layout:
        raise NotImplementedError


class StaircaseIndependence(ShapeRule):
    def __init__(self, name: str) -> None:
        ShapeRule.__init__(self, name)

    def apply(self, layout: Layout) -> Layout:
        raise NotImplementedError
