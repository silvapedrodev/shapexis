import pygame.font

from code.Const import FONT_PRIMARY, C_WHITE, C_YELLOW, C_RED, W_SCREEN, C_CYAN


class HUD:
    def __init__(self, player):
        self.player = player
        self.font_main = pygame.font.SysFont(FONT_PRIMARY, 12)
        self.font_small = pygame.font.SysFont(FONT_PRIMARY, 10)
        self.elapsed_time = 0
        self.start_ticks = pygame.time.get_ticks()

    def draw(self, screen, level_name, fps, elapsed_time):
        """Draws HUD information on the screen"""
        # HP Player
        hp_text = self.font_main.render(f"HP: {self.player.hp:02}", True, C_RED)
        screen.blit(hp_text, (20, 5))

        # Timer
        time_text = self.font_main.render(f"| TIMER: {elapsed_time:05.2f}s", True, C_CYAN)
        screen.blit(time_text, (90, 5))

        # level
        level_text = self.font_small.render(f"LEVEL: {level_name}", True, C_WHITE)
        screen.blit(level_text, (20, 60))

        # Score
        score_text = self.font_small.render(f"SCORE: {self.player.score}", True, C_YELLOW)
        screen.blit(score_text, (20, 35))

        # FPS
        fps_text = self.font_small.render(f"FPS: {int(fps)}", True, C_WHITE)
        screen.blit(fps_text, (W_SCREEN - 100, 5))
