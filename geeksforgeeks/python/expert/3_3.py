Display Snowfall using arcade library in Python



In this article, we are going to display snowfall using the _arcade_ Python
Package. The _Arcade_ library is a modern Python Module used widely for
developing 2D video games with compelling graphics and sound. It is an object-
oriented library and can be installed like any other Python Package.

 **Step-by-step Approach:**

  * First and foremost step in this series is to import the _arcade_ library in your Python IDE. Also import _random_ and _math_ module, since in displaying snowfall at random places on the screen.

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# Import required modules

import random

import math

import arcade  
  
---  
  
 __

 __

  * Specify the values for screen width, height, and title of the output screen.

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# Adjust window attributes

Width = 800

Height = 600

Title = "SnowFall"  
  
---  
  
 __

 __

  * Define a class _snow_fall_ which consists of ___init___ method and a function to reset snowfall to random position above screen.

## Python3

  

  

 __

 __  
 __

 __

 __  
 __  
 __

class snow_fall:

 def __init__(self):

 self.x = 0

 self.y = 0

 

 def reset_snow(self):

 

 # Reset flake to random position above screen

 self.y = random.randrange(Height, Height + 100)

 self.x = random.randrange(Width)  
  
---  
  
 __

 __

