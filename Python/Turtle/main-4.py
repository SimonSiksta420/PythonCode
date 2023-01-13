import turtle

s = turtle.Screen()
eragon = turtle.Turtle()
eragon.color("red")
eragon.shape("turtle")
eragon.speed(20)

# draw squares in each other with n user input
n = int(input("Enter the number of squares: "))
for i in range(n):
    for j in range(4):
        eragon.forward(100)
        eragon.left(90)
    eragon.penup()
    eragon.forward(10)
    eragon.left(90)
    eragon.forward(10)
    eragon.right(90)
    eragon.pendown()

s.exitonclick()