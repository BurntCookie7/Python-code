import time
import turtle as t
t.setup(width=500, height=500, startx=1, starty=0)
for i in range(3):
    t.forward(100)
    t.left(90)
t.forward(100)
t.penup()
t.left(90)
t.forward(50)
t.pendown()
t.circle(50)
t.backward(50)
t.left(65)
t.forward(111)
t.right(128.1)
t.forward(114)
t.hideturtle()
time.sleep(3)