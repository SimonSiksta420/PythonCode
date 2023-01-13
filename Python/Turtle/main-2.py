import turtle

s = turtle.Screen()
eragon = turtle.Turtle()
eragon.color("red")
eragon.shape("turtle")
eragon.speed(5)

sides = int(input("How many sides do you want your square to have? "))
for i in range(sides):
    eragon.forward(100)
    eragon.left(360/sides)

s.exitonclick()