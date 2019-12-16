from abc import abstractmethod

class Visitor():

    @abstractmethod
    def visit_cannon(self, cannon):
        pass

    @abstractmethod
    def visit_enemy(self, enemy):
        pass

    @abstractmethod
    def visit_missile(self, missile):
        pass

    @abstractmethod
    def visit_collision(self, collision):
        pass

    @abstractmethod
    def visit_game_info(self, game_info):
        pass


class Visitable():

    @abstractmethod
    def accept_visitor(self, visitor: Visitor):
        pass
