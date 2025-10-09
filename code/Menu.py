import sys

import pygame.image

from code.Const import W_SCREEN, C_YELLOW, FONT_PRIMARY, H_SCREEN, C_WHITE, TEXT_XL, TEXT_SM
from code.Utils import handle_quit, draw_background


class Menu:
    def __init__(self, screen):
        self.screen = screen
        self.options = ["PLAY", "SKINS", "SCORE", "EXIT"]
        self.selected_index = 0

    def run(self):

        # Load and play menu audio
        pygame.mixer_music.load('./assets/audio/menu.mp3')
        pygame.mixer_music.play(-1)
        pygame.mixer.music.set_volume(0.4)

        while True:
            draw_background(self.screen)
            self.draw_text("Shapexis", size=TEXT_XL, x=W_SCREEN // 2, y=192)

            # Draw options
            start_y = H_SCREEN - 150
            for i, option in enumerate(self.options):
                y_pos = start_y + i * 40
                color = C_YELLOW if i == self.selected_index else C_WHITE
                display_text = f"-{option}-" if i == self.selected_index else option
                self.draw_text(display_text, size=TEXT_SM, x=W_SCREEN // 2, y=y_pos, color=color)

            pygame.display.flip()

            for event in pygame.event.get():
                handle_quit(event)

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_DOWN:
                        self.selected_index = (self.selected_index + 1) % len(self.options)
                    elif event.key == pygame.K_UP:
                        self.selected_index = (self.selected_index - 1) % len(self.options)
                    elif event.key in (pygame.K_RETURN, pygame.K_SPACE):
                        if self.selected_index == 0:
                            return "level"
                        elif self.selected_index == 1:
                            return "skin_selector"
                        elif self.selected_index == 2:
                            return "score"
                        elif self.selected_index == 3:
                            pygame.quit()
                            sys.exit()

    def draw_text(self, text, size, x, y, color=C_YELLOW):
        font = pygame.font.Font(FONT_PRIMARY, size)
        text_surface = font.render(text, True, color)
        text_rect = text_surface.get_rect(center=(x, y))
        self.screen.blit(text_surface, text_rect)
