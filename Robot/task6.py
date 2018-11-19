import robot
r = robot.rmap()

r.lm('task6')


def task():

    width = int(input("Введите ширину: "))
    height = int(input("Введите высоту: "))

    if not width % 2:
        width += 1
    for i in range(width):
        r.pt()
        r.rt()
    r.lt(int(width/2) + 1)
    for i in range(height):
        r.pt()
        r.dn()

r.start(task)