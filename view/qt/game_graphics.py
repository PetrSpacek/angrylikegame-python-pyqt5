from PyQt5.QtCore import QPoint
from PyQt5.QtGui import QPainter, QPixmap, QPen, QColor

from model.game_info import AbsGameInfo
from utils.geometry import Position
from view.game_graphics import AbsGameGraphics
from view.qt.canvas import QtCanvas


class QtGameGraphics(AbsGameGraphics):
    def __init__(self, canvas: QtCanvas, labels: []):
        self.canvas = canvas
        self.labels = labels

    def draw_image(self, position: Position, image_path: str):
        painter = QPainter(self.canvas.get_widget()) # QPainter needs to be created before every drawing
        painter.drawPixmap(QPoint(position.x, position.y), QPixmap(image_path))

    def draw_colored_text(self, position: Position, text: str, color: str):
        pen = QPen()
        pen.setColor(QColor(color))
        painter = QPainter(self.canvas.get_widget()) # QPainter needs to be created before every drawing
        painter.setPen(pen)
        painter.drawText(QPoint(position.x, position.y), text)

    def draw_colored_line(self, start_position: Position, end_position: Position, color: str):
        pen = QPen()
        pen.setColor(QColor(color))
        pen.setDashOffset(1)
        pen.setWidth(2)
        painter = QPainter(self.canvas.get_widget())
        painter.setPen(pen)
        painter.drawLine(QPoint(start_position.x, start_position.y), QPoint(end_position.x, end_position.y))

    def draw_game_info(self, game_info: AbsGameInfo):
        self.labels[0].setText(f"Shooting mode: {game_info.get_shooting_mode_name()}")
        self.labels[1].setText(f"Damage: {min_precision(game_info.get_damage())}")
        self.labels[2].setText(f"Missile speed: {min_precision(game_info.get_missile_speed())}")
        self.labels[3].setText(f"Angle: {- game_info.get_angle()}")
        self.labels[4].setText(f"Gravity: {min_precision(game_info.get_gravity())}")
        self.labels[5].setText(f"Score: {game_info.get_score()}")
        self.labels[6].setText(f"Wave: {game_info.get_wave_number()}")

def min_precision(x) -> str:
    f = float(x)
    if f.is_integer():
        return f"{int(f)}"
    else:
        return "{0:.1f}".format(f)