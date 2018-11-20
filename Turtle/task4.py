import turtle
import math

n = 100
d = 50
for i in range(n):
    turtle.forward(d*math.sin(math.pi/n))
    turtle.left(360/n)

