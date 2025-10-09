import pygame
from datetime import datetime

from code.Const import W_SCREEN, FONT_PRIMARY, C_WHITE, C_YELLOW
from code.Score import Score
from code.Utils import handle_quit, draw_background


class WinnerScreen:
    def __init__(self, screen, player_skin, player_score):
        self.screen = screen
        self.player_skin = player_skin
        self.player_score = player_score
        self.font_title = pygame.font.Font(FONT_PRIMARY, 28)
        self.font_text = pygame.font.Font(FONT_PRIMARY, 28)
        self.font_input = pygame.font.Font(FONT_PRIMARY, 36)
        self.nickname = ""
        self.running = True
        self.score_system = Score(screen)

        # Load and play victory screen audio
        pygame.mixer_music.load('./assets/audio/winner_scene.mp3')
        pygame.mixer.music.play(1)
        pygame.mixer_music.set_volume(0.5)

    def run(self):

        while self.running:
            draw_background(self.screen)

            title_surface = self.font_title.render("Congratulations! You Win!", True, C_YELLOW)
            title_rect = title_surface.get_rect(center=(W_SCREEN // 2, 150))
            self.screen.blit(title_surface, title_rect)

            # instruction
            instr_surface = self.font_text.render("Enter your nickname (max 10 chars):", True, C_WHITE)
            instr_rect = instr_surface.get_rect(center=(W_SCREEN // 2, 280))
            self.screen.blit(instr_surface, instr_rect)

            # input
            input_surface = self.font_input.render(self.nickname or "_", True, C_YELLOW)
            input_rect = input_surface.get_rect(center=(W_SCREEN // 2, 340))
            self.screen.blit(input_surface, input_rect)

            pygame.display.flip()

            for event in pygame.event.get():
                handle_quit(event)

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN and len(self.nickname) > 0:
                        current_date = get_formatted_date()
                        self.score_system.save_score(self.nickname, self.player_skin, self.player_score, current_date)

                        self.running = False
                        return "menu"

                    # BACKSPACE
                    elif event.key == pygame.K_BACKSPACE:
                        self.nickname = self.nickname[:-1]

                    elif len(self.nickname) < 10 and event.unicode.isalnum():
                        self.nickname += event.unicode.upper()
        return None


def get_formatted_date():
    now = datetime.now()
    return now.strftime("%m/%d/%Y %H:%M:%S")
