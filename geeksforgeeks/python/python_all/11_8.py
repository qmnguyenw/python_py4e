Python program to print the hexadecimal value of the numbers from 1 to N



Given a number N, the task is to write a Python program to print the
hexadecimal value of the numbers from 1 to N.

 **Examples:**

    
    
     **Input:** 3
    **Output:** 1
            2
            3
    
    **Input:** 11
    **Output:** 1
            2
            3
            4
            5
            6
            7
            8
            9
            a
            b

 **Approach:**

  * We will take the value of N as input.
  * Then, we will run the for loop from 1 to N+1 and traverse each “ **i** ” through hex() function.
  * Print each hexadecimal value.

 **Note:** The **hex()** function is one of the built-in functions in Python3,
which is used to convert an integer number into its corresponding hexadecimal
form.

 **Below are the implementations based on the above approach:**

  

  

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# Python program to print the hexadecimal value of the

# numbers from 1 to N

 

# Function to find the hexadecimal value of the numbers

# in the range 1 to N

def hex_in_range(n):

 

 # For loop traversing from 1 to N (Both Inclusive)

 for i in range(1, n+1):

 

 # Printing hexadecimal value of i

 print(hex(i)[2:])

 

# Calling the function with input 3

print("Input: 3")

hex_in_range(3)

 

# Calling the function with input 11

print("Input: 11")

hex_in_range(11)  
  
---  
  
 __

 __

 **Output:**

    
    
    Input: 3
    1
    2
    3
    Input: 11
    1
    2
    3
    4
    5
    6
    7
    8
    9
    a
    b

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

