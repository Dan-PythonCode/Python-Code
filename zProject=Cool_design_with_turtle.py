from turtle import *
color = ("#FFFFFF")
begin_fill()
while True:
    forward(200)
    left(170)
    if abs(pos()) < 1:
        break
done()

