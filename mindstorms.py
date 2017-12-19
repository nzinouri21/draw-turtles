import turtle
#This is the actual thing that moves around and draws stuff on the computer!

def draw_square():
    window = turtle.Screen()
    window.bgcolor("red")

    #brad is an instance of a class called Turtle
    brad = turtle.Turtle()
    brad.shape("turtle")
    brad.color("blue")
    brad.speed(2)

    i=0
    while i<4:
        brad.forward(100)
        brad.right(90)
        i=i+1
    #window.exitonclick()

def draw_circle():
    window = turtle.Screen()
    window.bgcolor("green")

    #angie is another instance of a class called Turtle
    angie = turtle.Turtle()
    angie.shape("arrow")
    angie.color("yellow")
    angie.circle(100)

    #window.exitonclick()

def draw_triangle():
    window = turtle.Screen()
    window.bgcolor("red")

    #angie is another instance of a class called Turtle
    nazanin = turtle.Turtle()
    nazanin.shape("circle")
    nazanin.color("blue")

    nazanin.forward(100)
    nazanin.left(120)
    nazanin.forward(100)
    nazanin.left(120)
    nazanin.forward(100)

    window.exitonclick()

draw_square()
draw_circle()
draw_triangle()
