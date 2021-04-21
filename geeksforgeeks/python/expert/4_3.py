How to draw 2-layered and colored spider web in Python using Turtle Module?



 **Prerequisite:** **Python Turtle module Basics**

We all must have seen the spiderweb at our homes but have you ever wonder how
many efforts and patience is required for building that. Let’s salute the
efforts of Spider and continue building one by ourselves. Spiderwebs usually
comprise radical and spiral threads. What if you can make a colored 2-layered
spiderweb. Here is a simple tutorial.

 **Approach used :**

The turtle is moved back and forth to build the radical threads first. The
turtle is rotated by an angle of 60 degrees to draw each radical thread. The
length of the spiral thread is set to 50 and reduced by 10 at each iteration.
The inner loop is concerned with building single spiral thread and the
layering of the web, while the outer loop controls the number of spirals to be
built.

## Python3

  

  

 __

 __  
 __

 __

 __  
 __  
 __

import turtle as t

 

# define turtle speed

t.speed(2)

 

# radical thread 

for i in range(6):

 t.forward(100)

 t.backward(100)

 t.right(60)

 

# spiral thread length

side = 50

 

# Spider web color

t.fillcolor("Yellow")

 

# building web

t.begin_fill()

 

for i in range(10):

 t.penup()

 t.goto(0, 0)

 t.pendown()

 t.setheading(0)

 t.forward(side)

 t.right(120)

 

 for j in range(6):

 t.forward(side-2)

 t.right(60)

 side = side - 10

 

t.end_fill()  
  
---  
  
 __

 __

