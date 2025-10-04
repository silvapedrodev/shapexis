import pygame


class Entity:
    def __init__(self, x, y, color, size, hp):
        self.color = color
        self.size = size
        self.radius = size // 2
        self.rect = pygame.Rect(x - self.radius, y - self.radius, size, size)
        self.hp = hp

    def draw(self, screen):
        pygame.draw.circle(screen, self.color, self.rect.center, self.radius)

    def update_rect(self, x, y):
        # atualiza o rect ao mover a entidade
        self.rect.center = (x, y)

    def is_dead(self):
        return self.hp <= 0
