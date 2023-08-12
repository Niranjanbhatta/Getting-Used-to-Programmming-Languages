from turtle import Turtle, Screen
import random

is_race_on = False

new_turtle = Turtle()
screen = Screen()
screen.setup(width =  500, height = 400)

user_bet = screen.textinput(title = "Make your bet ", prompt = "Which colour will win the race? Enter a color to start: ")
colors = ("red","orange","yellow","green","blue","purple")
y_position = [-150 ,-100 ,-50 ,0 ,50 ,100]
all_turtle = []

for turtle_index in range (0 , 6):
    new_turtle = Turtle(shape="turtle")
    new_turtle.color(colors[turtle_index])
    new_turtle.penup()
    new_turtle.goto(x=-230, y= y_position[turtle_index])
    all_turtle.append(new_turtle)

if user_bet:
    is_race_on = True
    
while is_race_on:
    
    for turtle in all_turtle:
        
        if turtle.xcor() > 230:
            winning_color = turtle.pencolor()
            is_race_on = False
            if winning_color == user_bet:
                print(f"You Won! The {winning_color} colored turtle is the winner")
            else:
                print(f"You Lost! The {winning_color} colored turtle is the winner")
            
        random_distance = random.randint(0,20)
        turtle.forward(random_distance)
    
screen.exitonclick()
