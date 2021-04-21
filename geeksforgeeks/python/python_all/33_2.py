Star fractal printing using Turtle in Python



 **Prerequisite:**Turtle Programming Basics

Fractals are objects that tend to have self-similar structures repeated a
finite number of times. The objective of this article is to draw a star
fractal where a star structure is drawn on each corner of the star and this
process is repeated until the input size reduces to a value of **10**. For
achieving this star fractal pattern the **turtle** module is used.

###  **Methods used**

  * **forward(value):** It moves the turtle in forward direction.
  *  **speed(value):** It changes the speed of the turtle.
  *  **penup():** Stop drawing.
  *  **pendown():** Start drawing.
  *  **left(value):** It moves the turtle towards the left.

###  **Approach**

  1. Import turtle.
  2. Initialise the turtle.
  3. Change the background color.
  4. Make a function to draw a star.
  5. Call the above function recursively inside the for loop to make the entire start pattern.

Below is the implementation of the above approach.

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# import turtle

import turtle

 

# initialise turtle instance

stars = turtle.Turtle()

 

# increases the speed of turtle

stars.speed(10)

 

# to change the background color

stars.getscreen().bgcolor("black")

stars.color("red")

 

# stop drawing

stars.penup()

 

# move the turtle

stars.goto((-200, 50))

 

# start drawing

stars.pendown()

 

# function to draw stars

def star(turtle, size):

 if size <= 10:

 return

 else:

 for i in range(5):

 

 # moving turtle forward

 turtle.forward(size)

 star(turtle, size/3)

 

 # moving turtle left

 turtle.left(216)

 

 

# calling the star function

star(stars, 360)

turtle.done()  
  
---  
  
 __

 __

 **Output:**

  

  

![](https://media.geeksforgeeks.org/wp-
content/uploads/20200910141654/Screenshot722-300x288.png)  

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

