Turtle – Draw Lines using arrow keys



In this article, we will learn how to draw lines using the keyboard (arrow
keys) in the turtle graphics. Let’s first discuss some methods used in the
implementation below:

  1.  **wn.listen():** Using this then we can give keyboard inputs
  2.  **wn.onkeypress(func, “key”):** This function is used to bind fun to the key-release event of the key. In order to be able to register key-events, TurtleScreen must have focus.
  3.  **setx(position):** This method is used to set the turtle’s second coordinate to x, leaving the first coordinate unchanged Here, whatever the position of the turtle is, it set the x coordinate to the given input keeping the y coordinate unchanged.
  4.  **sety(position):** This method is used to set the turtle’s second coordinate to y, leaving the first coordinate unchanged Here, whatever the position of the turtle is, it set the y coordinate to the given input keeping the x coordinate unchanged.
  5.  **ycor():** This function is used to return the turtle’s y coordinate of the current position of the turtle. It doesn’t require any argument.
  6.  **xcor():** This function is used to return the turtle’s x coordinate of the current position of the turtle. It doesn’t require any argument
  7.  **head.penup:** Picks the pen up so the turtle does not draw a line as it moves
  8.  **head.hideturtle:** This method is used to make the turtle invisible. It’s a good idea to do this while you’re in the middle of a complicated drawing because hiding the turtle speeds up the drawing observably. This method does not require any argument.
  9.  **head.clear:** This function is used to delete the turtle’s drawings from the screen
  10.  **head.write:** This function is used to write text at the current turtle position.

 **Approach**

  * Import the turtle modules.
  * Get a screen to draw on
  * Define two instances for the turtle one is a pen and another is the head.
  * Head is for telling which key is currently pressed
  * Define the functions for the up, down, left, right movement of the turtle.
  * In the respective up, left, right and down functions set the arrow to move 100 units in up, left, right, and down directions respectively by changing the x and y coordinates.
  * Use function listen() for giving keyboard inputs.
  * Use onkeypress in order to register key-events.

 **Below is the Python implementation of the above approach:**

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# import for turtle module

import turtle

 

# making a workScreen

wn = turtle.Screen()

 

# defining 2 turtle instance

head = turtle.Turtle()

pen = turtle.Turtle()

 

# head is for telling which key is pressed

head.penup()

head.hideturtle()

 

# head is at 0,260 coordinate

head.goto(0, 260)

head.write("This is to tell which key is currently pressed",

 align="center", font=("courier", 14, "normal"))

 

 

def f():

 y = pen.ycor()

 pen.sety(y+100)

 head.clear()

 head.write("UP", align="center", font=("courier",
24, "normal"))

 

 

def b():

 y = pen.ycor()

 pen.sety(y-100)

 head.clear()

 head.write("Down", align="center", font=("courier",
24, "normal"))

 

 

def l():

 x = pen.xcor()

 pen.setx(x-100)

 head.clear()

 head.write("left", align="center", font=("courier",
24, "normal"))

 

 

def r():

 x = pen.xcor()

 pen.setx(x+100)

 head.clear()

 head.write("Right", align="center", font=("courier",
24, "normal"))

 

 

wn.listen()

wn.onkeypress(f, "Up") # when up is pressed pen will go up

wn.onkeypress(b, "Down") # when down is pressed pen will go down

wn.onkeypress(l, "Left") # when left is pressed pen will go left

wn.onkeypress(r, "Right") # when right is pressed pen will go right  
  
---  
  
 __

 __

 **Output**

  

  

![](https://media.geeksforgeeks.org/wp-
content/uploads/20210120160503/GIF20210120154521.gif)  

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

