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

#3rd
import turtle

window = turtle.Screen()
t = turtle.Turtle()
n = int(input("number of corner?"))
sz = int(input("length of polygon?"))
window.bgcolor("lightgreen")
t.color("hotpink")

def  draw_poly(t, n, sz):
    for _ in range(n):
        t.forward(sz)
        t.left(360/n)

draw_poly(t, n, sz)
window.exitonclick()

#4th
import turtle

def square(aik,size):
    for _ in range(4):
        aik.forward(size)
        aik.left(90)

window = turtle.Screen()
window.bgcolor("lightgreen")
aik = turtle.Turtle()
aik.color("blue")
aik.speed(0)

for _ in range(20):
    square(aik, 70)
    aik.left(18)

window.exitonclick()

#5th
import turtle

window = turtle.Screen()
window.bgcolor("lightgreen")
aik = turtle.Turtle()
aik.color("blue")
aik.speed(0)
uzunluk = 10

for _ in range(103):
    aik.right(90)
    uzunluk +=2
    aik.forward(uzunluk)

for _ in range(103):
    aik.right(91)
    uzunluk +=2
    aik.forward(uzunluk)

window.exitonclick()

#6th
import turtle
window = turtle.Screen()
window.bgcolor("lightgreen")
aik = turtle.Turtle()
aik.color("blue")
def draw_poly(aik, number_of_sides, size):
    angle = 360 / number_of_sides
    for _ in range(number_of_sides):
        aik.forward(size)
        aik.left(angle)
def draw_equitriangle(aik, size):
    draw_poly(aik, 3, size)
draw_equitriangle(aik, 100)
window.exitonclick()

#7th
def sum_total(n):
    result = (n * (n + 1)) / 2
    return result
print(sum_total(10))

#8th
import math
def area_of_circle(r):
    result= math.pi * r ** 2
    return result
print(area_of_circle(3))

#9th
import turtle
window = turtle.Screen()
aik = turtle.Turtle

def draw_star(length, angle):
    for _ in range(5)
        aik.left(angle)
        aik.forward(length)
window.exitonclick()

#9th
import turtle

def draw_star(drawing):
    for _ in range(5):
        drawing.forward(100)
        drawing.right(144)

screen = turtle.Screen()
aik = turtle.Turtle()

draw_star(aik)
screen.exitonclick()

#10th
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

