How to capitalize first character of string in Python



The problem of case changes a string is quite common and has been discussed
many times. Sometimes, we might have a problem like this in which we need to
convert the initial character of string to upper case. Let’s discuss certain
ways in which this can be performed.

 **Method #1 : Using string slicing +upper()**  
This task can easily be performed using the upper method which uppercases the
characters provided to it and slicing can be used to add the remaining string
after the lowercase first character.

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Initial character upper case

# Using upper() + string slicing

 

# initializing string 

test_str = "geeksforgeeks"

 

# printing original string 

print("The original string is : " + str(test_str))

 

# Using upper() + string slicing

# Initial character upper case

res = test_str[0].upper() + test_str[1:]

 

# printing result 

print("The string after uppercasing initial character : " +
str(res))  
  
---  
  
 __

 __

 **Output :**

    
    
    The original string is : geeksforgeeks
    The string after uppercasing initial character : Geeksforgeeks
    

**Method #2 : Usingcapitalize()**  
We can use inbuilt method to perform this task. This method is recommended to
solve this problem and performs the task of converting to upper case
internally.

  

  

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Initial character upper case

# Using capitalize() + string slicing

 

# initializing string 

test_str = "geeksforgeeks"

 

# printing original string 

print("The original string is : " + str(test_str))

 

# Using capitalize() + string slicing

# Initial character upper case

res = test_str.capitalize()

 

# printing result 

print("The string after uppercasing initial character : " +
str(res))  
  
---  
  
 __

 __

 **Output :**

    
    
    The original string is : geeksforgeeks
    The string after uppercasing initial character : Geeksforgeeks
    

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

