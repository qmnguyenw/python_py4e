Making an object jump with gravity using arcade module in Python3



The Arcade library is a modern Python Module used widely for developing 2D
video games with compelling graphics and sound. Arcade is an object-oriented
library. It can be installed like any other Python Package. Now, it’s up to
the necessity of the developer, what type of game, graphics, and sound he/she
wants to use using this toolkit. So, in this article, we will learn how to
make an object jump with gravity using the Arcade library in Python. And for
understanding that concept, let’s take an example of a robust ball.

Following are the steps:

 **Step 1:** Import arcade module .

    
    
    import arcade

 **Step 2:** Define parameters of the output screen.

    
    
    # Size of the screen
    WIDTH = 600
    HEIGHT = 600
    TITLE = "Robust Ball "

 **Step 3:** Define the radius of the ball.

  

  

    
    
    # Size of the ball.
    BALL_RADIUS = 50

 **Step 4:** Define the value of gravitational constant.

    
    
    #  gravity 
    GRAVITATIONAL_CONSTANT = 0.3

 **Step 5:** Define a bouncing velocity for the ball.

    
    
    # Percent of velocity maintained on a bounce.
    BOUNCE = 0.9

 **Step 6:** Define a function to draw a ball using
arcade.draw_circle_filled() .

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

def draw(_delta_time):

 

 # Start the render.

 arcade.start_render()

 

 # Draw ball

 arcade.draw_circle_filled(draw.x, draw.y, BALL_RADIUS,

 arcade.color.RED)

 

 draw.x += draw.delta_x

 draw.y += draw.delta_y

 draw.delta_y -= GRAVITATIONAL_CONSTANT  
  
---  
  
 __

 __

 **Step 7:** Define function to Figure out if we hit the left or right edge so
that we can reverse.

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# Figure out if we hit the left or

# right edge and need to reverse.

if draw.x < BALL_RADIUS and draw.delta_x < 0:

 draw.delta_x *= -BOUNCE

 elif draw.x > WIDTH - BALL_RADIUS and draw.delta_x > 0:

 draw.delta_x *= -BOUNCE  
  
---  
  
 __

 __

 **Step 8:** Also, Define function to Figure out if we hit the bottom so that
we can reverse.

## Python3

  

  

 __

 __  
 __

 __

 __  
 __  
 __

# See if we hit the bottom

if draw.y < BALL_RADIUS and draw.delta_y < 0:

 

 if draw.delta_y * -1 > GRAVITATIONAL_CONSTANT * 15:

 draw.delta_y *= -BOUNCE

 else:

 draw.delta_y *= -BOUNCE / 2  
  
---  
  
 __

 __

