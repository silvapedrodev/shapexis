import pygame
import sys

from code.Const import BG_MENU


def handle_quit(event):
    """Function that checks if the player closed the window."""
    if event.type == pygame.QUIT:
        pygame.quit()
        sys.exit()


def draw_background(screen):
    bg_image = pygame.image.load(BG_MENU).convert_alpha()
    screen.blit(bg_image, (0, 0))
