#
# from model.game_model import GameModel
#
# m = GameModel()
# m.cannon_shoot = MagicMock()
# m.register_command(CannonShoot(m))
# m.cannon_shoot.assert_called_with("3")

class Nib:
    def __init__(self):
        self.n = 4

    def method(self):
        return self.n



class Foo:

    def method(self, method):
        if method() == 4:
            print("ratata")

nib = Nib()
foo = Foo()
foo.method(nib.method)