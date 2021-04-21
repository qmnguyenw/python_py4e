Draw Spiraling Square using Turtle in Python



 **Prerequisite:** Python Turtle Basic

 **Turtle** is an inbuilt module of python. It enables us to draw any drawing
by a turtle, methods defined in the turtle module and by using some logical
loops. To draw something on the screen(cardboard) just move the turtle(pen).
To move turtle(pen) there are some functions i.e forward(), backward(), etc.

 **Approach to draw a Spiraling Square of size n:**

  * Import turtle and create a turtle instance.
  * Using for loop(i = 0 to i < n * 4) and repeat below step
    * turtle.forward(i * 10).
    * turtle.right(90).
  * Close the turtle instance.

Below is the implementation:

## Python3

  

  

 __

 __  
 __

 __

 __  
 __  
 __

# importing turtle module

import turtle

 

# size 

n = 10

 

# creating instance of turtle

pen = turtle.Turtle()

 

# loop to draw a side

for i in range(n * 4):

 

 # drawing side of

 # length i*10

 pen.forward(i * 10)

 

 # changing direction of pen

 # by 90 degree in clockwise

 pen.right(90)

 

# closing the instance

turtle.done()  
  
---  
  
 __

 __

