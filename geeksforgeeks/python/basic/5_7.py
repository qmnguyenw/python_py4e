turtle.onscreenclick() function in Python



The turtle module provides turtle graphics primitives, in both object-oriented
and procedure-oriented ways. Because it uses Tkinter for the underlying
graphics, it needs a version of Python installed with Tk support.

## turtle.onscreenclick()

This function is used to bind fun to a mouse-click event on canvas.

 **Syntax :**

    
    
    turtle.onscreenclick(fun, btn=1, add=None)
    

**Parameters:** **Arguments** | **Description** | fun| a function with two
arguments, the coordinates of the clicked point on the canvas.| btn| number of
the mouse-button defaults to 1 (left mouse button)| add| True or False. If
True, new binding will be added, otherwise it will replace a former binding  
---|---  
  
  

  

Below is the implementation of the above method with an example :

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# import packages

import turtle

import random

 

# global colors

col = ['red', 'yellow', 'green', 'blue',

 'white', 'black', 'orange', 'pink']

 

# method to call on screen click

 

 

def fxn(x, y):

 global col

 ind = random.randint(0, 7)

 

 # set screen color randomly

 sc.bgcolor(col[ind])

 

# set screen

sc = turtle.Screen()

sc.setup(400, 300)

 

# call method on screen click

turtle.onscreenclick(fxn)  
  
---  
  
 __

 __

 **Output :**

![](https://media.geeksforgeeks.org/wp-
content/uploads/20200723170024/onscreenclick1.gif)

Here we can find that whenever the user clicks (yellow-colored dot on arrow)
on screen it changes the background color of the turtle graphics window
randomly.

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

