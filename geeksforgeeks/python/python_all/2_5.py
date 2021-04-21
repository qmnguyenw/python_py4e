Python Program to Get K initial powers of N



Given size K and value N, the task is to write a Python Program to compute a
list of powers of N till K.

    
    
     **Input :** N = 4, K = 6
    **Output :** [1, 4, 16, 64, 256, 1024]
    **Explanation :** 4^i is output till i = K. 
    
    **Input :** N = 3, K = 6
    **Output :** [1, 3, 9, 27, 81, 243]
    **Explanation :** 3^i is output till i = K. 

**Method #1 : Using** **list comprehension** **\+ ** operator**

In this, the values are incremented till K using list comprehension and ** is
used to get required power of numbers.

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Get K initial powers of N

# Using list comprehension + ** operator

 

# initializing N

N = 4

 

# printing original list

print("The original N is : " + str(N))

 

# initializing K 

K = 6

 

# list comprehension provides shorthand for problem

res = [N ** idx for idx in range(0, K)]

 

# printing result

print("Square values of N till K : " + str(res))  
  
---  
  
 __

 __

 **Output:**

    
    
    The original N is : 4
    Square values of N till K : [1, 4, 16, 64, 256, 1024]

 **Method #2 : Using** **pow()** **+** **list comprehension** ****

  

  

In this, we perform the task of computing power using pow(), the rest of all
the functions are performed using list comprehension.

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Get K initial powers of N

# Using pow() + list comprehension 

from math import pow

 

# initializing N

N = 4

 

# printing original list

print("The original N is : " + str(N))

 

# initializing K 

K = 6

 

# list comprehension provides shorthand for problem

# squaring using pow()

res = [int(pow(N, idx)) for idx in range(0, K)]

 

# printing result

print("Square values of N till K : " + str(res))  
  
---  
  
 __

 __

 **Output:**

    
    
    The original N is : 4
    Square values of N till K : [1, 4, 16, 64, 256, 1024]

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

