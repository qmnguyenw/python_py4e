Python – Write “GFG” using Turtle Graphics



IN this article we will learn how to write **“GFG”** using Turtle Graphics in
Python. For that lets first know what is Turtle Graphics.

> ### Turtle graphics
>
>   *  **backward(length):** moves the pen in the backward direction by x
> unit.
>   *  **right(angle):** rotate the pen in the clockwise direction by an angle
> x.
>   *  **left(angle):** rotate the pen in the anticlockwise direction by an
> angle x.
>   *  **penup():** stop drawing of the turtle pen.
>   *  **pendown():** start drawing of the turtle pen.
>

>
> ####

## Approach

  * import the turtle modules.
    
        import turtle

  * Get a screen to draw on
    
        ws=turtle.Screen()

  * Define an instance for **turtle.**
  * for printing **G** we have to make a semicircle and then complete it by rotating the turtle and moving it forward.
  * Then for **F** move pen up using **penup() ,** then **goto()** to desired coordinates, then pen it down for drawing using **pendown()** and draw F.
  * for remaining **G** go to other coordinates and do same as done for 1st **G**.

 **Below is the python implementation for the above approach:**

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

#python program for printing "GFG"

#importing turtle modules

import turtle

 

#setting up workscreen

ws=turtle.Screen()

 

#defining turtle instance

t=turtle.Turtle()

 

#turtle pen will be of "GREEN" color

t.color("Green")

 

#setting width of pen

t.width(3)

 

 

#for printing letter "G"

for x in range(180):

 t.backward(1)

 t.left(1)

t.right(90)

t.forward(50)

t.right(90)

t.forward(30)

t.right(90)

t.forward(50)

 

 

#for printing letter "F"

t.penup()

t.goto(40,0)

t.pendown()

t.forward(110)

t.goto(40,0)

t.left(90)

t.forward(50)

t.penup()

t.goto(40,-50)

t.pendown()

t.forward(40)

 

 

#for printing letter "G"

t.penup()

t.goto(150,0)

t.pendown()

for x in range(180):

 t.backward(1)

 t.left(1)

t.right(90)

t.forward(50)

t.right(90)

t.forward(30)

t.right(90)

t.forward(50)  
  
---  
  
 __

 __

### Output:

![](https://media.geeksforgeeks.org/wp-content/uploads/20200519014647/gfg-
turtgfg.gif)  

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

  
  

  

My Personal Notes _arrow_drop_up_

Save

