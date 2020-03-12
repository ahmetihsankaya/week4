import turtle

def draw_star(drawing):
    for _ in range(5):
        drawing.forward(100)
        drawing.right(144)

screen = turtle.Screen()
screen.bgcolor("lightgreen")
aik = turtle.Turtle()
aik.color("hotpink")

aik.penup()
aik.setposition(-175, 100)
aik.pendown()

draw_star(aik)

for _ in range (4):
    aik.penup()
    aik.forward(350)
    aik.right(144)
    aik.pendown()
    draw_star(aik)

screen.exitonclick()



