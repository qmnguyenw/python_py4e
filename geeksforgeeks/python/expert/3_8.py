Draw a circle using Arcade in Python3



The arcade library is a high-tech Python Package with advanced set of tools
for making 2D games with gripping graphics and sound. It is Object-oriented
and is especially built for Python 3.6 and above versions.

Arcade inbuilt functions to draw circle :-

![](https://media.geeksforgeeks.org/wp-content/uploads/20201010234709/cir.JPG)

 **1.** **arcade.draw_circle_outline( ) :** This function is used to draw the
outline of a circle.

> **Syntax:** arcade.draw_circle_outline(center_x, center_y, radius, color,
> border_width, num_segments)
>
>  
>
>
>  
>
>
>  **Parameters:**
>
>   *  **center_x** – x position that is the center of the circle.
>   *  **center_y** – y position that is the center of the circle.
>   *  **radius** – width of the circle.
>   *  **color** – color which with outline will be drawn.
>   *  **border_width** – Width of the circle outline in pixels.
>   *  **num_segments** – Higher is the number of segments, higher is the
> quality, but slower render time. The default value is -1 which means arcade
> will try to calculate a reasonable amount of segments based on the size of
> the circle.
>

Let’s take an example-

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

arcade.open_window(600, 600, "Draw an arc for GfG ")

 

#set background

arcade.set_background_color(arcade.color.WHITE)

 

# Start the render process.

arcade.start_render()

 

#function to draw a circle

arcade.draw_circle_outline(300, 285, 88, arcade.color.GREEN,
9,-1)

 

#finish drawing

arcade.finish_render()

 

#to display everything

arcade.run()  
  
---  
  
 __

 __

 **Output:**

![](https://media.geeksforgeeks.org/wp-
content/uploads/20201010235958/outlineci.png)

Since, now you know how to draw a simple outline of a circle. Let’s draw the
Olympic flag using this arcade.draw_circle_outline( ).

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

arcade.open_window(600, 600, "Draw an arc for GfG ")

 

# set background color

arcade.set_background_color(arcade.color.WHITE)

 

# Start the render process.

arcade.start_render()

 

# function for designing olympic flag

arcade.draw_circle_outline(100, 285, 88, arcade.color.BLUE,
9, -1)

arcade.draw_circle_outline(300, 285, 88, arcade.color.BLACK,
9, -1)

arcade.draw_circle_outline(500, 285, 88, arcade.color.RED, 9,
-1)

arcade.draw_circle_outline(200, 185, 88, arcade.color.YELLOW,
9, -1)

arcade.draw_circle_outline(400, 185, 88, arcade.color.GREEN,
9, -1)

 

# finished drawing

arcade.finish_render()

 

# to display everything

arcade.run()  
  
---  
  
 __

 __

 **Output:**

  

  

![](https://media.geeksforgeeks.org/wp-
content/uploads/20201011002435/olympic-660x369.png)

 **2.** **arcade.draw_circle_filled( ) :** This function is used to draw color
filled circle .

> **Synax: arcade.draw_circle_outline(center_x, center_y, radius, color,
> num_segments)**
>
>  **Parameters:**
>
>   * center_x – x position that is the center of the circle.
>   * center_y – y position that is the center of the circle.
>   * radius – width of the circle.
>   * color – color which with outline will be drawn.
>   * num_segments – Higher is the number of segments, higher is the quality,
> but slower render time. The default value is -1 which means arcade will try
> to calulate a reasonable amount of segments based on the size of the circle.
>

Let’s take an example-

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

 

# Open the window. Set the window title and dimensions (width and height)

arcade.open_window(600, 600, "Draw a circle for GfG ")

 

# set background

arcade.set_background_color(arcade.color.WHITE)

 

# Start the render process.

arcade.start_render()

 

# draw circle

arcade.draw_circle_filled(300, 450, 78, arcade.color.PINK,
0)

 

 

# finish drawing

arcade.finish_render()

 

# to display everything

arcade.run()  
  
---  
  
 __

 __

 **Output:**

![](https://media.geeksforgeeks.org/wp-
content/uploads/20201011125147/pinkzzs.png)

Since, now you know how to draw a simple outline of a circle. Let’s draw a
snowman using this arcade.draw_circle_filled( ).

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

arcade.open_window(600, 600, "Draw a circle for GfG ")

 

# set background

arcade.set_background_color(arcade.color.WHITE)

 

# Start the render process.

arcade.start_render()

 

# snowman upper part

arcade.draw_circle_filled(300, 450, 68, arcade.color.SKY_BLUE,
0)

 

# snowman eyes

arcade.draw_circle_filled(289, 475, 8, arcade.color.BLACK,
0)

arcade.draw_circle_filled(329, 475, 8, arcade.color.BLACK,
0)

 

# snowman lower part

arcade.draw_circle_filled(300, 350, 88, arcade.color.BLUE,
0)

arcade.draw_circle_filled(300, 250, 108, arcade.color.SKY_BLUE,
0)

 

# finish drawing

arcade.finish_render()

 

# to display everything

arcade.run()  
  
---  
  
 __

 __

 **Output:**

![](https://media.geeksforgeeks.org/wp-
content/uploads/20201011130819/SNOWMAN.png)  

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

