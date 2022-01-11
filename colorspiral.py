""" 컬러 나선형을 
그리는 모듈"""
import turtle
def cspiral(sides=6, size=360, x=0, y=0):
    t=turtle.Pen()
    t.speed(0)
    t.penup()
    t.setpos(x,y)
    t.pendown()
    turtle.bgcolor("black")
    colors = ["red", "yellow", "blue", "orange", "green", "purple"]
    for n in range(size):
        t.pencolor(colors[n%sides])
        t.forward(n*3/sides + n)
        t.left(360/sides + 1)
        t.width(n*sides/100)
