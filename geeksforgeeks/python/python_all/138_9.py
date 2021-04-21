Python | Ways to check if given string contains only letter



Given a string, write a Python program to find whether a string contains only
letters and no other keywords. Let’s discuss a few methods to complete the
task.

 **Method #1: Usingisalpha() method**

 __

 __  
 __

 __

 __  
 __  
 __

# Python code to demonstrate

# to find whether string contains

# only letters

 

# Initialising string

ini_str = "ababababa"

 

# Printing initial string

print ("Initial String", ini_str)

 

# Code to check whther string contains only number

if ini_str.isalpha():

 print("String contains only letters")

else:

 print("String doesn't contains only letters")  
  
---  
  
 __

 __

  
**Method #2: Usingre**

 __

 __  
 __

 __

 __  
 __  
 __

# Python code to demonstrate

# to find whether string contains

# only letters

import re

 

# Initialising string

ini_str = "ababababa"

 

# Printing initial string

print ("Initial String", ini_str)

 

# Code to check whther string contains only number

pattern = re.compile("^[a-zA-Z]+$")

if pattern.match(ini_str):

 print ("Contains only letters")

else:

 print ("Doesn't contains only letters")  
  
---  
  
 __

 __

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

  
  

  

My Personal Notes _arrow_drop_up_

Save

