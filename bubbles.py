from tkinter import *
import random

root = Tk()
width = 400
height = 400
root.geometry('400x400')
canvas = Canvas(root, bg='white')
canvas.pack(fill=BOTH, expand=1)
colors = ['red', 'orange', 'yellow', 'green', 'blue', 'gray', 'black', 'violet', 'cyan']
cnt = 5
r = 30
balls = []

for i in range(cnt):
    x = random.randint(r, width-r)
    y = random.randint(r, height-r)
    dx = random.randint(1,   10)
    dy = random.randint(1, 10)
    circle = canvas.create_oval(x-r, y-r, x+r, y+r, fill=random.choice(colors))
    ball = [x, y,   dx, dy, circle]
    balls.append(ball)


def tick_handler():
    
    global balls
    for i in range(len(balls)):
        x, y, dx, dy, circle = balls[i]
        x += dx
        y += dy
        if x < 0:
            dx = -dx
            x = 0
        elif x > width-r:
            dx = -dx
            x = width-r
        if y < 0:
            dy = -dy
            y = 0
        elif y > height-r:
            dy = -dy
            y = height-r
        balls[i] = [x, y, dx, dy, circle]
        canvas.move(circle, dx, dy)

    
def time_handler():
    
    global freeze
    speed = speed_scale.get()
    if speed == 0:
        print("Заморозка")
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
