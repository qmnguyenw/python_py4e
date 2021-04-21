Python | Display images with PyGame



 **Pygame** is a cross-platform set of Python modules designed for writing
video games. It includes computer graphics and sound libraries designed to be
used with the Python programming language. Now, it’s up to the imagination or
necessity of developer, what type of game he/she wants to develop using this
toolkit.

Command to install **pygame** :

    
    
    pip install pygame
    

There are four basic steps to displaying images on the pygame window :

  * Create a display surface object using display.set_mode() method of pygame.
  * Create a Image surface object i.e.surface object in which image is drawn on it, using image.load() method of pygame.
  * Copy the image surface object to the display surface object using blit() method of pygame display surface object.
  * Show the display surface object on the pygame window using display.update() method of pygame.

Now, let’s see the code displaying image using pygame :

 __

 __  
 __

 __

 __  
 __  
 __

# import pygame module in this program

import pygame

 

# activate the pygame library .

# initiate pygame and give permission

# to use pygame's functionality.

pygame.init()

 

# define the RGB value

# for white colour

white = (255, 255, 255)

 

# assigning values to X and Y variable

X = 400

Y = 400

 

# create the display surface object

# of specific dimension..e(X, Y).

display_surface = pygame.display.set_mode((X, Y ))

 

# set the pygame window name

pygame.display.set_caption('Image')

 

# create a surface object, image is drawn on it.

image = pygame.image.load(r'C:\Users\user\Pictures\geek.jpg')

 

# infinite loop

while True :

 

 # completely fill the surface object

 # with white colour

 display_surface.fill(white)

 

 # copying the image surface object

 # to the display surface object at

 # (0, 0) coordinate.

 display_surface.blit(image, (0, 0))

 

 # iterate over the list of Event objects

 # that was returned by pygame.event.get() method.

 for event in pygame.event.get() :

 

 # if event object type is QUIT

 # then quitting the pygame

 # and program both.

 if event.type == pygame.QUIT :

 

 # deactivates the pygame library

 pygame.quit()

 

 # quit the program.

 quit()

 

 # Draws the surface object to the screen. 

 pygame.display.update() 

   
  
---  
  
__

__

**Output :**  
![output-1](https://media.geeksforgeeks.org/wp-
content/uploads/Screenshot-5414.png)  

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

  
  

  

My Personal Notes _arrow_drop_up_

Save

