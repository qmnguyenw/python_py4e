Python – Integers String to Integer List



Given a Integers String, composed of negative and positive numbers, convert to
integer list.

>  **Input** : test_str = ‘4 5 -3 2 -100 -2’  
>  **Output** : [4, 5, -3, 2, -100, -2]  
>  **Explanation** : Negative and positive string numbers converted to
> integers list.
>
>  **Input** : test_str = ‘-4 -5 -3 2 -100 -2’  
>  **Output** : [-4, -5, -3, 2, -100, -2]  
>  **Explanation** : Negative and positive string numbers converted to
> integers list.

 **Method #1 : Using list comprehension + int() + split()**

In this, we split integers using split() and int() is used to integral
conversion. Elements inserted in List using list comprehension

  

  

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Integers String to Integer List

# Using list comprehension + int() + split()

import string

 

# initializing string

test_str = '4 5 -3 2 -100 -2 -4 9'

 

# printing original string

print("The original string is : " + str(test_str))

 

# int() converts to required integers

res = [int(ele) for ele in test_str.split()]

 

# printing result 

print("Converted Integers : " + str(res))   
  
---  
  
__

__

**Output**

    
    
    The original string is : 4 5 -3 2 -100 -2 -4 9
    Converted Integers : [4, 5, -3, 2, -100, -2, -4, 9]
    

**Method #2 : Using map() + int()**

In this, the task of extension of logic of integer conversion is done using
map().

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Integers String to Integer List

# Using map() + int()

import string

 

# initializing string

test_str = '4 5 -3 2 -100 -2 -4 9'

 

# printing original string

print("The original string is : " + str(test_str))

 

# int() converts to required integers

# map() extends logic of int to each split

res = list(map(int, test_str.split()))

 

# printing result 

print("Converted Integers : " + str(res))   
  
---  
  
__

__

**Output**

    
    
    The original string is : 4 5 -3 2 -100 -2 -4 9
    Converted Integers : [4, 5, -3, 2, -100, -2, -4, 9]
    

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

