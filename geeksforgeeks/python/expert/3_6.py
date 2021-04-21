Draw an arc using Arcade in Python



The arcade library is a high-tech Python Package with an advanced set of tools
for making 2D games with gripping graphics and sound. It is Object-oriented
and is specially built for Python 3.6 and above versions.

Arcade has two inbuilt functions for drawing arc:

![](https://media.geeksforgeeks.org/wp-content/uploads/20201010223909/arc.JPG)

 **1: arcade.draw_arc_outline ( ):** This function is used to draw an arc
which is useful for drawing curved lines

>  **Syntax:** arcade.draw_arc_outline(center_x , center_y, width , height,
> color, start_angle, end_angle , border_width, tilt_angle, num_segments)
>
>  
>
>
>  
>
>
>  **Parameters:**
>
>   *  **center_x :** x position that is the center of the arc.
>   *  **center_y :** y position that is the center of the arc.
>   *  **width** : width of the arc.
>   *  **height :** height of the arc.
>   *  **color** : Outline color of the arc.
>   *  **start_angle** : start angle of the arc in degrees.
>   *  **end_angle** : end angle of the arc in degrees.
>   *  **border_width** : width of line in pixels.
>   *  **tilt_angle** : angle the arc is tilted.
>   *  **num_segments :** Higher is the num of segments ,better is the quality
> .
>

Let’s see the below example:-

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

import arcade

 

# Open the window. Set the window title and

# dimensions (width and height)

arcade.open_window(600, 600, "Draw an arc for GfG ")

 

arcade.set_background_color(arcade.color.WHITE)

 

# Start the render process.

arcade.start_render()

 

arcade.draw_arc_outline(150, 81, 15, 36,

 arcade.color.BLACK, 90, 360)

 

arcade.finish_render()

 

arcade.run()  
  
---  
  
 __

 __

 **Output:**

![](https://media.geeksforgeeks.org/wp-
content/uploads/20201010232155/ARrrc-300x172.png)

 **2:** **arcade.draw_arc_filled( ):** This function is used to draw a arc
filled with color which are useful for drawing pie-wedges, or Pac-Man.

>  **Syntax:** arcade.draw_arc_outline(center_x , center_y, width , height,
> color, start_angle, end_angle , tilt_angle, num_segments)
>
>  **Parameters:**
>
>   *  **center_x :** x position that is the center of the arc.
>   *  **center_y** : y position that is the center of the arc.
>   *  **width** : width of the arc.
>   *  **height :** height of the arc.
>   *  **color** : color to be filled in the arc.
>   *  **start_angle** : start angle of the arc in degrees.
>   *  **end_angle** : end angle of the arc in degrees.
>   *  **tilt_angle :** angle the arc is tilted.
>   *  **num_segments** : Number of line segments used to draw the arc.
>

Let’s take an example to get a clear picture of the functionality.

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# import arcade module

import arcade

 

# Open the window. Set the window title and

# dimensions (width and height)

arcade.open_window(600, 600, "Draw an arc for GfG ")

 

# set a background color

arcade.set_background_color(arcade.color.WHITE)

 

# Start the render process.

arcade.start_render()

 

# function for drawing arc

arcade.draw_arc_filled(150, 144, 85, 86,

 arcade.color.BOTTLE_GREEN, 90, 360, 45, 54)

 

# finished drawing

arcade.finish_render()

 

# to diaplay everything

arcade.run()  
  
---  
  
 __

 __

 **Output:**

![](https://media.geeksforgeeks.org/wp-
content/uploads/20201010233731/ARrrc.png)  

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

