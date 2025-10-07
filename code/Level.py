import os.path

import pygame

from code.Enemy import Enemy
from code.HUD import HUD
from code.Utils import handle_quit
from code.Const import W_SCREEN, H_SCREEN, PLAYER_HIT, LEVEL_DURATION


class Level:
    def __init__(self, screen, player, level_number, max_levels, spawn_delay, speed_multiplier):
        self.screen = screen
        self.player = player
        self.level_number = level_number
        self.max_levels = max_levels
        self.spawn_delay = spawn_delay
        self.speed_multiplier = speed_multiplier

        self.clock = pygame.time.Clock()
        self.start_ticks = pygame.time.get_ticks()
        self.hud = HUD(self.player)

        self.enemies = []
        self.spawn_timer = 0
        self.game_over = False

        # Load the background
        bg_path = f'./assets/bg-level-0{self.level_number}.png'
        if not os.path.exists(bg_path):
            bg_path = './assets/bg-level-01.png'
        self.bg_image = pygame.image.load(bg_path).convert_alpha()
        self.bg_image = pygame.transform.scale(self.bg_image, (W_SCREEN, H_SCREEN))

    def run(self, events):
        self.clock.tick(60)
        fps = int(self.clock.get_fps())

        # Handles level countdown timer
        now = pygame.time.get_ticks()
        elapsed_time = now - self.start_ticks
        remaining_time = max(0, LEVEL_DURATION - elapsed_time)
        remaining_seconds = remaining_time / 1000

        if remaining_time <= 0:
            return "next_level"

        # Render elements
        self.screen.blit(self.bg_image, (0, 0))
        self.player.move()
        self.player.update_shoots()
        self.player.draw(self.screen)

        # draw HUD
        self.hud.draw(self.screen, self.level_number, fps, remaining_seconds)

        # enemies
        self.update_enemies()
        self.draw_enemies()

        for event in events:
            handle_quit(event)
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                self.player.shoot()

        if self.player.is_dead():
            self.game_over = True
            return "game_over"

        return None

    def spawn_enemy(self):
        enemy = Enemy(self.player, self.speed_multiplier)
        self.enemies.append(enemy)

    def update_enemies(self):
        self.spawn_timer += 1
        if self.spawn_timer >= self.spawn_delay:
            self.spawn_enemy()
            self.spawn_timer = 0

        enemies_to_remove = []
        for enemy in self.enemies:
            enemy.update()

            # enemy → player collision
            if enemy.rect.colliderect(self.player.rect):
                self.player.take_damage(enemy.damage)
                enemy.hp = 0
                enemies_to_remove.append(enemy)

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
