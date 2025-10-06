from Code.Level import Level
from Code.Const import ENEMY_SPAWN, ENEMY_SPAWN_DECAY_RATE, SPEED_ENEMY_MULTIPLIER


class LevelFactory:
    def __init__(self, screen, max_levels):
        self.screen = screen
        self.max_levels = max_levels

    def create_level(self, level_number, player):
        """Creates and returns a level."""
        if level_number > self.max_levels:
            return None

        # Progressive difficulty
        spawn_delay = max(30, int(ENEMY_SPAWN * (ENEMY_SPAWN_DECAY_RATE ** (level_number - 1))))
        speed_multiplier = round(1.0 * (SPEED_ENEMY_MULTIPLIER ** (level_number - 1)), 2)

        level = Level(
            screen=self.screen,
            player=player,
            level_number=level_number,
            max_levels=self.max_levels,
            spawn_delay=spawn_delay,
            speed_multiplier=speed_multiplier
        )

        return level
