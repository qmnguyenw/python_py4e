Draw an ellipse using Arcade library in Python



 **Prerequisite:**Arcade Library

The _Arcade_ library is a modern Python Module used for developing 2D video
games with enthralling graphics and sound. It is an object-oriented library.
It can be installed like any other Python Package in your IDE.

 _Arcade_ Module has two inbuilt functions for drawing an ellipse i.e
_arcade.draw_ellipse_outline()_ and _arcade.draw_ellipse_filled()_. This is a
plus point in the _arcade_ module, otherwise, you must have noticed that in
Python modules like _turtle_ , you need to create a function for drawing any
primitive design.

![](https://media.geeksforgeeks.org/wp-
content/uploads/20200930172717/ellipse-660x237.JPG)

 **1) arcade.draw_ellipse_outline():** This method is used to outline of an
ellipse.

  

  

> **Syntax:** arcade.draw_ellipse_outline(centre_x, centre_y, width, height,
> color, border_width, tilt_angle, num_segments)
>
>  **1\. centre_x:** x position that is the center of the ellipse.  
>  **2\. centre_y:** y position that is the center of the ellipse.  
>  **3\. Width:** Width of the ellipse.  
>  **4\. Height:** Height of the ellipse.  
>  **5\. Color:** This is used to define the colors used for making outline of
> the ellipse with the help of arcade.color function.  
>  **6\. border_width:** Width of the ellipse outline in pixels.  
>  **7\. tilt_angle:** Angle in degrees to tilt the ellipse.  
>  **8\. num_segments:** Number of triangle segments that make up this
> ellipse. The default value is -1 that clearly means that arcade will
> calculate amount of segments based on the size of the ellipse.

 **Implementation of the above method:**

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# Import required modules

import arcade

 

# Specify Parameters

SCREEN_WIDTH = 600

SCREEN_HEIGHT = 800

SCREEN_TITLE = "Welcome to GeeksForGeeks "

 

# Open the window

arcade.open_window(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)

 

# Set the background color

arcade.set_background_color(arcade.color.BABY_BLUE)

 

# Start drawing

arcade.start_render()

 

# Draw ellipse

arcade.draw_ellipse_outline(

 400, 363, 250, 130, arcade.color.AMBER, 10, 180,
-1)

 

# Finish drawing

arcade.finish_render()

 

# Display everything

arcade.run()  
  
---  
  
 __

 __

 **Output:**

![](https://media.geeksforgeeks.org/wp-
content/uploads/20201001133238/Ellipse-300x157.png)

 **2)** **arcade.draw_ellipse_filled():** This method is used to draw filled
ellipse.

>  **Syntax:** arcade.draw_ellipse_filled(centre_x, centre_y, width, height,
> color, tilt_angle, num_segments)
>
>  
>
>
>  
>
>
>  **1\. centre_x:** x position that is the center of the ellipse.  
>  **2\. centre_y:** y position that is the center of the ellipse.  
>  **3\. Width:** Width of the ellipse.  
>  **4\. Height:** Height of the ellipse.  
>  **5\. Color:** This is used to define the colors used for making outline of
> the ellipse with the help of arcade.color function.  
>  **6\. border_width:** Width of the ellipse outline in pixels.  
>  **7\. tilt_angle:** Angle in degrees to tilt the ellipse.  
>  **8\. num_segments:** Number of triangle segments that make up this
> ellipse. The default value is -1 that clearly means that arcade will
> calculate amount of segments based on the size of the ellipse.

All other parameters are same as _arcade.draw_ellipse_outline()_ except the
_border_width_. In _arcade.draw_ellipse_filled()_ we don’t require
border_width.

 **Implementation of the above method:**

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# Import required modules

import arcade

 

# Specify Parameters

SCREEN_WIDTH = 600

SCREEN_HEIGHT = 800

SCREEN_TITLE = "Welcome to GeeksForGeeks "

 

# Open the window

arcade.open_window(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)

 

# Set the background color

arcade.set_background_color(arcade.color.BABY_BLUE)

 

# start drawing

arcade.start_render()

 

# Draw ellipse

arcade.draw_ellipse_filled(400, 363, 250, 130,
arcade.color.AMBER, 180, -1)

 

# Finish drawing

arcade.finish_render()

 

# Display everything

arcade.run()  
  
---  
  
 __

 __

 **Output:**

![](https://media.geeksforgeeks.org/wp-
content/uploads/20201001134041/Ellipsee-300x135.png)  

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

