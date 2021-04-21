turtle.circle() method in Python



The Turtle module provides turtle graphics primitives, in both object-oriented
and procedure-oriented ways. Because it uses Tkinter for the underlying
graphics, it needs a version of Python installed with Tk support.

###  turtle.circle() :

This method is used to draw a circle with a given radius.

>  **Syntax:** turtle.circle(radius, extent=None, steps=None)
>
>  **Parameters:**
>
>   *  **radius:** Radius of the circle.
>   *  **extent:** The part of the circle in degrees as an arc.
>   *  **steps:** Divide the shape in the equal number of given steps.
>

Below is the implementation of the above method with some examples :

  

  

 **Example 1:**

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# importing turtle package

import turtle

 

# draw circle of radius 

# 80 pixel

turtle.circle(80)  
  
---  
  
 __

 __

 **Output** :

![Draw circle of radius 80](https://media.geeksforgeeks.org/wp-
content/uploads/20200712121822/circle.gif)

 **Example 2:**

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# importing turtle package

import turtle

 

# draw circle of radius 80 

# pixel and extent = 180

# so it draw half circle

turtle.circle(80, 

 extent = 180)  
  
---  
  
 __

 __

 **Output** :

![draw a semi circle of radius 80](https://media.geeksforgeeks.org/wp-
content/uploads/20200712122137/arc.gif)

 **Example 3:**

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# importing turtle package

import turtle

 

# draw circle of radius 80

# pixel and steps = 5

# so it draw pentagon with

# equal length 5 sides

turtle.circle(80, 

 steps = 5)  
  
---  
  
 __

 __

 **Output :**

![Draw regular pentagon ](https://media.geeksforgeeks.org/wp-
content/uploads/20200712122535/steps.gif)  

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

