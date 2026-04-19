import turtle as t
import random as r
#Controls
#WASD is basic movement, and the arrows are tank controls
# "r" clears the canvas, "h" takes you to the center of the canvas, and spacebar toggles the pen up and down
# "q" increases the pen size, and "e" decreases the pen size
# "c" changes the color cycling through the rainbow
# press "f" before drawing a shape and you can press "f" again to fill it
#the "[" key makes you move shorter and the "]" key makes you move father


#Configuration
t.speed(0)
t.delay(0)
t.listen()
t.shape("turtle")

#Vairiables
pen_size = 1
pen_is_down = True
distance = 25
colors = ["black", "red", "orange", "green", "blue", "purple"]
current_color = 0
filling = False

#Functions

#move the turtle left
def left():
    global distance
    t.seth(180)
    t.fd(distance)
    
#move the turtle right
def right():
    global distance
    t.seth(0)
    t.fd(distance)

#move the turtle up
def up():
    global distance
    t.seth(90)
    t.fd(distance)

#move the turtle down
def down():
    global distance
    t.seth(-90)
    t.fd(distance)
    
def tank_forward():
    global distance
    t.fd(distance)

def tank_backward():
    global distance
    t.bk(distance)

def tank_right():
    t.rt(45)

def tank_left():
    t.lt(45)

def pen_toggle():
    global pen_is_down
    if pen_is_down:
        pen_is_down = False
        t.pu()
    else:
        pen_is_down = True
        t.pd()

def size_up():
    global pen_size
    pen_size+=1
    t.width(pen_size)
    print(f"pen size is {pen_size}")

def size_down():
    global pen_size
    pen_size-=1
    if pen_size <= 0:
        pen_size = 1
        t.width(pen_size)
    else:
        t.width(pen_size)
    print(f"pen size is {pen_size}")

def center():
    t.pu()
    t.home()
    t.pd()

def distance_up():
    global distance
    distance+=1
    print(f"you are moving {distance} pixels")

def distance_down():
    global distance
    distance-=1
    print(f"you are moving {distance} pixels")

def change_color():
    global current_color
    current_color+=1
    if current_color > 5:
        current_color = 0
    t.color(colors[current_color])
    print("current color is " + colors[current_color])

def fill():
    global filling
    if filling:
        t.end_fill()
        filling = False
    else:
        t.begin_fill()
        filling = True
        
    
    
#Basic controls
t.onkeypress(left, key="a")
t.onkeypress(right, key="d")
t.onkeypress(up, key="w")
t.onkeypress(down, key="s")

#Tank controls
t.onkeypress(tank_forward, key="Up")
t.onkeypress(tank_backward, key="Down")
t.onkeypress(tank_right, key="Right")
t.onkeypress(tank_left, key="Left")

#Other controls
t.onkeypress(t.clear, key="r")
t.onkeypress(center, key="h")
t.onkeypress(pen_toggle, key="space")
t.onkeypress(size_up, key="q")
t.onkeypress(size_down, key="e")
t.onkeypress(distance_up, key="]")
t.onkeypress(distance_down, key="[")
t.onkeypress(change_color, key="c")
t.onkeypress(fill, key="f")
#t.onkeypress(t.end_fill, key="v")

