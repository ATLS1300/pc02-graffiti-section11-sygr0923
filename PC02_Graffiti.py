#!/usr/bin/env python
# coding: utf-8

'''
Turtle starter code
ATLS 1300
Author: Dr. Z
Author: YOUR NAME
May 29, 2020
'''

import turtle #import the library of commands that you'd like to use

turtle.colormode(255)

# Create a panel to draw on. 
panel = turtle.Screen()
w = 750 # width of panel
h = 750 # height of panel
panel.setup(width=w, height=h) #600 x 600 is a decent size to work on. 
#You can experiment by making it the size of your screen or super tiny!

# Create a colorful background and add Bezos image to it
image = "Bezos.gif"
panel.bgcolor("lightsteelblue1")
panel.bgpic(image)

#=======Add your code here======
turtle.penup()
turtle.begin_fill()
turtle.goto(-18,100)
turtle.pendown()
turtle.circle(20)
turtle.end_fill()
turtle.penup()
turtle.begin_fill()
turtle.forward(40)
turtle.goto(40,100)
turtle.pendown()
turtle.circle(20)
turtle.end_fill()
turtle.pensize(3)
turtle.penup()
turtle.goto(-15,116)
turtle.pendown()
turtle.forward(50)
turtle.penup()
turtle.goto(-17,116)
turtle.pendown()
turtle.backward(60)
turtle.right(45)
turtle.backward(20)
# Extra Credit Shapes
turtle.penup()
turtle.color("Red")
turtle.pensize(2)
turtle.goto(-16,130)
turtle.pendown()
turtle.forward(15)
turtle.right(90)
turtle.forward(15)
turtle.right(90)
turtle.forward(15)
turtle.right(90)
turtle.forward(15)
turtle.penup()
turtle.goto(30,120)
turtle.pendown()
turtle.forward(15)
turtle.right(90)
turtle.forward(15)
turtle.right(90)
turtle.forward(15)
turtle.right(90)
turtle.forward(15)
turtle.right(90)
turtle.penup()
turtle.goto(111,-90)
turtle.pendown()
turtle.right(90)
turtle.forward(20)
turtle.penup()
turtle.forward(10)
turtle.pendown()
turtle.forward(20)
turtle.penup()
turtle.forward(10)
turtle.pendown()
turtle.forward(20)
turtle.penup()
turtle.forward(10)
turtle.pendown()
turtle.forward(20)
turtle.penup()
turtle.forward(10)
turtle.pendown()
turtle.forward(20)
turtle.penup()
turtle.forward(10)
turtle.pendown()
turtle.forward(20)
turtle.penup()
turtle.forward(10)
turtle.pendown()
turtle.forward(20)
turtle.penup()
turtle.goto(0,0)
turtle.done()


#=======Clean up code (do not change)======
# this code ensures that your script runs correctly each time.
#turtle.done()
