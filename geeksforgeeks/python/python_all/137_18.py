Python | Ways to split strings on Uppercase characters



Given a string, write a Python program to split strings on Uppercase
characters. Let’s discuss a few methods to solve the problem.  
 **Method #1: Using re.findall() method**  

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# Python code to demonstrate

# to split strings

# on uppercase letter

import re

# Initialising string

ini_str = 'GeeksForGeeks'

# Printing Initial string

print ("Initial String", ini_str)

# Splitting on UpperCase using re

res_list = []

res_list = re.findall('[A-Z][^A-Z]*', ini_str)

# Printing result

print("Resultant prefix", str(res_list))  
  
---  
  
 __

 __

**Output:**

    
    
    Initial String GeeksForGeeks
    Resultant prefix ['Geeks', 'For', 'Geeks']
    
    
    

**Method #2: Using re.split()**  

  

  

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# Python code to demonstrate

# to split strings

# on uppercase letter

import re

# Initialising string

ini_str = 'GeeksForGeeks'

# Printing Initial string

print ("Initial String", ini_str)

# Splitting on UpperCase using re

res_list = [s for s in re.split("([A-Z][^A-Z]*)", ini_str)
if s]

# Printing result

print("Resultant prefix", str(res_list))  
  
---  
  
 __

 __

 **Output:**

    
    
    Initial String GeeksForGeeks
    Resultant prefix ['Geeks', 'For', 'Geeks']
    
    
    

  
**Method #3: Using enumerate**  

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# Python code to demonstrate

# to split strings

# on uppercase letter

# Initialising string

ini_str = 'GeeksForGeeks'

# Printing Initial string

print ("Initial String", ini_str)

# Splitting on UpperCase

res_pos = [i for i, e in enumerate(ini_str+'A') if
e.isupper()]

res_list = [ini_str[res_pos[j]:res_pos[j + 1]]

 for j in range(len(res_pos)-1)]

# Printing result

print("Resultant prefix", str(res_list))  
  
---  
  
 __

 __

**Output:**

    
    
    Initial String GeeksForGeeks
    Resultant prefix ['Geeks', 'For', 'Geeks']
    
    
    

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

