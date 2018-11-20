import turtle
import math

def draw_circle(d):
    n = 100
    for i in range(n):
        turtle.forward(d*math.sin(math.pi/n))
        turtle.left(360/n)

turtle.speed('fastest')
cnt = 10
d = 100
turtle.left(90)
for i in range(cnt):
    for j in range(2):
        draw_circle(d)
        turtle.left(180)    
    d += 20
