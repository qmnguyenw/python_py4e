Sorting algorithm visualization : Insertion Sort



An algorithm like Insertion Sort can be understood easily by visualizing. In
this article, a program that visualizes the Insertion Sort Algorithm has been
implemented.  
The Graphical User Interface(GUI) is implemented in python using pygame
library.  
 **Approach:**

  * Generate random array and fill the pygame window with bars. Bars are straight vertical lines, which represents array elements.
  * Set all bars to green color (unsorted).
  * Use **pygame.time.delay()** to slow down the algorithm, so that we can see the sorting process.
  * Implement a timer to see how the algorithm performs.
  * The actions are performed using ‘pygame.event.get()’ method, which stores all the events which user performs, such as start, reset.
  * Blue color is used to highlight bars that are involved in sorting at a paticular time.
  * Orange color highlights the bars sorted.

 **Observations:**  
We can clearly see from the Insertion Sort visualization, that insertion Sort
is very slow compared to other sorting algorithms like Mergesort or Quicksort.  
 **Examples:**

>  **Input:**  
>  Press “Enter” key to Perform Visualization.  
> Press “R” key to generate new array.  
>  **Output:**  
>  **Initial:**  
> ![](https://media.geeksforgeeks.org/wp-
> content/uploads/20200622003316/Screenshot-from-2020-06-22-00-27-42.png)  
>  **Sorting:**  
> ![](https://media.geeksforgeeks.org/wp-
> content/uploads/20200622003313/Screenshot-from-2020-06-22-00-28-06.png)  
>  **Final:**  
> ![](https://media.geeksforgeeks.org/wp-
> content/uploads/20200622003311/Screenshot-from-2020-06-22-00-29-56.png)

Please make sure to install the pygame library before running the below
program.

Below is the implementation of the above visualizer:

## Python

 __

 __  
 __

 __

 __  
 __  
 __

# Python implementation of the

# Sorting visualiser: Insertion Sort 

 

# Imports

import pygame

import random

import time

pygame.font.init()

startTime = time.time()

# Total window

screen = pygame.display.set_mode(

 (900, 650)

 )

 

# Title and Icon 

pygame.display.set_caption(

 "SORTING VISUALISER"

 )

 

# Uncomment below lines for setting 

# up the icon for the visuliser

# img = pygame.image.load('sorticon.png')

# pygame.display.set_icon(img)

 

# Boolean variable to run 

# the program in while loop

run = True

 

# Window size and some initials

width = 900

length = 600

array =[0]*151

arr_clr =[(0, 204, 102)]*151

clr_ind = 0

clr =[(0, 204, 102), (255, 0, 0), \

 (0, 0, 153), (255, 102, 0)]

fnt = pygame.font.SysFont("comicsans", 30)

fnt1 = pygame.font.SysFont("comicsans", 20)

 

# Function to generate new Array

def generate_arr():

 for i in range(1, 151):

 arr_clr[i]= clr[0]

 array[i]= random.randrange(1, 100)

 

# Initially generate a array

generate_arr() 

 

# Function to refill the 

# updates on the window 

def refill():

 screen.fill((255, 255, 255))

 draw()

 pygame.display.update()

 pygame.time.delay(10)

 

# Sorting Algorithm: Insertion sort

def insertionSort(array):

 

 for i in range(1, len(array)):

 pygame.event.pump() 

 refill()

 key = array[i]

 arr_clr[i]= clr[2]

 j = i-1

 while j>= 0 and key<array[j]:

 arr_clr[j]= clr[2]

 array[j + 1]= array[j]

 refill()

 arr_clr[j]= clr[3]

 j = j-1

 array[j + 1]= key 

 refill()

 arr_clr[i]= clr[0]

 

# Function to Draw the array values

def draw():

 # Text should be rendered

 txt = fnt.render("SORT: PRESS 'ENTER'", \

 1, (0, 0, 0))

 # Position where text is placed

 screen.blit(txt, (20, 20))

 txt1 = fnt.render("NEW ARRAY: PRESS 'R'", \

 1, (0, 0, 0))

 screen.blit(txt1, (20, 40))

 txt2 = fnt1.render("ALGORITHM USED:"\

 "INSERTION SORT", 1, (0, 0, 0))

 screen.blit(txt2, (600, 60))

 text3 = fnt1.render("Running Time(sec): "+\

 str(int(time.time() - startTime)), \

 1, (0, 0, 0))

 screen.blit(text3, (600, 20))

 element_width =(width-150)//150

 boundry_arr = 900 / 150

 boundry_grp = 550 / 100

 pygame.draw.line(screen, (0, 0, 0), (0, 95), \

 (900, 95), 6)

 

 # Drawing the array values as lines

 for i in range(1, 151):

 pygame.draw.line(screen, arr_clr[i], \

 (boundry_arr * i-3, 100), \

 (boundry_arr * i-3, \

 array[i]*boundry_grp + 100), element_width)

 

# Program should be run 

# continuously to keep the window open

while run:

 # background

 screen.fill((255, 255, 255))

 

 # Event handler stores all event 

 for event in pygame.event.get():

 

 # If we click Close button in window

 if event.type == pygame.QUIT:

 run = False

 if event.type == pygame.KEYDOWN:

 if event.key == pygame.K_r:

 generate_arr() 

 if event.key == pygame.K_RETURN:

 insertionSort(array) 

 draw()

 pygame.display.update()

 

pygame.quit()  
  
---  
  
 __

 __

  
 **Output:**  

https://media.geeksforgeeks.org/wp-content/cdn-
uploads/20200623001915/visualiser16-2020-06-23_00.14.17.mp4

Attention reader! Don’t stop learning now. Get hold of all the important DSA
concepts with the **DSA Self Paced Course** at a student-friendly price and
become industry ready. To complete your preparation from learning a language
to DS Algo and many more, please refer **Complete Interview Preparation
Course** **.**

  
  

  

My Personal Notes _arrow_drop_up_

Save

