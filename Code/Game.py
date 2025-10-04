import pygame

from code.Const import W_SCREEN, H_SCREEN
from code.Level import Level
from code.Menu import Menu


class Game:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((W_SCREEN, H_SCREEN))
        pygame.display.set_caption('Shapexis')
        self.running = True
        self.state = "menu"

    def run(self):
        menu = Menu(self.screen)
        level = Level(self.screen)
        while self.running:
            events = pygame.event.get()
            if self.state == "menu":
                result = menu.run()
                if result == "level":
                    self.state = "level"
                    level = Level(self.screen)
            elif self.state == "level":
                result = level.run(events)
                if result == "game_over":
                    self.state = "menu"

            pygame.display.flip()

        pygame.quit()
