import turtle
import math


def draw_polygon(d, n):
    turtle.left(90+180/n)
    for i in range(n):
        turtle.forward(d*math.sin(math.pi/n))
        turtle.left(360/n)

d = 60
n = 3
s = 15
for i in range(5):
    draw_polygon(d, n)

    turtle.right(90+180/n)
    turtle.penup()
    turtle.forward(s)
    turtle.pendown()

    n+=1
    d+=2*s
