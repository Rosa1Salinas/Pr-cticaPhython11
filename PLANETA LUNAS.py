import turtle


screen = turtle.Screen()
screen.bgcolor("black")


planeta = turtle.Turtle()
planeta.color("blue")
planeta.shape("circle")
planeta.shapesize(7)
planeta.penup()
planeta.goto(0, 0)


luna1 = turtle.Turtle()
luna1.color("gray")
luna1.shape("circle")
luna1.shapesize(1)
luna1.penup()
luna1.goto(100, 0)


luna2 = turtle.Turtle()
luna2.color("lightgray")
luna2.shape("circle")
luna2.shapesize(0.7)
luna2.penup()
luna2.goto(-100, 0)


turtle.done()