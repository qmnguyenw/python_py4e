Colored Flower by circles using Turtle in Python



 **Turtle** is an inbuilt module in Python. It provides drawing using a screen
(cardboard) and turtle (pen). To draw something on the screen, we need to move
the turtle (pen). To move turtle, there are some functions i.e forward(),
backward(), etc.

#### To draw Flower :

> Following steps are used :
>
>   * Import Turtle
>   * Set screen
>   * Make Turtle Object
>   * Define colors used for drawing
>   * Loop to draw circles oriented by angle.
>

Below is the implementation :

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# import turtle package

import turtle

 

# screen object

sc = turtle.Screen() 

 

# turtle object

pen = turtle.Turtle() 

 

 

# Driver Code

# colors

col = ['violet', 'indigo', 'blue', 'green', 

 'yellow', 'orange', 'red']

 

# screen size

sc.setup(500,500) 

 

# screen color

sc.bgcolor('black')

 

# turtle size

pen.pensize(4) 

 

# turtle object

pen.speed(20) 

 

# integer variable 

# for accessing colors

i = 0

 

# loop to draw 30 circles 

for angle in range(0, 360, 12):

 

 # color of circle

 pen.color(col[i]) 

 

 if i == 6: 

 i = 0

 

 else:

 i += 1

 

 # Set the orientation of

 # the turtle to angle

 pen.seth(angle) 

 

 # circle of radius 80

 pen.circle(80) 

 

# hide the turtle

pen.ht()  
  
---  
  
 __

 __

#### Output :

![Coloured flower by circle](https://media.geeksforgeeks.org/wp-
content/uploads/20200622141955/Flower.gif)  

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

  
  

  

My Personal Notes _arrow_drop_up_

Save

