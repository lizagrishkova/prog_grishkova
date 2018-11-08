import graphics as gr

window = gr.GraphWin("Picture", 1000, 1000)

sky = gr.Rectangle(gr.Point(0, 0), gr.Point(1000, 500))
sky.draw(window)
sky.setFill('cyan')

ray1 = gr.Line(gr.Point(100, 100), gr.Point(300, 100))
ray1.draw(window)

ray2 = gr.Line(gr.Point(100, 100), gr.Point(250, 200))
ray2.draw(window)

ray3 = gr.Line(gr.Point(100, 100), gr.Point(200, 250))
ray3.draw(window)

ray4 = gr.Line(gr.Point(100, 100), gr.Point(100, 300))
ray4.draw(window)

sun = gr.Circle(gr.Point(100, 100), 50)
sun.draw(window)
sun.setFill('yellow')

sea = gr.Rectangle(gr.Point(0, 500), gr.Point(1000, 1000))
sea.draw(window)
sea.setFill('blue')
   

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

fish_fin1 = gr.Polygon(gr.Point(150, 620), gr.Point(240, 570), gr.Point(250, 620))
fish_fin1.draw(window)
fish_fin1.setFill('red')

fish_fin2 = gr.Polygon(gr.Point(150, 680), gr.Point(240, 730), gr.Point(250, 680))
fish_fin2.draw(window)
fish_fin2.setFill('red')

fish_body = gr.Oval(gr.Point(100, 600), gr.Point(300, 700))
fish_body.draw(window)
fish_body.setFill('red')

fish_tail = gr.Polygon(gr.Point(300, 650), gr.Point(350, 700), gr.Point(350, 600))
fish_tail.draw(window)
fish_tail.setFill('red')

fish_eye = gr.Circle(gr.Point(150, 650), 10)
fish_eye.draw(window)
fish_eye.setFill('black')


cloud1 = gr.Circle(gr.Point(750, 100), 30)
cloud1.draw(window)
cloud1.setFill('white')

cloud2 = gr.Circle(gr.Point(780, 100), 30)
cloud2.draw(window)
cloud2.setFill('white')

cloud3 = gr.Circle(gr.Point(810, 100), 30)
cloud3.draw(window)
cloud3.setFill('white')

cloud4 = gr.Circle(gr.Point(765, 75), 30)
cloud4.draw(window)
cloud4.setFill('white')

cloud5 = gr.Circle(gr.Point(795, 75), 30)
cloud5.draw(window)
cloud5.setFill('white')

bird1 = gr.Polygon(gr.Point(750, 200), gr.Point(800, 250), gr.Point(850, 200), gr.Point(800, 270))
bird1.draw(window)
bird1.setFill('black')

bird2 = gr.Polygon(gr.Point(800, 300), gr.Point(850, 350), gr.Point(900, 300), gr.Point(850, 370))
bird2.draw(window)
bird2.setFill('black')

flag = gr.Polygon(gr.Point(480, 50), gr.Point(560, 50), gr.Point(530, 70), gr.Point(560, 90), gr.Point(480, 90))
flag.draw(window)
flag.setFill('magenta')

window.getMouse()

window.close()
