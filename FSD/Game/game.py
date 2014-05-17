import pygame
import sys
from constants import *
from board import  *
from screenprint import *
from pygame.locals import *

pygame.init()

screen = pygame.display.set_mode((WIDTH, HEIGHT))
plays = 1 #plays variable will help us to check the turns of each players
def game():
    global rows_num
    global printing
    global signprint

    printing = PrintImage(screen)  #PrintImage is a class of the screenprint file I made (in order to reuse code)
    printing.showLogo(screen)
    printing.showRules(screen)
    printing.showInput1(screen)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN and event.key == pygame.K_RETURN: #the showInput1 asks to be pressed Enter
                plays = 1 #reseting the variable plays to 1, we can play the game over and over
                rows_num = rowInput() #calls the rowInput function
                board = Board(rows_num, screen) #Board is a class from board.py file.
                board.draw(rows_num, screen) #draw method will draw onto our screen the board

            elif event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
                pygame.quit() #game will exit if pygame receives the quit event or escape key is pressed
                sys.exit()

            if event.type == pygame.MOUSEBUTTONUP: #when the mouse button is released
                clicked_x, clicked_y = pygame.mouse.get_pos() #we will get position x and y from the click
                signprint = PrintSign(screen, rows_num, clicked_x, clicked_y, plays) #call the PrintSign method
                if (signprint.drawsign(screen, rows_num, clicked_x, clicked_y, plays)) != False:
                    plays += 1 #add 1 to plays if the above method goes well. Next player's turn!


def rowInput ():
    rows = "" #it is a string
    printing.showInput2(screen) #showInput 2 tells the player that he must choose a number between 3 and 12
    while True:
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN and event.unicode.isalnum(): #checking if the pressed is alfanumeric
                rows += event.unicode #if it is, concatenate it to rows string

            if event.type == pygame.KEYDOWN and event.key == pygame.K_RETURN and len(rows) > 0: #after enter is pressed
                rows_num = int(rows) #rows_num will be an integer
                if rows_num <= 12 and rows_num > 2: #check if it's inside the range aforesaid
                    return rows_num # back to line 31
                else:
                    game() #else, lets start it over

            elif event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
                pygame.quit()  #once again we are prepared to quit
                sys.exit()


game()