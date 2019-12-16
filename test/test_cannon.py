from model.game_info import GameInfoA
from utils.game_object_factory import GameObjectFactoryA
from utils.geometry import Position


def test_shooting_mode_toggle(qtbot):
    factory = GameObjectFactoryA()
    cannon = factory.create_cannon(Position(0,0))
    orig_shooting_mode = cannon.active_shooting_mode
    # Switch to next shooting mode
    cannon.next_shooting_mode()
    assert cannon.active_shooting_mode != orig_shooting_mode
    # Switch back to original shooting mode
    cannon.next_shooting_mode()
    assert cannon.active_shooting_mode == orig_shooting_mode

def test_simple_shooting_mode(qtbot):
    factory = GameObjectFactoryA()
    cannon = factory.create_cannon(Position(0, 0))
    cannon.use_simple_shooting_mode()
    damage = cannon.active_shooting_mode.get_damage()
    angle = 0
    gravity = 10
    missile_speed = 5
    game_info = GameInfoA(cannon.active_shooting_mode, angle, missile_speed, gravity)
    angle = cannon.angle
    missiles = cannon.shoot(game_info)
    assert len(missiles) == 1
    assert missiles[0].get_position() == Position(0, 0)
    assert missiles[0].angle == angle
    assert missiles[0].step_size == missile_speed
    assert missiles[0].damage == damage
    assert missiles[0].gravity == gravity

def test_double_shooting_mode(qtbot):
    factory = GameObjectFactoryA()
    cannon = factory.create_cannon(Position(0,0))
    cannon.use_double_shooting_mode()
    damage = cannon.active_shooting_mode.get_damage()
    angle = 0
    gravity = 10
    missile_speed = 5
    game_info = GameInfoA(cannon.active_shooting_mode, angle, missile_speed, gravity)
    angle = cannon.angle
    missiles = cannon.shoot(game_info)
    assert len(missiles) == 2
    assert missiles[0].get_position() == Position(0, 0)
    assert missiles[0].angle == angle -5
    assert missiles[0].step_size == missile_speed
    assert missiles[0].damage == damage
    assert missiles[0].gravity == gravity

    assert missiles[1].get_position() == Position(0, 0)
    assert missiles[1].angle == angle +5
    assert missiles[1].step_size == missile_speed
    assert missiles[1].damage == damage
    assert missiles[1].gravity == gravity