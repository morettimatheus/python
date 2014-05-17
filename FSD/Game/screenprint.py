from constants import *
import pygame
from checkVictory import *

class PrintSign:
    def __init__(self, screen, rows_num, x, y, plays): #class' constructor
        self.screen = screen
        self.rows_num = rows_num
        self.x = x
        self.y = y
        self.plays = plays

    def drawsign (self, screen, rows_num, x, y, plays): #we'll get the screen, num of rows, x and y coordinates
        #and the number of plays
        rows = rows_num
        noplays = plays
        X = pygame.image.load('Images/X.png') #loading our X sprite
        X = pygame.transform.smoothscale (X, (WIDTH/(2*rows), HEIGHT/(2*rows))) #sprites are resized to fit perfectly
        O = pygame.image.load('Images/O.png')
        O = pygame.transform.smoothscale(O, (WIDTH/(2*rows), HEIGHT/(2*rows)))
        cellsize = WIDTH/rows #this will make some formulas easier
        if noplays == 1: #when the game is starting, we will create a matrix
            global gameplay
            gameplay = [[0 for k in range(rows_num)] for k in range(rows_num)] #creates a matrix: Gameplay of 0s
        for i in range (rows): #our i will increase
            if x > i * cellsize and x < (i + 1) * cellsize: #and we will test if it's inside the left and right margin
                #of our square
                for j in range (rows): #check top and bottom margin
                    if y > j * cellsize and y < (j + 1) * cellsize:  # else will just add 1 to i and check again
                        if noplays%2 == 0 and gameplay[i][j] == 0: #if it's empty and if the play is even
                            screen.blit(O, [((4 * i + 1) * cellsize) / 4, (4 * j + 1) * cellsize / 4]) #blit our O
                            gameplay[i][j] = 1 #lets set our matrix cell to 1

                        else:
                            if  gameplay[i][j] == 0: #num of plays is odd and if the place is empty
                                screen.blit(X, [((4 * i + 1) * cellsize) / 4, (4 * j + 1) * cellsize / 4])
                                gameplay[i][j] = 2

                            else:
                                busy = pygame.mixer.Sound('Sounds/busy.wav')
                                busy.play() #lets play a sound as feedback so the player know the place is busy
                                return False #this return False won't let the number of plays be increased
                                #this way, player can try to place his sign again

                        pygame.display.update()

                        winner = checkVictory(gameplay, rows) #let's call the checkVictory class
                        winner.check(gameplay, rows) #and the check method.


class PrintImage: #let's print our images!
    def __init__(self, screen): #class constructor
        self.screen = screen

    def showRules(self, screen):
        screen.fill(RULESBG) #this color and the others are defined inside constants.py file
        rules = pygame.image.load('Images/rules.png')
        screen.blit(rules, (0,0))
        pygame.display.update()
        pygame.time.wait(5000) #after blitting, lets wait 5 seconds so the user reads the rules

    def showLogo(self, screen):
        screen.fill(BGBLUE)
        logo = pygame.image.load('Images/logo.png')
        screen.blit(logo, (0,0))
        pygame.display.update()
        pygame.time.wait(2000) #2 seconds of wait while they see our logo

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
