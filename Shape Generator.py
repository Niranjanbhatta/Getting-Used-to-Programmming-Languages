import turtle as t
import random

tim = t.Turtle()

colors = ["medium aquamarine", "CornflowerBlue", "DarkOrchid", "IndianRed", "DeepSkyBlue", "LightSeaGreen", "wheat", "SlateGray", "SeaGreen"]

def draw_shape(num_side):
    angle = 360 / num_side
    for _ in range(num_side):
        tim.forward(50)
        tim.right(angle)
        
for shape_side_n in range(3,11):
    tim.color(random.choice(colors))
    draw_shape(shape_side_n)
