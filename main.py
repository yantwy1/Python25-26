from myfunctions import *
bob.speed(0)
#turtle.tracer(0)
from random import randint 
turtle.colormode(255)
turtle.bgcolor(0,0,190)


for times in range(60):
    x = randint(-1000,1000)
    y = randint(-10,500)
    jump(x,y)
    for times in range(2):
        snowflake(30,155,10)
        bob.forward(5)
        bob.left(5)


jump(875,520)
bob.fillcolor(220,220,220)
bob.begin_fill()
bob.circle(190)
bob.end_fill()


jump(800,575)
for times in range(20):
    crater(30,45,5)
    bob.forward(10)
    bob.left(4)

bob.color("black")
bob.width(3)
jump(90,-500)
bob.fillcolor(255,255,255)
bob.begin_fill()
bob.circle(160)
bob.end_fill()

jump(70,-250)
bob.fillcolor(255,255,255)
bob.begin_fill()
bob.circle(110)
bob.end_fill()

bob.color("black")
bob.width(3)
jump(60,-50)
bob.fillcolor(255,255,255)
bob.begin_fill()
bob.circle(80)
bob.end_fill()

jump(-95,80)
bob.setheading(0)
bob.width(3)
bob.fillcolor(0,0,0)
bob.begin_fill()
bob.forward(75)
bob.left(90)
bob.forward(200)
bob.right(90)
bob.forward(100)
bob.right(90)
bob.forward(200)
bob.left(90)
bob.forward(100)
bob.right(180)
bob.forward(150)
bob.end_fill()

jump(0,50)
bob.fillcolor("black")
bob.begin_fill()
bob.circle(15)

jump(67,50)

bob.circle(15)
bob.end_fill()



