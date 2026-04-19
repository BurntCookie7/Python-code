import turtle
import random
import sys
range_number = random.randint(1, 1000)
turtle.delay(0)
turtle.speed(0)
turtle.color("blue")
turtle.bgcolor("black")
turtle.hideturtle()
turtle.pensize(3)
while True:
    for i in range(20):
        turn_amount = random.randrange(29, 99)
        red_val = random.random()
        blue_val = random.random() 
        green_val = random.random()
        turtle.color(red_val, green_val, blue_val)
        range_number = random.randint(1, 500)
        for i in range(range_number):
            turtle.fd(i)
            turtle.lt(turn_amount)
        #x_coord = random.randint(-400, 400)
        #y_coord = random.randint(-400, 400)
        turtle.penup()
        turtle.goto(random.randint(-400, 400), random.randint(-400, 400))
        turtle.pendown()
    turtle.clear()
