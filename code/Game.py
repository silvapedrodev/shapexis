import pygame

from Code.Const import W_SCREEN, H_SCREEN, MAX_LEVELS
from Code.LevelFactory import LevelFactory
from Code.Menu import Menu
from Code.Player import Player


class Game:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((W_SCREEN, H_SCREEN))
        pygame.display.set_caption('Shapexis')
        self.running = True
        self.state = "menu"
        self.factory = LevelFactory(self.screen, MAX_LEVELS)
        self.current_level = None

    def run(self):
        menu = Menu(self.screen)
        player = None

        while self.running:
            events = pygame.event.get()

            if self.state == "menu":
                result = menu.run()

                if result == "level":
                    if player is None:
                        player = Player(W_SCREEN // 2, H_SCREEN // 2)
                    self.current_level = self.factory.create_level(1, player)
                    self.state = "level"
            elif self.state == "level":
                result = self.current_level.run(events)

                if result == "game_over":
                    self.state = "menu"
                    player = None

                elif result == "next_level":
                    next_level_number = self.current_level.level_number + 1
                    next_level = self.factory.create_level(next_level_number, player)

                    if next_level:
                        self.current_level = next_level
                    else:
                        print("🎉 Todos os níveis concluídos!")
                        self.state = "menu"
                        player = None

            pygame.display.flip()

        pygame.quit()
