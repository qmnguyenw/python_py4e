Python | Check whether string contains only numbers or not



Given a string, write a Python program to find whether a string contains only
numbers or not. Let’s see a few methods to solve the above task.

 **Method #1: Usingisdigit() method**

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate

# how to check whether string contains

# only numbers or not

 

# Initialising string

ini_string1 = '1234556'

ini_string2 = 'ab123bc'

 

# printing initial string

print ("Initial Strings : ", ini_string1, ini_string2)

 

# Using isdigit()

if ini_string1.isdigit():

 print ("String1 contains all numbers")

else:

 print ("String1 doesn't contains all numbers")

 

if ini_string2.isdigit():

 print ("String2 conatins all numbers")

else:

 print ("String2 doesn't contains all numbers")  
  
---  
  
 __

 __

 **Output:**

    
    
    Initial Strings :  1234556 ab123bc
    String1 contains all numbers
    String2 doesn't contains all numbers
    

  
**Method #2: Using regex**

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate

# how to check whether string contains

# only numbers or not

import re

 

# Initialising string

ini_string1 = '1234556'

ini_string2 = 'ab123bc'

 

# printing initial string

print ("Initial Strings : ", ini_string1, ini_string2)

 

# Using regex()

if re.match('^[0-9]*$', ini_string1):

 print ("String1 contains all numbers")

else:

 print ("String1 doesn't contains all numbers")

 

if re.match('^[0-9]*$', ini_string2):

 print ("String2 conatins all numbers")

else:

 print ("String2 doesn't contains all numbers")  
  
---  
  
 __

 __

 **Output:**

  

  

    
    
    Initial Strings :  1234556 ab123bc
    String1 contains all numbers
    String2 doesn't contains all numbers
    

