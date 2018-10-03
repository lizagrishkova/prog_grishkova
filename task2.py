import graphics as gr

window = gr.GraphWin("Picture", 1000, 1000)

def draw_sky():
    sky = gr.Rectangle(gr.Point(0,0), gr.Point(1000, 500))
    sky.draw(window)
    sky.setFill('cyan')

def draw_rays():
    ray1 = gr.Line(gr.Point(100, 100), gr.Point(300, 100))
    ray1.draw(window)

    ray2 = gr.Line(gr.Point(100, 100), gr.Point(250, 200))
    ray2.draw(window)

    ray3 = gr.Line(gr.Point(100, 100), gr.Point(200, 250))
    ray3.draw(window)

    ray4 = gr.Line(gr.Point(100, 100), gr.Point(100, 300))
    ray4.draw(window)

def draw_sun():
    sun = gr.Circle(gr.Point(100, 100), 50)
    sun.draw(window)
    sun.setFill('yellow')

def draw_sea():
    sea = gr.Rectangle(gr.Point(0, 500), gr.Point(1000, 1000))
    sea.draw(window)
    sea.setFill('blue')
    
def draw_boat():
    mast = gr.Line(gr.Point(480, 85),gr.Point(480, 450))
    mast.draw(window)

    sail1 = gr.Polygon(gr.Point(480, 100), gr.Point(480, 400), gr.Point(780,400))
    sail1.draw(window)
    sail1.setFill('white')                   

    sail2 = gr.Polygon(gr.Point(480, 100), gr.Point(480, 400), gr.Point(300,400))
    sail2.draw(window)
    sail2.setFill('white')

    boat = gr.Polygon(gr.Point(200, 450), gr.Point(800, 450), gr.Point(700, 550), gr.Point(300, 550))
    boat.draw(window)
    boat.setFill('brown')

    flag = gr.Polygon(gr.Point(480,50), gr.Point(560,50), gr.Point(530, 70), gr.Point(560,90), gr.Point(480,90))
    flag.draw(window)
    flag.setFill('magenta')

def draw_fish():
    fish_fin1 = gr.Polygon(gr.Point(550,620), gr.Point(640,570),gr.Point(650,620))
    fish_fin1.draw(window)
    fish_fin1.setFill('red')

    fish_fin2 = gr.Polygon(gr.Point(550,680), gr.Point(640,730),gr.Point(650,680))
    fish_fin2.draw(window)
    fish_fin2.setFill('red')

    fish_body = gr.Oval(gr.Point(500, 600), gr.Point(700, 700))
    fish_body.draw(window)
    fish_body.setFill('red')

    fish_tail = gr.Polygon(gr.Point(700, 650), gr.Point(750, 700), gr.Point(750,600))
    fish_tail.draw(window)
    fish_tail.setFill('red')

    fish_eye = gr.Circle(gr.Point(550, 650), 10)
    fish_eye.draw(window)
    fish_eye.setFill('black')

def draw_clouds():
    cloud1_1 = gr.Circle(gr.Point(800,100), 30)
    cloud1_1.draw(window)
    cloud1_1.setFill('white')

    cloud1_2 = gr.Circle(gr.Point(830,100), 30)
    cloud1_2.draw(window)
    cloud1_2.setFill('white')

    cloud1_3 = gr.Circle(gr.Point(860,100), 30)
    cloud1_3.draw(window)
    cloud1_3.setFill('white')

    cloud1_4 = gr.Circle(gr.Point(815,75), 30)
    cloud1_4.draw(window)
    cloud1_4.setFill('white')

    cloud1_5 = gr.Circle(gr.Point(845,75), 30)
    cloud1_5.draw(window)
    cloud1_5.setFill('white')

    cloud2_1 = gr.Circle(gr.Point(620,160), 30)
    cloud2_1.draw(window)
    cloud2_1.setFill('white')

    cloud2_2 = gr.Circle(gr.Point(650, 160), 30)
    cloud2_2.draw(window)
    cloud2_2.setFill('white')

    cloud2_3 = gr.Circle(gr.Point(680,160), 30)
    cloud2_3.draw(window)
    cloud2_3.setFill('white')

    cloud2_4 = gr.Circle(gr.Point(635, 135), 30)
    cloud2_4.draw(window)
    cloud2_4.setFill('white')

    cloud2_5 = gr.Circle(gr.Point(665,135), 30)
    cloud2_5.draw(window)
    cloud2_5.setFill('white')

    cloud3_1 = gr.Circle(gr.Point(820,235), 30)
    cloud3_1.draw(window)
    cloud3_1.setFill('white')

    cloud3_2 = gr.Circle(gr.Point(850,235), 30)
    cloud3_2.draw(window)
    cloud3_2.setFill('white')

    cloud3_3 = gr.Circle(gr.Point(880,235), 30)
    cloud3_3.draw(window)
    cloud3_3.setFill('white')

    cloud3_4 = gr.Circle(gr.Point(835,210), 30)
    cloud3_4.draw(window)
    cloud3_4.setFill('white')

    cloud3_5 = gr.Circle(gr.Point(865,210), 30)
    cloud3_5.draw(window)
    cloud3_5.setFill('white')

def draw_birds():
    bird1 = gr.Polygon(gr.Point(270,200), gr.Point(320,250), gr.Point(370,200),gr.Point(320,270))
    bird1.draw(window)
    bird1.setFill('black')

    bird2 = gr.Polygon(gr.Point(200,300), gr.Point(250,350), gr.Point(300,300),gr.Point(250,370))
    bird2.draw(window)
    bird2.setFill('black')


def draw_picture():
    draw_sky()
    draw_rays()
    draw_sun()
    draw_sea()
    draw_boat()
    draw_fish()
    draw_clouds()
    draw_birds()

draw_picture()    
    
window.getMouse()

window.close()
