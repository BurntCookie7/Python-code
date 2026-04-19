import turtle as t
import random
t.speed(0)
t.delay(0)
t.pu()
t.bgcolor("darkgreen")

#Picks a random location
#limit -- determines the limit on the x axis and y axis of where the turtle will go
def random_location(limit):
    t.pu()
    t.goto(random.randrange(-limit, limit), random.randrange(-limit, limit))

#Draws a tree
#leaves_sides -- determines how many sides the shape making up the leaves has
#WARNING numbers above 9 for leaves_sides will cause issues 
#WARNING some numbers for leaves_sides will cause an offset on the log
def draw_tree(leaves_sides):
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
    for i in range(leaves_sides):
        t.fd(100 - leaves_sides*(leaves_sides-1))
        t.lt(360/leaves_sides)
    t.end_fill()
    
#Draws a house
#size -- the size of the house
def house(size):
    t.heading()
    t.color(.3, .1, 0)
    t.begin_fill()
    for i in range(4):
        t.fd(size)
        t.lt(90)
    t.end_fill()
    t.color("orange")
    t.lt(90)
    t.fd(size)
    t.rt(90)
    t.pd()
    t.begin_fill()
    for i in range(3):
        t.fd(size)
        t.lt(120)
    t.end_fill()

#generates a villag and trees
#house_size -- determines the size argument on house()
#house_amount -- determines the amount of houses placed
#tree_amount -- determines the amount of trees that are placed
#leaves_sides -- determines the leaves_sides argument on draw_tree()
def generate_village(house_size, house_amount, tree_amount, leaves_sides):
    for i in range(tree_amount):
        random_location(400)
        draw_tree(leaves_sides)
    for i in range(house_amount):
        random_location(300)
        house(house_size)

#Run all the functions
#WARNING ingore the fact there are houses on top of trees/leaves
generate_village(40, 50, 70, 3)
input("Press Enter to regenerate")
t.home()
t.clear()
generate_village(35, 30, 60, 5)
input("Press Enter to regenerate")
