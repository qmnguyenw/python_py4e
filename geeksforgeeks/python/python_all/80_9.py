Python | Test if String contains Alphabets and Spaces



Sometimes, while testing of credibility of string being a part of containing
just alphabets, an exception of spaces has to be mentioned explicitely and
becomes a problem. This can occur in domains that deal with data. Lets discuss
certain ways in which this task can be performed.

 **Method #1 : Using all() +isspace() + isalpha()**  
This is one of the way in which this task can be performed. In this, we
compare the string for all elements being alphabets or space only.

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Test if String contains Alphabets and Spaces

# Using isspace() + isalpha() + all()

import re

 

# initializing string

test_str = 'geeksforgeeks is best for geeks'

 

# printing original string

print("The original string is : " + test_str)

 

# Test if String contains Alphabets and Spaces

# Using isspace() + isalpha() + all()

res = test_str != '' and all(chr.isalpha() or
chr.isspace() for chr in test_str)

 

# printing result 

print("Does String contain only space and alphabets : " + str(res))
  
  
---  
  
__

__

**Output :**

    
    
    The original string is : geeksforgeeks is best for geeks
    Does String contain only space and alphabets : True
    

**Method #1 : Using regex**  
This problem can also be solved by employing regex to include only space and
alphabets in a string.

  

  

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Test if String contains Alphabets and Spaces

# Using regex

import re

 

# initializing string

test_str = 'geeksforgeeks is best for geeks'

 

# printing original string

print("The original string is : " + test_str)

 

# Test if String contains Alphabets and Spaces

# Using regex

res = bool(re.match('[a-zA-Z\s]+$', test_str))

 

# printing result 

print("Does String contain only space and alphabets : " + str(res))
  
  
---  
  
__

__

**Output :**

    
    
    The original string is : geeksforgeeks is best for geeks
    Does String contain only space and alphabets : True
    

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

