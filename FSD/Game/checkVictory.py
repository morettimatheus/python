from screenprint import *
from constants import *

def printOwinner():
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    screen.fill(CLOUDCOLOR)
    owinner = pygame.image.load('Images/owinner.png')
    screen.blit(owinner, (0,0))
    pygame.display.update()
    win = pygame.mixer.Sound('Sounds/win.wav')
    win.play()

def printXwinner():
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    screen.fill(CLOUDCOLOR)
    xwinner = pygame.image.load('Images/xwinner.png')
    screen.blit(xwinner, (0,0))
    pygame.display.update()
    win = pygame.mixer.Sound('Sounds/win.wav')
    win.play()


class checkVictory:
    def __init__(self, gameplay, rows):
        self.gameplay = gameplay
        self.rows = rows

    def check(self, gameplay, rows):
        no_crosses = 0
        no_noughts = 0
        for i in range (rows): #this for will test for wins on the top-right to left-bottom diagonal.
            if gameplay[i][i] == 2:
                no_crosses += 1

            elif gameplay[i][i] == 1:
                no_noughts += 1

            if no_noughts == rows:
                printOwinner()


            elif no_crosses == rows:
                printXwinner()


        for i in range (rows): #horizontal line check ##### CANT MANAGE IT TO WORK ####
            no_crosses = 0
            no_noughts = 0
            for j in range(rows):
                if gameplay[i][j] == 2:
                    no_crosses += 1

                elif gameplay[i][j] == 1:
                    no_noughts += 1

                if no_noughts == rows:
                    printOwinner()


                elif no_crosses == rows:
                    printXwinner()


        no_crosses = 0
        no_noughts = 0
        for i in range (rows): #vertical line check
            no_crosses = 0
            no_noughts = 0
            for j in range(rows):
                if gameplay[j][i] == 2:
                    no_crosses += 1

                elif gameplay[j][i] == 1:
                    no_noughts += 1

                if no_noughts == rows:
                    printOwinner()


                elif no_crosses == rows:
                    printXwinner()


        #no_crosses = 0
        #no_noughts = 0
        '''
        for i in range (rows): #/ diagonal check #####CANT MAKE IT WORK AS WELL #####
            for j in range(rows):
                if gameplay[i][((rows-1)-j)] == 2:
                    no_crosses += 1

                elif gameplay[i][((rows-1)-j)] == 1:
                    no_noughts += 1

                if no_noughts == rows:
                    printOwinner()

                elif no_crosses == rows:
                    printXwinner()
                    '''


