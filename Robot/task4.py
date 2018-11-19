import robot
r = robot.rmap()

r.lm('task4')


def task():
    while not r.wu():
        r.up()
    while not r.wr():
        r.rt()
    r.lt()
    for i in range(5):
        for j in range(3):
            r.dn()
            r.pt()
            r.dn()
        r.up(5)
        r.lt()


r.start(task)