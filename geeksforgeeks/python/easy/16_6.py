Introduction to pygame



Game programming is very rewarding nowadays and it can also be used in
advertising and as a teaching tool too. Game development includes mathematics,
logic, physics, AI, and much more and it can be amazingly fun. In python, game
programming is done in pygame and it is one of the best modules for doing so.  

**Installing pygame:**  
Pygame requires Python; if you don’t already have it, you can download it from
python.org. Use python 3.6.1 or greater, because it is much friendlier to
newbies, and additionally runs faster.  
The best way to install pygame is with the pip tool (which python uses to
install packages). Note, this comes with python in recent versions. We use the
–user flag to tell it to install into the home directory, rather than
globally.  

    
    
    python3 -m pip install -U pygame --user
    
    
    

To see if it works, run one of the included examples:  

    
    
    python3 -m pygame.examples.aliens
    
    
    

If it works, we are ready to go!  
Once you have installed pygame, you’re ready to create your very first pygame
instance.  

## Python3

  

  

 __

 __  
 __

 __

 __  
 __  
 __

# import the pygame module

import pygame

# import pygame.locals for easier

# access to key coordinates

from pygame.locals import *

# Define our square object and call super to

# give it all the properties and methods of pygame.sprite.Sprite

# Define the class for our square objects

class Square(pygame.sprite.Sprite):

 def __init__(self):

 super(Square, self).__init__()

 

 # Define the dimension of the surface

 # Here we are making squares of side 25px

 self.surf = pygame.Surface((25, 25))

 

 # Define the color of the surface using RGB color coding.

 self.surf.fill((0, 200, 255))

 self.rect = self.surf.get_rect()

# initialize pygame

pygame.init()

# Define the dimensions of screen object

screen = pygame.display.set_mode((800, 600))

# instantiate all square objects

square1 = Square()

square2 = Square()

square3 = Square()

square4 = Square()

# Variable to keep our game loop running

gameOn = True

# Our game loop

while gameOn:

 # for loop through the event queue

 for event in pygame.event.get():

 

 # Check for KEYDOWN event

 if event.type == KEYDOWN:

 

 # If the Backspace key has been pressed set

 # running to false to exit the main loop

 if event.key == K_BACKSPACE:

 gameOn = False

 

 # Check for QUIT event

 elif event.type == QUIT:

 gameOn = False

 # Define where the squares will appear on the screen

 # Use blit to draw them on the screen surface

 screen.blit(square1.surf, (40, 40))

 screen.blit(square2.surf, (40, 530))

 screen.blit(square3.surf, (730, 40))

 screen.blit(square4.surf, (730, 530))

 # Update the display using flip

 pygame.display.flip()  
  
---  
  
 __

 __

