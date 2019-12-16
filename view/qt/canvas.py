from PyQt5.QtWidgets import QWidget
from PyQt5.QtCore import Qt
from PyQt5 import QtGui

from controller.qt import QtGameController
from view.canvas import AbsCanvas


class QtCanvasWidget(QWidget):
    def __init__(self, canvas):
        super().__init__()
        self.setFocusPolicy(Qt.ClickFocus)
        self.canvas = canvas

    def keyPressEvent(self, event: QtGui.QKeyEvent):
        self.canvas._controller.process_input(event)

    def paintEvent(self, event: QtGui.QPaintEvent):
        self.canvas._view.render()

    def update(self):
        super().update()


class QtCanvas(AbsCanvas):
    def __init__(self, view, controller: QtGameController):
        super().__init__(view, controller)
        self.widget = QtCanvasWidget(self)

    def get_widget(self) -> QtCanvasWidget:
        return self.widget

    def update(self):
        self.widget.update()
