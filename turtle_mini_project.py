import turtle

radius = int(raw_input("What radius do you want?"))
num_petals = int(raw_input("How many petals do you want?"))

nazanin = turtle.Turtle()

def draw_petal(nazanin, radius):
    #radius = int(raw_input("What radius do you want?"))
    window = turtle.Screen()
    window.bgcolor("green")

    nazanin.shape("turtle")

    heading = nazanin.heading()
    nazanin.circle(radius, 60)
    nazanin.left(120)
    nazanin.circle(radius, 60)
    nazanin.setheading(heading)



dexter = turtle.Turtle()
def draw_flower(dexter, num_petals):
    for _ in range(num_petals):
        draw_petal(dexter, radius)
        dexter.left(360 / num_petals)

    dexter.hideturtle()
    screen = Screen()
    screen.exitonclick()




draw_flower(dexter, num_petals)
