import turtle
import math

def draw_star(n):
    l = 100
    for i in range(n):
        turtle.forward(l)
        turtle.left(180-180/n)

draw_star(11)
