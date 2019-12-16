from model.command import AbsCommand
from model.game_model import AbsGameModel
from model.game_object import GameObject


class GameModelProxy(AbsGameModel):
    def __init__(self, subject: AbsGameModel):
        self.subject = subject

    def move_cannon_up(self):
        self.subject.move_cannon_up()

    def move_cannon_down(self):
        self.subject.move_cannon_down()

    def aim_cannon_up(self):
        self.subject.aim_cannon_up()

    def aim_cannon_down(self):
        self.subject.aim_cannon_down()

    def cannon_shoot(self):
        self.subject.cannon_shoot()

    def toggle_shooting_mode(self):
        self.subject.toggle_shooting_mode()

    def create_memento(self) -> object:
        return self.subject.create_memento()

    def restore_memento(self, memento):
        self.subject.restore_memento(memento)

    def register_command(self, command: AbsCommand):
        self.subject.register_command(command)

    def undo_last_command(self):
        self.subject.undo_last_command()

