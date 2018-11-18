import robot
r = robot.rmap()

r.lm('task3')


def task():
    r.rt()
    for i in range(8):
        if r.fd():
            r.dn()
            r.up()
        r.rt()


r.start(task)