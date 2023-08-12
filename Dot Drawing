import turtle as t
import random

tim = t.Turtle()
t.colormode(255)
tim.penup()
tim.speed("fastest")
tim.hideturtle()

def random_color():
    r = random.randint(0,255)
    g = random.randint(0,255)
    b = random.randint(0,255)
    random_color = (r, g, b)
    return random_color

tim.setheading(225)
tim.forward(300)
tim.setheading(0)

def straight():
    for row in range(1,10):
        tim.dot(20, random_color())
        tim.forward(50)
    
def turn_right():
    tim.right(90)
    tim.forward(50)
    tim.right(90)
    
def turn_left():
    tim.left(90)
    tim.forward(50)
    tim.left(90)
    
        
for dot in range(5):
    straight()
    turn_left()
    tim.forward(50)
    straight()
    turn_right()
    tim.forward(50)
 
screen = t.Screen()
screen.exitonclick()
