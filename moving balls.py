import pygame as pyg
import random as rand


def random_rgb():
    return rand.randint(0, 255), rand.randint(0, 255), rand.randint(0, 255)


class PygView(object):

    def __init__(self, width=800, height=600, fps=35):

        pyg.init()
        pyg.display.set_caption("Press ESC to quit")

        self.width = width
        self.height = height

        self.screen = pyg.display.set_mode((self.width, self.height), pyg.DOUBLEBUF)
        self.background = pyg.Surface(self.screen.get_size()).convert()
        self.background.fill((255, 255, 255))

        self.act_surface = self.screen
        self.act_rgb = 255, 0, 0

    def draw_dynamic(self):

        self.act_surface = self.screen

    def set_color(self, rgb):

        self.act_rgb = rgb

    def circle(self, x, y, radius):
        rad2 = 2 * radius
        surface = pyg.Surface((rad2, rad2))
        pyg.draw.circle(surface, self.act_rgb, (radius, radius), radius)
        surface.set_colorkey((0, 0, 0))
        self.act_surface.blit(surface.convert_alpha(), (x, y))

    def run(self, draw_dynamic):
        """The mainloop
        """
        running = True
        while running:
            for event in pyg.event.get():
                if event.type == pyg.QUIT:
                    running = False
                elif event.type == pyg.KEYDOWN:
                    if event.key == pyg.K_ESCAPE:
                        running = False

            draw_dynamic()
            pyg.display.flip()
            self.screen.blit(self.background, (0, 0))

        pyg.quit()


class Ball(object):

    def __init__(self, x, y, radius, speed_x, speed_y, color):

        self.x = x
        self.y = y
        self.radius = radius

        self.speed_x = speed_x
        self.speed_y = speed_y
        self.color = color

    def draw(self, view):

        color = self.color
        view.set_color(color)
        view.circle(self.x, self.y, self.radius)


def action(balls, width, height, view):

    def animate_balls():

        for ball in balls:
            if ball.x + 2 * ball.radius > width or ball.x < 0:
                ball.speed_x = -ball.speed_x
                ball.x += ball.speed_x
            else:
                ball.x += ball.speed_x

            if ball.y + 2 * ball.radius > height or ball.y < 0:
                ball.speed_y = -ball.speed_y
                ball.y += ball.speed_y
            else:
                ball.y += ball.speed_y

            ball.draw(view)

    return animate_balls


def main(width, height):

    view = PygView(width, height)
    AMOUNT_OF_BALLS = 5

    view.draw_dynamic()
    balls = []
    for i in range(AMOUNT_OF_BALLS):
        R = rand.randint(20, 60)
        x = rand.randint(R, width - 2*R)
        y = rand.randint(R, height - 2*R)
        speed_x = rand.randint(1, 3)
        speed_y = rand.randint(1, 3)
        ball = Ball(x, y, R, speed_x, speed_y, random_rgb())
        balls.append(ball)

    loopfunc = action(balls, width, height, view)
    view.run(loopfunc)


if __name__ == '__main__':
    main(900, 600)
