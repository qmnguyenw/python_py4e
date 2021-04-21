Arcade inbuilt functions to draw point(s) in Python3



The Arcade library is a modern Python Module used widely for developing 2D
video games with compelling graphics and sound. Arcade is an object-oriented
library. It can be installed like any other Python Package.

In this article, we will learn what are the arcade inbuilt functions to draw
point.

Arcade library is a modern framework, which makes drawing illustrations very
easily through its inbuilt functions. In arcade, we have two inbuilt functions
to draw point.

![](https://media.geeksforgeeks.org/wp-
content/uploads/20201007204204/pointss.JPG)

 **1\. arcade.draw_point( ):** It is used to draw a point and you can even
draw multiple points using this function by calling it as many times you want
to.

  

  

> **Syntax:** arcade.draw_point(x , y, color , size)
>
>  **Parameters:**
>
>   *  **x –** is position of point.
>   *  **y** -is position of point.
>   *  **Color** – specify color using arcade.color.COLOR NAME. (Note that
> color name should in Capital letters.)
>   *  **Size –** Size of the point in pixels.
>

 **Approach For drawing a point using arcade.draw_point:**

  1. Import Arcade module
  2. Open the window and Set the window parameters.
  3. Set the background color of the output window.(optional)
  4. Start the render process
  5. Implement aracde.draw_point() with its specified parameters.
  6. Finish rendering
  7. Keep the window up until you close it.

 **Program 1:** (Program to draw a single point)

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

arcade.open_window(600, 600, "Draw a point for GfG ")

 

arcade.set_background_color(arcade.color.WHITE)

 

# Start the render process. 

arcade.start_render()

 

# Draw a point

arcade.draw_point(60, 495, arcade.color.RED, 10)

 

# Finish the render.

arcade.finish_render()

 

# Keep the window up until someone closes it.

arcade.run()  
  
---  
  
 __

 __

 **Output:**

![](https://media.geeksforgeeks.org/wp-
content/uploads/20200928125855/point-300x298.png)

 **Program 2:** (Program to draw multiple points)

  

  

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

import arcade

 

# Open the window

arcade.open_window(600, 600, "Draw a point for GfG ")

arcade.set_background_color(arcade.color.BLUE)

 

# Start the render process

arcade.start_render()

 

# Draw a point

arcade.draw_point(60, 495, arcade.color.RED, 10)

 

# Draw a point

arcade.draw_point(80, 500, arcade.color.YELLOW, 10)

 

# Finish the render.

arcade.finish_render()

 

# Keep the window up until someone closes it.

arcade.run()  
  
---  
  
 __

 __

 **Output:**

![](https://media.geeksforgeeks.org/wp-
content/uploads/20200929000031/POints-200x192.png)

 **2\. arcade.draw_points ( ):** With this function, it is easier to draw
multiple points that to in a particular pattern.

> **Syntax:** arcade.draw_points(point_list , color , size)
>
>  **Parameters:**
>
>   *  **point_list –** It is basically list of points where each point is in
> a list. So it is a list of lists.
>   *  **Color** -specify color using arcade.color.COLOR NAME. (Note that
> color name should in Capital letters.)
>   *  **Size** – Size of the point in pixels.
>

 **Program:**

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

import arcade

 

# Open the window

arcade.open_window(600, 600, "Draw a point for GfG ")

 

arcade.set_background_color(arcade.color.ORANGE)

 

# Start the render process.

arcade.start_render()

 

# Draw a points

point_list = ((165, 495),

 (165, 480),

 (165, 465),

 (195, 495),

 (195, 480),

 (195, 465))

arcade.draw_points(point_list, arcade.color.GREEN , 10)

 

# Finish the render.

arcade.finish_render()

 

# Keep the window up until someone closes it.

arcade.run()  
  
---  
  
 __

 __

 **Output:**

![](https://media.geeksforgeeks.org/wp-
content/uploads/20201007212156/savee.png)  

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

