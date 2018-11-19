import turtle

x = int(input())
for i in range(1, x):
    if i % 2:
        print(i, 'odd', sep=' ')
    else:
        print(i, 'even', sep=' ')