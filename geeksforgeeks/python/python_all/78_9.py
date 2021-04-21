Python – Wildcard Substring search



Sometimes, while working with Python Strings, we have problem in which, we
need to search for substring, but have some of characters missing and we need
to find the match. This can have application in many domains. Lets discuss
certain ways in which this task can be performed.

 **Method #1 : Usingre.search()**  
This is one of the way in which this task can be performed. In this, we feed
the regex compile with the substring and search for it using main string in
search().

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Wildcard Substring search

# Using re.search()

import re

 

# initializing string

test_str = 'geeksforgeeks is best for geeks'

 

# printing original string

print("The original string is : " + str(test_str))

 

# initializing Substring

sub_str = '..st'

 

# Wildcard Substring search

# Using re.search()

temp = re.compile(sub_str) 

res = temp.search(test_str)

 

# printing result 

print("The substring match is : " + str(res.group(0)))   
  
---  
  
__

__

**Output :**

    
    
    The original string is : geeksforgeeks is best for geeks                                                                
    The substring match is : best     
    

**Method #2 : Usingre.finditer()**  
This is yet another way to solve this problem. In this, we can also extract
the position of match if required.

  

  

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Wildcard Substring search

# Using re.finditer()

import re

 

# initializing string

test_str = 'geeksforgeeks is best for geeks'

 

# printing original string

print("The original string is : " + str(test_str))

 

# initializing Substring

sub_str = '..st'

 

# Wildcard Substring search

# Using re.finditer()

temp = re.compile(sub_str) 

res = temp.search(test_str)

 

# printing result 

print("The substring match is : " + str(res.group(0)))   
  
---  
  
__

__

**Output :**

    
    
    The original string is : geeksforgeeks is best for geeks                                                                
    The substring match is : best     
    

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

