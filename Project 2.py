import turtle as t

#setup
t.bgcolor("black")
t.speed(0)
t.delay(0)
t.hideturtle()
'''
#Draw a square
t.begin_fill()
t.color("red")
for i in range(4):
    t.forward(50)
    t.right(90)
t.end_fill()

input("Press enter to draw a triangle")
t.clear()

#Draw a triangle
t.begin_fill()
t.color("purple")
for i in range(3):
    t.forward(50)
    t.left(360/3)
t.end_fill()

input("Press enter to draw a circle")
t.clear()

#Draw a circle
t.color("blue")
t.begin_fill()
for i in range(360):
    t.fd(1)
    t.lt(1)
t.end_fill()

input("Press enter to draw a spiral")
t.clear()
'''
#Draw a spiral
t.begin_fill()
t.color("green")
for i in range(5000):
    t.fd(i/100)
    t.lt(9)
    print(i)
t.end_fill()
