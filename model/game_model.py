from model.command import AbsCommand
from model.game_info import AbsGameInfo, GameInfoA
from observer import Observable, Observer
from model.game_object import GameObject
from utils.game_object_factory import GameObjectFactoryA
from config import CANNON_POS_X, CANNON_POS_Y, ENEMIES_CNT, COLLISION_EFFECT_DURATION, GRAVITY, MISSILE_STEP_SIZE

from collections import deque
from random import randint
from abc import abstractmethod
from typing import List
import pickle

from utils.geometry import Position, Rectangle


class AbsGameModel:

    def set_game_area(self, area: Rectangle):
        self.game_area = area
        self.enemy_area = Rectangle(self.game_area.x1 + 100, self.game_area.y1 + 150,
                                    self.game_area.x2 - 500, self.game_area.y2 - 20)
        self._game_area_ready()

    @abstractmethod
    def _game_area_ready(self):
        pass

    @abstractmethod
    def get_game_objects(self):
        pass

    @abstractmethod
    def get_game_info(self):
        pass

    @abstractmethod
    def move_cannon_up(self):
        pass

    @abstractmethod
    def move_cannon_down(self):
        pass

    @abstractmethod
    def aim_cannon_up(self):
        pass

    @abstractmethod
    def aim_cannon_down(self):
        pass

    @abstractmethod
    def cannon_shoot(self):
        pass

    @abstractmethod
    def toggle_shooting_mode(self):
        pass

    @abstractmethod
    def create_memento(self) -> object:
        pass

    @abstractmethod
    def restore_memento(self, memento):
        pass

    @abstractmethod
    def register_command(self, command: AbsCommand):
        pass

    @abstractmethod
    def undo_last_command(self):
        pass


class GameModel(Observable, AbsGameModel):
    def __init__(self):
        self.enemies = []
        self.missiles = []
        self.collisions = []
        self.observers = []
        self.go_factory = GameObjectFactoryA()
        self.cannon = self.go_factory.create_cannon(Position(CANNON_POS_X, CANNON_POS_Y))
        self.unprocessed_commands = deque()
        self.processed_commands = deque()
        self.game_info = GameInfoA(self.cannon.active_shooting_mode, self.cannon.angle, MISSILE_STEP_SIZE, GRAVITY)
        self.enemies_in_wave = ENEMIES_CNT

    def time_tick(self):
        self._process_commands()
        self._move_missiles()
        self._remove_old_collisions()
        self._check_collisions()
        self._destroy_objects_outside_game_area()
        if len(self.enemies) == 0:
            self._next_wave()

        self._notify_observers()

    def _game_area_ready(self):
        self._spawn_enemies(self.enemies_in_wave)

    def _next_wave(self):
        self.game_info.increment_wave_number()
        self._reset_level()
        # Increase number of enemies and spawn new wave
        self.enemies_in_wave += 2
        self._spawn_enemies(self.enemies_in_wave)
        # Increase base damage
        self.game_info.set_damage(self.game_info.get_damage() * 1.05)
        self.cannon.update_base_damage(self.game_info.get_damage())
        # Increase base missile speed
        self.game_info.set_missile_speed(self.game_info.get_missile_speed() * 1.05)

    def _reset_level(self):
        self.missiles.clear()
        self.collisions.clear()
        self.unprocessed_commands.clear()
        self.processed_commands.clear()

    def _remove_old_collisions(self):
        for collision in self.collisions:
            if collision.get_age() > COLLISION_EFFECT_DURATION:
                self.collisions.remove(collision)

    def _spawn_enemies(self, number_of_enemies):
        for _ in range(0, number_of_enemies + 1):
            x = randint(self.enemy_area.x1, self.enemy_area.x2)
            y = randint(self.enemy_area.y1, self.enemy_area.y2)
            self.enemies.append(self.go_factory.create_enemy(Position(x, y)))

    def move_cannon_up(self):
        self.cannon.move_up(self._is_object_inside_game_area)
        self._notify_observers()

    def move_cannon_down(self):
        self.cannon.move_down(self._is_object_inside_game_area)
        self._notify_observers()

    def aim_cannon_up(self):
        self.cannon.aim_up()
        self.game_info.set_angle(self.cannon.angle)
        self._notify_observers()

    def aim_cannon_down(self):
        self.cannon.aim_down()
        self.game_info.set_angle(self.cannon.angle)
        self._notify_observers()

    def _move_missiles(self):
        for missile in self.missiles:
            missile.move()

    def _check_collisions(self):
        for missile in self.missiles:
            self._check_collisions_with_enemies(missile)

    def _check_collisions_with_enemies(self, missile):
        for enemy in self.enemies:
            if enemy.get_hitbox().intersects(missile.get_hitbox()):
                self.missiles.remove(missile)
                self.collisions.append(self.go_factory.create_collision(enemy.get_position()))
                enemy.get_hit_by(missile)
                if enemy.is_dead():
                    self.enemies.remove(enemy)
                    self.game_info.add_score_points(enemy.score_points)

    def _destroy_objects_outside_game_area(self):
        for enemy in self.enemies:
            if not self._is_object_inside_game_area(enemy):
                self.enemies.remove(enemy)

        for missile in self.missiles:
            if not self._is_object_inside_game_area(missile):
                self.missiles.remove(missile)

    def cannon_shoot(self):
        missile_batch = self.cannon.shoot(self.game_info)
        self.missiles.extend(missile_batch)
        self._notify_observers()

    def toggle_shooting_mode(self):
        self.cannon.next_shooting_mode()
        self.game_info.set_shooting_mode_name(self.cannon.active_shooting_mode.get_name())
        self.game_info.set_damage(self.cannon.active_shooting_mode.damage)
        self._notify_observers()

    def get_cannon(self):
        return self.cannon

    def get_game_objects(self) -> List[GameObject]:
        return [self.cannon, *self.enemies, *self.missiles, *self.collisions]

    def get_game_info(self) -> AbsGameInfo:
        return self.game_info

    def _is_object_inside_game_area(self, object: GameObject):
        return self.game_area.contains(object.get_hitbox())

    def register_observer(self, observer: Observer):
        self.observers.append(observer)

    def unregister_observer(self, observer: Observer):
        self.observers.remove(observer)

    def _notify_observers(self):
        for observer in self.observers:
            observer.update()

    def register_command(self, command: AbsCommand):
        self.unprocessed_commands.append(command)

    def _process_commands(self):
        while self.unprocessed_commands:
            cmd = self.unprocessed_commands.popleft()
            cmd.do_execute()
            self.processed_commands.appendleft(cmd)

    def undo_last_command(self):
        if self.processed_commands:
            cmd = self.processed_commands.popleft()
            cmd.do_unexecute()
            self._notify_observers()

    def create_memento(self) -> object:
        memento = dict(vars(self))
        # Delete properties that do not need to be pickled (stored as memento)
        del memento["go_factory"]
        del memento["observers"]
        del memento["unprocessed_commands"]
        del memento["processed_commands"]
        return pickle.dumps(memento)

    def restore_memento(self, memento):
        previous_state = pickle.loads(memento)
        vars(self).update(previous_state)
