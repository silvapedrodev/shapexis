import math
from Code.Entity import Entity
from Code.Const import W_SCREEN, H_SCREEN, SPEED_SHOOT, SIZE_SHOOT, C_YELLOW


class Shoot(Entity):
    def __init__(self, x, y, target_x, target_y):
        super().__init__(x, y, C_YELLOW, SIZE_SHOOT, 1)
        self.speed = SPEED_SHOOT

        self.pos_x = x
        self.pos_y = y

        # calculate normalized direction
        dx = target_x - x
        dy = target_y - y
        dist = math.hypot(dx, dy)
        if dist == 0:
            dist = 1
        self.dir_x = dx / dist
        self.dir_y = dy / dist

    def update(self):
        self.pos_x += self.dir_x * self.speed
        self.pos_y += self.dir_y * self.speed

        self.rect.centerx = int(self.pos_x)
        self.rect.centery = int(self.pos_y)

    def off_screen(self):
        return (self.rect.right < 0 or self.rect.left > W_SCREEN or
                self.rect.bottom < 0 or self.rect.top > H_SCREEN)
