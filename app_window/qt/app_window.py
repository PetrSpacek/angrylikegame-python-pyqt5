from PyQt5 import uic
from PyQt5.QtCore import QTimer
from PyQt5.QtWidgets import QMainWindow, QScrollArea,QHBoxLayout

from app_window.app_window import AbsAppWindow
from config import APP_ROOT, CANVAS_WIDTH, CANVAS_HEIGHT, TIME_TICK_DURATION
from model.game_model import GameModel
from utils.geometry import Rectangle
from view.qt.game_graphics import QtGameGraphics
from view.qt.view import QtGameView
from view.qt.canvas import QtCanvas

qt_creator_file = f'{APP_ROOT}\\ui\\mainWindow.ui'
UiMainWindow, _ = uic.loadUiType(qt_creator_file)


class QtAppWindow(QMainWindow, UiMainWindow, AbsAppWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        UiMainWindow.__init__(self)
        self.setupUi(self)

        model = GameModel()
        self.timer = QTimer()
        self.timer.timeout.connect(model.time_tick)
        view = QtGameView(model)
        controller = view.make_controller()
        canvas = QtCanvas(view, controller)

        # Get Game info labels from "metrics" layout
        layout = self.findChild(QHBoxLayout, "metrics")
        labels = [ layout.itemAt(i).widget() for i in range(0, layout.count())]
        view.set_game_graphics(QtGameGraphics(canvas, labels))

        model.set_game_area(Rectangle(0, 0, CANVAS_WIDTH, CANVAS_HEIGHT))

        canvas_holder = self.findChild(QScrollArea, 'canvasHolder')
        canvas_holder.setWidget(canvas.get_widget())
        canvas_holder.setStyleSheet('background-color: white')

    def start_timer(self):
        self.timer.start(TIME_TICK_DURATION)
