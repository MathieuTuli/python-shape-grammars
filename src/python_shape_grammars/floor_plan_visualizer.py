import sys

from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtGui import QPainter, QPen
from PyQt5.QtCore import Qt

from .floor_plan import FloorPlan


class FloorPlanVisualizer(QMainWindow):
    def __init__(self, top: int, left: int, width: int, height: int) -> None:
        super().__init__()
        self.floor_plan: FloorPlan = None
        self.top = top
        self.left = left
        self.width = width
        self.height = height
        self.setGeometry(top, left, width, height)
        self.setWindowTitle("Floor Plan Visualizer")
        self.show()

    def populate_from_floor_plan(self, floor_plan: FloorPlan) -> None:
        raise NotImplementedError

    def paintEvent(self, event) -> None:
        painter = QPainter(self)
        painter.setPen(QPen(Qt.black, 1))
        painter.drawLine(self.left, self.top,
                         self.left + self.width, self.top)
        painter.drawLine(self.left, self.top,
                         self.left, self.top + self.width)
        painter.drawLine(self.left, self.top + self.height,
                         self.left + self.width, self.top + self.width)
        painter.drawLine(self.left + self.width, self.top,
                         self.left + self.width, self.top + self.height)

    def visualize(self, painter: QPainter) -> None:
        if self.floor_plan:
            for room in self.floor_plan.rooms:
                rectangle = room.rectangle
                label = room.label_node
                staircase = room.staircase
                if rectangle:
                    painter.setPen(Qt.red, 1)
                    pass
                if label:
                    painter.setPen(Qt.green, 1)
                    pass
                if staircase:
                    painter.setPen(Qt.red, 1)
                    pass


if __name__ == '__main__':
    app = QApplication(sys.argv)
    fpv = FloorPlanVisualizer(top=0, left=0, width=300, height=300)
    sys.exit(app.exec())
