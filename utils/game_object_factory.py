from abc import abstractmethod

from model.cannon import AbsCannon, CannonA
from model.collision import AbsCollision, CollisionA
from model.enemy import AbstEnemy, EnemyA
from model.missile import AbsMissile, MissileA
from model.missile_movement_strategy import RealisticMovingStrategy

from config import ENEMY_A_HEALTH, ENEMY_A_SCORE_POINTS
from utils.geometry import Position


class AbsGameObjectFactory():

    @abstractmethod
    def create_cannon(self, position: Position) -> AbsCannon:
        pass

    @abstractmethod
    def create_enemy(self, position: Position) -> AbstEnemy:
        pass

    @abstractmethod
    def create_missile(self, position: Position, angle: int, damage: float, missile_speed: float, gravity: float) -> AbsMissile:
        pass

    @abstractmethod
    def create_collision(self, position: Position) -> AbsCollision:
        pass


class GameObjectFactoryA(AbsGameObjectFactory):

    def create_cannon(self, position: Position):
        return CannonA(position, self)

    def create_enemy(self, position: Position):
        return EnemyA(position, ENEMY_A_HEALTH, ENEMY_A_SCORE_POINTS)

    def create_missile(self, position: Position, angle: int, damage: float, missile_speed: float, gravity: float) -> AbsMissile:
        return MissileA(position, angle, damage, missile_speed, gravity, RealisticMovingStrategy())

    def create_collision(self, position: Position):
        return CollisionA(position)
