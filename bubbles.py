from tkinter import *
import random

root = Tk()
width = 400
height = 400
root.geometry('400x400')
canvas = Canvas(root, bg='white')
canvas.pack(fill=BOTH, expand=1)
colors = ['red', 'orange', 'yellow', 'green', 'blue', 'gray', 'black', 'violet', 'cyan']
AMOUNT_OF_BALLS = 5
R = 30
balls = []

for i in range(AMOUNT_OF_BALLS):
    x = random.randint(R, width-R)
    y = random.randint(R, height-R)
    dx = random.randint(1, 10)
    dy = random.randint(1, 10)
    circle = canvas.create_oval(x-R, y-R, x+R, y+R, fill=random.choice(colors))
    ball = [x, y, dx, dy, circle]
    balls.append(ball)


def tick_handler():
    
    global balls
    for j in range(len(balls)):
        x_ball, y_ball, dx_ball, dy_ball, circle_ball = balls[j]
        x_ball += dx_ball
        y_ball += dy_ball
        if x_ball < 0:
            dx_ball = -dx_ball
            x_ball = 0
        elif x_ball > width-R:
            dx_ball = -dx_ball
            x_ball = width-R
        if y_ball < 0:
            dy_ball = -dy_ball
            y_ball = 0
        elif y_ball > height-R:
            dy_ball = -dy_ball
            y_ball = height-R
        balls[j] = [x_ball, y_ball, dx_ball, dy_ball, circle_ball]
        canvas.move(circle_ball, dx_ball, dy_ball)

    
def time_handler():
    
    global freeze
    speed = speed_scale.get()
    if speed == 0:
        freeze = True
        return
    tick_handler()
    sleep_dt = 1100 - 100*speed
    root.after(sleep_dt, time_handler)

    
def unfreezer(event):
    
    global freeze
    if freeze:
        speed = speed_scale.get()
        if speed != 0:
            freeze = False
            root.after(0, time_handler)


speed_scale = Scale(root, orient=HORIZONTAL, length=300, from_=0, to=10, tickinterval=1, resolution=1)

speed_scale.pack()
speed_scale.set(1)
freeze = False
root.after(10, time_handler)
speed_scale.bind("<Motion>", unfreezer)

root.mainloop()
