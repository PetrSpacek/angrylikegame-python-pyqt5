from abc import abstractmethod

from model.game_info import AbsGameInfo
from utils.geometry import Position


class AbsGameGraphics:

    @abstractmethod
    def draw_image(self, position: Position, image_path: str):
        pass

    @abstractmethod
    def draw_colored_text(self, position: Position, text: str, color: str):
       pass

    @abstractmethod
    def draw_colored_line(self, start_position: Position, end_position: Position, color: str):
        pass

    @abstractmethod
    def draw_game_info(self, game_info: AbsGameInfo):
        pass