uniform() method in Python Random module



uniform() is a method specified in the random library in Python 3.  

Nowadays, in general, day-day tasks, there’s always the need to generate
random numbers in a range. Normal programming constructs require a method more
than just one word to achieve this particular task. In python, there’s an
inbuilt method, “ **uniform()** ” which performs this task with ease and using
just the one word. This method is defined in “ **random** ” module

> Syntax : **uniform(int x, int y)**
>
>  **Parameters :**  
>  **x** Specifies the lower limit of the random number required to generate.  
>  **y** Specifies the upper limit of the random number required to generate.
>
>  **Returns :** Returns the generated floating point random number between
> lower limit and upper limit
>
>  
>
>
>  
>

  
**Code #1 :** Code to generate float random number.

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate

# the working of uniform()

 

# for using uniform()

import random

 

# initializing bounds 

a = 4

b = 9

 

# printing the random number

print("The random number generated between 4 and 9 is : ", end
="")

print(random.uniform(a, b))  
  
---  
  
 __

 __

Output:

    
    
    The random number generated between 4 and 9 is : 7.494931618830411
    

**Application :**  
There are many possible applications that can be thought of this function,
some of the notable being generating random numbers in casino games, for
lottery or custom games.  
Below is the game that decided the winner on the basis of closeness to a
certain value.

  
**Code #2 :** Application of uniform() – A Game

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate

# the application of uniform()

 

# for using uniform()

import random, math

 

# initializing player numbers

player1 = 4.50

player2 = 3.78

player3 = 6.54

 

# generating winner random number

winner = random.uniform(2, 9)

 

# finding closest 

diffa = math.fabs(winner - player1)

diffb = math.fabs(winner - player2)

diffc = math.fabs(winner - player3)

 

# printing winner

if(diffa < diffb and diffa < diffc):

 print("The winner of game is : ", end ="")

 print("Player1")

 

if(diffb < diffc and diffb < diffa):

 print("The winner of game is : ", end ="")

 print("Player2")

 

if(diffc < diffb and diffc < diffa):

 print("The winner of game is : ", end ="")

 print("Player3")  
  
---  
  
 __

 __

Output:

    
    
    The winner of game is : Player2
    

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

