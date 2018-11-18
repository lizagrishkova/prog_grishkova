import graphics as gr
import time

window = gr.GraphWin("Picture", 1000, 1000)


def draw_ray(x_sun, y_sun, x, y):
    
    ray = gr.Line(gr.Point(x_sun, y_sun), gr.Point(x, y))
    ray.draw(window)


def draw_sun():
  
    x = 300
    y = 100
    for i in range(4):
        draw_ray(100, 100, x, y)
        x -= 65
        y += 65
    sun = gr.Circle(gr.Point(100, 100), 50)
    sun.draw(window)
    sun.setFill('yellow')


def draw_sky():
    
    sky = gr.Rectangle(gr.Point(0, 0), gr.Point(1000, 500))
    sky.draw(window)
    sky.setFill('cyan')
    draw_sun()


def draw_sea():

    sea = gr.Rectangle(gr.Point(0, 500), gr.Point(1000, 1000))
    sea.draw(window)
    sea.setFill('blue')

    
def draw_boat():

    mast = gr.Line(gr.Point(480, 85), gr.Point(480, 450))
    mast.draw(window)

    sail1 = gr.Polygon(gr.Point(480, 100), gr.Point(480, 400), gr.Point(780, 400))
    sail1.draw(window)
    sail1.setFill('white')                   

    sail2 = gr.Polygon(gr.Point(480, 100), gr.Point(480, 400), gr.Point(300, 400))
    sail2.draw(window)
    sail2.setFill('white')

    boat = gr.Polygon(gr.Point(200, 450), gr.Point(800, 450), gr.Point(700, 550), gr.Point(300, 550))
    boat.draw(window)
    boat.setFill('brown')

    flag = gr.Polygon(gr.Point(480, 50), gr.Point(560, 50), gr.Point(530, 70), gr.Point(560, 90), gr.Point(480, 90))
    flag.draw(window)
    flag.setFill('magenta')


def draw_fish():

    fish_fin1 = gr.Polygon(gr.Point(550, 620), gr.Point(640, 570), gr.Point(650, 620))
    fish_fin1.draw(window)
    fish_fin1.setFill('red')

    fish_fin2 = gr.Polygon(gr.Point(550, 680), gr.Point(640, 730), gr.Point(650, 680))
    fish_fin2.draw(window)
    fish_fin2.setFill('red')

    fish_body = gr.Oval(gr.Point(500, 600), gr.Point(700, 700))
    fish_body.draw(window)
    fish_body.setFill('red')

    fish_tail = gr.Polygon(gr.Point(700, 650), gr.Point(750, 700), gr.Point(750, 600))
    fish_tail.draw(window)
    fish_tail.setFill('red')

    fish_eye = gr.Circle(gr.Point(550, 650), 10)
    fish_eye.draw(window)
    fish_eye.setFill('black')


def draw_bird(x, y):
    
    # x, y - координаты левого крыла
    bird = gr.Polygon(gr.Point(x, y), gr.Point(x + 50, y + 50), gr.Point(x + 100, y), gr.Point(x + 50, y + 70))  
    bird.draw(window)
    bird.setFill('black')


def draw_cloud(x, y, size):

    # x, y - координаты центра левого нижнего круга, size - радиус одного круга
    for i in range(3):
        cloud = gr.Circle(gr.Point(x, y), size)
        x += size
        cloud.draw(window)
        cloud.setFill('white')
    x = x - 2.5 * size 
    y = y - size
    for i in range(2):
        cloud = gr.Circle(gr.Point(x, y), size)
        x += size
        cloud.draw(window)
        cloud.setFill('white')


def draw_moving_cloud():
    
    cloud1 = gr.Circle(gr.Point(820, 235), 30)
    cloud1.draw(window)
    cloud1.setFill('white')

    cloud2 = gr.Circle(gr.Point(850, 235), 30)
    cloud2.draw(window)
    cloud2.setFill('white')

    cloud3 = gr.Circle(gr.Point(880, 235), 30)
    cloud3.draw(window)
    cloud3.setFill('white')

    cloud4 = gr.Circle(gr.Point(835, 205), 30)
    cloud4.draw(window)
    cloud4.setFill('white')

    cloud5 = gr.Circle(gr.Point(865, 205), 30)
    cloud5.draw(window)
    cloud5.setFill('white')

    for i in range(25):
        time.sleep(0.2)
        cloud1.move(10, 0)
        cloud2.move(10, 0)
        cloud3.move(10, 0)
        cloud4.move(10, 0)
        cloud5.move(10, 0)

   
def draw_picture():

    draw_sky()
    # draw_sun()
    draw_bird(270, 200)
    draw_bird(200, 300)
    draw_sea()
    draw_boat()
    draw_fish()
    draw_cloud(800, 100, 30)
    draw_cloud(620, 160, 30)
    draw_moving_cloud()
    # draw_cloud(820, 235, 30)


draw_picture()    
    
window.getMouse()

window.close()
