Python Program to find the Quotient and Remainder of two numbers



Given two numbers n and m. The task is to find the quotient and remainder of
two numbers by dividing n by m.

 **Examples:**

    
    
     **Input:**
    n = 10
    m = 3
    **Output:**
    Quotient:  3
    Remainder 1
    
    **Input**
    n = 99
    m = 5
    **Output:**
    Quotient:  19
    Remainder 4
    

**Method 1:** Naive approach

The naive approach is to find the quotient using the double division **(//)**
operator and remainder using the modulus **(%)** operator.

 **Example:**

  

  

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# Python program to find the

# quotient and remainder

 

def find(n, m):

 

 # for quotient

 q = n//m

 print("Quotient: ", q)

 

 # for remainder

 r = n%m

 print("Remainder", r)

 

# Driver Code

find(10, 3)

find(99, 5)  
  
---  
  
 __

 __

 **Output:**

    
    
    Quotient:  3
    Remainder 1
    Quotient:  19
    Remainder 4
    

**Method 2:** Using divmod() method

Divmod() method takes two numbers as parameters and returns the tuple
containing both quotient and remainder.

 **Example:**

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# Python program to find the

# quotient and remainder using

# divmod() method

 

 

q, r = divmod(10, 3)

print("Quotient: ", q)

print("Remainder: ", r)

 

q, r = divmod(99, 5)

print("Quotient: ", q)

print("Remainder: ", r)  
  
---  
  
 __

 __

 **Output:**

    
    
    Quotient:  3
    Remainder 1
    Quotient:  19
    Remainder 4
    

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

