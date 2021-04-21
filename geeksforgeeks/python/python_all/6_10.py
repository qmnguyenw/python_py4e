Python Program to test if the String only Numbers and Alphabets



Given a String, our task is to write a Python program to check if string
contains both numbers and alphabets, not either nor punctuations.

 **Examples:**

    
    
     **Input :** test_str = 'Geeks4Geeks'
    **Output :** True
    **Explanation :** Contains both number and alphabets.
    
    **Input :** test_str = 'GeeksforGeeks'
    **Output :** False
    **Explanation :** Doesn't contain number.

 **Method #1 : Using** **isalpha()** **+** **isdigit()** **+** **any()** **+**
**all()** **+** **isalnum()**

In this, we check for all digits containing is alphabets and numbers
combination using all(), isalpha() and isdigit(). The any() and isalnum() is
used to filter out possibility of punctuations.

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Test if string contains both Numbers and Alphabets only

# Using isalpha() + isdigit() + any() + all() + isalnum()

 

# initializing string

test_str = 'Geeks4Geeks'

 

# printing original string

print("The original string is : " + str(test_str))

 

# conditional combination for getting result.

res = not ((all(idx.isdigit() for idx in test_str) or
(all(idx.isalpha() 

 for idx in test_str)) or (any(not idx.isalnum() for
idx in test_str))))

 

# printing result

print("Does string contain both numbers and alphabets only? : " +
str(res))  
  
---  
  
 __

 __

 **Output:**

  

  

    
    
    The original string is : Geeks4Geeks
    Does string contain both numbers and alphabets only? : True

 **Method #2 : Using** **regex**

Using regex is one of the ways in which this problem can be solved.

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Test if string contains both Numbers and Alphabets only

# Using regex

import re

 

# initializing string

test_str = 'Geeks4Geeks'

 

# printing original string

print("The original string is : " + str(test_str))

 

# conditional combination for getting result.

res = bool(re.match("^(?=.*[a-zA-Z])(?=.*[\d])[a-zA-Z\d]+$",
"A530"))

 

# printing result

print("Does string contain both numbers and alphabets only? : " +
str(res))  
  
---  
  
 __

 __

 **Output:**

    
    
    The original string is : Geeks4Geeks
    Does string contain both numbers and alphabets only? : True

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

