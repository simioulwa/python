# polygon
import turtle

screen = turtle.Screen()
screen.screensize(400, 400)
screen.title("Polygon")
screen.bgcolor("black")
t = turtle.Turtle()
t.color("darkorange")
t.width(3)
l = 5
while True:
    t.forward(l)
    t.left(90)
    l+=4
