import random

import pygame
from code.Const import FONT_PRIMARY, W_SCREEN, H_SCREEN, C_WHITE, C_GRAY, FONT_SECONDARY, C_RED_2
from code.Utils import handle_quit


class GameOverScreen:
    def __init__(self, screen):
        self.screen = screen

        self.death_messages = [
            "At the end of the day, the King and the pawn go back into the same box because the game is The Game.",
            "Life is a game where, no matter how hard you try, death wins at the end.",
            "You fought bravely, but weakness still consumes you.",
            "Another failure. Did you really think you stood a chance?",
            "Your struggle was meaningless. The void welcomes you.",
            "Strength? Skill? Illusions. Death always collects its due.",
            "You are just another pawn removed from the board.",
            "No matter how many times you try, the darkness waits patiently.",
            "Even heroes fall. You are no different.",
            "The end comes not with glory, but with silence.",
            "You thought you were strong. Death proved otherwise.",
            "The world forgets the weak. You are already forgotten.",
            "You delayed the inevitable, but you could never escape it.",
            "Courage fades. Fear devours. Death claims.",
            "Your life was a flicker. Now it is extinguished.",
            "You were never the main character. Just another soul lost.",
        ]

        self.message = random.choice(self.death_messages)

        # Load and play game over screen audio
        pygame.mixer_music.load('./assets/audio/death_scene.mp3')
        pygame.mixer_music.play(-1)

    def run(self):
        while True:
            self.screen.fill((0, 0, 0))

            font = pygame.font.Font(FONT_PRIMARY, 48)
            text = font.render("YOU DIED", True, C_RED_2)
            rect = text.get_rect(center=(W_SCREEN // 2, H_SCREEN // 2 - 70))
            self.screen.blit(text, rect)

            small_font = pygame.font.Font(FONT_PRIMARY, 24)
            hint = small_font.render("Press ENTER to return to menu", True, C_WHITE)
            hint_rect = hint.get_rect(center=(W_SCREEN // 2, H_SCREEN // 2 + 40))
            self.screen.blit(hint, hint_rect)

            message_font = pygame.font.Font(FONT_SECONDARY, 16)
            max_width = 700

            self.render_text_wrapped(
                f'"{self.message}"',
                message_font,
                C_GRAY,
                W_SCREEN // 2,
                H_SCREEN // 2 + 90,
                max_width
            )

            pygame.display.flip()

            for event in pygame.event.get():
                handle_quit(event)
                if event.type == pygame.KEYDOWN and event.key == pygame.K_RETURN:
                    return "menu"

    def render_text_wrapped(self, text, font, color, x, y, max_width, line_spacing=5):
        words = text.split(' ')
        lines = []
        current_line = ""

        for word in words:
            test_line = current_line + word + " "
            if font.size(test_line)[0] <= max_width:
                current_line = test_line
            else:
                lines.append(current_line.strip())
                current_line = word + " "
        if current_line:
            lines.append(current_line.strip())

        for i, line in enumerate(lines):
            rendered = font.render(line, True, color)
            line_rect = rendered.get_rect(center=(x, y + i * (font.get_height() + line_spacing)))
            self.screen.blit(rendered, line_rect)
