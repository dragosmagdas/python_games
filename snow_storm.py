from turtle import *
import random
shape("turtle")
speed(3)
pensize(6)
Screen().bgcolor("cyan")
colors = ["blue", "green", "yellow", "pink", "purple", "white"]

def vshape(size):
    right(25)
    forward(size)
    backward(size)
    left(50)
    forward(size)
    backward(size)
    right(25)

def snowFlakeArm(size):
    for x in range(0,4):
        forward(size)
        vshape(size)
    backward(size*4)
        
def snowflake(size):
    for x in range(0,6):
        color(colors[x])
        snowFlakeArm(size)
        right(60)
        
for i in range(0,15):
    size = random.randint(5,30)
    x = random.randint(-400,400)
    y = random.randint(-400,400)
    penup()  
    goto(x,y)
    pendown()  
    snowflake(size) 
