import turtle
turtle.speed('fastest')


def curve(l, n):
    if n == 0:
        turtle.forward(l)
    else:
        curve(l/3, n-1)
        turtle.left(60)
        curve(l/3, n-1)
        turtle.right(120)
        curve(l/3, n-1)
        turtle.left(60)
        curve(l/3, n-1)


def snowflake(l, n):
    for i in range(3):
        curve(l, n)
        turtle.right(120)


l = 200
n = 3
snowflake(l, n)
