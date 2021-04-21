How to make a box with the help of nested loops using Python arcade?



Arcade library is modern framework currently used in making 2D games. Nested
loop discussed here are analogous to nested loops in any other programming
language.

The following tutorial will step by step explain how to draw a box with the
help of nested loops using Python’s arcade module.

  1. Import arcade library.
  2. Here we will be using circles to form a box. Thus, declare parameters, that will be used later in the program to specify spacing and margin between two circles.
  3.  **** Use arcade.open_window() to specify the width, height and title of the output screen.
  4. Set the background color of the output screen.(optional)
  5. Tell arcade module that you will now be sending drawing commands.
  6. Define the functionality using nested loop i.e one loop inside the other. We have defined a for loop for each row and inside that another for loop for column.
  7. Finally, we need to inform arcade module that which object we want the box should be made up of. Here, a circle is employed but you can define any other geometrical shape of your choice.
  8. Tell arcade that you have finished drawing and ask it to stop the output at the output window until the user doesn’t press exit.

Below is the implementation.

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

 

#specify parameters

col_spacing = 20

row_spacing = 20

lmargin = 110

bmargin = 110

 

# Open the window

arcade.open_window(500, 500, "BOX")

 

#set the background

arcade.set_background_color(arcade.color.BABY_PINK)

 

# Start the render process.

arcade.start_render()

 

# Loop for each row

for row in range(10):

 

 # Loop for each column

 for col in range(10):

 

 # Calculate our location

 x = col * col_spacing + lmargin

 y = row * row_spacing + bmargin

 

 # Draw the objects

 arcade.draw_circle_filled(x+1, y+2, 10,
arcade.color.BLUE)

 

# Finish.

arcade.finish_render()

 

# Keep the window up.

arcade.run()  
  
---  
  
 __

 __

 **Output:**

  

  

![](https://media.geeksforgeeks.org/wp-
content/uploads/20201001114031/BOX-300x235.png)  

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

