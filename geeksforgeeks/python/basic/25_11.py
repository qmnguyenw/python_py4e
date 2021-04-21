factorial() in Python



Not many people know, but python offers a direct function that can compute the
factorial of a number without writing the whole code for computing factorial.

 **Naive method to compute factorial**

 __

 __  
 __

 __

 __  
 __  
 __

# Python code to demonstrate naive method

# to compute factorial

n = 23

fact = 1

 

for i in range(1,n+1):

 fact = fact * i

 

print ("The factorial of 23 is : ",end="")

print (fact)  
  
---  
  
 __

 __

Output :

    
    
    The factorial of 23 is : 25852016738884976640000
    

**Using math.factorial()**

This method is defined in “ **math** ” module of python. Because it has C type
internal implementation, it is fast.

  

  

    
    
    **math.factorial(x)**
    **Parameters :**
    **x :** The number whose factorial has to be computed.
    **Return value :**
    Returns the factorial of desired number.
    **Exceptions :**
    Raises Value error if number is **negative or non-integral.**
    

__

__  
__

__

__  
__  
__

# Python code to demonstrate math.factorial()

import math

 

print ("The factorial of 23 is : ", end="")

print (math.factorial(23))  
  
---  
  
 __

 __

Output :

    
    
    The factorial of 23 is : 25852016738884976640000
    

**Exceptions in math.factorial()**

  *  **If give number is Negative :**

 __

 __  
 __

 __

 __  
 __  
 __

# Python code to demonstrate math.factorial()

# Exceptions ( negative number )

 

import math

 

print ("The factorial of -5 is : ",end="")

 

# raises exception

print (math.factorial(-5))  
  
---  
  
 __

 __

Output :

    
    
    The factorial of -5 is : 
    

Runtime Error :

    
    
    Traceback (most recent call last):
      File "/home/f29a45b132fac802d76b5817dfaeb137.py", line 9, in 
        print (math.factorial(-5))
    ValueError: factorial() not defined for negative values
    

  * **If given number is Non – Integral Value :**

 __

 __  
 __

 __

 __  
 __  
 __

# Python code to demonstrate math.factorial()

# Exceptions ( Non-Integral number )

 

import math

 

print ("The factorial of 5.6 is : ",end="")

 

# raises exception

print (math.factorial(5.6))  
  
---  
  
 __

 __

Output :

    
    
    The factorial of 5.6 is : 
    

Runtime Error :

    
    
    Traceback (most recent call last):
      File "/home/3987966b8ca9cbde2904ad47dfdec124.py", line 9, in 
        print (math.factorial(5.6))
    ValueError: factorial() only accepts integral values
    

This article is contributed by **Manjeet Singh**. If you like GeeksforGeeks
and would like to contribute, you can also write an article using
contribute.geeksforgeeks.org or mail your article to
contribute@geeksforgeeks.org. See your article appearing on the GeeksforGeeks
main page and help other Geeks.

Please write comments if you find anything incorrect, or you want to share
more information about the topic discussed above.

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

