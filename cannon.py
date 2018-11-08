import math
from tkinter import *

root = Tk()
root.geometry('800x600')        
canvas = Canvas(root, bg='white') 
canvas.pack(fill=BOTH, expand=1)

g = 9.8  # Ускорение свободного падения для снаряда.
r = 20  # Радиус пушечного ядра


def draw_cannon():
    cannon = canvas.create_oval(0, 500, 100, 600, fill='black')
    cannon_muzzle = canvas.create_line(50, 550, 100, 500, fill='black', width=30)


class Cannon:
    max_velocity = 10

    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.shell_num = None  # TODO: оставшееся на данный момент количество снарядов
        self.direction = math.pi / 4

    def aim(self, event):
        x = event.x
        y = event.y
        self.direction = math.atan((y - self.y)/(x - self.x))
        """
        Меняет направление direction так, чтобы он из точки
         (self.x, self.y) указывал в точку (x, y).
        :param x: координата x, в которую целимся
        :param y: координата y, в которую целимся
        :return: None
        """

    def fire(self, dt):
        if self.shell_num > 0:
            cannonball = canvas.create_oval(self.x-r, self.y-r, self.x+r, self.y+r, fill=random.choice(colors))
        """
        Создаёт объект снаряда (если ещё не потрачены все снаряды)
        летящий в направлении угла direction
        со скоростью, зависящей от длительности клика мышки
        :param dt:  длительность клика мышки, мс
        :return: экземпляр снаряда типа Shell
        """
        pass


class Shell:
    standard_radius = 5

    def __init__(self, x, y, vx, vy):
        self.x, self.y = x, y
        self.vx, self.vy = vx, vy
        self.r = standard_raduis

    def go(self, dt):
        """
        Сдвигает снаряд исходя из его кинематических характеристик
        и длины кванта времени dt
        в новое положение, а также меняет его скорость.
        :param dt:
        :return:
        """
        ax, ay = 0, g
        self.x += self.vx*dt + ax*(dt**2)/2
        self.y += self.vy*dt + ay*(dt**2)/2
        self.vx += ax*dt
        self.vy += ay*dt
        # TODO: Уничтожать (в статус deleted) снаряд, когда он касается земли.

    def detect_collision(self, other):
        """
        Проверяет факт соприкосновения снаряда и объекта other
        :param other: объект, который должен иметь поля x, y, r
        :return: логическое значение типа bool
        """
        length = ((self.x - other.x)**2 + (self.y - other.y)**2)**0.5
        return length <= self.r + other.r


class Target:
    standard_radius = 5

    def __init__(self, x, y, vx, vy):
        self.x, self.y = x, y
        self.vx, self.vy = vx, vy
        self.r = standard_raduis

    def go(self, dt):
        """
        Сдвигает шарик-мишень исходя из его кинематических характеристик
        и длины кванта времени dt
        в новое положение, а также меняет его скорость.
        :param dt:
        :return:
        """
        ax, ay = 0, g
        self.x += self.vx * dt
        self.y += self.vy * dt
        self.vx += ax * dt
        self.vy += ay * dt
        # TODO: Шарики-мишени должны отражаться от стенок

    def collide(self, other):
        """
        Расчёт абсолютно упругого соударения
        :param other:
        :return:
        """
        pass  # TODO


cannon = Cannon(40, 40)
draw_cannon()
canvas.bind('<Motion>', cannon.aim)
