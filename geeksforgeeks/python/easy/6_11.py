Create a simple Animation using Turtle in Python



 **Prerequisistes:** Turtle Programming in Python

 **Turtle** is a Python feature like a drawing board, which lets us command a
turtle to draw all over it! We can use functions like turtle.forward(…) and
turtle.right(…) which can move the turtle around. Let’s create a basic
animation where different little turtles race around a track created for them.

### Requirements

  * Turtle Module
  * Random Module

### Approach

  * Firstly, import the required modules.

  * There are different shapes of pointer available in the turtle module(like arrow, classic and turtle). As this is a “Turtle Race”, we need the ‘turtle’ and ‘classic’ shape.
  * We’ll use the classic shape to draw the racing track.
  * List the specs of the first turtle, enter the turtle in the track and set the turtle ready for the race.
  * Do the same for the rest of the turtles.
  * Use the randint() to set the speed of the turtles.

Below is the implementation.

 __

 __  
 __

 __

 __  
 __  
 __

# required modules

from turtle import * from random import randint

 

 

# classic shape turtle

speed(0)

penup()

goto(-140, 140)

 

# racing track

 

for step in range(15):

 write(step, align ='center')

 right(90)

 

 for num in range(8):

 penup()

 forward(10)

 pendown()

 forward(10)

 

 penup()

 backward(160)

 left(90)

 forward(20)

 

# first player details

player_1 = Turtle()

player_1.color('red')

player_1.shape('turtle')

 

# first player proceeds to racing track

player_1.penup()

player_1.goto(-160, 100)

player_1.pendown()

 

# 360 degree turn

for turn in range(10):

 player_1.right(36)

 

# second player details

player_2 = Turtle()

player_2.color('blue')

player_2.shape('turtle')

 

# second player enters in the racing track

player_2.penup()

player_2.goto(-160, 70)

player_2.pendown()

 

# 360 degree turn

for turn in range(72):

 player_2.left(5)

 

# third player details

player_3 = Turtle()

player_3.shape('turtle')

player_3.color('green')

 

# third player enters in the racing track

player_3.penup()

player_3.goto(-160, 40)

player_3.pendown()

 

# 360 degree turn

for turn in range(60):

 player_3.right(6)

 

# fourth player details

player_4 = Turtle()

player_4.shape('turtle')

player_4.color('orange')

 

# fourth player enters in the racing track

player_4.penup()

player_4.goto(-160, 10)

player_4.pendown()

 

# 360 degree turn

for turn in range(30):

 player_4.left(12)

 

# turtles run at random speeds

for turn in range(100):

 player_1.forward(randint(1, 5))

 player_2.forward(randint(1, 5))

 player_3.forward(randint(1, 5))

 player_4.forward(randint(1, 5))  
  
---  
  
 __

 __

 **Output:**

![](https://media.geeksforgeeks.org/wp-content/uploads/20200511155109/gfg-
article-2.png)

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

  
  

  

My Personal Notes _arrow_drop_up_

Save

