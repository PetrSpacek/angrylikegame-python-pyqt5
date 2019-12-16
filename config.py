import os

# Path to application root folder
APP_ROOT = os.path.abspath(os.path.join(__file__, '..\\'))
print(APP_ROOT)
ASSETS_FOLDER = f"{APP_ROOT}\\ui\\assets"

# Duration of one game tick (50 default)
TIME_TICK_DURATION = 50

# Duration of collision effect (in seconds)
COLLISION_EFFECT_DURATION = 3 * TIME_TICK_DURATION / 1000

# Canvas size
CANVAS_WIDTH = 1015
CANVAS_HEIGHT = 710

# Images paths
CANNON_A_IMG = f"{ASSETS_FOLDER}\\cannon.png"
MISSILE_A_IMG = f"{ASSETS_FOLDER}/missile.png"
ENEMY_A_IMG = f"{ASSETS_FOLDER}/enemy1.png"
COLLISION_A_IMG = f"{ASSETS_FOLDER}/collision2.png"

# Cannon initial position
CANNON_POS_X = 10
CANNON_POS_Y = 300

# Initial game info
GRAVITY = 10
ENEMIES_CNT = 5
BASE_MISSILE_DAMAGE = 10.2
CANNON_STEP_SIZE = 4
MISSILE_STEP_SIZE = 15

# Enemy details
ENEMY_A_HEALTH = 30
ENEMY_A_SCORE_POINTS = 100
