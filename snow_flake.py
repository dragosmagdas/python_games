from turtle import *
import random
shape("turtle")
speed(3)
pensize(6)
Screen().bgcolor("cyan")
colors = ["blue", "green", "yellow", "pink", "purple", "white"]

def vshape():
    right(25)
    forward(100)
    backward(50)
    left(50)
    forward(100)
    backward(50)
    right(25)

def snowFlakeArm():
        forward(30)
        vshape()
        backward(120)
        
def snowflake():
    for x in range(0,6):
        color(colors[x])
        snowFlakeArm()
        right(60)
        
snowflake()      
