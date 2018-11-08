import graphics as gr

window = gr.GraphWin("Picture", 1000, 1000)


def draw(obj, color):
    
    obj.draw(window)
    obj.setFill(color)

    
def draw_ray(x_sun, y_sun, x, y):
    
    ray = gr.Line(gr.Point(x_sun, y_sun), gr.Point(x, y)) 
    draw(ray, 'black')


def draw_sun():

    x = 300
    y = 100
    for i in range(4):
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

    mast = gr.Line(gr.Point(480, 85), gr.Point(480, 450))
    draw(mast, 'black')

    sail1 = gr.Polygon(gr.Point(480, 100), gr.Point(480, 400), gr.Point(780, 400))
    draw(sail1, 'white')               

    sail2 = gr.Polygon(gr.Point(480, 100), gr.Point(480, 400), gr.Point(300, 400))
    draw(sail2, 'white')

    boat = gr.Polygon(gr.Point(200, 450), gr.Point(800, 450), gr.Point(700, 550), gr.Point(300, 550))
    draw(boat, 'brown')

    flag = gr.Polygon(gr.Point(480, 50), gr.Point(560, 50), gr.Point(530, 70), gr.Point(560, 90), gr.Point(480, 90))
    draw(flag, 'magenta')


def draw_fish():

    fish_fin1 = gr.Polygon(gr.Point(550, 620), gr.Point(640, 570), gr.Point(650, 620))
    draw(fish_fin1, 'red')

    fish_fin2 = gr.Polygon(gr.Point(550, 680), gr.Point(640, 730), gr.Point(650, 680))
    draw(fish_fin2, 'red')
    
    fish_body = gr.Oval(gr.Point(500, 600), gr.Point(700, 700))
    draw(fish_body, 'red')

    fish_tail = gr.Polygon(gr.Point(700, 650), gr.Point(750, 700), gr.Point(750, 600))
    draw(fish_tail, 'red')

    fish_eye = gr.Circle(gr.Point(550, 650), 10)
    draw(fish_eye, 'black')


def draw_cloud(x, y, size):

    # x, y - координаты центра левого нижнего круга, size - радиус одного круга
    for i in range(3):
        cloud = gr.Circle(gr.Point(x, y), size)
        x += size
        draw(cloud, 'white')
    x = x - 2.5 * size 
    y = y - size
    for i in range(2):
        cloud = gr.Circle(gr.Point(x, y), size)
        x += size
        draw(cloud, 'white')
    
    
def draw_bird(x, y):

    # x, y - координаты левого крыла
    bird = gr.Polygon(gr.Point(x, y), gr.Point(x + 50, y + 50), gr.Point(x + 100, y), gr.Point(x + 50, y + 70))  
    draw(bird, 'black')
   
   
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

window.getMouse()

window.close()
