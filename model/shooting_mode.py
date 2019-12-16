from abc import abstractmethod

from config import BASE_MISSILE_DAMAGE


class ShootingMode:

    def __init__(self, damage: float):
        self.damage = damage

    def get_damage(self):
        return self.damage

    @abstractmethod
    def update_base_damage(self, damage):
        pass

    @abstractmethod
    def shoot(self, cannon, damage: float, missile_speed: float, gravity: float):
        pass

    @abstractmethod
    def next_mode(self, cannon):
        pass

    @abstractmethod
    def get_name(self) -> str:
        pass


class SimpleShootingMode(ShootingMode):

    def __init__(self):
        super().__init__(BASE_MISSILE_DAMAGE)

    def update_base_damage(self, damage):
        self.damage = damage

    def shoot(self, cannon, damage: float, missile_speed: float, gravity: float):
        cannon.prepare_missile(cannon.get_position(), cannon.get_angle(), damage, missile_speed, gravity)

    def next_mode(self, cannon):
         cannon.use_double_shooting_mode()

    def get_name(self) -> str:
        return "Simple"


class DoubleShootingMode(ShootingMode):

    def __init__(self):
        super().__init__(BASE_MISSILE_DAMAGE / 2)

    def update_base_damage(self, damage):
        self.damage = damage / 2

    def shoot(self, cannon, damage: float, missile_speed: float, gravity: float):
        cannon.prepare_missile(cannon.get_position(), cannon.get_angle() - 5, damage, missile_speed, gravity)
        cannon.prepare_missile(cannon.get_position(), cannon.get_angle() + 5, damage, missile_speed, gravity)

    def next_mode(self, cannon):
        cannon.use_simple_shooting_mode()

    def get_name(self) -> str:
        return "Double missile"
