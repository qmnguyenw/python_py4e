Creating start Menu in Pygame



 **Pygame** **** is a Python library that can be used specifically to design
and build games. Pygame supports only 2d games that are built using different
shapes or sprites. Pygame doesn’t have an in-built layout design or any in-
built UI system this means there is no easy way to make UI or levels for a
game. The only way to make levels or different menus in pygame is by using
functions.

##

##  **Using Functions As Menus**

 **Functions** in Pygame are a way to contain different menus or levels by
defining an event type in each function, then calling the functions from their
respective container function.

For example, the game function will be called if the player hits the play
button on the start menu. So, the start menu function becomes container
functions for the game function. The important thing to note is that the start
function can’t be called directly from game function. If the game contains
different unlockable levels, then the previous level becomes the container
function for the next level.

 **Sample Code For A Game Containing Start Menu**

Python program to demonstrate Menus And Levels

  

  

## Python

 __

 __  
 __

 __

 __  
 __  
 __

import pygame 

import sys 

 

 

# initializing the constructor 

pygame.init() 

 

# screen resolution 

res = (720,720) 

 

# opens up a window 

screen = pygame.display.set_mode(res) 

 

# white color 

color = (255,255,255) 

 

# light shade of the button 

color_light = (170,170,170) 

 

# dark shade of the button 

color_dark = (100,100,100) 

 

# stores the width of the 

# screen into a variable 

width = screen.get_width() 

 

# stores the height of the 

# screen into a variable 

height = screen.get_height() 

 

# defining a font 

smallfont = pygame.font.SysFont('Corbel',35) 

 

# rendering a text written in 

# this font 

text = smallfont.render('quit' , True , color) 

 

while True: 

 

 for ev in pygame.event.get(): 

 

 if ev.type == pygame.QUIT: 

 pygame.quit() 

 

 #checks if a mouse is clicked 

 if ev.type == pygame.MOUSEBUTTONDOWN: 

 

 #if the mouse is clicked on the 

 # button the game is terminated 

 if width/2 <= mouse[0] <= width/2+140 and
height/2 <= mouse[1] <= height/2+40: 

 pygame.quit() 

 

 # fills the screen with a color 

 screen.fill((60,25,60)) 

 

 # stores the (x,y) coordinates into 

 # the variable as a tuple 

 mouse = pygame.mouse.get_pos() 

 

 # if mouse is hovered on a button it 

 # changes to lighter shade 

 if width/2 <= mouse[0] <= width/2+140 and
height/2 <= mouse[1] <= height/2+40: 


pygame.draw.rect(screen,color_light,[width/2,height/2,140,40])


 

 else: 


pygame.draw.rect(screen,color_dark,[width/2,height/2,140,40])


 

 # superimposing the text onto our button 

 screen.blit(text , (width/2+50,height/2)) 

 

 # updates the frames of the game 

 pygame.display.update()   
  
---  
  
__

__

**Output:**

https://media.geeksforgeeks.org/wp-content/uploads/20200825140241/pygame-
window-2020-08-25-13-58-26_770T9JQ7.compressed.mp4

  

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

