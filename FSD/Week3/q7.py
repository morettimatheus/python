import turtle
shapes = {"4": 90, "5": 72, "6": 60, "7": 51, "8": 45, "9": 40, "10": 36}
while True:
    userInput = input("Please type in the number of sides you want")
    userColor = input("What color?")
    for i in range (0,int(userInput)):
        turtle.color(userColor)
        turtle.forward(100)
        turtle.right(shapes[userInput])

    cont = input("Press y if you want to continue: ")
    if cont != "y" and cont != "Y":
        break

    else:
        turtle.reset()


