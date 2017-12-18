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

    brad.forward(100)
    brad.right(90)
    brad.forward(100)
    brad.right(90)
    brad.forward(100)
    brad.right(90)
    brad.forward(100)
    brad.right(90)

    angie = turtle.Turtle()
    angie.shape("arrow")
    angie.color("yellow")
    angie.circle(100)

    window.exitonclick()



draw_square()
