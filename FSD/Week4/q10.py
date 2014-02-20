import turtle
wn = turtle.Screen()
wn.bgcolor("blue")
jamal = turtle.Turtle()
jamal.color("white")
jamal.pensize(10)

def LShape(x,y):
    x1 = x
    y1 = y
    jamal.setx(x)
    jamal.sety(y)
    jamal.right(90)
    jamal.forward(150)
    jamal.left(90)
    jamal.forward(75)
    x1+=10
    y1+=20
    while x1 <= 120 and y1 <= 120:
        flag = True
        LShape(x1,y1)
    wn.exitonclick()
LShape(0,0)