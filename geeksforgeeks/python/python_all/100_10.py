Python – K Matrix Initialization



Sometimes in the world of competitive programming, we need to initialise the
matrix, but we don’t wish to do it in a longer way using a loop. We need a
shorthand for this. This type of problem is quite common in dynamic
programming domain. Let’s discuss certain ways in which this can be done.

 **Method #1 : Using List comprehension**  
List comprehension can be treated as a shorthand for performing this
particular operation. In list comprehension, we can initialise the inner list
with K and then extend this logic to each row again using the list
comprehension.

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate

# K Matrix Initialization 

# using list comprehension

 

# Declaring rows

N = 5

 

# Declaring columns

M = 4

 

# initializing K 

K = 7

 

# using list comprehension 

# to initializing matrix

res = [ [ K for i in range(N) ] for j in range(M) ]

 

# printing result 

print("The matrix after initializing with K : " + str(res))  
  
---  
  
 __

 __

 **Output :**

    
    
    The matrix after initializing with K : [[7, 7, 7, 7, 7], [7, 7, 7, 7, 7], [7, 7, 7, 7, 7], [7, 7, 7, 7, 7]]
    

**Method #2 : Using list comprehension + “*” operator**  
This problem can also be simplified using the * operator which can slightly
reduce the tedious way task is done and can simply use multiply operator to
extent the initialization to all N rows.

  

  

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate

# K Matrix Initialization 

# using list comprehension

# and * operator

 

# Declaring rows

N = 5

 

# Declaring columns

M = 4

 

# initializing K

K = 7

 

# using list comprehension 

# to initializing matrix

res = [ [K for i in range(M)] * N]

 

# printing result 

print("The matrix after initializing with K : " + str(res))  
  
---  
  
 __

 __

 **Output :**

    
    
    The matrix after initializing with K : [[7, 7, 7, 7, 7], [7, 7, 7, 7, 7], [7, 7, 7, 7, 7], [7, 7, 7, 7, 7]]
    

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

