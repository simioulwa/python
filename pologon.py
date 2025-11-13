# polygon
import turtle

screen = turtle.Screen()
screen.screensize(400, 400)
screen.title("Polygon")
screen.bgcolor("black")
t = turtle.Turtle()
t.color("deeppink")

n = 6
a = 360 / 6
t.begin_fill()
for i in range(n):
    t.forward(100)
    t.right(a)
t.end_fill()
turtle.done()
