Draw Panda Using Turtle Graphics in Python



Turtle is an inbuilt module in Python. It provides:

  1. Drawing using a screen (cardboard).
  2. Turtle (pen).

To draw something on the screen, we need to move the turtle (pen), and to move
the turtle, there are some functions like the forward(), backward(), etc.

 **Prerequisite:**Turtle Programming Basics

### Draw Panda Using Turtle Graphics

In this section, we will discuss how to draw a Panda using Turtle Graphics.

**Approach:**

  

  

>   1. _Import Turtle._
>   2.  _Make Turtle Object._
>   3.  _Define a method to draw a circle with dynamic radius and color._
>   4.  _Draw ears of Panda with black color circles._
>   5.  _Draw face of Panda with white color circle._
>   6.  _Draw eyes of Panda with black and white color concentric circles._
>   7.  _Draw nose of Panda with black color circle._
>   8.  _Draw two semicircle for mouth below nose._
>

 **Code:**

## python3

 __

 __  
 __

 __

 __  
 __  
 __

# Draw a Panda using Turtle Graphics

# Import turtle package

import turtle

 

# Creating a turtle object(pen)

pen = turtle.Turtle()

 

# Defining method to draw a colored circle 

# with a dynamic radius

def ring(col, rad):

 

 # Set the fill

 pen.fillcolor(col)

 

 # Start filling the color

 pen.begin_fill()

 

 # Draw a circle

 pen.circle(rad)

 

 # Ending the filling of the color

 pen.end_fill()

 

##########################Main Section#############################

 

# pen.up --> move turtle to air

# pen.down --> move turtle to ground

# pen.setpos --> move turtle to given position

# ring(color, radius) --> draw a ring of specified color and radius

###################################################################

 

##### Draw ears #####

# Draw first ear

pen.up()

pen.setpos(-35, 95)

pen.down

ring('black', 15)

 

# Draw second ear

pen.up()

pen.setpos(35, 95)

pen.down()

ring('black', 15)

 

##### Draw face #####

pen.up()

pen.setpos(0, 35)

pen.down()

ring('white', 40)

 

##### Draw eyes black #####

 

# Draw first eye

pen.up()

pen.setpos(-18, 75)

pen.down

ring('black', 8)

 

# Draw second eye

pen.up()

pen.setpos(18, 75)

pen.down()

ring('black', 8)

 

##### Draw eyes white #####

 

# Draw first eye

pen.up()

pen.setpos(-18, 77)

pen.down()

ring('white', 4)

 

# Draw second eye

pen.up()

pen.setpos(18, 77)

pen.down()

ring('white', 4)

 

##### Draw nose #####

pen.up()

pen.setpos(0, 55)

pen.down

ring('balck', 5)

 

##### Draw mouth #####

pen.up()

pen.setpos(0, 55)

pen.down()

pen.right(90)

pen.circle(5, 180)

pen.up()

pen.setpos(0, 55)

pen.down()

pen.left(360)

pen.circle(5, -180)

pen.hideturtle()  
  
---  
  
 __

 __

 **Output:**

![Panda Using Turtle Graphics](https://media.geeksforgeeks.org/wp-
content/uploads/20200622210706/Panda.gif)  

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

