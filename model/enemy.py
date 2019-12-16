from model.game_object import GameObject
from model.missile import AbsMissile
from utils.geometry import Position
from visitor import Visitor
from abc import abstractmethod
from config import ENEMY_A_IMG


class AbstEnemy(GameObject):
    def __init__(self, position: Position, icon_path: str, health: int, score_points: int):
        super().__init__(position, icon_path)
        self.health = health
        self.orig_health = health
        self.score_points = score_points

    def accept_visitor(self, visitor: Visitor):
        visitor.visit_enemy(self)

    def is_dead(self):
        return self.health <= 0

    def get_health_color(self) -> str:
        ratio = self.health / self.orig_health * 100
        if 100.0 >= ratio > 66.7:
            return "black"
        if 66.7 >= ratio > 33.4:
            return "orange"
        if 33.4 >= ratio > 0:
            return "red"

    @abstractmethod
    def get_hit_by(self, missile: AbsMissile):
        pass


class EnemyA(AbstEnemy):
    def __init__(self, position: Position, health: int, score_points: int):
        super().__init__(position, ENEMY_A_IMG, health, score_points)

    def get_hit_by(self, missile: AbsMissile):
        self.health -= missile.damage
