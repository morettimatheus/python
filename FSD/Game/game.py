import pygame
import sys
from pygame.locals import *

pygame.init()
screen = pygame.display.set_mode((600, 600))
font = pygame.font.SysFont('helvetica', 20)
rows_num = 6 ########################## check ##########################
def game():
    screen.fill((200, 200, 200))
    message = font.render("Please type in how many rows you want for your TIC TAC TOE", True, (0,0,0))
    screen.blit(message, (20,300))
    message = font.render("Press ENTER", True, (0,0,0))
    screen.blit(message, (250,330))
    pygame.display.flip()
    while True:
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN and event.key == pygame.K_RETURN:
                rows_num = rowInput()
                drawBoard(rows_num)

            elif event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
                pygame.quit()
                sys.exit()

            if event.type == pygame.MOUSEBUTTONUP:
                clicked_x, clicked_y = pygame.mouse.get_pos()
                drawSign(clicked_x, clicked_y)

def drawSign(x, y):##################check##################
    rows = rows_num
    X = pygame.image.load('X.png')
    X = pygame.transform.smoothscale (X, (600/(2*rows), 600/(2*rows)))
    O = pygame.image.load('O.png')
    O = pygame.transform.smoothscale(O, (600/(2*rows), 600/(2*rows)))
    for i in range (0, rows*rows):
        for j in range (0, rows*rows):
            if x > i * 600/rows and x < (i + 1) * 600/rows:
                if y > j * 600/rows and x < (j + 1) * 600/rows:
                    screen.blit(O, [((i + 1) * 600/rows)/4, ((j + 1) * 600/rows)/4, 100, 100])
                    print(x)
                    print(y)
                    pygame.display.flip()





def rowInput ():
    rows = ""
    screen.fill((200, 200, 200))
    message = font.render("Choose from 3 to 12! Press ENTER after you typed it.", True, (0,0,0))
    screen.blit(message, (100,330))
    while True:
        pygame.display.flip()
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

def drawBoard(rows):
    screen.fill((100, 100, 100))
    pygame.draw.rect(screen, (255,255,255), [0, 0, 600, 600], 10)
    for i in range (0, rows):
        i *= 600/rows
        for j in range (0, rows):
            j *= 600/rows
            pygame.draw.rect(screen, (255,255,255), [i, j, 600/rows, 600/rows], 5)

    pygame.display.flip()




game()
