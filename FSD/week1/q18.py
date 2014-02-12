import turtle

side_lenght = int(input("size of the square"))
bgcolor = input("background color")
shape = input("please choose a shape")
shape_colour = input("choose the colour of the shape")

turtle.shape(shape)
turtle.fillcolor(shape_colour)
turtle.bgcolor(bgcolor)
turtle.forward(side_lenght)
turtle.right(90)
turtle.forward(side_lenght)
turtle.right(90)
turtle.forward(side_lenght)
turtle.right(90)
turtle.forward(side_lenght)

turtle.done()