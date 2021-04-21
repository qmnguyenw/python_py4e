Draw a Hut using turtle module in Python



Turtle is a inbuilt module in Python, which has many functions like forward(),
backward(), right() and left() etc. You can draw a hut on the screen just by
using the turtle module in Python. In this article, we will create a hut using
the turtle module.

 **Approach:**

  1. Import turtle
  2. Set the background color.
  3. Define a function to draw the front portion of the hut i.e rectangle.
  4. Define a function to draw the top portion of the hut i.e equilateral triangle.
  5. Define a function to draw the side portion of the hut i.e Parallelogram.
  6. Use penup() and pendown() function to draw windows and door for the hut.
  7. Fill the appropriate colors in the Hut.

Below is the implementation.

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

import turtle

import math

 

# Set the background color

screen = turtle.Screen()

screen.bgcolor("lightpink")

 

# Create our turtle

t = turtle.Turtle()

t.color("black")

t.shape("turtle")

t.speed(5)

 

# Define a funtion to draw and

# fill a rectangle with the given

# dimensions and color

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

 

 

# Define a function to draw and fill an equalateral right

# triangle with the given hypotenuse length and color. This

# is used to create a roof shape.

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

 

 

# Define a function to draw and fill a parallelogram, used to

# draw the side of the house

def drawParallelogram(t, width, height, color):

 t.fillcolor(color)

 t.begin_fill()

 t.left(30)

 t.forward(width)

 t.left(60)

 t.forward(height)

 t.left(120)

 t.forward(width)

 t.left(60)

 t.forward(height)

 t.left(90)

 t.end_fill()

 

 

# Draw and fill the front of the house

t.penup()

t.goto(-150, -120)

t.pendown()

drawRectangle(t, 100, 110, "blue")

 

# Draw and fill the front door

t.penup()

t.goto(-120, -120)

t.pendown()

drawRectangle(t, 40, 60, "lightgreen")

 

# Front roof

t.penup()

t.goto(-150, -10)

t.pendown()

drawTriangle(t, 100, "magenta")

 

# Side of the house

t.penup()

t.goto(-50, -120)

t.pendown()

drawParallelogram(t, 60, 110, "yellow")

 

# Window

t.penup()

t.goto(-30, -60)

t.pendown()

drawParallelogram(t, 20, 30, "brown")

 

# Side roof

t.penup()

t.goto(-50, -10)

t.pendown()

t.fillcolor("orange")

t.begin_fill()

t.left(30)

t.forward(60)

t.left(105)

t.forward(100 / math.sqrt(2))

t.left(75)

t.forward(60)

t.left(105)

t.forward(100 / math.sqrt(2))

t.left(45)

t.end_fill()

turtle.done()  
  
---  
  
 __

 __

 **Output:**

  

  

https://media.geeksforgeeks.org/wp-content/uploads/20200915222323/Hut.mp4

  

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

