Python | Ways to find nth occurrence of substring in a string



Given a string and a substring, write a Python program to find the nth
occurrence of the string. Let’s discuss a few methods to solve the given task.

 **Method #1: Using re**

 __

 __  
 __

 __

 __  
 __  
 __

# Python code to demonstrate

# to find nth occurrence of substring

 

import re

 

# Initialising values

ini_str = "abababababab"

substr = "ab"

occurrence = 4

 

 

# Finding nth occurrence of substring

inilist = [m.start() for m in re.finditer(r"ab", ini_str)]

if len(inilist)>= 4:

 

 # Printing result

 print ("Nth occurrence of substring at",
inilist[occurrence-1])

else:

 print ("No {} occurrence of substring lies in given
string".format(occurrence))  
  
---  
  
 __

 __

  
**Method #2: Using find() method**

 __

 __  
 __

 __

 __  
 __  
 __

# Python code to demonstrate

# to find nth occurrence of substring

 

# Initialising values

ini_str = "abababababab"

sub_str = "ab"

occurrence = 4

 

 

# Finding nth occurrence of substring

val = -1

for i in range(0, occurrence):

 val = ini_str.find(sub_str, val + 1)

 

# Printing nth occurrence

print ("Nth occurrence is at", val)  
  
---  
  
 __

 __

  
**Method #3: Using startswith() and list comprehension**

 __

 __  
 __

 __

 __  
 __  
 __

# Python code to demonstrate

# to find nth occurrence of substring

 

# Initialising values

ini_str = "abababababab"

substr = "ab"

occurrence = 4

 

 

# Finding nth occurrence of substring

inilist = [i for i in range(0, len(ini_str))

 if ini_str[i:].startswith(substr)]

 

if len(inilist)>= 4:

 

 # Printing result

 print ("Nth occurrence of substring at",
inilist[occurrence-1])

else:

 print ("No {} occurrence of substring lies in given
string".format(occurrence))

   
  
---  
  
__

__

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

  
  

  

My Personal Notes _arrow_drop_up_

Save

