import turtle
turtle.bgcolor("black")
turtle.speed(0)
x = - 225
y = 300
turtle.setx(x)
turtle.sety(y)
turtle.color("green")

def star():	
    for i in range (0,5):    	
        turtle.right(144)
        turtle.forward(100)
        i += 1

def verticalMove ():
	turtle.penup()
	global y
	y -= 150
	turtle.sety(y)

def horizMove ():
	global x
	x += 150
	turtle.setx(x)

def horizLine ():
	turtle.pendown()
	star()
	for j in range (0,4):
		turtle.penup()
		horizMove()
		turtle.pendown()
		star()
		j += 1

horizLine()
verticalMove()
x = - 300
turtle.setx(x)

horizLine()
verticalMove()
x = - 225
turtle.setx(x)

horizLine()
verticalMove()
x = - 300
turtle.setx(x)

horizLine()

turtle.done()