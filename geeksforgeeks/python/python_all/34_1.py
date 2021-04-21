Python program to uppercase the given characters



Given a string and set of characters, convert all the characters occurred from
character set in string to uppercase()

>  **Input** : test_str = ‘gfg is best for geeks’, upper_list = [‘g’, ‘e’,
> ‘b’]  
> **Output** : GfG is BEst for GEEks  
> **Explanation** : Only selective characters uppercased.
>
>  **Input** : test_str = ‘gfg is best’, upper_list = [‘g’, ‘e’, ‘b’]  
> **Output** : GfG is BEst  
> **Explanation** : Only selective characters uppercased.

**Method #1 : Using loop + upper()**

The combination of the above functions can be used to solve this problem. In
this, we check for each character using a loop, if it is in the characters, it
is converted to uppercase using upper().

  

  

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Uppercase custom characters

# Using upper() + loop

 

# initializing string

test_str = 'gfg is best for geeks'

 

# printing original string

print("The original string is : " + str(test_str))

 

# initializing upperlist 

upper_list = ['g', 'e', 'b', 'k']

 

res = ''

for ele in test_str:

 

 # checking for presence in upper list 

 if ele in upper_list:

 res += ele.upper()

 else :

 res += ele

 

# printing result 

print("String after reconstruction : " + str(res))  
  
---  
  
 __

 __

 **Output**

    
    
    The original string is : gfg is best for geeks
    String after reconstruction : GfG is BEst for GEEKs
    
    

**Method #2 : Using list comprehension**

This is yet another way in which this task can be performed. In this, we
perform the task in a similar way as the above method, but as a shorthand
using one-liner list comprehension.

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Uppercase custom characters

# Using list comprehension

 

# initializing string

test_str = 'gfg is best for geeks'

 

# printing original string

print("The original string is : " + str(test_str))

 

# initializing upperlist 

upper_list = ['g', 'e', 'b', 'k']

 

# one-liner used to solve problem

res = "".join([ele.upper() if ele in upper_list else ele
for ele in test_str])

 

# printing result 

print("String after reconstruction : " + str(res))  
  
---  
  
 __

 __

 **Output**

    
    
    The original string is : gfg is best for geeks
    String after reconstruction : GfG is BEst for GEEKs
    
    

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

