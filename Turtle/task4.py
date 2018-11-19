import turtle


a = 30
for i in range(10):
    turtle.penup()
    turtle.goto(-a/2, -a/2)
    turtle.pendown()
    for j in range(4):
        turtle.forward(a)
        turtle.left(90)
    a += 30
