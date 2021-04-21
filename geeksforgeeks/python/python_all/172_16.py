Python regex to find sequences of one upper case letter followed by lower case
letters



Write a Python Program to find sequences of one upper case letter followed by
lower case letters. If found, print ‘Yes’, otherwise ‘No’.

 **Examples:**

    
    
    **Input :** Geeks
    **Output :** Yes
    
    **Input :** geeksforgeeks
    **Output :** No
    

**Approach:** Using re.search()

To check if the sequence of one upper case letter followed by lower case
letters we use regular expression ‘[A-Z]+[a-z]+$‘.

  

  

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to find sequences of one upper

# case letter followed by lower case letters

import re

 

# Function to match the string

def match(text):

 

 # regex

 pattern = '[A-Z]+[a-z]+$'

 

 # searching pattern

 if re.search(pattern, text):

 return('Yes')

 else:

 return('No')

 

# Driver Function

print(match("Geeks"))

print(match("geeksforGeeks"))

print(match("geeks"))  
  
---  
  
 __

 __

 **Output:**

    
    
    Yes
    Yes
    No

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

