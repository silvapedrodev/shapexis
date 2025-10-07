# C
C_BLUE = 51, 153, 255
C_CYAN = 0, 255, 255
C_GRAY = 143, 143, 143
C_GREEN = 0, 204, 102
C_GREEN_2 = 139, 224, 200
C_ORANGE = 255, 44, 3
C_PURPLE = 102, 0, 204
C_PURPLE_2 = 109, 46, 219
C_RED = 255, 51, 51
C_RED_2 = 136, 8, 8
C_WHITE = 255, 255, 255
C_YELLOW = 255, 255, 0

# E
ENEMY_COLORS = [C_ORANGE, C_RED, C_PURPLE_2, C_BLUE, C_GREEN, C_GREEN_2, C_CYAN]
ENEMY_SPAWN = 120  # (2 seconds if 60 fps)
ENEMY_SPAWN_DECAY_RATE = 0.85

ENEMY_LEVELS = {
    1: {"size": 10, "hp": 1.5, "damage": 5, "score": 10, "speed": 2.5},
    2: {"size": 25, "hp": 4.5, "damage": 7, "score": 15, "speed": 2},
    3: {"size": 35, "hp": 7, "damage": 9, "score": 28, "speed": 1.5},
    4: {"size": 50, "hp": 9.8, "damage": 12, "score": 40, "speed": 1.3},
    5: {"size": 80, "hp": 13.5, "damage": 15, "score": 75, "speed": 1},
    6: {"size": 200, "hp": 22, "damage": 35, "score": 130, "speed": 1},
}

# F
FONT_PRIMARY = "./assets/fonts/Pixeled.ttf"
FONT_SECONDARY = "./assets/fonts/Bender.otf"

# L
LEVEL_DURATION = 60000  # 1s

# M
MAX_LEVELS = 3

# P
PLAYER_HP = 100
PLAYER_HIT = 1.3

# T
TEXT_SM = 24
TEXT_XL = 64

# S
SIZE_PLAYER = 20
SIZE_H_LINE_PLAYER = 30
SIZE_W_LINE_PLAYER = 4
SIZE_SHOOT = 8

SPEED_ENEMY = 1
SPEED_ENEMY_MULTIPLIER = 1.05

SPEED_PLAYER = 10
SPEED_SHOOT = 8

W_SCREEN = 960
H_SCREEN = 540
