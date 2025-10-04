import pygame.image

from code.Const import W_SCREEN, C_YELLOW, FONT_PRIMARY
from code.Utils import handle_quit


class Menu:
    def __init__(self, screen):
        self.screen = screen
        self.bg_image = pygame.image.load('./assets/bg_1.png').convert_alpha()
        self.area = self.bg_image.get_rect(left=0, top=0)

    def run(self):

        while True:
            self.screen.blit(self.bg_image, (0, 0))

            self.draw_text("Shapexis", size=64, x=W_SCREEN // 2, y=192, bold=True)
            self.draw_text("Play", size=38, x=W_SCREEN // 2, y=440)

            pygame.display.flip()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    handle_quit(event)
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        return "level"

    def draw_text(self, text, size, x, y, bold=False):
        font = pygame.font.SysFont(FONT_PRIMARY, size, bold=bold)
        text_surface = font.render(text, True, C_YELLOW)
        text_rect = text_surface.get_rect(center=(x, y))
        self.screen.blit(text_surface, text_rect)
