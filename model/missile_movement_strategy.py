from abc import abstractmethod
import math

from utils.geometry import Position


class MovingStrategy:

    @abstractmethod
    def update_position(self, missile):
        pass


class SimpleMovingStrategy(MovingStrategy):

    def update_position(self, missile):
        x = math.cos(math.radians(missile.angle)) * missile.step_size
        y = math.sin(math.radians(missile.angle)) * missile.step_size
        missile._move_by(Position(x, y))


class RealisticMovingStrategy(MovingStrategy):

    def update_position(self, missile):
        speed = missile.step_size
        gravity = missile.gravity
        angle = math.radians(-missile.angle)
        time = missile.flight_time
        x = (speed * math.cos(angle) * time)
        y = (speed * math.sin(angle) * time) - (gravity * (time ** 2)) / 2

        missile._move_by(Position(x, -y))
        missile.flight_time += 0.1