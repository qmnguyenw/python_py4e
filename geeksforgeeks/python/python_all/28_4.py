Python program to print k characters then skip k characters in a string



Given a String, extract K characters alternatively.

>  **Input** : test_str = ‘geeksgeeksisbestforgeeks’, K = 4  
> **Output** : geekksisforg  
> **Explanation** : Every 4th alternate range is sliced.  
>  **Input** : test_str = ‘geeksgeeksisbest’, K = 4  
> **Output** : geekksis  
> **Explanation** : Every 4th alternate range is sliced.  
>

**Method #1 : Using loop + slicing**

In this, we perform task of getting K characters using slicing, and loop is
used to perform task of concatenation.

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Alternate K Length characters

# Using loop + slicing 

 

# initializing string

test_str = 'geeksgeeksisbestforgeeks'

 

# printing original string

print("The original string is : " + str(test_str))

 

# initializing K 

K = 4

 

res = ''

 

# skipping k * 2 for altering effect

for idx in range(0, len(test_str), K * 2):

 

 # concatenating K chars

 res += test_str[idx : idx + K]

 

# printing result 

print("Transformed String : " + str(res))   
  
---  
  
__

__

**Output:**

  

  

    
    
    The original string is : geeksgeeksisbestforgeeks
    Transformed String : geekksisforg
    

**Method #2 : Using list comprehension + join()**

This is similar to the above way, only difference being its one liner
approach, and join() is used to perform task of convert back to string.

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Alternate K Length characters

# Using list comprehension + join()

 

# initializing string

test_str = 'geeksgeeksisbestforgeeks'

 

# printing original string

print("The original string is : " + str(test_str))

 

# initializing K 

K = 4

 

# slicing K using slicing, join for converting back to string

res = ''.join([test_str[idx : idx + K] for idx in
range(0, len(test_str), K * 2)])

 

# printing result 

print("Transformed String : " + str(res))   
  
---  
  
__

__

**Output:**

    
    
    The original string is : geeksgeeksisbestforgeeks
    Transformed String : geekksisforg
    

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

