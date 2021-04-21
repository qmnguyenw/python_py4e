How to show a timer on screen using arcade in Python3?



 **Prerequisite:** Arcade library

Arcade is a modern framework, which is used to make 2D video games. In this,
article, you will learn how to show an on-screen timer using the arcade module
of Python. Displaying a timer on screen is not tough job, just follow the
below steps:-

 **Step 1:** First of all import the arcade module of Python

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

import arcade  
  
---  
  
 __

 __

 **Step 2:** Define parameters necessary for the output screen.

  

  

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

WIDTH= 800

HEIGHT = 600

TITLE = "Timer"  
  
---  
  
 __

 __

 **Step 3:** Define a class MYTimer and under that class, set the background
color and starting time.

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

class MyTimer(arcade.Window):

 

 def setup(self):

 arcade.set_background_color(arcade.color.WHITE)

 self.total_time = 0.0  
  
---  
  
 __

 __

 **Step 4:** Under MyTimer class, define one function to calculate the minutes
and seconds.

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

def on_draw(self):

 

 # Start the render.

 arcade.start_render()

 

 # Calculate minutes

 minutes = int(self.total_time) // 60

 

 # Calculate seconds by using a modulus

 seconds = int(self.total_time) % 60

 

 # Figure out your output

 output = f"Time: {minutes:02d}:{seconds:02d}"

 

 # Output the timer text.

 arcade.draw_text(output, 300, 300, arcade.color.BOTTLE_GREEN,
45)  
  
---  
  
 __

 __

 **Step 5:** Now, define an on_update function to update time with each
increasing minutes and seconds.

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

def on_update(self, delta_time):

 self.total_time += delta_time  
  
---  
  
 __

 __

 **Step 6:** Last and foremost step is to define main() and call it in the
end.

  

  

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

def main():

 window = MyTimer()

 window.setup()

 arcade.run()

 

main()  
  
---  
  
 __

 __

 **Complete code**

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

 

# screen parameters

SCREEN_WIDTH = 800

SCREEN_HEIGHT = 600

SCREEN_TITLE = "Timer "

 

# define class

 

 

class MyTimer(arcade.Window):

 

 def setup(self):

 arcade.set_background_color(arcade.color.WHITE)

 self.total_time = 0.0

 

 def on_draw(self):

 

 # Start the render.

 arcade.start_render()

 

 # Calculate minutes

 minutes = int(self.total_time) // 60

 

 # Calculate seconds by using a modulus

 seconds = int(self.total_time) % 60

 

 # Figure out your output

 output = f"Time: {minutes:02d}:{seconds:02d}"

 

 # Output the timer text.

 arcade.draw_text(output, 300, 300, arcade.color.BOTTLE_GREEN,
45)

 

 # update

 def on_update(self, delta_time):

 self.total_time += delta_time

 

# main function

def main():

 window = MyTimer()

 window.setup()

 arcade.run()

 

 

# call main function

main()  
  
---  
  
 __

 __

 **Output:**

https://media.geeksforgeeks.org/wp-content/uploads/20201011133204/TIMEER.mp4

  

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

