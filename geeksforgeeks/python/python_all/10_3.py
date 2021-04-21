Python program to print the octal value of the numbers from 1 to N



Given a number N, the task is to write a Python program to print the octal
value of the numbers from 1 to N.

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
            10
            11
            12
            13

 **Approach:**

  * We will take the value of N as input.
  * Then, we will run the for loop from 1 to N+1 and traverse each “ **i** ” through oct() function.
  * Print each octal value.

 **Note:** The **oct()** function **** is one of the built-in methods in
Python3. The oct() method takes an integer and returns its octal
representation in a string format.

**Below are the implementations based on the above approach:**

  

  

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# Python program to print the octal value of the

# numbers from 1 to N

 

# Function to find the octal value of the numbers

# in the range 1 to N

def octal_in_range(n):

 

 # For loop traversing from 1 to N (Both Inclusive)

 for i in range(1, n+1):

 

 # Printing octal value of i

 print(oct(i)[2:])

 

 

# Calling the function with input 3

print("Input: 3")

octal_in_range(3)

 

# Calling the function with input 11

print("Input: 11")

octal_in_range(11)  
  
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
    10
    11
    12
    13

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

