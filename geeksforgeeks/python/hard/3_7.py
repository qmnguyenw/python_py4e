Snowfall display using Pygame in Python



Not everybody must have witnessed Snowfall personally but wait a minute, What
if you can see the snowfall right on your screen by just a few lines of
creativity and Programming.

Before starting the topic, it is highly recommended revising the basics of
Pygame.

## Steps for snowfall creation

 **1\. Importing modules**

First, we need to import the Pygame module by using the command.

> import pygame  
>
>
>  
>
>
>  
>

Also, along with Pygame, we will also need random module. Python has a built-
in module that you can use to make random numbers just by importing random
module.

> import random  
>

**2\. Initialize the game engine**

It simply means choose the colors you want to use. In programming World,
Whatever you can think you can make. At the end of the article , you will find
green snowfall on the white background.

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# initialize

pygame.init()

 

# choosen colours will be used

# to display the output

WHITE = [255, 255, 255]

GREEN = [0, 255, 0]  
  
---  
  
 __

 __

 **3\. Specify the size of the screen**

 **** It can be a new number depending upon the resolution of your system.

## Python3

  

  

 __

 __  
 __

 __

 __  
 __  
 __

# specify the size

 

SIZE = [400, 400]

screen = pygame.display.set_mode(SIZE)  
  
---  
  
 __

 __

