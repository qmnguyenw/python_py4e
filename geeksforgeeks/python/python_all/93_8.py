Python – Lowercase Kth Character in string



The problem of lowercasing a string is quite common and has been discussed
many times. But sometimes, we might have a problem like this in which we need
to convert the Nth character of string to lowercase. Let’s discuss certain
ways in which this can be performed.

 **Method #1 : Using string slicing +lower()**  
This task can easily be performed using the lower method which lowercases the
characters provided to it and slicing can be used to add the remaining string
after the lowercase Nth character.

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Kth Character Lowercase

# Using lower() + string slicing 

 

# initializing string 

test_str = "GEEKSFORGEEKS"

 

# printing original string 

print("The original string is : " + str(test_str)) 

 

# initializing K

K = 4

 

# Using lower() + string slicing 

# Kth Character Lowercase

res = test_str[:K] + test_str[K].lower() + test_str[K + 1:]


 

# printing result 

print("The string after lowercasing Kth character : " + str(res))   
  
---  
  
__

__

**Output :**

    
    
    The original string is : GEEKSFORGEEKS
    The string after lowercasing Kth character : GEEKsFORGEEKS
    

**Method #2 : Usinglambda + string slicing + lower()**  
The recipe of lambda function has to be added if we need to perform the task
of handling None values or empty strings as well, and this becomes essential
to handle edge cases.

  

  

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Kth Character Lowercase

# Using lower() + string slicing + lambda 

 

# initializing string 

test_str = "GEEKSFORGEEKS"

 

# printing original string 

print("The original string is : " + str(test_str)) 

 

# initializing K

K = 4

 

# Using lower() + string slicing + lambda 

# Kth Character Lowercase

res = lambda test_str: test_str[:K] + test_str[K].lower() +
test_str[K + 1:] if test_str else '' 

 

# printing result 

print("The string after lowercasing initial character : " +
str(res(test_str)))   
  
---  
  
__

__

**Output :**

    
    
    The original string is : GEEKSFORGEEKS
    The string after lowercasing Kth character : GEEKsFORGEEKS
    

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

