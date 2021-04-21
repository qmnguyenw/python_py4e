Draw a parabola using Arcade in Python3



Arcade is a Python library which is used for developing 2Dimensional Games.
Arcade needs support for OpenGL 3.3+. In arcade, basic drawing does not
require knowledge on how to define functions or classes or how to do loops,
simply we have inbuilt functions for drawing primitives.

Arcade inbuilt function for drawing parabola:-

![](https://media.geeksforgeeks.org/wp-
content/uploads/20201011182728/parabola-660x129.JPG)

 **1\. arcade.draw_parabola_outline( ):** This function draws the outline of a
parabola.

> **Syntax:** arcade.draw_parabola_outline(start_x , start_y, end_x , height ,
> color, border_width, tilt_angle)
>
>  
>
>
>  
>
>
>  **Parameters:**
>
>   *  **start_x** : The starting x position of the parabola
>   *  **start_y** : The starting y position of the parabola
>   *  **end_x :** The ending x position of the parabola
>   *  **height** : The height of the parabola
>   *  **color :** The color of the parabola
>   *  **border_width:** The width of the parabola
>   *  **tilt_angle :** The angle of the tilt of the parabola.
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

# import module

import arcade

 

# Open the window. Set the window title and dimensions (width and height)

arcade.open_window(600, 600, "Draw a parabola for GfG ")

 

# set background

arcade.set_background_color(arcade.color.WHITE)

 

# Start the render process.

arcade.start_render()

 

# function to draw a parabola

arcade.draw_parabola_outline(50, 80, 100, 120,
arcade.color.GREEN, 10, 0)

 

# finish drawing

arcade.finish_render()  
  
---  
  
 __

 __

 **Output:**

![](https://media.geeksforgeeks.org/wp-
content/uploads/20201011202655/parabo.png)

 **2\. arcade.draw_parabola_filled( ):** This function is used to draw a color
filed parabola.

>  **Syntax:** arcade.draw_parabola_outline(start_x , start_y, end_x , height
> , color, tilt_angle)
>
>  **Parameters:**
>
>  
>
>
>  
>
>
>   *  **start_x :** The starting x position of the parabola
>   *  **start_y** : The starting y position of the parabola
>   *  **end_x** :The ending x position of the parabola
>   *  **height :** The height of the parabola
>   *  **color :** The color of the parabola
>   *  **tilt_angle** : The angle of the tilt of the parabola.
>

 **Example :**

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# import module

import arcade

 

# Open the window. Set the window title and dimensions (width and height)

arcade.open_window(600, 600, "Draw a parabola for GfG ")

 

# set background

arcade.set_background_color(arcade.color.WHITE)

 

# Start the render process.

arcade.start_render()

 

# function to draw a parabola

arcade.draw_parabola_filled(25, 80, 100, 110,
arcade.color.GREEN ,0)

 

# finish drawing

arcade.finish_render()

 

# to display everything

arcade.run()  
  
---  
  
 __

 __

 **Output:**

![](https://media.geeksforgeeks.org/wp-
content/uploads/20201011230033/para-200x200.png)

 **Example :** Program to draw a rainbow using a series of parabola

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# import module

import arcade

 

# Open the window. Set the window title and dimensions (width and height)

arcade.open_window(600, 600, "Draw a parabola for GfG ")

 

#set background

arcade.set_background_color(arcade.color.WHITE)

 

# Start the render process.

arcade.start_render()

 

# function to draw a rainbow parabola

arcade.draw_parabola_filled(25, 80, 500, 300,
arcade.color.RED ,0)

arcade.draw_parabola_filled(50, 80, 470, 280,
arcade.color.ORANGE ,0)

arcade.draw_parabola_filled(75, 80, 440, 260,
arcade.color.YELLOW ,0)

arcade.draw_parabola_filled(100, 80, 410, 240,
arcade.color.GREEN ,0)

arcade.draw_parabola_filled(125, 80, 380, 220,
arcade.color.SKY_BLUE ,0)

arcade.draw_parabola_filled(150, 80, 350, 200,
arcade.color.VIOLET ,0)

arcade.draw_parabola_filled(175, 80, 325, 180,
arcade.color.INDIGO ,0)

 

# finish drawing

arcade.finish_render()

 

# to display everything

arcade.run()  
  
---  
  
 __

 __

 **Output:**

![](https://media.geeksforgeeks.org/wp-
content/uploads/20201011232429/rainbow.png)  

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

