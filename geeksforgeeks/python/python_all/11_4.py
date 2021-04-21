Python profram to calculate square of a given number



Given a number, the task is to write a Python program to calculate square of
the given number.

 **Examples:**

    
    
     **Input:** 4
    **Output:** 16
    
    **Input:** 3
    **Output:** 9
    
    **Input:** 10
    **Output:** 100

We will provide the number, and we will get the square of that number as
output. We have three ways to do so:

  * Multiplying the number to get the square **(N * N)**
  * Using Exponent Operator
  * Using math.pow() Method

 **Method 1: Multiplication**

In this approach, we will multiply the number with one another to get the
square of the number.

  

  

 **Example:**

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# Declaring the number.

n = 4

 

# Finding square by multiplying them

# with each other

square = n * n

 

# Printing square

print(square)  
  
---  
  
 __

 __

 **Output:**

    
    
    16

 **Method 2: Using Exponent Operator**

In this approach, we use the exponent operator to find the square of the
number.

>  **Exponent Operator:** **
>
>  **Return:** a ** b will return a raised to power b as output.

 **Example:**

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# Declaring the number.

n = 4

 

# Finding square by using exponent operator

# This will yield n power 2 i.e. square of n

square = n ** 2

 

# Printing square

print(square)  
  
---  
  
 __

 __

 **Output:**

  

  

    
    
    16

 **Method 3: Using pow() Method**

In this approach, we will use the pow() method to find the square of the
number. This function computes x**y and returns a float value as output.

>  **Syntax:** float pow(x,y)
>
>  **Parameters :**
>
>  **x :** Number whose power has to be calculated.
>
>  **y :** Value raised to compute power.  
>
>
> **Return Value :**  
>  Returns the value x**y in float.

 **Example:**

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# Declaring the number.

n = 4

 

# Finding square by using pow method

# This will yield n power 2 i.e. square of n

square = pow(n, 2)

 

# Printing square

print(square)  
  
---  
  
 __

 __

 **Output:**

    
    
    16.0

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

