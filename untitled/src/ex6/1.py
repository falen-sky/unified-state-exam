from turtle import *

# https://inf-ege.sdamgia.ru/problem?id=58249
m = 15
tracer(0)
for i in range(5):
    forward(8*m)
    right(60)
    forward(8*m)
    right(120)
pu()
for x in range(-15,15):
    for y in range(-15,15):
        goto(x*m, y*m)
        dot(3)
done()


