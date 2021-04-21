Draw house using Turtle programming in Python



 **Prerequisite:**Turtle Programming in Python

“Turtle” is a Python feature like a drawing board, which lets us command a
turtle to draw all over it! ”turtle” comes packed with the standard Python
package and need not be installed externally.

 **Step 1:** Import turtle and math module in Python.

    
    
    import turtle
    import math
    

**Step 2:** Choose a background color for your output screen. You can choose
any color, we will use yellow color just to make it attractive.

    
    
    screen = turtle.Screen()
    screen.bgcolor("yellow")
    

**Step 3:** Choose the color and speed of your turtle(pen) who will draw the
house on the screen.

  

  

    
    
    t.color("black")
    t.shape("turtle")
    t.speed(1)
    

**Step 4:** Now, we need to draw the base of your house and for that, you need
to draw a rectangle.

You can fill any color in your of your choice just by changing the color name
in the t.fillcolor(‘ ‘) command.

    
    
    t.fillcolor('cyan')
    t.begin_fill( )
    t.right(90)
    t.forward(250)
    t.left(90)
    t.forward(400)
    t.left(90)
    
    t.forward(250)
    
    t.left(90)
    t.forward(400)
    t.right(90)
    t.end_fill()
    

The base of the house will look this:

https://media.geeksforgeeks.org/wp-
content/uploads/20200913124224/Rectangle.mp4

 **Step 5:** Now you created the base, the next step is to create the top of
the house. Draw a triangle for the upper portion, just to keep it simple.

    
    
    # for creating triangle
    # i.e top of the house
    t.fillcolor('brown')
    t.begin_fill()
    t.right(45)
    t.forward(200)
    t.right(90)
    t.forward(200)
    t.left(180)
    t.forward(200)
    t.right(135)
    t.forward(259)
    t.right(90)
    t.forward(142)
    t.end_fill()
    
    

**Step 6:** We must secure our house by Putting the Door and also windows for
ventilation. Here is the code for that-

    
    
    # for windows and
    # for creating door
    t.right(90)
    t.forward(400)
    t.left(90)
    t.forward(50)
    t.left(90)
    t.forward(150)
    t.right(90)
    t.forward(200)
    t.right(180)
    t.forward(200)
    t.right(90)
    t.forward(200)
    t.right(90)
    t.forward(150)
    t.right(90)
    t.forward(200)
    t.right(90)
    t.forward(150)
    
    t.right(90)
    t.forward(100)
    t.right(90)
    t.forward(150)
    t.right(90)
    t.forward(100)
    t.right(90)
    t.forward(75)
    t.right(90)
    t.forward(200)
    
    

**Complete Code:**

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

import turtle

 

 

t = turtle.Turtle()

 

# for background

screen = turtle.Screen()

screen.bgcolor("yellow")

 

#color and speed

# of turtle

# creating the house

t.color("black")

t.shape("turtle")

t.speed(1)

 

# for creating base of

# the house

t.fillcolor('cyan')

t.begin_fill()

t.right(90)

t.forward(250)

t.left(90)

t.forward(400)

t.left(90)

t.forward(250)

t.left(90)

t.forward(400)

t.right(90)

t.end_fill()

 

# for top of

# the house

t.fillcolor('brown')

t.begin_fill()

t.right(45)

t.forward(200)

t.right(90)

t.forward(200)

t.left(180)

t.forward(200)

t.right(135)

t.forward(259)

t.right(90)

t.forward(142)

t.end_fill()

 

# for door and

# windows

t.right(90)

t.forward(400)

t.left(90)

t.forward(50)

t.left(90)

t.forward(150)

t.right(90)

t.forward(200)

t.right(180)

t.forward(200)

t.right(90)

t.forward(200)

t.right(90)

t.forward(150)

t.right(90)

t.forward(200)

t.right(90)

t.forward(150)

t.right(90)

t.forward(100)

t.right(90)

t.forward(150)

t.right(90)

t.forward(100)

t.right(90)

t.forward(75)

t.right(90)

t.forward(200)

t.right(180)

t.forward(200)

t.right(90)

t.forward(75)

t.left(90)

t.forward(15)

t.left(90)

t.forward(200)

t.right(90)

t.forward(15)

t.right(90)

t.forward(75)  
  
---  
  
 __

 __

 **Output:**

https://media.geeksforgeeks.org/wp-content/uploads/20200913125802/House.mp4

  

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

