import robot
r = robot.rmap()

r.lm('task5')


def task():
    for i in range(3):
        for j in range(5):
            r.pt()
            r.dn()
            r.rt()
            r.pt()
            r.up()
            r.rt()
            r.pt()
            if not r.wr():
                r.rt()
        if not r.wd():
            r.dn(3)
            r.lt(14)


r.start(task)