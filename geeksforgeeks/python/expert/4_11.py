Draw a happy face using Arcade Library in Python



Arcade is a Python module used for developing 2D games. For drawing a happy
face, steps are as follows:

  * Import arcade library.

    
    
    import arcade

  * Open the window.

    
    
    arcade.open_window(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)

The function used with arcade is open_window. This command opens a window with
a given size i.e width and height along with screen title.

  * Specify the values of parameters defined using open_window.

    
    
    SCREEN_WIDTH = 600
    SCREEN_HEIGHT = 600
    SCREEN_TITLE = "Happy Face GfG "

  * Choose a colour for background screen of your output.

    
    
    arcade.set_background_color(arcade.color.BLACK)

  * This command will tell the Arcade library that you start drawing.

    
    
    arcade.start_render()

  * Write a function to draw the circle for the base of the face using the in-built function draw_circle_filled() function.

    
    
    x = 300
    y = 300
    radius = 200
    arcade.draw_circle_filled(x, y, radius, arcade.color.YELLOW)

  * Similarly, write function for drawing the right and left eye of the face using the draw_circle_filled() function.

    
    
    # Draw the right eye
    x = 370
    y = 350
    radius = 20
    arcade.draw_circle_filled(x, y, radius, arcade.color.BLACK)
    # Draw the left eye
    x = 230
    y = 350
    radius = 20
    arcade.draw_circle_filled(x, y, radius, arcade.color.BLACK)

  * For the happy face, smile is the most important part. Use draw_arc_outline() function to draw smile .

    
    
    # Draw the smile
    x = 300
    y = 280
    width = 120
    height = 100
    start_angle = 190
    end_angle = 350
    arcade.draw_arc_outline(x, y, width, height,
                           arcade.color.BLACK, 
                           start_angle, end_angle, 10)

  * This command will tell the arcade library that you are done with drawing.

    
    
    # Finish drawing
    arcade.finish_render()

  * This command is to keep the window open.

    
    
    # Keep the window open until the user
    # hits the 'close' button
    arcade.run()

 **Complete Source Code:**

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

import arcade

 

 

# specify the parameters

SCREEN_WIDTH = 600

SCREEN_HEIGHT = 600

SCREEN_TITLE = "Happy Face GfG "

 

# Open the window. Set the window title and dimensions

arcade.open_window(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)

 

# Set the background color

arcade.set_background_color(arcade.color.BLACK)

 

# start render process

arcade.start_render()

 

# Draw the face

x = 300

y = 300

radius = 200

arcade.draw_circle_filled(x, y, radius, arcade.color.YELLOW)

 

# Draw the right eye

x = 370

y = 350

radius = 20

arcade.draw_circle_filled(x, y, radius, arcade.color.BLACK)

 

# Draw the left eye

x = 230

y = 350

radius = 20

arcade.draw_circle_filled(x, y, radius, arcade.color.BLACK)

 

# Draw the smile

x = 300

y = 280

width = 120

height = 100

start_angle = 190

end_angle = 350

arcade.draw_arc_outline(x, y, width, height, arcade.color.BLACK,

 start_angle, end_angle, 10)

 

# Finish drawing

arcade.finish_render()

 

# Keep the window open until the user hits 

# the 'close' button

arcade.run()  
  
---  
  
 __

 __

 **Output:**

  

  

https://media.geeksforgeeks.org/wp-content/uploads/20200926225402/Happy-
Face.mp4

  

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

