import pygame
from constants import *
class Board:
    def __init__(self, rows, screen): #constructor of our Board class
        self.rows = rows
        self.screen = screen


    def draw(self, rows, screen):
        screen.fill(BOARDBG) #color defined inside constants.py
        pygame.draw.rect(screen, WHITE, [0, 0, WIDTH, HEIGHT], 10)
        for i in range (0, self.rows): #this piece of code draws rects using the number of rows we have
            i *= WIDTH/rows
            for j in range (0, self.rows):
                j *= HEIGHT/rows
                pygame.draw.rect(screen, WHITE, [i, j, WIDTH/rows, HEIGHT/rows], 5)

        pygame.display.flip()

