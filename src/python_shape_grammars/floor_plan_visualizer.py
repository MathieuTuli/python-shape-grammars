from PyQt5.QtWidgets import QApplication, QLabel

from .floor_plan import FloorPlan


class FloorPlanVisualizer:
    def __init__(self) -> None:
        self.app = QApplication([])

    def populate_from_floor_plan(self, floor_plan: FloorPlan) -> None:
        raise NotImplementedError

    def visualize(self) -> None:
        label = QLabel("TEST")
        label.show()
        self.app.exec_()


if __name__ == '__main__':
    fpv = FloorPlanVisualizer()
    fpv.visualize()
