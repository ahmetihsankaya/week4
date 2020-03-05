import turtle
window = turtle.Screen()
window.bgcolor("lightgreen")
tess = turtle.Turtle()
tess.shape("turtle")
tess.color("blue")

for _ in range(12):
    tess.stamp()
    tess.penup()
    tess.forward(100)
    tess.pendown()
    tess.forward(20)
    tess.penup()
    tess.forward(20)
    tess.stamp()

tess.clear()

window.bgcolor("blue")
window.exitonclick()

