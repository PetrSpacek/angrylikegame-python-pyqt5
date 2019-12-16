from model.game_object import GameObject
from model.missile_movement_strategy import MovingStrategy
from utils.geometry import Position
from visitor import Visitor
from config import MISSILE_A_IMG


class AbsMissile(GameObject):
    def __init__(self, position: Position, icon_path: str, angle: float, damage: float, step_size: float, gravity: float,
                 movement_strategy: MovingStrategy):
        super().__init__(position, icon_path)
        self.angle = angle
        self.damage = damage
        self.step_size = step_size
        self.gravity = gravity
        self.movement_strategy = movement_strategy
        self.flight_time = 0

    def move(self):
        self.movement_strategy.update_position(self)

    def accept_visitor(self, visitor: Visitor):
        visitor.visit_missile(self)

    def __repr__(self):
        return f"Missile {self.position}"


class MissileA(AbsMissile):
    def __init__(self, position: Position, angle: float, damage: float, step_size: float, gravity: float,
                 movement_strategy: MovingStrategy):
        super().__init__(position, MISSILE_A_IMG, angle, damage, step_size, gravity, movement_strategy)
