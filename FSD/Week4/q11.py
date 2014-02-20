import turtle
radius = 10
turtle.speed(0)
def main():


    multipleCircles(10, -1, 1)

    multipleCircles(10, -1, -1)

    multipleCircles(10, 1, 1)

    multipleCircles(10, 1, -1)



def multipleCircles(radius, a, b):
    if radius < 150:

        turtle.pu()
        turtle.goto(2*a*radius, 2*b*radius)
        turtle.pd()
        turtle.circle(radius)
        radius += 5

        multipleCircles(radius, a, b)


main()

turtle.exitonclick()




