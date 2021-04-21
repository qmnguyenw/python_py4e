Draw sun using Turtle module in Python



 **Prerequisite:**Turtle Programming in Python

In this article, let’s learn how to draw the Sun using turtle in Python.
Turtle is an inbuilt module in Python. It helps draw pattens by providing a
screen and turtle (pen) as tools. To move the turtle as desired functions
defined within the module like forward(), backward(), right(), left() etc.
will be employed.

 **Approach:**

  * Import turtle module
  * Set up a screen for turtle.
  * Instantiate a turtle object.
  * For making sun, define a method for circle along with radius and color.
  * Define a function for creating sun rays.

Below is the implementation of the above approach.

## Python3

  

  

 __

 __  
 __

 __

 __  
 __  
 __

import turtle

 

 

screen = turtle.Screen()

 

# background color

screen.bgcolor("lightpink")

 

# turtle object

y = turtle.Turtle()

 

# define function

# for drawing rays of Sun

def drawFourRays(t, length, radius):

 

 for i in range(4):

 t.penup()

 t.forward(radius)

 t.pendown()

 t.forward(length)

 t.penup()

 t.backward(length + radius)

 t.left(90)

 

 

# Draw circle

# to make sun

y.penup()

y.goto(85, 110)

y.fillcolor("yellow")

y.pendown()

y.begin_fill()

y.circle(45)

y.end_fill()

 

# Use the defined

# function to draw rays

y.penup()

y.goto(85, 169)

y.pendown()

drawFourRays(y, 85, 54)

y.right(45)

drawFourRays(y, 85, 54)

y.left(45)

 

# To keep the

# output window active

turtle.done()  
  
---  
  
 __

 __

