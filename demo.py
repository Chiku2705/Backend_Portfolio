import turtle
import time

screen = turtle.Screen()
screen.bgcolor("black")
screen.title("💔 Breaking Heart in the middle")

pen = turtle.Turtle()
pen.color("pink")
pen.pensize(3)
pen.speed(5)

def draw_heart():
    pen.begin_fill()
    pen.fillcolor("pink")
    pen.left(140)
    pen.forward(180)
    pen.circle(-90, 200)
    pen.left(120)
    pen.circle(-90, 200)
    pen.forward(180)
    pen.end_fill()

draw_heart()
time.sleep(1)

pen.penup()
pen.goto(0, 150)
pen.pendown()
pen.color("black")
pen.pensize(4)

pen.right(400)
pen.forward(40)
pen.left(30)
pen.forward(25)
pen.right(30)
pen.forward(30)
pen.left(35)
pen.forward(40)

pen.hideturtle()
turtle.done()
