import turtle

t = turtle.getturtle()
def test_func():
    print("testing")
#t.clear()
#t.write("Hello!", font = ("Courier", 20))
    

#t.hideturtle()
t.write("Click me!", font = ("Courier", 20))
t.onclick(test_func, 1)
