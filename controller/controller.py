from abc import abstractmethod

from model.game_model import AbsGameModel


class AbsGameController:
    def __init__(self, model: AbsGameModel):
        self.model = model

    @abstractmethod
    def process_input(self, event: object):
        pass
