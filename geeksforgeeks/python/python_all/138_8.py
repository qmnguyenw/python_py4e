Python | Ways to count number of substring in string



Given a string and a substring, write a Python program to find how many
numbers of substring are there in the string (including overlapping cases).
Let’s discuss a few methods below.

 **Method #1: Usingre.findall()**

 __

 __  
 __

 __

 __  
 __  
 __

# Python code to demonstrate

# to count total number

# of substring in string

 

import re

# Initialising string

ini_str = "ababababa"

sub_str = 'aba'

 

# Count count of substrings using re.findall

res = len(re.findall('(?= aba)', ini_str))

 

# Printing result

print("Number of substrings", res)  
  
---  
  
 __

 __

 **Output:**

    
    
    Number of substrings 0
    

**Method #2: Usingre.finditer()**

 __

 __  
 __

 __

 __  
 __  
 __

# Python code to demonstrate

# to count total number

# of substring in string

 

import re

# Initialising string

ini_str = "ababababa"

sub_str = 'aba'

 

# Count count of substrings using re.finditer

res = sum(1 for _ in re.finditer('(?= aba)', ini_str))

 

# Printing result

print("Number of substrings", res)  
  
---  
  
 __

 __

 **Output:**

  

  

    
    
    Number of substrings 0
    

