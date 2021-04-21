Python program to find the gcd of two numbers



Given two numbers. The task is to find the GCD of the two numbers.

 **Using STL :**

In Python, the math module contains a number of mathematical operations, which
can be performed with ease using the module. math.gcd() function compute the
greatest common divisor of 2 numbers mentioned in its arguments.

>  **Syntax:** math.gcd(x, y)
>
>  **Parameter:**
>
>  
>
>
>  
>
>
>  **x** : Non-negative integer whose gcd has to be computed.
>
>  **y** : Non-negative integer whose gcd has to be computed.
>
>  **Returns:** An absolute/positive integer value after calculating the GCD
> of given parameters x and y.
>
>  **Exceptions:** When Both x and y are 0, function returns 0, If any number
> is a character, Type error is raised.

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# Python code to demonstrate the working of gcd()

# importing "math" for mathematical operations

import math

 

# prints 12

print("The gcd of 60 and 48 is : ", end="")

print(math.gcd(60, 48))  
  
---  
  
 __

 __

 **Output**

    
    
    The gcd of 60 and 48 is : 12
    

**Using Recursion :**

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# Python code to demonstrate naive

# method to compute gcd ( recursion )

 

 

def hcf(a, b):

 if(b == 0):

 return a

 else:

 return hcf(b, a % b)

 

a = 60

b = 48

 

# prints 12

print("The gcd of 60 and 48 is : ", end="")

print(hcf(60, 48))  
  
---  
  
 __

 __

 **Output**

    
    
    The gcd of 60 and 48 is : 12
    

**Using Euclidean Algorithm :**

The Euclid’s algorithm (or Euclidean Algorithm) is a method for efficiently
finding the greatest common divisor (GCD) of two numbers. The GCD of two
integers X and Y is the largest number that divides both of X and Y (without
leaving a remainder).

Pseudo Code of the Algorithm-

  1. Let a, b be the two numbers
  2. a mod b = R
  3. Let a = b and b = R
  4. Repeat Steps 2 and 3 until a mod b is greater than 0
  5. GCD = b
  6. Finish

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# Recursive function to return gcd of a and b

def gcd(a, b):

 

 # Everything divides 0

 if (a == 0):

 return b

 if (b == 0):

 return a

 

 # base case

 if (a == b):

 return a

 

 # a is greater

 if (a > b):

 return gcd(a-b, b)

 return gcd(a, b-a)

 

# Driver program to test above function

a = 98

b = 56

if(gcd(a, b)):

 print('GCD of', a, 'and', b, 'is', gcd(a, b))

else:

 print('not found')  
  
---  
  
 __

 __

 **Output**

    
    
    GCD of 98 and 56 is 14
    

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

