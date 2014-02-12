#!/usr/bin/python
# -*- coding: latin-1 -*-
import random

print("GAME INSTRUCTIONS")
print("-----------------")
print("Welcome to Camel!")
print("You have stolen a camel to make your way across the great Mobi desert.")
print("The camel’s owners want their camel back and are chasing you down!")
print("You have 5 flasks of water with you. Survive your desert trek and outrun the camel’s owners.")

game_over = False
miles_travelled = 0
days_passed = 0
player_turn = 0
owners_turn = 0
thirst = 0
camel_tiredness = 0
owners_distance = 10
MAX_TIREDNESS = 8
MAX_THIRST = 6
MAX_FLASKS = 5
WINNING_DISTANCE = 200
flasks = MAX_FLASKS

while game_over == False:
    print("1. Drink from your flasks.")
    print("2. Ahead moderate speed.")
    print("3. Ahead full speed.")
    print("4. Stop for the night")
    print("5. Check your status.")
    print("6. Quit.")
    print()
    player_choice = input("Please type in your choice:  ")

    if player_choice == "6":
        game_over = True

    elif player_choice == "5":
        print("Miles travelled so far: ", miles_travelled)
        print("Days passed:  ", days_passed)
        print("Water flasks left: ", flasks)
        print("The owner is", owners_distance, "miles behind you")
        print()

    elif player_choice == "4":
        camel_tiredness = 0
        days_passed += 1
        owners_turn = random.randint(6,18)
        owners_distance -= owners_turn
        print("The camel is no longer tired.")

    elif player_choice == "3":
        thirst += 1
        days_passed += 1
        player_turn = random.randint(9,21)
        miles_travelled += player_turn
        owners_distance += player_turn
        camel_tiredness += random.randint(0,4)

        print("You have travelled", player_turn, "miles")

    elif player_choice == "2":
        thirst += 1
        days_passed += 1
        camel_tiredness += 1
        player_turn = random.randint(4,13)
        miles_travelled += player_turn
        owners_distance += player_turn

        print("You have travelled", player_turn, "miles")

    elif player_choice == "1":
        if flasks > 0:
            flasks -= 1
            thirst = 0
            print("You have", flasks, "flasks remaining")

        else:
            print ("You have ran out of water")

    if thirst >= 4 and thirst <= MAX_THIRST:
        print("You are thirsty")

    elif thirst > MAX_THIRST:
        print("After", days_passed, "days of run, you died of thirst. Game over!")
        game_over = True
        break

    if camel_tiredness >= 5 and camel_tiredness <= MAX_TIREDNESS:
        print("You are tired")

    elif camel_tiredness > MAX_TIREDNESS:
        print("After", days_passed, "days of run, your camel died and you got caught. Game over!")
        game_over = True
        break

    if owners_distance == 0:
        print("You have been caught after", days_passed, "days. Gave over!")
        game_over = True
        break

    elif owners_distance < 15:
        print("The owners are getting close!")

    if miles_travelled >= WINNING_DISTANCE:
        print("You won after", days_passed, "days of run! Congratulations!")
        game_over = True
        break

    oasis = random.randint(0,11)
    if oasis == 7:
        print("You have found an oasis! Your camel is now rest, you are no longer thirsty and all your water flasks have been refilled")
        flasks = MAX_FLASKS
        thirst = 0
        camel_tiredness = 0

    bag = random.randint (0,21)
    if bag == 13:
        print("You stumbled upon a bag. Something appears to be inside it.") 
        print ("1. You are feeling brave! Open the bag to see what's inside.")
        print("2. You don't want to take any unnecessary risks. Leave the bag as it is.")
        choice = input("Enter your choice:   ")
        if choice == "2":
            print("You decided to continue your journey")

        else:
            lamp = random.randint(0,3)
            if lamp == 1:
                print("You found a lamp with a genie inside! He took you out of the desert and you won the game!")
                game_over = True
                break

            else:
                print("A black scorpion stung you and you are now dead. Game over!")
                game_over = True
                break





