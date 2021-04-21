Draw a car using Turtle in Python



 **Prerequisite:**Turtle module, Drawing Shapes

There are many modules in python which depicts graphical illustrations, one of
them is _turtle_ , it is an in-built module in Python, which lets the user
control a pen( _turtle_ ) to draw on screen(drawing board). It is mostly used
to illustrate figures, shapes, designs etc. In this article, we will learn how
to draw a Car using the _turtle_ module.

**To draw a car in Python using** _ **Turtle**_ **module:**

  1. We are going to create different shapes using the _turtle_ module in-order to illustrate a car.
  2. Tyres can be drawn using _circle()_ function.
  3. The upper body can be thought of a rectangle.
  4. Roof and windows are similar to trapezoid.
  5. Overlapping all the above shapes in particular positions will illustrate a car. 

**Let’s try to understand it better with the help of the below program:**

## Python3

  

  

 __

 __  
 __

 __

 __  
 __  
 __

#Python program to draw car in turtle programming

 

# Import required library 

import turtle

 

 

car = turtle.Turtle()

 

 

# Below code for drawing rectangular upper body

car.color('#008000')

car.fillcolor('#008000')

car.penup()

car.goto(0,0)

car.pendown()

car.begin_fill()

car.forward(370)

car.left(90)

car.forward(50)

car.left(90)

car.forward(370)

car.left(90)

car.forward(50)

car.end_fill()

 

 

# Below code for drawing window and roof

car.penup()

car.goto(100, 50)

car.pendown()

car.setheading(45)

car.forward(70)

car.setheading(0)

car.forward(100)

car.setheading(-45)

car.forward(70)

car.setheading(90)

car.penup()

car.goto(200, 50)

car.pendown()

car.forward(49.50)

 

 

# Below code for drawing two tyres

car.penup()

car.goto(100, -10)

car.pendown()

car.color('#000000')

car.fillcolor('#000000')

car.begin_fill()

car.circle(20)

car.end_fill()

car.penup()

car.goto(300, -10)

car.pendown()

car.color('#000000')

car.fillcolor('#000000')

car.begin_fill()

car.circle(20)

car.end_fill()

 

 

car.hideturtle()  
  
---  
  
 __

 __

