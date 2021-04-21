How to Create custom Turtle shapes in Python?



In Turtle, by default, we have an arrowhead-shaped cursor for drawing on the
canvas. This can be changed to some other predefined shape or we can also
create a custom shape and register it under a name. Not just that, we can even
use _gif_ format images to replace our cursor.

## Changing cursor to predefined shapes

The **shape()** function is used to set the shape of the cursor. The pre-
defined shapes include _turtle_ , _arrow_ , _circle_ , _square_ and
_triangle_.

 __

 __  
 __

 __

 __  
 __  
 __

import turtle

 

# turtle object

c_turtle = turtle.Turtle()

 

# changing the cursor

# shape to cirlce

c_turtle.shape('circle')  
  
---  
  
 __

 __

 **Output :**

![](https://media.geeksforgeeks.org/wp-
content/uploads/20200728190712/Screenshot-2020-07-28-at-7.06.26-PM.png)

## Registering new shapes

The turtle module has **register_shape()** function for registering custom
shapes.

>  **Syntax :** turtle.register_shape(name, shape)  
>  **Parameters :**
>
>  
>
>
>  
>
> * name : a string- the name of the shape to be registered.
> * shape : a tuple of tuples containing the coordinates for the custom shape.

The n-tuple argument for the shape parameter, denotes the relative position of
each corner of an n-sided polygon. Let us try to create a simple diamond shape
to understand this.

Consider this diamond, having length of diagonal = 20, in a Cartesian plane :

![](https://media.geeksforgeeks.org/wp-
content/uploads/20200728172732/diamond11.jpg)

To create this shape, we need to pass these coordinates in clockwise order.

 __

 __  
 __

 __

 __  
 __  
 __

import turtle

 

# turtle object

dimond_turtle = turtle.Turtle()

 

# the coordinates

# of each corner

shape =((0, 0), (10, 10), (20, 0), (10,
-10))

 

# registering the new shape

turtle.register_shape('diamond', shape)

 

# changing the shape to 'diamond'

dimond_turtle.shape('diamond')  
  
---  
  
 __

 __

 **Output :**

![](https://media.geeksforgeeks.org/wp-
content/uploads/20200728172851/Screenshot-2020-07-27-at-8.36.00-PM-300x290.png)

## Using images for Turtle cursor

To use an image as the cursor, we need to pass the image file path as
parameter to _register_shape()_. Note that this image has to be in _gif_
format.

 __

 __  
 __

 __

 __  
 __  
 __

import turtle

 

# turtle object

img_turtle = turtle.Turtle()

 

# registering the image

# as a new shape

turtle.register_shape('example.gif')

 

# setting the image as cursor

img_turtle.shape('example.gif')  
  
---  
  
 __

 __

 **Output :**  
![](https://media.geeksforgeeks.org/wp-
content/uploads/20200728173323/Screenshot-2020-07-28-at-5.28.06-PM1.png)

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

