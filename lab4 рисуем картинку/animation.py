import graphics as gr
import time

window = gr.GraphWin("Picture", 1000, 1000)


def draw(obj, color):
    obj.draw(window)
    obj.setFill(color)


def make_points(dot):
    return gr.Point(dot[0], dot[1])


def draw_polygon(points, color):
    obj = gr.Polygon(list(map(make_points, points)))
    draw(obj, color)


def draw_ray(x_sun, y_sun, x, y):
    ray = gr.Line(gr.Point(x_sun, y_sun), gr.Point(x, y))
    draw(ray, 'black')


def draw_sun():
    x = 300
    y = 100
    for k in range(4):
        draw_ray(100, 100, x, y)
        x -= 65
        y += 65
    sun = gr.Circle(gr.Point(100, 100), 50)
    draw(sun, 'yellow')


def draw_sky():
    sky = gr.Rectangle(gr.Point(0, 0), gr.Point(1000, 500))
    draw(sky, 'cyan')


def draw_sea():
    sea = gr.Rectangle(gr.Point(0, 500), gr.Point(1000, 1000))
    draw(sea, 'blue')


def draw_boat():
    draw_polygon([[480, 85], [480, 450]], 'black')  # mast
    draw_polygon([[480, 100], [480, 400], [780, 400]], 'white')  # sail1
    draw_polygon([[480, 100], [480, 400], [300, 400]], 'white')  # sail2
    draw_polygon([[200, 450], [800, 450], [700, 550], [300, 550]], 'brown')  # boat
    draw_polygon([[480, 50], [560, 50], [530, 70], [560, 90], [480, 90]], 'magenta')  # flag


def draw_fish():
    draw_polygon([[550, 620], [640, 570], [650, 620]], 'red')  # fish_fin1
    draw_polygon([[550, 680], [640, 730], [650, 680]], 'red')  # fish_fin2

    fish_body = gr.Oval(gr.Point(500, 600), gr.Point(700, 700))
    draw(fish_body, 'red')

    draw_polygon([[700, 650], [750, 700], [750, 600]], 'red')  # fish_tail

    fish_eye = gr.Circle(gr.Point(550, 650), 10)
    draw(fish_eye, 'black')


def draw_cloud(x, y, size):
    # x, y - координаты центра левого нижнего круга, size - радиус одного круга
    global clouds
    clouds = []
    for j in range(3):
        cloud_circle = gr.Circle(gr.Point(x, y), size)
        x += size
        clouds.append(cloud_circle)
    x = x - 2.5 * size
    y = y - size
    for j in range(2):
        cloud_circle = gr.Circle(gr.Point(x, y), size)
        x += size
        clouds.append(cloud_circle)
    for cloud_circle in clouds:
        draw(cloud_circle, 'white')


def draw_bird(x, y):
    # x, y - координаты левого крыла
    draw_polygon([[x, y], [x + 50, y + 50], [x + 100, y], [x + 50, y + 70]], 'black')  # bird


def draw_picture():
    draw_sky()
    draw_sun()
    draw_bird(270, 200)
    draw_bird(200, 300)
    draw_sea()
    draw_boat()
    draw_fish()
    draw_cloud(800, 100, 30)
    draw_cloud(620, 160, 30)
    draw_cloud(820, 235, 30)


draw_picture()
for i in range(250):
    time.sleep(0.01)
    for cloud in clouds:
        cloud.move(1, 0)

window.getMouse()

window.close()
