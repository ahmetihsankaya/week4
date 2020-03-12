#1st
import turtle

def square(aik):
    for _ in range(4):
        aik.forward(20)
        aik.left(90)
    aik.penup()
    aik.forward(40)
    aik.pendown()

window = turtle.Screen()
aik = turtle.Turtle()
window.bgcolor("lightgreen")
aik.color("hotpink")

for _ in range(5):
    square(aik)

window.exitonclick()

#2nd
import turtle

def square(aik,size):
    aik.penup()
    aik.backward(10)
    aik.right(90)
    aik.forward(10)
    aik.left(90)
    aik.pendown()

    for _ in range(4):
        aik.forward(size)
        aik.left(90)

window = turtle.Screen()
aik = turtle.Turtle()
window.bgcolor("lightgreen")
aik.color("hotpink")

for n in range(1,6):
    square(aik,n * 20)

window.exitonclick()

