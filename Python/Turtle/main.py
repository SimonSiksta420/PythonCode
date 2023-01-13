import turtle

s = turtle.Screen()
eragon = turtle.Turtle()
eragon.color("red")
eragon.shape("turtle")
eragon.speed(5)

eragon.forward(100)
eragon.left(90)
eragon.forward(200)

eragon.penup()
eragon.left(90)
eragon.forward(200)
eragon.pendown()
eragon.forward(120)

s.exitonclick()