Python program to display half diamond pattern of numbers with star border



Given a number n, the task is to write a Python program to print a half
diamond pattern of numbers with a star border.

 **Examples:**

    
    
     **Input: n = 5**
    **Output:**
    
    *
    *1*
    *121*
    *12321*
    *1234321*
    *123454321*
    *1234321*
    *12321*
    *121*
    *1*
    *
    
    
    **Input: n = 3**
    **Output:**
    
    *
    *1*
    *121*
    *12321*
    *121*
    *1*
    *

 **Approach:**

  * Two for loops will be run in this program in order to print the numbers as well as stars.
  * First print * and then run for loop from 1 to (n+1) to print up to the rows in ascending order.
  * In this particular for loop * will be printed up to i and then one more for loop will run from 1 to i+1 in order to print the numbers in ascending order.
  * Now one more loop will run from i-1 to 0 in order to print the number in the reverse order.
  * Now one star will be printed and this for loop will end.
  * Now second for loop will run from n-1 to 0 to print the pattern as in the middle in which the numbers are in a reverse manner.
  * In this for loop also the same work will be done as in first for loop.
  * The required pattern will be displayed.

 **Below is the implementation of the above pattern:**

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# function to display the pattern up to n

def display(n): 

 

 print("*")

 

 for i in range(1, n+1):

 print("*", end="")

 

 # for loop to display number up to i

 for j in range(1, i+1): 

 print(j, end="")

 

 # for loop to display number in reverse direction 

 for j in range(i-1, 0, -1): 

 print(j, end="")

 

 print("*", end="")

 print()

 

 # for loop to display i in reverse direction

 for i in range(n-1, 0, -1):

 print("*", end="")

 for j in range(1, i+1):

 print(j, end="")

 

 for j in range(i-1, 0, -1):

 print(j, end="")

 

 print("*", end="")

 print()

 

 print("*")

 

 

# driver code

n = 5

print('\nFor n =', n)

display(n)

 

n = 3

print('\nFor n =', n)

display(n)  
  
---  
  
 __

 __

 **Output:**

    
    
    For n = 5
    *
    *1*
    *121*
    *12321*
    *1234321*
    *123454321*
    *1234321*
    *12321*
    *121*
    *1*
    *
    
    For n = 3
    *
    *1*
    *121*
    *12321*
    *121*
    *1*
    *

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

  
  

  

My Personal Notes _arrow_drop_up_

Save

