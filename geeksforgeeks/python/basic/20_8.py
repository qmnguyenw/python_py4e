randint() Function in Python



 ** _randint()_** is an inbuilt function of the _random module_ in Python3.
The random module gives access to various useful functions and one of them
being able to generate random numbers, which is _randint()_.  
  
 **Syntax :**

    
    
    randint(start, end)

 **Parameters :**

    
    
     **(start, end) :** Both of them must be integer type values.

 **Returns :**

    
    
    A random integer in range [start, end] including the end points.

 **Errors and Exceptions :**

    
    
    **ValueError :** Returns a ValueError when floating
                 point values are passed as parameters.
    
    **TypeError :** Returns a TypeError when anything other than 
                numeric values are passed as parameters.

  
**Code #1 :**

  

  

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 program explaining work

# of randint() function

 

# imports random module

import random

 

# Generates a random number between

# a given positive range

r1 = random.randint(0, 10)

print("Random number between 0 and 10 is % s" % (r1))

 

# Generates a random number between 

# two given negative range

r2 = random.randint(-10, -1)

print("Random number between -10 and -1 is % d" % (r2))

 

# Generates a random number between 

# a positive and a negative range

r3 = random.randint(-5, 5)

print("Random number between -5 and 5 is % d" % (r3))  
  
---  
  
 __

 __

 **Output :**

    
    
    Random number between 0 and 10 is 5
    Random number between -10 and -1 is -7
    Random number between -5 and 5 is 2
    

  
**Code #2 :** Program demonstrating the ValueError.

 __

 __  
 __

 __

 __  
 __  
 __

# imports random module

import random

 

'''If we pass floating point values as

parameters in the randint() function'''

 

r1 = random.randint(1.23, 9.34)

print(r1)  
  
---  
  
 __

 __

 **Output :**

    
    
    Traceback (most recent call last):
      File "/home/f813370b9ea61dd5d55d7dadc8ed5171.py", line 6, in 
        r1=random.randint(1.23, 9.34)
      File "/usr/lib/python3.5/random.py", line 218, in randint
        return self.randrange(a, b+1)
      File "/usr/lib/python3.5/random.py", line 182, in randrange
        raise ValueError("non-integer arg 1 for randrange()")
    ValueError: non-integer arg 1 for randrange()
    

  
**Code #3 :** Program demonstrating the TypeError.

 __

 __  
 __

 __

 __  
 __  
 __

# imports random

import random

 

'''If we pass string or character literals as

parameters in the randint() function'''

 

r2 = random.randint('a', 'z')

print(r2)  
  
---  
  
 __

 __

 **Output :**

    
    
    Traceback (most recent call last):
      File "/home/fb805b21fea0e29c6a65f62b99998953.py", line 5, in 
        r2=random.randint('a', 'z')
      File "/usr/lib/python3.5/random.py", line 218, in randint
        return self.randrange(a, b+1)
    TypeError: Can't convert 'int' object to str implicitly
    

  
**Applications :**

The randint() function can be used to simulate a lucky draw situation.

Let’s say User has participated in a lucky draw competition. The user gets
three chances to guess the number between 1 and 10. If guess is correct user
wins, else loses the competition.

 __

 __  
 __

 __

 __  
 __  
 __

# importing randint function

# from random module

from random import randint

 

# Function which generates a new 

# random number everytime it executes

def generator():

 return randint(1, 10)

 

# Function takes user input and returns

# true or false depending whether the

# user wins the lucky draw!

def rand_guess():

 

 # calls generator() which returns a

 # random integer between 1 and 10

 random_number = generator()

 

 # defining the number of

 # guesses the user gets

 guess_left = 3

 

 # Setting a flag variable to check

 # the win-condition for user

 flag = 0

 

 # looping the number of times

 # the user gets chances

 while guess_left > 0:

 

 # Taking a input from the user

 guess = int(input("Pick your number to "

 "enter the lucky draw\n"))

 

 # checking whether user's guess

 # matches the generated win-condition

 if guess == random_number:

 

 # setting flag as 1 if user guessses 

 # correctly and then loop is broken

 flag = 1

 break

 

 else:

 

 # If user's choice doesn't match

 # win-condition then it is printed

 print("Wrong Guess!!")

 

 # Decrementing number of 

 # guesses left by 1 

 guess_left -= 1

 

 # If win-condition is satisfied then,

 # the function rand_guess returns True

 if flag is 1:

 return True

 

 # Else the function returns False

 else:

 return False

 

# Driver code

if __name__ == '__main__':

 if rand_guess() is True:

 print("Congrats!! You Win.")

 else :

 print("Sorry, You Lost!")  
  
---  
  
 __

 __

 **Output :**

    
    
    Pick your number to enter the lucky draw
    8
    Wrong Guess!!
    Pick your number to enter the lucky draw
    9
    Wrong Guess!!
    Pick your number to enter the lucky draw
    0
    Congrats!! You Win.
    

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

