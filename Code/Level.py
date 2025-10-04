import pygame

from code.Enemy import Enemy
from code.HUD import HUD
from code.Player import Player
from code.Utils import handle_quit
from code.Const import W_SCREEN, H_SCREEN, ENEMY_SPAWN, PLAYER_HIT, LEVEL_DURATION


class Level:
    def __init__(self, screen):
        self.screen = screen
        self.start_ticks = pygame.time.get_ticks()
        self.bg_image = pygame.image.load('./assets/bg_3.png').convert_alpha()
        self.bg_image = pygame.transform.scale(self.bg_image, (W_SCREEN, H_SCREEN))
        self.player = Player(W_SCREEN // 2, H_SCREEN // 2)
        self.clock = pygame.time.Clock()
        self.hud = HUD(self.player)

        self.enemies = []
        self.spawn_timer = 0
        self.spawn_delay = ENEMY_SPAWN
        self.game_over = False

    def run(self, events):
        self.clock.tick(60)
        self.player.move()
        self.player.update_shoots()
        self.player.draw(self.screen)

        # Handles frame rate monitoring and level countdown timer
        fps = int(self.clock.get_fps())
        now = pygame.time.get_ticks()
        elapsed_time = now - self.start_ticks
        remaining_time = max(0, LEVEL_DURATION - elapsed_time)
        remaining_seconds = remaining_time / 1000

        # draw background and HUD
        self.screen.blit(self.bg_image, (0, 0))
        self.hud.draw(self.screen, fps, remaining_seconds)

        self.player.move()
        self.player.draw(self.screen)

        # enemies
        self.update_enemies()
        self.draw_enemies()

        if self.player.is_dead():
            self.game_over = True
            return "game_over"

        for event in events:
            handle_quit(event)

            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                self.player.shoot()
        return None

    def spawn_enemy(self):
        enemy = Enemy(self.player)
        self.enemies.append(enemy)

    def update_enemies(self):
        self.spawn_timer += 1
        if self.spawn_timer >= self.spawn_delay:
            self.spawn_enemy()
            self.spawn_timer = 0

        enemies_to_remove = []

        for enemy in self.enemies:
            enemy.update()

            # enemy > player collision
            if enemy.rect.colliderect(self.player.rect):
                self.player.hp -= enemy.damage
                enemy.hp = 0
                enemies_to_remove.append(enemy)
                if self.player.is_dead():
                    print("GAME OVER")

            for shoot in self.player.shoots[:]:
                if enemy.rect.colliderect(shoot.rect):
                    enemy.hp -= PLAYER_HIT
                    self.player.shoots.remove(shoot)
                    if enemy.is_dead() and enemy not in enemies_to_remove:
                        enemies_to_remove.append(enemy)
                        self.player.add_score(enemy.score)

        for enemy in enemies_to_remove:
            if enemy in self.enemies:
                self.enemies.remove(enemy)

    def draw_enemies(self):
        for enemy in self.enemies:
            enemy.draw(self.screen)
