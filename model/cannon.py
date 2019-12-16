from abc import abstractmethod
from typing import List

from config import CANNON_STEP_SIZE, CANNON_A_IMG
from model.game_info import AbsGameInfo
from model.game_object import GameObject
from utils.geometry import Position
from visitor import Visitor
from model.missile import AbsMissile
from model.shooting_mode import SimpleShootingMode, DoubleShootingMode


class AbsCannon(GameObject):
    def __init__(self, position: Position, icon_path: str, go_factory, step_size):
        super().__init__(position, icon_path)
        self.go_factory = go_factory
        self.step_size = step_size
        self.missile_batch = []
        self.simple_shooting_mode = SimpleShootingMode()
        self.double_shooting_mode = DoubleShootingMode()
        self.angle = 0

    def move_up(self, is_move_valid):
        self._move_by(Position(0, -self.step_size))
        if not is_move_valid(self): # Revert cannon's move up if it is not valid
            self._move_by(Position(0, self.step_size))

    def move_down(self, is_move_valid):
        self._move_by(Position(0, self.step_size))
        if not is_move_valid(self): # Revert cannon's move down if it is not valid
            self._move_by(Position(0, -self.step_size))

    @abstractmethod
    def aim_up(self):
        pass

    @abstractmethod
    def aim_down(self):
        pass

    def shoot(self, game_info: AbsGameInfo) -> List[AbsMissile]:
        self.missile_batch.clear()
        self.active_shooting_mode.shoot(self, game_info.get_damage(), game_info.get_missile_speed(), game_info.get_gravity())
        return self.missile_batch

    def prepare_missile(self, position: Position, angle: int, damage: float, missile_speed: float, gravity: float):
        self.missile_batch.append(self.go_factory.create_missile(position, angle, damage, missile_speed, gravity))

    def use_simple_shooting_mode(self):
        self.active_shooting_mode = self.simple_shooting_mode

    def use_double_shooting_mode(self):
        self.active_shooting_mode = self.double_shooting_mode

    def next_shooting_mode(self):
        self.active_shooting_mode.next_mode(self)

    def update_base_damage(self, damage):
        self.simple_shooting_mode.update_base_damage(damage)
        self.double_shooting_mode.update_base_damage(damage)

    def accept_visitor(self, visitor: Visitor):
        visitor.visit_cannon(self)

    def get_step_size(self):
        return self.step_size

    def get_angle(self):
        return self.angle


class CannonA(AbsCannon):
    def __init__(self, position: Position, go_factory):
        super().__init__(position, CANNON_A_IMG, go_factory, CANNON_STEP_SIZE)
        self.use_simple_shooting_mode()

    def aim_up(self):
        if self.angle - 10 > -80:
            self.angle -= 10

    def aim_down(self):
        if self.angle + 10 < 80:
            self.angle += 10
