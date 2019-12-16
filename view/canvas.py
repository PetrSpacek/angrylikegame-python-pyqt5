from abc import abstractmethod

from controller import AbsGameController
from observer import Observer


class AbsCanvas(Observer):

    def __init__(self, view, controller: AbsGameController):
        super().__init__()
        self._view = view
        self._controller = controller
        self._view.model.register_observer(self)

    @abstractmethod
    def update(self):
        pass
