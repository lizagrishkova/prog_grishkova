from tkinter import *
import random
root = Tk()
root.geometry('800x600')
canv = Canvas(root, bg='white')
canv.pack(fill=BOTH, expand=1)

colors = ['red', 'orange', 'yellow', 'green', 'blue', 'gray', 'black', 'violet', 'cyan']
cnt_win = 0
cnt_lose = 0

def draw_circle():
    global r_circle, x_circle, y_circle 
    root.after(600, draw_circle)
    canv.delete(ALL)
    r_circle = random.randint(10,150)
    x_circle = random.randint(r_circle,800-r_circle)
    y_circle = random.randint(r_circle,600-r_circle)
    canv.create_oval(x_circle - r_circle, y_circle - r_circle, x_circle + r_circle, y_circle + r_circle, fill = random.choice(colors))
    canv.create_text(400, 25, text = "Попадания" , font = 'Arial 15')
    canv.create_text(460, 25, text = cnt_win, font = 'Arial 15')
    canv.create_text(400, 45, text = "Промахи" , font = 'Arial 15')
    canv.create_text(460, 45, text = cnt_lose, font = 'Arial 15')
    
def left_button(event):
    x = event.x
    y = event.y
    global cnt_win, cnt_lose
    if (x - x_circle)**2 + (y - y_circle)**2 <= r_circle**2:
        cnt_win += 1
    else:
        cnt_lose += 1
    #canv.create_text(400,580, text = cnt)
        
root.bind('<Button-1>', left_button)
root.after_idle(draw_circle)
mainloop()
