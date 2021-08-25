from turtle import *
import turtle
import random

'''def isInscreen(w,t):
    if random.random()>0.1:
        return True
    else:
        return False
t=turtle.Turtle()
wn=turtle.Screen()
wn.bgcolor("lightgreen")
t.shape('turtle')
while isInscreen(wn,t):
    coin=random.randrange(0,4)
    if coin==0:
        t.left(90)
    else:
        t.right(90)
    t.forward(50)
wn.exitonclick()
'''
'''
wn=turtle.Screen()
alex=turtle.Turtle()
wn.bgcolor("lightgreen")
alex.shape('turtle')
alex.forward(150)
alex.left(90)
alex.forward(75)
alex.left(90)
alex.forward(150)
alex.left(90)
alex.forward(75)
'''
#str=input("Please enter a string:")
#n=int(input("enter the number of turms you want to move yr shape:"))
'''
wn=turtle.Screen()
wn.bgcolor("grey")

elan=turtle.Turtle()
elan.shape('circle')
elan.fillcolor("red")
distance=10
for _ in range(50):
    elan.forward(distance)
    elan.stamp()
    elan.right(90)
    distance=distance+10
wn.exitonclick()
'''
#fave_colour = input("What is your favourite color:")
wn=turtle.Screen()
ch=turtle.Turtle()
color("red")
wn.bgcolor("grey")
ch.color("red")
begin_fill()
for i in range(4):
    forward(200)
    ch.stamp()
    right(90)
end_fill()

hideturtle()
wn.exitonclick()