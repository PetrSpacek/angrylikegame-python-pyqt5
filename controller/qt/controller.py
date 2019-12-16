from PyQt5.QtGui import QKeyEvent
from PyQt5.QtCore import Qt

from controller.controller import AbsGameController
from model.command import CannonMoveUp, CannonMoveDown, CannonAimUp, CannonAimDown, CannonShoot, ToggleShootingMode
from model.game_model import AbsGameModel


class QtGameController(AbsGameController):
    def __init__(self, model: AbsGameModel):
        super().__init__(model)

    def process_input(self, event: QKeyEvent):
        if event.key() == Qt.Key_Up:
            self.model.register_command(CannonMoveUp(self.model))
        elif event.key() == Qt.Key_Down:
            self.model.register_command(CannonMoveDown(self.model))
        elif event.key() == Qt.Key_Left:
            self.model.register_command(CannonAimUp(self.model))
        elif event.key() == Qt.Key_Right:
            self.model.register_command(CannonAimDown(self.model))
        elif event.key() == Qt.Key_Space:
            self.model.register_command(CannonShoot(self.model))
        elif event.key() == Qt.Key_M:
            self.model.register_command(ToggleShootingMode(self.model))
        elif event.key() == Qt.Key_Z:
            self.model.undo_last_command()
