from abc import abstractmethod

from controller import AbsGameController
from model.game_model import AbsGameModel
from view.game_graphics import AbsGameGraphics
from view.renderer import GameRenderer


class AbsGameView():
    def __init__(self, model: AbsGameModel):
        self.model = model
        self.renderer = GameRenderer()

    def set_game_graphics(self, graphics: AbsGameGraphics):
        self.renderer.set_game_graphics(graphics)

    def render(self):
        # Render Game info
        self.model.get_game_info().accept_visitor(self.renderer)
        # Render Game objects
        for go in self.model.get_game_objects():
            go.accept_visitor(self.renderer)

    @abstractmethod
    def make_controller(self) -> AbsGameController:
        pass