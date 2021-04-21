How to animate an object using Arcade module?



 **Prerequisite:**Arcade Library

The world of Programming is very vast, and animation is its key soul. In this,
tutorial you will learn how to animate objects in Python using Arcade Module.
Arcade is a present day Programming module used for developing 2D games with
gripping sound and graphics.

Before starting with the article, you must revise your concepts of arcade
Python module. To explain the whole concept of animating an object, Let’s take
an example to understand it completely. You all must aware with the nested
loop being in C, Python or Java and have probably created a lot of patterns
using it. Here, we will animate a box with the help of _arcade_ Python
library.

**Step-by-step Approach:**

 **Step1)** Import _arcade_ library.

  

  

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# Import required module

import arcade  
  
---  
  
 __

 __

 **Step2)** Here we will specify some parameters, that we will be using later
in the program to declare width, height and title of the screen.

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# Set up the constants

 

# Size of the screen

SCREEN_WIDTH = 720

SCREEN_HEIGHT = 480

SCREEN_TITLE = "Bouncing Box"

 

# Size of the rectangle

RECT_WIDTH = 50

RECT_HEIGHT = 50  
  
---  
  
 __

 __

 **Step3)** Define the function for drawing the box
arcade.draw_rectangle_filled( ) Modify rectangles position based on the delta
vector.

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# Explicilt function generate animated bouncing box

def on_draw(delta_time):

 

 # Start the render.

 arcade.start_render()

 

 arcade.draw_rectangle_filled(on_draw.center_x, on_draw.center_y,

 RECT_WIDTH, RECT_HEIGHT,

 arcade.color.GREEN)

 

 on_draw.center_x += on_draw.delta_x * delta_time

 on_draw.center_y += on_draw.delta_y * delta_time

 

 # Figure out if we hit the edge and need to reverse.

 if on_draw.center_x < RECT_WIDTH // 2 \

 or on_draw.center_x > SCREEN_WIDTH - RECT_WIDTH // 2:

 on_draw.delta_x *= -1

 if on_draw.center_y < RECT_HEIGHT // 2 \

 or on_draw.center_y > SCREEN_HEIGHT - RECT_HEIGHT // 2:

 on_draw.delta_y *= -1  
  
---  
  
 __

 __

 **Step4:** -Now, define function-specific variables. Also, we need to give
them initial values. Then the values will persist between function calls.

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# Set initial positions

on_draw.center_x = 100

on_draw.center_y = 50

on_draw.delta_x = 115

on_draw.delta_y = 130  
  
---  
  
 __

 __

 **Step5)** Now, last step is define the main function. Under which, you need
to define background colors.

  

  

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# Driver code

 

# Open up our window

arcade.open_window(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)

arcade.set_background_color(arcade.color.WHITE)

 

# Tell the computer to call the draw command at the specified interval.

arcade.schedule(on_draw, 1 / 80)

 

# Run the program

arcade.run()  
  
---  
  
 __

 __

 **Below is the complete program of the above approach:**

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# Import required module

import arcade

 

 

# Set up the constants

 

# Size of the screen

SCREEN_WIDTH = 720

SCREEN_HEIGHT = 480

SCREEN_TITLE = "Bouncing Box"

 

# Size of the rectangle

RECT_WIDTH = 50

RECT_HEIGHT = 50

 

 

# Explicilt function generate animated bouncing box

def on_draw(delta_time):

 

 # Start the render.

 arcade.start_render()

 

 arcade.draw_rectangle_filled(on_draw.center_x, on_draw.center_y,

 RECT_WIDTH, RECT_HEIGHT,

 arcade.color.GREEN)

 

 on_draw.center_x += on_draw.delta_x * delta_time

 on_draw.center_y += on_draw.delta_y * delta_time

 

 # Figure out if we hit the edge and need to reverse.

 if on_draw.center_x < RECT_WIDTH // 2 \

 or on_draw.center_x > SCREEN_WIDTH - RECT_WIDTH // 2:

 on_draw.delta_x *= -1

 if on_draw.center_y < RECT_HEIGHT // 2 \

 or on_draw.center_y > SCREEN_HEIGHT - RECT_HEIGHT // 2:

 on_draw.delta_y *= -1

 

 

# Set initial positions

on_draw.center_x = 100

on_draw.center_y = 50

on_draw.delta_x = 115

on_draw.delta_y = 130

 

 

# Driver code

 

# Open up our window

arcade.open_window(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)

arcade.set_background_color(arcade.color.WHITE)

 

# Tell the computer to call the draw command at the specified interval.

arcade.schedule(on_draw, 1 / 80)

 

# Run the program

arcade.run()  
  
---  
  
 __

 __

 **Output:**

https://media.geeksforgeeks.org/wp-content/uploads/20201006231620/Bouncing-
Box.mp4

  

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

