import turtle

screen = turtle.Screen()
screen.title("Square")
screen.bgcolor("black")

t = turtle.Turtle()
t.color("deeppink")
t.pensize(3)

side = 100
for _ in range(4):
    t.forward(side)
    t.right(90)

turtle.done()
