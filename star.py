# polygon
import turtle

screen = turtle.Screen()
screen.screensize(400, 400)
screen.title("Polygon")
screen.bgcolor("black")
t = turtle.Turtle()
t.color("deeppink")

n = 3
a = 360 / 3

for i in range(n):
    t.forward(100)
    t.left(a)

t.left(90)
t.penup()
t.forward(65)
t.right(90)
t.pendown()

for i in range(n):
    t.forward(100)
    t.right(a)

turtle.done()
