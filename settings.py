# game options
TITLE = 'Platformer'
WIDTH = 480
HEIGHT = 600
FPS = 60
FONT_NAME = 'Arial'
HS_FILE = 'highscore.txt'
SPRITESHEET = 'spritesheet_jumper.png'

# player properties
PLAYER_ACC = 0.5
PLAYER_FRICTION = -0.12
PLAYER_GRAV = 0.8
PLAYER_JUMP = 21

# game properties
BOOST_POWER = 60
POW_SPAWN_PCT = 7
MOB_FREQ = 5000
PLAYER_LAYER = 2
PLATFORM_LAYER = 1
POW_LAYER = 1
MOB_LAYER = 2
CLOUD_LAYER = 0

# starting platforms
PLATFORM_LIST = [
    (0, HEIGHT - 50),
    (WIDTH / 2 - 50, HEIGHT * 3 / 4),
    (125, HEIGHT - 350),
    (350, 200),
    (280, 100)
]

# define colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
LIGHTBLUE = (0, 155, 155)
DEEP_SKY_BLUE = (0, 191, 255)
AQUA = (0, 255, 255)
BG_COLOR = DEEP_SKY_BLUE
