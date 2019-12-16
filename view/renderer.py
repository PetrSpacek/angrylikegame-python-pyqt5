import math

from model.cannon import AbsCannon
from model.enemy import AbstEnemy
from model.missile import AbsMissile
from model.collision import AbsCollision
from model.game_info import AbsGameInfo
from utils.geometry import Position
from view.game_graphics import AbsGameGraphics
from visitor import Visitor


class GameRenderer(Visitor):

    def set_game_graphics(self, graphics: AbsGameGraphics):
        self.graphics = graphics

    def visit_cannon(self, cannon: AbsCannon):
        self.graphics.draw_image(cannon.get_position(), cannon.get_icon_path())
        # Draw angle
        x = math.cos(math.radians(cannon.angle)) * 50
        y = math.sin(math.radians(cannon.angle)) * 50
        self.graphics.draw_colored_line(cannon.get_position(), cannon.get_position() + Position(x, y), "green")

    def visit_enemy(self, enemy: AbstEnemy):
        self.graphics.draw_image(enemy.get_position(), enemy.get_icon_path())
        health_str = "{0:.1f}".format(enemy.health) if not float(enemy.health).is_integer() else f"{enemy.health}"
        orig_health_str = "{0:.1f}".format(enemy.orig_health) if not float(enemy.orig_health).is_integer() else f"{enemy.orig_health}"
        self.graphics.draw_colored_text(enemy.get_position() - Position(0, 5), f"{health_str}/{orig_health_str}",
                                        enemy.get_health_color())

    def visit_missile(self, missile: AbsMissile):
        self.graphics.draw_image(missile.get_position(), missile.get_icon_path())

    def visit_collision(self, collision: AbsCollision):
        self.graphics.draw_image(collision.get_position(), collision.get_icon_path())

    def visit_game_info(self, game_info: AbsGameInfo):
        self.graphics.draw_game_info(game_info)
