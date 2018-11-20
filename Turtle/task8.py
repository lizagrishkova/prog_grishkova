import turtle
import math

def draw_circle():
    n = 100
    d = 200
    for i in range(n):
        turtle.forward(d*math.sin(math.pi/n))
        turtle.left(360/n)

turtle.speed('fastest')
cnt = 10
for i in range(cnt):
    draw_circle()
    turtle.left(360/cnt)
