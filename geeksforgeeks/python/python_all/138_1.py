Python | Ways to determine common prefix in set of strings



Given a set of strings, write a Python program to determine common prefix from
a set of strings. Given below are a few methods to solve the above task.

 **Method #1: Using Naive Approach**

 __

 __  
 __

 __

 __  
 __  
 __

# Python code to demonstrate

# to find common prefix

# from set of strings

 

# Initialising string

ini_strlist = ['akshat', 'akash', 'akshay', 'akshita']

 

# Finding commom prefix using Naive Approach

res = ''

prefix = ini_strlist[0]

 

for string in ini_strlist[1:]:

 while string[:len(prefix)] != prefix and prefix:

 prefix = prefix[:len(prefix)-1]

 if not prefix:

 break

res = prefix

 

# Printing result

print("Resultant prefix", str(res))  
  
---  
  
 __

 __

 **Output:**

    
    
    Resultant prefix ak
    

  
**Method #2: Using itertools.takewhile and zip**

 __

 __  
 __

 __

 __  
 __  
 __

# Python code to demonstrate

# to find common prefix

# from set of strings

 

from itertools import takewhile

 

# Initialising string

ini_strlist = ['akshat', 'akash', 'akshay', 'akshita']

 

# Finding commom prefix using Naive Approach

res = ''.join(c[0] for c in takewhile(lambda x:

 all(x[0] == y for y in x),
zip(*ini_strlist)))

 

# Printing result

print("Resultant prefix", str(res))  
  
---  
  
 __

 __

 **Output:**

    
    
    Resultant prefix ak
    

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

  
  

  

My Personal Notes _arrow_drop_up_

Save

