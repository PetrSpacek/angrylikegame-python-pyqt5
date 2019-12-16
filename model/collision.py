from model.game_object import GameObject
from utils.geometry import Position
from visitor import Visitor
from datetime import datetime
from PyQt5.QtGui import QPixmap
from config import COLLISION_A_IMG


class LifetimeLimitedGameObject(GameObject):
    def __init__(self, position: Position, icon: QPixmap):
        self.created_on = datetime.now()
        super().__init__(position, icon)

    def get_age(self):
        return (datetime.now() - self.created_on).total_seconds()


class AbsCollision(LifetimeLimitedGameObject):

    def accept_visitor(self, visitor: Visitor):
        visitor.visit_collision(self)


class CollisionA(AbsCollision):
    def __init__(self, position: Position):
        super().__init__(position, COLLISION_A_IMG)
