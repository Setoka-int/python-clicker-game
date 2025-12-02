from turtle import *

tracer(0)
left(90)
k = 20
for _ in range(7):
    forward(15 * 20)
    right(90)
pu()
for x in range(-k, k):
    for y in range(-k, k):
        goto(x*k, y*k)
        dot(5)
done()
