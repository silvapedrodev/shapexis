import pygame
from code.Const import W_SCREEN, FONT_PRIMARY, C_YELLOW, C_WHITE, DATABASE_NAME, BG_MENU
from code.DBProxy import DBProxy
from code.Data_Skins import SKINS
from code.Utils import handle_quit


class Score:
    def __init__(self, screen):
        self.screen = screen
        self.bg_image: pygame.Surface = pygame.image.load(BG_MENU).convert_alpha()
        self.area = self.bg_image.get_rect(topleft=(0, 0))
        self.font_title = pygame.font.Font(FONT_PRIMARY, 32)
        self.font_text = pygame.font.Font(FONT_PRIMARY, 14)
        self.running = True
        self.db = DBProxy(f'{DATABASE_NAME}.db')

    def save_score(self, name, avatar, score, date):
        data = {
            'name': name,
            'avatar': avatar,
            'score': score,
            'date': date
        }

        self.db.save_score(data)
        self.db.close()

        check_unlocks(score)

    def show_ranking(self):
        db = DBProxy(f'{DATABASE_NAME}.db')

        # Table size
        table_width = 600
        column_spacing = [40, 80, 150, 80, 150]
        start_x = (W_SCREEN - table_width) // 2
        start_y = 90
        row_height = 40

        while self.running:
            self.screen.blit(self.bg_image, self.area)

            title_surface = self.font_title.render("TOP SCORES", True, C_YELLOW)
            title_rect = title_surface.get_rect(center=(W_SCREEN // 2, 40))
            self.screen.blit(title_surface, title_rect)

            # Header
            headers = ["#", "SKIN", "NAME", "SCORE", "DATE"]
            x = start_x
            for i, text in enumerate(headers):
                header = self.font_text.render(text, True, C_YELLOW)
                self.screen.blit(header, (x, start_y))
                x += column_spacing[i]

            scores = db.retrieve_top10()
            y = start_y + row_height

            for i, (_, name, avatar, score, date) in enumerate(scores):
                x = start_x

                # Position
                pos_surface = self.font_text.render(str(i + 1), True, C_WHITE)
                self.screen.blit(pos_surface, (x, y))
                x += column_spacing[0]

                # Skin
                self.render_skin(avatar, x, y)
                x += column_spacing[1]

                # Name
                name_surface = self.font_text.render(name, True, C_WHITE)
                self.screen.blit(name_surface, (x, y))
                x += column_spacing[2]

                # Score
                score_surface = self.font_text.render(str(score), True, C_WHITE)
                self.screen.blit(score_surface, (x, y))
                x += column_spacing[3]

                # Date
                date_surface = self.font_text.render(date, True, C_WHITE)
                self.screen.blit(date_surface, (x, y))

                y += row_height

            pygame.display.flip()

            for event in pygame.event.get():
                handle_quit(event)
                if event.type == pygame.KEYDOWN:
                    if event.key in (pygame.K_RETURN, pygame.K_ESCAPE):
                        self.running = False

        db.close()
        return "menu"

    def render_skin(self, skin_name, x, y):
        if skin_name in SKINS:
            skin_path = SKINS[skin_name]["path"]
            skin_img = pygame.image.load(skin_path).convert_alpha()
            skin_img = pygame.transform.scale(skin_img, (36, 36))
            self.screen.blit(skin_img, (x, y))


def get_top_score():
    """Retrieves the highest score from the database."""
    db = DBProxy(f"{DATABASE_NAME}.db")
    top = db.retrieve_top10()
    db.close()
    return top[0][3] if top else 0


def check_unlocks(score):
    """Unlocks skins according to the score reached"""
    unlock_conditions = {
        340: "Black Hole",
        555: "Watermelon",
        1135: "Orange",
        1810: "Sun",
        2200: "Planet 1",
        2500: "Planet 2",
        3000: "Planet 3",
    }

    unlocked_count = 0

    for required, skin_name in unlock_conditions.items():
        if score >= required and not SKINS[skin_name]["unlocked"]:
            SKINS[skin_name]["unlocked"] = True

    return unlocked_count
