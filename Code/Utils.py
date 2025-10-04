import pygame
import sys

def handle_quit(event):
    """Function that checks if the player closed the window."""
    if event.type == pygame.QUIT:
        pygame.quit()
        sys.exit()