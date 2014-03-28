import pygame
import sys
from constants import *
from board import  *
from screenprint import *
from pygame.locals import *

pygame.init()

screen = pygame.display.set_mode((WIDTH, HEIGHT))

font = pygame.font.SysFont('helvetica', 20)
plays = 1
def game():
    global rows_num
    global printing
    global signprint

    printing = PrintImage(screen)
    printing.showLogo(screen)
    printing.showInput1(screen)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN and event.key == pygame.K_RETURN:
                plays = 1
                rows_num = rowInput()
                printing.showRules(screen)
                board = Board(rows_num, screen)
                board.draw(rows_num, screen)

            elif event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
                pygame.quit()
                sys.exit()

            if event.type == pygame.MOUSEBUTTONUP:
                clicked_x, clicked_y = pygame.mouse.get_pos()
                signprint = PrintSign(screen, rows_num, clicked_x, clicked_y, plays)
                if (signprint.drawsign(screen, rows_num, clicked_x, clicked_y, plays)) != False:
                    plays += 1


def rowInput ():
    rows = ""
    printing.showInput2(screen)
    while True:
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN and event.unicode.isalnum():
                rows += event.unicode

            if event.type == pygame.KEYDOWN and event.key == pygame.K_RETURN and len(rows) > 0:
                rows_num = int(rows)
                if rows_num <= 12 and rows_num > 2:
                    return rows_num
                else:
                    game()

            elif event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
                pygame.quit()
                sys.exit()

def checkVictory():
    print("hello")


game()