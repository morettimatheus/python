import pygame
from constants import *
class Board:
    def __init__(self, rows, screen):
        self.rows = rows
        self.screen = screen


    def draw(self, rows, screen):
        screen.fill(BOARDBG)
        pygame.draw.rect(screen, WHITE, [0, 0, WIDTH, HEIGHT], 10)
        for i in range (0, self.rows):
            i *= WIDTH/rows
            for j in range (0, self.rows):
                j *= HEIGHT/rows
                pygame.draw.rect(screen, WHITE, [i, j, WIDTH/rows, HEIGHT/rows], 5)

        pygame.display.flip()

