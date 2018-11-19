import turtle
import math

n = 50
d = 50
turtle.left(90)

for k in range (10):
    for i in range(n):
        x = 10/n
        turtle.forward(d*math.sin(math.pi/n))
        turtle.left(360/n)
        d += x
    
