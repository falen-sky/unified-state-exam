#https://inf-ege.sdamgia.ru/problem?id=59799
from turtle import *
tracer(0)
m = 15
for i in range(2):
    forward(9*m)
    right(90)
    forward(15*m)
    right(90)
pu()
forward(12*m)
right(90)
pd()
for i in range(2):
    forward(6*m)
    right(90)
    forward(12*m)
    right(90)
pu()
for x in range(-15,15):
    for y in range(-15,15):
        goto(x*m,y*m)
        dot(3)
done()
# from turtle import *
# left(90)
# k = 20
# tracer(3)
# for i in range(2):
#     forward(9 * k)
#     right(90)
#     forward(15 * k)
#     right(90)
# pu()
# forward(12 * k)
# right(90)
# pd()
# for i in range(2):
#     forward(6*k)
#     right(90)
#     forward(12 * k )
#     right(90)
# pu()
# for x in range(-20, 20):
#     for y in range(-20, 20):
#         goto(x * k, y * k)
#         dot(5, "red")
#         dot(2, "white")
# mainloop()