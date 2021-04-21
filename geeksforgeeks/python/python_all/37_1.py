Python – Convert Binary tuple to Integer



Given Binary Tuple representing binary representation of number, convert to
integer.

>  **Input** : test_tup = (1, 1, 0)  
>  **Output** : 6  
>  **Explanation** : 4 + 2 = 6.
>
>  **Input** : test_tup = (1, 1, 1)  
>  **Output** : 7  
>  **Explanation** : 4 + 2 + 1 = 7.

 **Method #1 : Using join() + list comprehension + int()**

In this, we concatenate the binary tuples in string format using join() and
str(), then convert to integer by mentioning base as 2.

  

  

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Convert Binary tuple to Integer

# Using join() + list comprehension + int()

 

# initializing tuple

test_tup = (1, 1, 0, 1, 0, 0, 1)

 

# printing original tuple

print("The original tuple is : " + str(test_tup))

 

# using int() with base to get actual number

res = int("".join(str(ele) for ele in test_tup), 2) 

 

# printing result 

print("Decimal number is : " + str(res))   
  
---  
  
__

__

**Output**

    
    
    The original tuple is : (1, 1, 0, 1, 0, 0, 1)
    Decimal number is : 105
    

**Method #2 : Using bit shift and | operator**

In this we perform left bit shift and use or operator to get binary addition
and hence compute the result.

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Convert Binary tuple to Integer

# Using bit shift and | operator

 

# initializing tuple

test_tup = (1, 1, 0, 1, 0, 0, 1)

 

# printing original tuple

print("The original tuple is : " + str(test_tup))

 

 

res = 0

for ele in test_tup: 

 

 # left bit shift and or operator 

 # for intermediate addition

 res = (res << 1) | ele 

 

# printing result 

print("Decimal number is : " + str(res))   
  
---  
  
__

__

**Output**

    
    
    The original tuple is : (1, 1, 0, 1, 0, 0, 1)
    Decimal number is : 105
    

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

