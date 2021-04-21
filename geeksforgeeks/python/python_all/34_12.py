Python – Check if string contains any number



Given a String, check if it contains any number.

>  **Input** : test_str = ‘geeks4g2eeks’  
>  **Output** : True  
>  **Explanation** : Contains 4 and 2.
>
>  **Input** : test_str = ‘geeksforgeeks’  
>  **Output** : False  
>  **Explanation** : Contains no number.

 **Method #1 : Using any() + isdigit()**

The combination of above functions can be used to solve this problem. In this,
we check for number using isdigit() and check for any occurrence using any().

  

  

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Check if string contains any number

# Using isdigit() + any()

 

# initializing string

test_str = 'geeks4geeks'

 

# printing original string

print("The original string is : " + str(test_str))

 

# using any() to check for any occurrence

res = any(chr.isdigit() for chr in test_str)

 

# printing result 

print("Does string contain any digit ? : " + str(res))   
  
---  
  
__

__

**Output**

    
    
    The original string is : geeks4geeks
    Does string contain any digit ? : True
    

**Method #2 : Using next() + generator expression + isdigit()**

This is yet another way in which this task can be performed. This is
recommended in cases of larger strings, the iteration in generator is cheap,
but construction is usually inefficient.

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Check if string contains any number

# Using isdigit() + next() + generator expression

 

# initializing string

test_str = 'geeks4geeks'

 

# printing original string

print("The original string is : " + str(test_str))

 

# next() checking for each element, reaches end, if no element found as
digit

res = True if next((chr for chr in test_str if
chr.isdigit()), None) else False

 

# printing result 

print("Does string contain any digit ? : " + str(res))   
  
---  
  
__

__

**Output**

    
    
    The original string is : geeks4geeks
    Does string contain any digit ? : True
    

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

