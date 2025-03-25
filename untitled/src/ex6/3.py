#https://inf-ege.sdamgia.ru/problem?id=58249
import turtle
t=turtle.Turtle()
t.reset()
t.seth(90)
t.width(2)
t.speed(20)
k = 10 #коэффициент для увеличения масштаба
for i in range(5):
    t.seth(0)
    t.circle(5*k,180)
    t.seth(90)
    t.circle(5*k,180)
    t.seth(180)
    t.circle(5*k,180)
    t.seth(270)
    t.circle(5*k,180)
t.penup()
for x in range(-15,6,1):
    for y in range(-5,16):
        t.goto(x*k , y*k )
        t.dot(5)
t.penup()
turtle.mainloop()

"""
from turtle import *
k = 5; speed(0); color('black','red'); hideturtle(); begin_fill()
for i in range(5):
    seth(0); circle(5*k, 180); seth(90); circle(5*k, 180); seth(180); circle(5*k, 180); seth(270); circle(5*k, 180)
end_fill(); sc = getcanvas()
otv = ['in' if (h:=sc.find_overlapping(x,y,x,y)) and sc.itemcget(h[-1], 'fill')=='red' else 0
       for x in range(-100*k,100*k,k) for y in range(-100*k,100*k,k)]
print(otv.count('in'))
"""