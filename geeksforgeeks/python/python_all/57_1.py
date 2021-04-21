Python program to Count Uppercase, Lowercase, special character and numeric
values using Regex



 **Prerequisites:** Regular Expression in Python

Given a string. The task is to count the number of Uppercase, Lowercase,
special character and numeric values present in the string using Regular
expression in Python.

 **Examples:**

    
    
    **Input :**
    "ThisIsGeeksforGeeks!, 123" 
    
    **Output :**
    No. of uppercase characters = 4
    No. of lowercase characters = 15
    No. of numerical characters = 3
    No. of special characters = 2
    

**Approach:** The re.findall(pattern, string, flags=0) method can be used to
find all non-overlapping matches of a pattern in the string. The return value
is a list of strings.

Below is the implementation.

  

  

 __

 __  
 __

 __

 __  
 __  
 __

import re

 

 

string = "ThisIsGeeksforGeeks !, 123"

 

# Creating separate lists using 

# the re.findall() method.

uppercase_characters = re.findall(r"[A-Z]", string)

lowercase_characters = re.findall(r"[a-z]", string)

numerical_characters = re.findall(r"[0-9]", string)

special_characters = re.findall(r"[, .!?]", string)

 

print("The no. of uppercase characters is",
len(uppercase_characters))

print("The no. of lowercase characters is",
len(lowercase_characters))

print("The no. of numerical characters is",
len(numerical_characters))

print("The no. of special characters is", len(special_characters))  
  
---  
  
 __

 __

 **Output:**

    
    
    The no. of uppercase characters is 4
    The no. of lowercase characters is 15
    The no. of numerical characters is 3
    The no. of special characters is 4
    

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

