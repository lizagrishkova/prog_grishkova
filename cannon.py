import math
from tkinter import *


g = 9.8  # Ускорение свободного падения для снаряда.


class Cannon:
    max_velocity = 1000

    def __init__(self, canvas):
        self.power = 10
        self.x = 50
        self.y = 550
        self.r = 50
        self.canvas = canvas
        self.shell_num = None  # TODO: оставшееся на данный момент количество снарядов
        self.direction = math.pi / 4
        self.line_length = 100
        self.line = canv.create_line(self.x, self.y, self.x + self.line_length, self.y, width=30, fill="black")
        self.oval = canv.create_oval(self.x - self.r, self.y + self.r, self.x + self.r, self.y - self.r,
                                     outline="black", fill="black")

    def aim(self, x, y):
        """
        Меняет направление direction так, чтобы он из точки
         (self.x, self.y) указывал в точку (x, y).
        :param x: координата x, в которую целимся
        :param y: координата y, в которую целимся
        :return: None
        """
        self.direction = math.atan((self.y - y)/(self.x - x))
        self.draw()

    def fire(self, dt):
        """
        Создаёт объект снаряда (если ещё не потрачены все снаряды)
        летящий в направлении угла direction
        со скоростью, зависящей от длительности клика мышки
        :param dt:  длительность клика мышки, мс
        :return: экземпляр снаряда типа Shell
        """

        shell = Shell(self.x + self.line_length*math.cos(self.direction),
                      self.y + self.line_length*math.sin(self.direction), self.canvas)

        shells.append(shell)

    def draw(self):

        self.canvas.delete(self.line)

        self.line = self.canvas.create_line(
            self.x,
            self.y,
            self.x + self.line_length*math.cos(self.direction),
            self.y + self.line_length*math.sin(self.direction), width=30, fill="black"
        )


class Shell:
    global standard_radius
    standard_radius = 30

    def __init__(self, x, y, canvas):
        self.x, self.y = x, y
        self.Vx, self.Vy = 500, -500
        self.dx, self.dy = 0, 0
        self.r = standard_radius
        self.canvas = canvas
        self.oval = self.canvas.create_oval(self.x - self.r, self.y - self.r,
                                            self.x + self.r, self.y + self.r, fill='cyan')

    def go(self, dt):
        ax, ay = 0, g
        self.dx = self.Vx * dt + ax * (dt ** 2) / 2
        self.dy = self.Vy * dt + ay * (dt ** 2) / 2
        self.x += self.dx
        self.y += self.dy
        self.Vx += ax * dt
        self.Vy -= ay * dt

        print('x = {}, y = {}'.format(self.x, self.y))
        self.draw()

        # TODO: Уничтожать (в статус deleted) снаряд, когда он касается земли.

    def draw(self):
        self.canvas.move(self.oval, self.dx, self.dy)

    def detect_collision(self, other):
        """
        Проверяет факт соприкосновения снаряда и объекта other
        :param other: объект, который должен иметь поля x, y, r
        :return: логическое значение типа bool
        """

        length = ((self.x - other.x) ** 2 + (self.y - other.y) ** 2) ** 0.5
        return length <= self.r + other.r


class Target:
    standard_radius = 5

    def __init__(self, x, y, Vx, Vy):
        self.x, self.y = x, y
        self.Vx, self.Vy = Vx, Vy
        self.r = standard_radius

    def go(self, dt):
        """
        Сдвигает шарик-мишень исходя из его кинематических характеристик
        и длины кванта времени dt
        в новое положение, а также меняет его скорость.
        :param dt:
        :return:
        """

        ax, ay = 0, g
        self.x += self.Vx * dt + ax * (dt ** 2) / 2
        self.y += self.Vy * dt - ay * (dt ** 2) / 2
        self.Vx += ax * dt
        self.Vy -= ay * dt

        # TODO: Шарики-мишени должны отражаться от стенок

    def collide(self, other):
        """
        Расчёт абсолютно упругого соударения
        :param other:
        :return:
        """

        pass  # TODO


def mouse_move_handler(event):
    cannon.aim(event.x, event.y)


def mouse_left_click_handler(event):
    cannon.fire(100)


def tick():
    for shell in shells:
        shell.go(0.01)

    root.after(100, tick)


root = Tk()
fr = Frame(root)
root.geometry('800x600')
canv = Canvas(root, bg='white')
canv.pack(fill=BOTH, expand=1)

canv.bind('<Motion>', mouse_move_handler)
canv.bind('<Button-1>', mouse_left_click_handler)

shells = []

cannon = Cannon(canv)

tick()
root.mainloop()
