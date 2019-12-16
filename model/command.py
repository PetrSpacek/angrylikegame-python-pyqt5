from abc import ABC, abstractmethod


class AbsCommand(ABC):

    def __init__(self, receiver):
        self.receiver = receiver

    def do_execute(self):
        self.memento = self.receiver.create_memento()
        self._execute()

    @abstractmethod
    def _execute(self):
        pass

    def do_unexecute(self):
        if self.memento:
            self.receiver.restore_memento(self.memento)


class CannonMoveUp(AbsCommand):

    def _execute(self):
        self.receiver.move_cannon_up()


class CannonMoveDown(AbsCommand):

    def _execute(self):
        self.receiver.move_cannon_down()


class CannonAimUp(AbsCommand):

    def _execute(self):
        self.receiver.aim_cannon_up()


class CannonAimDown(AbsCommand):

    def _execute(self):
        self.receiver.aim_cannon_down()


class CannonShoot(AbsCommand):

    def _execute(self):
        self.receiver.cannon_shoot()


class ToggleShootingMode(AbsCommand):

    def _execute(self):
        self.receiver.toggle_shooting_mode()
