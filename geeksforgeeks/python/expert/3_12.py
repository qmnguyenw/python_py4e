Draw a triangle using Arcade in Python



Arcade is a Python library that is used for developing 2Dimensional Games.
Arcade needs support for OpenGL 3.3+. In the arcade, basic drawing does not
require knowledge on how to define functions or classes or how to do loops,
simply we have inbuilt functions for drawing primitives.

Arcade inbuilt function for drawing triangle:

![](https://media.geeksforgeeks.org/wp-
content/uploads/20201009224635/triangle-660x138.JPG)

 **1:** **arcade.draw_traingle_outline( ):** This function is used to draw an
outline of a triangle.

>  **Syntax:** arcade.draw_triangle_outline(x1 , y1, x2 , y2 , x3 , y3 ,
> color, border_width)
>
>  
>
>
>  
>
>
>  **Parameters:**
>
>   *  **x1:** x value of first coordinate.
>   *  **y1:** y value of first coordinate.
>   *  **x2:** x value of second coordinate.
>   *  **y2:** y value of second coordinate.
>   *  **x3:** x value of third coordinate.
>   *  **y3:** y value of third coordinate.
>   *  **color:** Outline color of the triangle.
>   *  **border_width:** Width of the border in pixels. Defaults to 1.
>

Let’s see an example to understand its functioning better.

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

#import module

import arcade

 

# Open the window. Set the window title and

# dimensions (width and height)

arcade.open_window(600, 600, "Draw a triangle for GfG ")

 

# set background color

arcade.set_background_color(arcade.color.BLACK)

 

# Start the render process.

arcade.start_render()

 

# triangle function

arcade.draw_triangle_outline(300, 200,

 80, 80,

 100, 300,

 arcade.color.YELLOW, 1)

 

 

# finished drawing

arcade.finish_render()

 

# display everything

arcade.run()  
  
---  
  
 __

 __

 **Output:**

![](https://media.geeksforgeeks.org/wp-
content/uploads/20201009235323/outline.png)

 **2:** **arcade.draw_triangle_filled( ):** This function is used to draw a
triangle filled with color.

>  **Syntax:** arcade.draw_triangle_filled(x1, y1, x2, y2 , x3 , y3, color)
>
>  **Parameters:**
>
>   *  **x1:** x value of first coordinate.
>   *  **y1:** y value of first coordinate.
>   *  **x2:** x value of second coordinate.
>   *  **y2:** y value of second coordinate.
>   *  **x3:** x value of third coordinate.
>   *  **y3:** y value of third coordinate.
>   *  **color:** color to be filled in triangle.
>

 **Example:**

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# import

import arcade

 

# Open the window. Set the window title and 

# dimensions (width and height)

arcade.open_window(600, 600, "Draw a triangle for GfG ")

 

# set background color

arcade.set_background_color(arcade.color.BLACK)

 

# Start the render process.

arcade.start_render()

 

# draw triangle

arcade.draw_triangle_filled(300, 200,

 80, 80,

 100, 300,

 arcade.color.YELLOW)

 

# finish drawing

arcade.finish_render()

 

# display everything

arcade.run()  
  
---  
  
 __

 __

 **Output:**

![](https://media.geeksforgeeks.org/wp-
content/uploads/20201010000146/trii.png)  

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

