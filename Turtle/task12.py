import turtle
import math


turtle.speed('fastest')

def draw_arc(d):
    n = 50
    for i in range(n):
        turtle.forward(d*math.sin(math.pi/n))
        turtle.right(180/n)

D = 40
d = 10
turtle.left(90)
for i in range(5):
    draw_arc(D)
    draw_arc(d)
