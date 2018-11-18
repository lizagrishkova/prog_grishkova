import robot
r = robot.rmap()

r.lm('task2')


def task():
    for i in range(5):
        r.up()
        r.pt()
        r.rt()
        r.dn()
        r.pt()
        r.up(2)
        r.pt()
        r.rt()
        r.dn()
        r.pt()
        r.dn()
        r.rt()


r.start(task)