Getting width and height of an image in Pygame



 **Prerequisites:** Pygame

To use graphics in python programs we use a module called Pygame. **Pygame**
provides high functionality for developing games and graphics in Python.
Nowadays Pygame are very much popular to build simple 2D games. In order to
run a program written in Python using Pygame module, a system must have Python
installed with Pygame module.

Following are the examples and steps needed to import the image using Pygame
and get the height and width of that image.

 **Image in used :**Link to the image

![](https://media.geeksforgeeks.org/wp-
content/uploads/20210116194758/download.png)

  

  

**Dimensions : 200×200**

###

##

### Method 1 : Using get_width() and get_height() :

The name of the function is explanatory enough as to what they are used for.

 **Approach**

  * Import pygame
  * Create an image object using _**pygame.image.load(“Provide image path here “)**_ and store it in a variable.
  * To get height of the image use _**image.get_height()**_ method _ **,**_ here image is the variable in which image object is stored.
  * Similarly, to get width of the image we use _**image.get_width()**_ method, here image is the variable in which image object is stored.
  * Print result.

 **Example:**

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# import pygame

import pygame

 

# creating image object

image =
pygame.image.load('/home/amninder/Pictures/Wallpapers/download.png')

 

# get_height method return the height of the surface pixel,

# in our case surface is image

print("Height of image= " + str(image.get_height()))

 

# get_width method return the width of the surface pixel,

# in our case surface is image

print("Width of image= " + str(image.get_width()))  
  
---  
  
 __

 __

 **Output:**

![](https://media.geeksforgeeks.org/wp-
content/uploads/20210111203902/Screenshotfrom20210111203834.png)

Method 1

###

### Method 2 : Using get_size() :

This function is capable of returning dimensions of the image provided to it
as reference as a tuple.

 **Approach**

  * Import module
  * Create a display object using **display.set_mode()** method **.**
  * Load image to a variable using **image.load()** method.
  * Using **blit()** method to draw the image on display surface object.
  * Use **get_size()** method to display image width and height, this get_size() method returns width and height in tuples. Eg. (200,400).
  * Use **display.flip()** to display content,i.e. anything that is drawn on the display surface object will be displayed on the window when the function is called in program.

 **Example:**

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

import pygame as py

 

# Initiate pygame and the modules that comes with pygame

py.init()

 

# setting frame/window/surface with some dimensions

window = py.display.set_mode((300, 300))

 

# to set title of pygame window

py.display.set_caption("GFG")

 

# creating image object

image =
py.image.load('/home/amninder/Pictures/Wallpapers/download.png')

 

# to display size of image

print("size of image is (width,height):", image.get_size())

 

# loop to run window continuously

while True:

 window.blit(image, (0, 0))

 

 # loop through the list of Event

 for event in py.event.get():

 # to end the event/loop

 if event.type == py.QUIT:

 

 # it will deactivate the pygame library

 py.quit()

 quit()

 

 # to display when screen update

 py.display.flip()  
  
---  
  
 __

 __

 **Output :**

![](https://media.geeksforgeeks.org/wp-
content/uploads/20210111210232/Screenshotfrom20210111210204.png)

Using method 2

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

