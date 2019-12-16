from model.shooting_mode import ShootingMode
from visitor import Visitor, Visitable


class AbsGameInfo(Visitable):
    def __init__(self, shooting_mode: ShootingMode, angle: int, missile_speed: float, gravity: float):
        self.damage = shooting_mode.get_damage()
        self.shooting_mode_name = shooting_mode.get_name()
        self.missile_speed = missile_speed
        self.angle = angle
        self.gravity = gravity
        self.score = 0
        self.wave_number = 1

    def accept_visitor(self, visitor: Visitor):
        visitor.visit_game_info(self)

    def get_damage(self):
        return self.damage

    def set_damage(self, damage: float):
        self.damage = damage

    def get_angle(self):
        return self.angle

    def set_angle(self, angle: int):
        self.angle = angle

    def get_gravity(self):
        return self.gravity

    def set_gravity(self, gravity: float):
        self.gravity = gravity

    def get_score(self):
        return self.score

    def add_score_points(self, score_points: int):
        self.score += score_points

    def get_shooting_mode_name(self):
        return self.shooting_mode_name

    def set_shooting_mode_name(self, shooting_mode_name: str):
        self.shooting_mode_name = shooting_mode_name

    def get_wave_number(self):
        return self.wave_number

    def increment_wave_number(self):
        self.wave_number += 1

    def get_missile_speed(self):
        return self.missile_speed

    def set_missile_speed(self, speed: float):
        self.missile_speed = speed


class GameInfoA(AbsGameInfo):
    pass

