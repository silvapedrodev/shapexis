import random, math
from Code.Const import W_SCREEN, H_SCREEN, ENEMY_LEVELS, ENEMY_COLORS
from Code.Entity import Entity


class Enemy(Entity):
    def __init__(self, player, speed_multiplier):
        # levels and their spawn probabilities
        levels = [1, 2, 3, 4, 5, 6]
        weights = [30, 25, 20, 15, 9, 2]

        level = random.choices(levels, weights=weights, k=1)[0]
        data = ENEMY_LEVELS[level]

        size = data["size"]
        hp = data["hp"]
        damage = data["damage"]
        score = data["score"]
        base_speed = data["speed"]

        x = random.randint(0, W_SCREEN)
        y = random.randint(0, H_SCREEN)

        color = random.choice(ENEMY_COLORS)

        super().__init__(x, y, color, size, hp)
        self.level = level
        self.speed = base_speed * speed_multiplier
        self.player = player
        self.damage = damage
        self.score = score

    def update(self):
        # movement towards the player
        dx = self.player.rect.centerx - self.rect.centerx
        dy = self.player.rect.centery - self.rect.centery
        dist = math.hypot(dx, dy)
        if dist == 0:
            dist = 1
        dir_x = dx / dist
        dir_y = dy / dist

        self.rect.x += dir_x * self.speed
        self.rect.y += dir_y * self.speed
