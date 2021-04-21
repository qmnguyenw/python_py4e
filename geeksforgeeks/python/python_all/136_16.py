Python | Check for spaces in string



Sometimes, we might have a problem in which we need to check if the string has
any of blank spaces. This kind of problem can be in Machine Learning domain to
get specific type of data set. Let’s discuss certain ways in which this kind
of problem can be solved.

 **Method #1 : Using regex**  
This kind of problem can be solved using the regex utility offered by python.
By feeding the appropriate regex string in search(), we can check presence
of space in a string.

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Check for spaces in string

# Using regex

import re

 

# initializing string 

test_str = "Geeks forGeeks"

 

# printing original string 

print("The original string is : " + test_str)

 

# Using regex

# Check for spaces 

res = bool(re.search(r"\s", test_str))

 

# printing result 

print("Does string contain spaces ? " + str(res))  
  
---  
  
 __

 __

 **Output :**

    
    
    The original string is : Geeks  forGeeks
    Does string contain spaces ? True
    

**Method #2 : Usingin operator**  
This task can also be performed using in operator. Just required to check for
a space in the string. The verdict returned is true even if a single space is
found and false otherwise.

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Check for spaces in string

# Using in operator

 

# initializing string 

test_str = "Geeks forGeeks"

 

# printing original string 

print("The original string is : " + test_str)

 

# Using in operator

# Check for spaces 

res = " " in test_str

 

# printing result 

print("Does string contain spaces ? " + str(res))  
  
---  
  
 __

 __

 **Output :**

    
    
    The original string is : Geeks  forGeeks
    Does string contain spaces ? True
    

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

  
  

  

My Personal Notes _arrow_drop_up_

Save

