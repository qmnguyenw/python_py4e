Draw a sun using arcade library Python



You might have drawn Sun using famous Python module like turtle but here we
discuss how the same approach can be achieved using arcade module. The Arcade
library is a modern Python Module used widely for developing 2D video games
with compelling graphics and sound. Arcade is an object-oriented library. It
can be installed like any other Python Package.

### Installation

To install this module, just simply run the following command on your command
prompt:

    
    
    pip install arcade
    

**Approach:**

The following steps illustrate how to create a basic drawing using arcade
module:

  * Import module.
  * Specify the parameters for your output screen like width, height, etc.
  * Open the window using the inbuilt open_window() in arcade. This command opens a window with a given size i.e width and height along with screen title.
  * Set a background color (optional). It can be done using set_background_color() method built into arcade
  * Tell your module to start drawing using start_render() command which is again built into arcade.
  * Start designing, you can use functions already available with arcade to do so.
  * Tell arcade module that you have completed the drawing using finish_render().
  * Run your code using run().

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

 

# set parameters 

Width= 700

Height=700

Title="SUN"

 

# open window

arcade.open_window(Width, Height, Title)

 

# Set the background color

arcade.set_background_color(arcade.csscolor.BLUE)

 

# Get ready to draw

arcade.start_render()

 

# Draw a sun

arcade.draw_circle_filled(500, 550, 40, arcade.color.YELLOW)

 

# Rays to the left, right, up, and down

arcade.draw_line(500, 550, 400, 550, arcade.color.YELLOW,
3)

arcade.draw_line(500, 550, 600, 550, arcade.color.YELLOW,
3)

arcade.draw_line(500, 550, 500, 450, arcade.color.YELLOW,
3)

arcade.draw_line(500, 550, 500, 650, arcade.color.YELLOW,
3)

 

# Diagonal ray

arcade.draw_line(500, 550, 550, 600, arcade.color.YELLOW,
3)

arcade.draw_line(500, 550, 550, 500, arcade.color.YELLOW,
3)

arcade.draw_line(500, 550, 450, 600, arcade.color.YELLOW,
3)

arcade.draw_line(500, 550, 450, 500, arcade.color.YELLOW,
3)

 

# Finish drawing

arcade.finish_render()

 

# Keep the window up until someone closes it.

arcade.run()  
  
---  
  
 __

 __

