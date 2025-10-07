import pygame

from code.Const import W_SCREEN, H_SCREEN, MAX_LEVELS
from code.GameOverScreen import GameOverScreen
from code.LevelFactory import LevelFactory
from code.Menu import Menu
from code.Player import Player
from code.SkinSelector import SkinSelector


class Game:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((W_SCREEN, H_SCREEN))
        pygame.display.set_caption('Shapexis')
        self.running = True
        self.state = "menu"
        self.factory = LevelFactory(self.screen, MAX_LEVELS)
        self.current_level = None
        self.selected_skin = "Default"

    def run(self):
        menu = Menu(self.screen)
        player = None

        while self.running:
            events = pygame.event.get()

            if self.state == "menu":
                result = menu.run()

                if result == "level":
                    if player is None:
                        selected_skin = getattr(self, "selected_skin", "Default")
                        player = Player(W_SCREEN // 2, H_SCREEN // 2, skin_name=selected_skin)
                    self.current_level = self.factory.create_level(1, player)
                    self.state = "level"

                elif result == "skin_selector":
                    skin_selector = SkinSelector(self.screen)
                    chosen_skin = skin_selector.run()
                    if chosen_skin == "menu":
                        self.state = "menu"
                    elif isinstance(chosen_skin, str):
                        self.selected_skin = chosen_skin
                        self.state = "menu"

            elif self.state == "level":
                result = self.current_level.run(events)
                if result == "game_over":
                    game_over_screen = GameOverScreen(self.screen)
                    next_state = game_over_screen.run()
                    if next_state == "menu":
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

                elif result == "menu":
                    self.state = "menu"
                    player = None

            pygame.display.flip()

        pygame.quit()
