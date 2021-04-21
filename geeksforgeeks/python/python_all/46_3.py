Python Program to Check Whether a Number is Positive or Negative or zero



Given a number. The task is to check whether the number is positive or
negative or zero.

 **Examples:**

    
    
     **Input:** 5
    **Output:** Positive
    
    **Input:** -5
    **Output:** Negative
    

**Approach:**

We will use the if-elif statements in Python. We will check whether the number
is greater than zero or smaller than zero or equal to zero.

Below is the implementation.

  

  

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# Python program to check whether

# the number is positive, negative

# or equal to zero

 

def check(n):

 

 # if the number is positive

 if n > 0:

 print("Positive")

 

 # if the number is negative

 elif n < 0:

 print("Negative")

 

 # if the number is equal to

 # zero

 else:

 print("Equal to zero")

 

# Driver Code

check(5)

check(0)

check(-5)  
  
---  
  
 __

 __

 **Output:**

    
    
    Positive
    Equal to zero
    Negative
    

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

