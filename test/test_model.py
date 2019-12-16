from unittest.mock import MagicMock

from model.command import CannonShoot, CannonMoveDown
from model.game_model import GameModel
from utils.geometry import Rectangle


def test_command_processing(qtbot, tmpdir):
    m = GameModel()
    m.set_game_area(Rectangle(0, 0, 600, 600))
    cannon_orig_pos = m.cannon.get_position()
    # Register two commands
    m.register_command(CannonMoveDown(m))
    m.register_command(CannonShoot(m))
    # Assert that there are two unprocessed commands
    assert len(m.unprocessed_commands) == 2
    # Simulate time tick
    m.time_tick()
    # Assert that both commands were processed correctly
    assert cannon_orig_pos != m.cannon.get_position() # Cannon has moved
    assert len(m.missiles) > 0 # Missile has been created
    assert len(m.unprocessed_commands) == 0
    assert len(m.processed_commands) == 2

def test_command_undo(qtbot, tmpdir):
    m = GameModel()
    m.set_game_area(Rectangle(0, 0, 600, 600))
    cannon_orig_pos = m.cannon.get_position()
    # Register command and simulate time tick
    m.register_command(CannonMoveDown(m))
    m.time_tick()
    # Assert that command was processed correctly
    assert cannon_orig_pos != m.cannon.get_position()  # Cannon has moved
    # Undo the command
    m.undo_last_command()
    # Assert that command was undone correctly
    assert cannon_orig_pos == m.cannon.get_position()

def test_observer(qtbot, tmpdir):
    m = GameModel()
    m.set_game_area(Rectangle(0, 0, 600, 300))
    # Mock the observer
    observer = MagicMock()
    # Register the observer
    m.register_observer(observer)
    # Simulate GameModel notifying its observers
    m._notify_observers()
    # Assert that observer's method "update" has been called once
    assert observer.update.called == 1

    # Unregister the observer
    m.unregister_observer(observer)
    # Simulate GameModel notifying its observers
    m._notify_observers()
    # Assert that observer's method "update" has NOT been called again
    assert observer.update.called == 1
