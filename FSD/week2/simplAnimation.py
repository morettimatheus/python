import turtle
import time
import random

# ----main
print('simple turtle animation for a set time')

# int screen size
screen_width = 800
screen_height = 800

turtle.setup(screen_width, screen_height)
window = turtle.Screen()
window.title("Simple Animation")

# get time for animation to run
num_seconds = 20

#Use the turtle graphics library at http://docs.python.org/3.0/library/turtle.html#turtle.onclick
#to see the effect of each of the statements below and then write the your comments


myBall = turtle.Turtle() # the var myBall is now an object (turtle) of the class (Turtle)
myBall.shape('circle') # we are changing the shape of our turtle (named myBall) to a circle
myBall.fillcolor('black') # we are changing its color to black
myBall.speed(0) # speed(0) means that no animation takes place. 
myBall.penup()# that means we wont draw while moving
myBall.setheading(random.randint(1,359))# heading angle will be a random number betweent 1 and 359

start_time = time.time()

# begin animation
terminate = False
while not terminate: # when the terminate var is true. 
     myBall.forward(10); 
     #print(myBall.xcor(), end='') # debug statements during development
     #print(myBall.heading()) # debug statements during development
     if((myBall.xcor() >screen_width / 2) or(myBall.xcor() < -screen_width / 2)):
         #print("if condition met") # debug statements during development
         myBall.setheading(180-myBall.heading()) # write a comment to explain what this line does
         
     elif((myBall.ycor() >screen_height / 2) or(myBall.ycor() < -screen_height / 2)):
         #print("if condition met") # debug statements during development
         myBall.setheading(90 - myBall.heading()) # write a comment to explain what this line does
      
   
     if time.time() - start_time > num_seconds:
        terminate = True
    
turtle.exitonclick()  
        
        