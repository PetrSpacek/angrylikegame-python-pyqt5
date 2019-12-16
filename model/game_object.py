from abc import abstractmethod
from PyQt5.QtGui import QPixmap

from utils.geometry import Position, Rectangle
from visitor import Visitable, Visitor


class GameObject(Visitable):
    def __init__(self, position: Position, icon_path: str):
        self.position = position
        self.icon_path = icon_path

        # Use PyQt's QPixmap to load image and get its dimensions
        pixmap = QPixmap(icon_path)
        self.hitbox_width = pixmap.width()
        self.hitbox_height = pixmap.height()

    def get_position(self):
        return self.position

    def get_hitbox(self) -> Rectangle:
        return Rectangle(self.position.x, self.position.y, self.hitbox_width, self.hitbox_height)

    def _move_by(self, position: Position):
        self.position += position

    def get_icon_path(self) -> str:
        return self.icon_path

    @abstractmethod
    def accept_visitor(self, visitor: Visitor):
        pass
