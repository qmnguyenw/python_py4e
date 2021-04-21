Python – Uppercase Nth character



The problem of capitalizing a string is quite common and has been discussed
many times. But sometimes, we might have a problem like this in which we need
to convert the Nth character of string to uppercase. Let’s discuss certain
ways in which this can be performed.

 **Method #1 : Using string slicing +upper()**  
This task can easily be performed using the upper method which uppercases the
characters provided to it and slicing can be used to add the remaining string
after the uppercase Nth character.

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Uppercase Nth character

# Using upper() + string slicing

 

# initializing string 

test_str = "GeeksforGeeks"

 

# printing original string 

print("The original string is : " + str(test_str))

 

# initializing N 

N = 4

 

# Using upper() + string slicing

# Uppercase Nth character

res = test_str[:N] + test_str[N].upper() + test_str[N +
1:]

 

# printing result 

print("The string after uppercasing Nth character : " + str(res))  
  
---  
  
 __

 __

 **Output :**

    
    
    The original string is : GeeksforGeeks
    The string after uppercasing Nth character : GeekSforGeeks
    

**Method #2 : Using lambda + string slicing +upper()**  
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

# Uppercase Nth character

# Using upper() + string slicing + lambda

 

# initializing string 

test_str = "GeeksforGeeks"

 

# printing original string 

print("The original string is : " + str(test_str))

 

# initializing N 

N = 4

 

# Using upper() + string slicing + lambda

# Uppercase Nth character

res = lambda test_str: test_str[:N] + test_str[N].upper() +
test_str[N + 1:] if test_str else ''

 

# printing result 

print("The string after uppercasing initial character : " +
str(res(test_str)))  
  
---  
  
 __

 __

 **Output :**

    
    
    The original string is : GeeksforGeeks
    The string after uppercasing Nth character : GeekSforGeeks
    

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

