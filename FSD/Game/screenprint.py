from constants import *
import pygame
from checkVictory import *

class PrintSign:
    def __init__(self, screen, rows_num, x, y, plays):
        self.screen = screen
        self.rows_num = rows_num
        self.x = x
        self.y = y
        self.plays = plays

    def drawsign (self, screen, rows_num, x, y, plays):
        rows = rows_num
        noplays = plays
        X = pygame.image.load('Images/X.png')
        X = pygame.transform.smoothscale (X, (WIDTH/(2*rows), HEIGHT/(2*rows)))
        O = pygame.image.load('Images/O.png')
        O = pygame.transform.smoothscale(O, (WIDTH/(2*rows), HEIGHT/(2*rows)))
        cellsize = WIDTH/rows
        if noplays == 1:
            global gameplay
            gameplay = [[0 for k in range(rows_num)] for k in range(rows_num)] #creates Gameplay of 0s
        for i in range (rows):
            if x > i * cellsize and x < (i + 1) * cellsize:
                for j in range (rows):
                    if y > j * cellsize and y < (j + 1) * cellsize:  # else will just add 1 to i and check again
                        if noplays%2 == 0 and gameplay[i][j] == 0:
                            screen.blit(O, [((4 * i + 1) * cellsize) / 4, (4 * j + 1) * cellsize / 4])
                            gameplay[i][j] = 1

                        else:
                            if  gameplay[i][j] == 0:
                                screen.blit(X, [((4 * i + 1) * cellsize) / 4, (4 * j + 1) * cellsize / 4])
                                gameplay[i][j] = 2

                            else:
                                busy = pygame.mixer.Sound('Sounds/busy.wav')
                                busy.play()
                                return False

                        pygame.display.update()

                        winner = checkVictory(gameplay, rows)
                        winner.check(gameplay, rows)


class PrintImage:
    def __init__(self, screen):
        self.screen = screen

    def showRules(self, screen):
        screen.fill(RULESBG)
        rules = pygame.image.load('Images/rules.png')
        screen.blit(rules, (0,0))
        pygame.display.update()
        pygame.time.wait(5000)

    def showLogo(self, screen):
        screen.fill(BGBLUE)
        logo = pygame.image.load('Images/logo.png')
        screen.blit(logo, (0,0))
        pygame.display.update()
        pygame.time.wait(2000)

    def showInput1 (self, screen):
        screen.fill(BGBLUE)
        input1 = pygame.image.load('Images/input1.png')
        screen.blit(input1, (0,0))
        pygame.display.update()

    def showInput2 (self, screen):
        screen.fill(BGBLUE)
        input2 = pygame.image.load('Images/input2.png')
        screen.blit(input2, (0,0))
        pygame.display.update()


    def xWinner (self, screen):
        screen.fill(CLOUDCOLOR)
        xwinner = pygame.image.load('Images/xwinner.png')
        screen.blit(xwinner, (0,0))
        pygame.display.update()

    def oWinner (self, screen):
        screen.fill(CLOUDCOLOR)
        owinner = pygame.image.load('Images/owinner.png')
        screen.blit(owinner, (0,0))
        pygame.display.update()
