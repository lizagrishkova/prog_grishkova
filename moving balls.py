import pygame as pyg
import random as rand


def random_rgb():
    return rand.randint(0, 255), rand.randint(0, 255), rand.randint(0, 255)


class PygView(object):

    def __init__(self, width=800, height=600):
        """Initializing screen surface for dynamic drawing
        """
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

    def __init__(self, x, y, radius, speed_x=1, speed_y=1, color=(0, 0, 255)):

        self.x = x
        self.y = y
        self.radius = radius
        self.act_radius = radius
        self.speed_x = speed_x
        self.speed_y = speed_y
        self.color = color

    @property
    def max_x(self):
        return self.x + self.radius*2

    @property
    def max_y(self):
        return self.y + self.radius*2

    def rel_move(self, dx, dy):

        self.x += dx
        self.y += dy

    def draw(self, view):

        color = self.color
        view.set_color(color)
        view.circle(self.x, self.y, self.act_radius)


def action(balls, width, height, view):
    """ Return a function for the pygame mainloop
    """

    right_moving = [True] * len(balls)
    down_moving = [True] * len(balls)

    def animate_balls():
        """ Draw moving balls
        """
        for i, ball in enumerate(balls):
            if right_moving[i]:
                if ball.x > 0 and ball.max_x < width:
                    ball.rel_move(ball.speed_x, ball.speed_y)
                else:
                    right_moving[i] = False
            else:
                ball.speed_x = -ball.speed_x
                ball.rel_move(3*ball.speed_x, ball.speed_y)
                right_moving[i] = True
                
            if down_moving[i]:
                if ball.y > 0 and ball.max_y < height:
                    ball.rel_move(ball.speed_x, ball.speed_y)
                else:
                    down_moving[i] = False
            else:
                ball.speed_y = -ball.speed_y
                ball.rel_move(ball.speed_x, 3*ball.speed_y)
                down_moving[i] = True
                
            ball.draw(view)

    return animate_balls


def main(width, height):

    view = PygView(width, height)
    AMOUNT_OF_BALLS = 5

    view.draw_dynamic()
    balls = []
    for i in range(AMOUNT_OF_BALLS):
        r = rand.randint(30, 60)
        x = rand.randint(r, width - 2*r)
        y = rand.randint(r, height - 2*r)
        speed_x = rand.randint(1, 2)
        speed_y = rand.randint(1, 2)
        ball = Ball(x, y, r, speed_x, speed_y, random_rgb())
        balls.append(ball)

    loopfunc = action(balls, width, height, view)
    view.run(loopfunc)


if __name__ == '__main__':
    main(900, 600)
