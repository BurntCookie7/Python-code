import turtle as t

#setup
t.bgcolor("black")
t.speed(0)
t.delay(0)
#t.hideturtle()

#Draw a circle
t.begin_fill()
t.color("lightblue")
t.circle(50)
t.end_fill()

#Move the turtle
t.penup()
t.forward(100)
t.pendown()

#Draw a square
t.begin_fill()
t.color("red")
for i in range(4):
    t.forward(50)
    t.right(90)
t.end_fill()

#Move the turtle
t.penup()
t.backward(200)
t.pendown()

#Draw a triangle
t.begin_fill()
t.color("purple")
for i in range(3):
    t.forward(50)
    t.left(360/3)
t.end_fill()

#Move the turtle
t.penup()
t.right(90)
t.forward(100)
t.pendown()

#Draw a triforce
t.color("yellow")
t.begin_fill()
t.right(90)
for i in range(3):
    t.forward(200)
    t.right(120)
t.forward(100)
t.right(60)
for i in range(3):
    t.forward(100)
    t.right(120)
t.end_fill()
