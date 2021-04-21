Python | Ways to remove n characters from start of given string



Given a string and a number ‘n’, the task is to remove a string of length ‘n’
from the start of the string. Let’s a few methods to solve the given task.  
  
 **Method #1: Using Naive Method**

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate

# how to remove 'n' characters from starting

# of a string

 

# Initialising string

ini_string1 = 'garg_akshat'

 

# Initialising number of characters to be removed

n = 5

 

# Printing initial string

print ("Initial String", ini_string1)

 

# Removing n characters from string using 

# Naive method

res = ''

for i in range(0, len(ini_string1)):

 if i>= n:

 res = res + ini_string1[i]

 

# Printing resultant string

print ("Resultant String", res)  
  
---  
  
 __

 __

 **Output:**

    
    
    Initial String garg_akshat
    Resultant String akshat
    

  
**Method #2: Usingreplace()**

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate

# how to remove 'n' characters from starting

# of a string

 

# Initialising string

ini_string1 = 'garg_akshat'

 

# Initialising number of characters to be removed

n = 5

 

# Printing initial string

print ("Initial String", ini_string1)

 

# Removing n characters from string using 

# replace() function

res = ini_string1.replace(ini_string1[:5], '', 1)

 

# Printing resultant string

print ("Resultant String", res)  
  
---  
  
 __

 __

 **Output:**

    
    
    Initial String garg_akshat
    Resultant String akshat
    

  
**Method #3: String slicing**

  

  

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate

# how to remove 'n' characters from starting

# of a string

 

# Initialising string

ini_string1 = 'gargakshat123'

 

# Initialising number of characters to be removed

n = 5

 

# Printing initial string

print ("Initial String", ini_string1)

 

# Removing n characters from a string

# This argument count length from zero 

# So length to be stripped is passed n-1

res = ini_string1[4:]

 

# Printing resultant string

print ("Resultant String", res)

   
  
---  
  
__

__

**Output:**

    
    
    Initial String gargakshat123
    Resultant String akshat123
    

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

