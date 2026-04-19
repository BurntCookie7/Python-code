import turtle as t
import random
t.speed(0)
t.delay(0)
t.pu()
t.bgcolor("darkgreen")

#Picks a random location
def random_location():
    t.pu()
    t.goto(random.randrange(-400, 400), random.randrange(-400, 400))

#Draws a tree
def draw_tree():
    t.pd()
    t.begin_fill()
    t.color(.5, .1 ,0)
    t.fd(30)
    t.lt(90)
    t.fd(100)
    t.lt(90)
    t.fd(30)
    t.lt(90)
    t.fd(100)
    t.end_fill()
    t.pu()
    t.bk(100)
    t.color("green")
    t.fd(50)
    t.lt(90)
    t.bk(35)
    t.pd()
    t.begin_fill()
    for i in range(3):
        t.fd(100)
        t.lt(120)
    t.end_fill()

#Draws a house
def house():
    t.heading()
    t.color(.3, .1, 0)
    t.begin_fill()
    for i in range(4):
        t.fd(50)
        t.lt(90)
    t.end_fill()
    t.color("orange")
    t.lt(90)
    t.fd(50)
    t.rt(90)
    t.pd()
    t.begin_fill()
    for i in range(3):
        t.fd(50)
        t.lt(120)
    t.end_fill()

def generate_village():
    for i in range(50):
        random_location()
        draw_tree()
    for i in range(10):
        random_location()
        house()

#Run all the functions    
generate_village()
