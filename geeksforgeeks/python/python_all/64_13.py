How to make Indian Flag using Turtle – Python



Here, we will be making “The Great Indian Flag” using Python Turtle Graphics.
Here, we will be using many turtle functions like **begin_fill(), end_fill()**
to fill color inside the Flag, **penup(), pendown(), goto() etc** to reaching
the target.

### Turtle graphics

In computer graphics, turtle graphics are vector graphics using a relative
cursor upon a Cartesian plane. Turtle is a drawing board like feature which
let us command the turtle and draw using it.

>  **Features of turtle graphics:**
>
>   *  **forward(x):** moves the pen in forward direction by x units.
>   *  **backward(x):** moves the pen in the backward direction by x units.
>   *  **right(x):** rotate the pen in the clockwise direction by an angle x.
>   *  **left(x):** rotate the pen in the anticlockwise direction by an angle
> x.
>   *  **penup():** stop drawing of the turtle pen.
>   *  **pendown():** start drawing of the turtle pen.
>   *  **begin_fill():** starts filling the color inside the shape.
>   *  **fillcolor(“color_name”):** sets the color to be filled.
>   *  **end_fill():** stops filling the color.
>

## Approach

1\. import the turtle modules.

    
    
    import turtle
    

2\. Get a screen to draw on.

  

  

    
    
    screen = turtle.Screen()
    
    
    
    

3\. Define an instance for **turtle(here “t”).**

4. **** For making **Indian Flag** lets divide the process into 4 steps:

  * The **rectangle with orange color.**
  * Then the **middle rectangle.**
  * Then the last **Green Rectangle.**
  * Then **Ashoka Chakra** inside the middle rectangle.

5\. Here dimensions of all three Rectangles are (800 units x 167 units), which
makes up dimensions of the flag as (800 units x 501 units).

6\. The turtle starts from coordinates (-400, 250).

7\. Then from that position it makes the **First rectangle of orange** color
**.**

8\. Then from the ending point of the first rectangle **,Turtle makes** the
**Second rectangle of no** color **.**

9\. Then the **Third green color rectangle is made.** Now for **Ashoka Chakra
we need to perform** a **set of operations**

  * A Big Blue circle and a white circle just smaller than blue.
  * Set of small blue circles on the inner lining of a blue and white circle.
  * And finally spokes inside the two blue and white circles starting from Centre towards the outer direction.

10\. Finally, The pride of one’s Nation is ready.

Below is the implementation of the above approach:

## Python

 __

 __  
 __

 __

 __  
 __  
 __

import turtle

from turtle import*

#screen for output

screen = turtle.Screen()

# Defining a turtle Instance

t = turtle.Turtle()

speed(0)

# initially penup()

t.penup()

t.goto(-400, 250)

t.pendown()

# Orange Rectangle

#white rectangle

t.color("orange")

t.begin_fill()

t.forward(800)

t.right(90)

t.forward(167)

t.right(90)

t.forward(800)

t.end_fill()

t.left(90)

t.forward(167)

# Green Rectangle

t.color("green")

t.begin_fill()

t.forward(167)

t.left(90)

t.forward(800)

t.left(90)

t.forward(167)

t.end_fill()

# Big Blue Circle

t.penup()

t.goto(70, 0)

t.pendown()

t.color("navy")

t.begin_fill()

t.circle(70)

t.end_fill()

# Big White Circle

t.penup()

t.goto(60, 0)

t.pendown()

t.color("white")

t.begin_fill()

t.circle(60)

t.end_fill()

# Mini Blue Circles

t.penup()

t.goto(-57, -8)

t.pendown()

t.color("navy")

for i in range(24):

 t.begin_fill()

 t.circle(3)

 t.end_fill()

 t.penup()

 t.forward(15)

 t.right(15)

 t.pendown()

 

# Small Blue Circle

t.penup()

t.goto(20, 0)

t.pendown()

t.begin_fill()

t.circle(20)

t.end_fill()

# Spokes

t.penup()

t.goto(0, 0)

t.pendown()

t.pensize(2)

for i in range(24):

 t.forward(60)

 t.backward(60)

 t.left(15)

 

#to hold the

#output window

turtle.done()  
  
---  
  
 __

 __

  
**Output:**

https://media.geeksforgeeks.org/wp-content/uploads/20200925192638/Indian-
Flag.mp4

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

