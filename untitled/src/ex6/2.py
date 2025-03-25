from turtle import*

#https://inf-ege.sdamgia.ru/problem?id=47307
tracer(0)
m =25
for i in range(4):
    forward(10*m)
    right(60)
    forward(10*m)
    right(120)
pu()
for x in range(-15,15):
    for y in range(-15, 15):
        goto(x*m,y*m)
        dot(3)
done()