import pygame
from code.Const import W_SCREEN, H_SCREEN, FONT_PRIMARY, C_WHITE, C_YELLOW, C_GRAY, C_RED
from code.Data_Skins import SKINS
from code.Utils import handle_quit


class SkinSelector:
    def __init__(self, screen):
        self.screen = screen
        self.font_title = pygame.font.Font(FONT_PRIMARY, 48)
        self.font = pygame.font.Font(FONT_PRIMARY, 24)
        self.skins = list(SKINS.items())
        self.index = 0
        self.selected_skin = None

    def run(self):
        while True:
            self.screen.fill((0, 0, 0))

            for event in pygame.event.get():
                handle_quit(event)
                if event.type == pygame.KEYDOWN:
                    if event.key in (pygame.K_RIGHT, pygame.K_d):
                        self.index = (self.index + 1) % len(self.skins)
                    elif event.key in (pygame.K_LEFT, pygame.K_a):
                        self.index = (self.index - 1) % len(self.skins)
                    elif event.key in (pygame.K_RETURN, pygame.K_SPACE):
                        name, data = self.skins[self.index]
                        if data["unlocked"]:
                            self.selected_skin = name
                            return name
                    elif event.key == pygame.K_ESCAPE:
                        return "menu"

            name, data = self.skins[self.index]
            image = pygame.image.load(data["path"]).convert_alpha()
            image = pygame.transform.scale(image, (100, 100))
            rect = image.get_rect(center=(W_SCREEN // 2, H_SCREEN // 2 - 40))
            self.screen.blit(image, rect)

            # skin nane
            name_color = C_YELLOW if data["unlocked"] else C_RED
            name_text = self.font.render(name, True, name_color)
            name_rect = name_text.get_rect(center=(W_SCREEN // 2, H_SCREEN // 2 + 80))
            self.screen.blit(name_text, name_rect)

            if not data["unlocked"]:
                locked = self.font.render("LOCKED", True, C_GRAY)
                locked_rect = locked.get_rect(center=(W_SCREEN // 2, H_SCREEN // 2 + 120))
                self.screen.blit(locked, locked_rect)

            title = self.font_title.render("SELECT YOUR SKIN", True, C_WHITE)
            title_rect = title.get_rect(center=(W_SCREEN // 2, 100))
            self.screen.blit(title, title_rect)

            pygame.display.flip()
