Draw tree using Turtle module in Python



 **Prerequisite:**Turtle module, Drawing Triangle, Drawing Rectangle

There are many modules in python which depicts graphical illustrations, one of
them is _turtle_ , it is an in-built module in Python, which lets the user
control a pen( _turtle_ ) to draw on screen(drawing board). It is mostly used
to illustrate figures, shapes, designs etc. In this article, we will learn how
to draw a simple tree using the _turtle_ module. Illustrating a Tree consists
of creating a single rectangle and then three triangles of same sizes
sequentially from the bottom.

 **Below are the steps to create a tree:**

  1. Import _turtle_ and _math_ module.
  2. Set screen with dimensions and color.
  3. Create a _turtle_ object.
  4. Create tree by illustrating stacked triangles and a rectangle.

 **Below is the program of the above approach:**

## Python3

  

  

 __

 __  
 __

 __

 __  
 __  
 __

# Python program to draw a tree using turtle

# Importing required modules

import turtle

import math

 

 

# Function to draw rectangle

def drawRectangle(t, width, height, color):

 t.fillcolor(color)

 t.begin_fill()

 t.forward(width)

 t.left(90)

 t.forward(height)

 t.left(90)

 t.forward(width)

 t.left(90)

 t.forward(height)

 t.left(90)

 t.end_fill()

 

 

# Function to draw triangle 

def drawTriangle(t, length, color):

 t.fillcolor(color)

 t.begin_fill()

 t.forward(length)

 t.left(135)

 t.forward(length / math.sqrt(2))

 t.left(90)

 t.forward(length / math.sqrt(2))

 t.left(135)

 t.end_fill()

 

 

# Set the background color

screen = turtle.Screen ( )

screen.bgcolor("skyblue")

 

 

# Creating turtle object

tip = turtle.Turtle()

tip.color ("black")

tip.shape ("turtle")

tip.speed (2)

 

 

# Tree base

tip.penup()

tip.goto(100, -130)

tip.pendown()

drawRectangle(tip, 20, 40, "brown")

 

 

# Tree top

tip.penup()

tip.goto(65, -90)

tip.pendown()

drawTriangle(tip, 90, "lightgreen")

tip.penup()

tip.goto(70, -45)

tip.pendown()

drawTriangle(tip, 80, "lightgreen")

tip.penup()

tip.goto(75, -5)

tip.pendown()

drawTriangle(tip, 70, "lightgreen")  
  
---  
  
 __

 __

