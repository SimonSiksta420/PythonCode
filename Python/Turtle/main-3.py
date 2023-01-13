import turtle

s = turtle.Screen()
eragon = turtle.Turtle()
eragon.color("red")
eragon.shape("turtle")
eragon.speed(5)

for i in range(10):
    eragon.circle(100)
    eragon.left(36)
    
s.exitonclick()