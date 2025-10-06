import pygame

from Code.Const import (W_SCREEN,
                        H_SCREEN,
                        SPEED_PLAYER,
                        C_RED,
                        SIZE_H_LINE_PLAYER,
                        SIZE_W_LINE_PLAYER,
                        SIZE_PLAYER,
                        C_PURPLE,
                        PLAYER_HP)
from Code.Entity import Entity
from Code.Shoot import Shoot


class Player(Entity):
    def __init__(self, x, y):
        super().__init__(x, y, C_PURPLE, SIZE_PLAYER, PLAYER_HP)
        self.speed = SPEED_PLAYER
        self.shoots = []
        self.aim_x = self.rect.centerx
        self.aim_y = self.rect.centery

        self.rect = pygame.Rect(x, y, 40, 40)
        self.hp = PLAYER_HP
        self.score = 0  # começa em 0

        """
            # add skins
            self.image = pygame.image.load("assets/player.png").convert_alpha()
            self.image = pygame.transform.scale(self.image, (40, 40))
    
            # atualiza rect baseado na imagem
            self.rect = self.image.get_rect(center=(x, y))
        """

    def move(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_w]:
            self.rect.y -= self.speed
        if keys[pygame.K_s]:
            self.rect.y += self.speed
        if keys[pygame.K_a]:
            self.rect.x -= self.speed
        if keys[pygame.K_d]:
            self.rect.x += self.speed

        self.rect.centerx = max(self.radius, min(self.rect.centerx, W_SCREEN - self.radius))
        self.rect.centery = max(self.radius, min(self.rect.centery, H_SCREEN - self.radius))

    def shoot(self):
        new_shoot = Shoot(self.aim_x, self.aim_y, pygame.mouse.get_pos()[0], pygame.mouse.get_pos()[1])
        self.shoots.append(new_shoot)

    def update_shoots(self):
        for shoot in self.shoots:
            shoot.update()
        # remove shots from screen
        self.shoots = [s for s in self.shoots if not s.off_screen()]

    def draw(self, screen):
        super().draw(screen)

        # screen.blit(self.image, self.rect) add skin

        mouse_x, mouse_y = pygame.mouse.get_pos()
        dx = mouse_x - self.rect.centerx
        dy = mouse_y - self.rect.centery
        length = SIZE_H_LINE_PLAYER
        distance = max(1, (dx ** 2 + dy ** 2) ** 0.5)
        end_x = self.rect.centerx + dx / distance * length
        end_y = self.rect.centery + dy / distance * length
        pygame.draw.line(screen, C_RED, self.rect.center, (end_x, end_y), SIZE_W_LINE_PLAYER)

        # update aim for shots
        self.aim_x = end_x
        self.aim_y = end_y

        for shoot in self.shoots:
            shoot.draw(screen)

    def add_score(self, value):
        self.score += value
