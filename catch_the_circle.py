from tkinter import *
import random
root = Tk()
root.geometry('800x600')
canv = Canvas(root, bg='white')
canv.pack(fill=BOTH, expand=1)

colors = ['red', 'orange', 'yellow', 'green', 'blue', 'gray', 'black', 'violet', 'cyan']

def left_button(event):
    r = 50
    x = event.x
    y = event.y
    canv.create_oval(x - r, y - r, x + r, y + r, fill = random.choice(colors))
    
def right_button(event):
    canv.delete(ALL)

root.bind('<Button-1>', left_button)
root.bind('<Button-3>', right_button)

mainloop()
