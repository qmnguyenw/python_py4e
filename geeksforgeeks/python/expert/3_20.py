Arcade inbuilt functions to draw polygon in Python3



The arcade library is a high-tech Python Package with advanced set of tools
for making 2D games with gripping graphics and sound. It is Object-oriented
and is especially built for Python 3.6 and above versions.

Arcade has two inbuilt functions for drawing a polygon:

![](https://media.geeksforgeeks.org/wp-
content/uploads/20201008211841/polygon.JPG)

 **1\. arcade.draw_polygon_outline( ) :** This function is used to draw the
outline of the polygon.

> **Syntax:** arcade.draw_polygon_outline (point_list, color, line_width )
>
>  
>
>
>  
>
>
>  **Parameters:**
>
>   *  **point_list:** List of points making up the lines. Each point is in a
> list. So it is a list of lists.
>   *  **color (Color):** specify color using arcade.color.COLOR NAME. (Note
> that color name should in Capital letters.)
>   *  **line_width:-** Width of the line in pixels.
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

import arcade

 

# Open the window. Set the window title and dimensions (width and height)

arcade.open_window(600, 600, "Draw a polygon for GfG ")

 

arcade.set_background_color(arcade.color.ORANGE)

 

# Start the render process.

arcade.start_render()

 

point_list = ((30, 240),

 (45, 240),

 (60, 255),

 (60, 285),

 (45, 300),

 (30, 300))

arcade.draw_polygon_outline(point_list, arcade.color.SPANISH_VIOLET, 3)

 

arcade.finish_render()

 

arcade.run()  
  
---  
  
 __

 __

 **Output:**

![](https://media.geeksforgeeks.org/wp-
content/uploads/20201008225716/polygonnn.png)

 **2\. arcade.draw_polygon_filled( ):** This inbuilt function of arcade is
used to draw polygon filled with color.

> **Syntax:** arcade.draw_polygon_filled (point_list, color )
>
>  **Parameters:**
>
>   *  **point_list-** It is basically List of points where each point is in a
> list. So it is a list of lists.
>   *  **Color –** specify color using arcade.color.COLOR NAME. (Note that
> color name should in Capital letters. )
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

import arcade

 

# Open the window. Set the window title and dimensions (width and height)

arcade.open_window(600, 600, "Draw a polygon for GfG ")

 

arcade.set_background_color(arcade.color.ORANGE)

 

# Start the render process.

arcade.start_render()

 

point_list = ((150, 240),

 (165, 240),

 (180, 255),

 (180, 285),

 (165, 300),

 (150, 300))

arcade.draw_polygon_filled(point_list, arcade.color.SPANISH_VIOLET)

 

arcade.finish_render()

 

arcade.run()  
  
---  
  
 __

 __

 **Output:**

![](https://media.geeksforgeeks.org/wp-
content/uploads/20201008225842/Pollll.png)  

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

