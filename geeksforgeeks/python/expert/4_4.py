Flipping Tiles (memory game) using Python3



Flipping tiles game can be played to test our memory. In this, we have a
certain even number of tiles, in which each number/figure has a pair. The
tiles are facing downwards, and we have to flip them to see them. In a turn,
one flips 2 tiles, if the tiles match then they are removed. If not then they
are flipped and placed back in the position. We keep on doing this until all
the tiles have been matched and removed.

To simulate this game in Python, we will be using the **turtle** and random
**modules**.

 **Approach:**

  1. Import turtle and random module. Python offers the random module that can generate random numbers, and turtle module is being used in making different objects.
  2. Set the screen and also choose the background color of your output screen window.
  3. Define a function for making a square for the base of your game.
  4. Define a function to keep a check of the index number.
  5. Define a function to make your game user-friendly i.e user click.
  6. Write a function to draw tiles on the square base defined in step 3.
  7. Finally use the shuffle() function to shuffle the numbers placed on the square tiles in the square box.

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# import modules

from random import *

from turtle import *

 

# set the screen

screen = Screen()

 

#choose background color

screen.bgcolor("yellow")

 

# define the function

# for creating a square section

# for the game

def Square(x, y):

 up()

 goto(x, y)

 down()

 color('white', 'green')

 begin_fill()

 for count in range(4):

 forward(50)

 left(90)

 end_fill()

 

# define functionn to

# keep a check of index number

def Numbering(x, y):

 return int((x + 200) // 50 + ((y + 200) //
50) * 8)

 

# define function

def Coordinates(count):

 return (count % 8) * 50 - 200, (count // 8) *
50 - 200

 

# define function

# to make it interactive 

# user click

def click(x, y):

 spot = Numbering(x, y)

 mark = state['mark']

 

 if mark is None or mark == spot or tiles[mark] !=
tiles[spot]:

 state['mark'] = spot

 else:

 hide[spot] = False

 hide[mark] = False

 state['mark'] = None

 

def draw():

 clear()

 goto(0, 0)

 stamp()

 

 for count in range(64):

 if hide[count]:

 x, y = Coordinates(count)

 Square(x, y)

 

 mark = state['mark']

 

 if mark is not None and hide[mark]:

 x, y = Coordinates(mark)

 up()

 goto(x + 2, y)

 color('black')

 write(tiles[mark], font=('Arial', 30, 'normal'))

 

 update()

 ontimer(draw, 10)

 

tiles = list(range(32)) * 2

state = {'mark': None}

hide = [True] * 64

 

# for shuffling the

# numbers placed inside 

# the square tiles

shuffle(tiles)

tracer(False)

onscreenclick(click)

draw()

done()  
  
---  
  
 __

 __

 **Output:**

  

  

https://media.geeksforgeeks.org/wp-content/uploads/20200915143723/Test-Your-
memory.mp4

  

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

