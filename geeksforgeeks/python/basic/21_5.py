Python | cmp() function



cmp() method in Python 2.x compares two integers and returns -1, 0, 1
according to comparison.  
cmp() **does not work in python 3.x**. You might want to see list comparison
in Python.

    
    
     **Syntax:**
    cmp(a, b)
    **Parameters:**
    a and b are the two numbers in which the comparison is being done. 
    **Returns:**
    -1 if a<b
    
    0 if a=b
    
    1 if a>b
    

__

__  
__

__

__  
__  
__

# Python program to demonstrate the

# use of cmp() method

 

# when a<b

a = 1

b = 2

print(cmp(a, b)) 

 

# when a = b 

a = 2

b = 2

print(cmp(a, b)) 

 

# when a>b 

a = 3

b = 2

print(cmp(a, b))  
  
---  
  
 __

 __

 **Output:**

    
    
    -1
    0 
    1
    

**Practical Application:** Program to check if a number is even or odd using
cmp function.

Approach: Compare 0 and n%2, if it returns 0, then it is even, else its odd.

Below is the Python implementation of the above program:

  

  

 __

 __  
 __

 __

 __  
 __  
 __

# Python program to check if a number is

# odd or even using cmp function 

 

# check 12 

n = 12

if cmp(0, n % 2): 

 print"odd"

else: 

 print"even"

 

# check 13 

n = 13

if cmp(0, n % 2): 

 print"odd"

else: 

 print"even"  
  
---  
  
__

__

**Output:**

    
    
    even
    odd
    

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

