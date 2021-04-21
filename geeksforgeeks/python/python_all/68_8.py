How to Get Coordinate Of Screen in Python Turtle ?



Turtle is a special feature in python which contains a graphical library. In
this article we will learn how to Get Coordinate Of Screen in Python Turtle.

Turtle has many built in function to create this program we use following.

>  **import turtle – > **This is the python library which allow us to access
> turtle library.
>
>  **Turtle()– >** This Method is used to make object.
>
>  **onscreenclick(functionname,1) – > **This is turtle function which sends
> the coordinate to function; 1 is for left click and 3 is for Right click
>
>  
>
>
>  
>
>
>  **speed()– > **This is used to increse or decrease the speed of turtle
> pointer.
>
>  **listen()– > T**his allows the server to listen to incoming connections.
>
>  **done()– > **This is used to hold the the screen.

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# turtle library

import turtle 

 

#This to make turtle object

tess=turtle.Turtle() 

 

# self defined function to print coordinate

def buttonclick(x,y): 

 print("You clicked at this coordinate({0},{1})".format(x,y))

 

 #onscreen function to send coordinate

turtle.onscreenclick(buttonclick,1) 

turtle.listen() # listen to incoming connections

turtle.speed(10) # set the speed

turtle.done() # hold the screen  
  
---  
  
 __

 __

###  **Output:**

![](https://media.geeksforgeeks.org/wp-
content/uploads/20200519211456/turtle.gif)  

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

