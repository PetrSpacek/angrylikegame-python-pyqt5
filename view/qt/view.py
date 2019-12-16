from controller.qt import QtGameController
from model.game_model import AbsGameModel
from model.game_model_proxy import GameModelProxy
from view.view import AbsGameView


class QtGameView(AbsGameView):
    def __init__(self, model: AbsGameModel):
        super().__init__(model)

    def make_controller(self) -> QtGameController:
        return QtGameController(GameModelProxy(self.model))
