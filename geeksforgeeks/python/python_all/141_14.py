Python Regex | Program to accept string ending with alphanumeric character



 **Prerequisite:**Regular expression in Python

Given a string, write a Python program to check whether the given string is
ending with only alphanumeric character or Not.

 **Examples:**

    
    
    **Input:** ankitrai326
    **Output:** Accept
    
    **Input:** ankirai@
    **Output:** Discard
    

In this program, we are using search() method of _re module_.  
 **re.search() :** This method either returns None (if the pattern doesn’t
match), or re.MatchObject that contains information about the matching part
of the string. This method stops after the first match, so this is best suited
for testing a regular expression more than extracting data.

 _Alphanumeric characters_ in the POSIX/C locale consist of either 36 case-
insensitive symbols (A-Z and 0-9) or 62 case-sensitive characters (A-Z, a-z
and 0-9).

  

  

Let’s see the Python program for this :

 __

 __  
 __

 __

 __  
 __  
 __

# Python program to accept string ending

# with only alphanumeric character.

# import re module

 

# re module provides support

# for regular expressions

import re

 

# Make a regular expression to accept string

# ending with alphanumeric character

regex = '[a-zA-z0-9]$'

 

# Define a function for accepting string

# ending with alphanumeric character

def check(string): 

 

 # pass the regualar expression

 # and the string in search() method

 if(re.search(regex, string)): 

 print("Accept") 

 

 else: 

 print("Discard") 

 

 

# Driver Code 

if __name__ == '__main__' : 

 

 # Enter the string 

 string = "ankirai@"

 

 # calling run function 

 check(string)

 

 string = "ankitrai326"

 check(string)

 

 string = "ankit."

 check(string)

 

 string = "geeksforgeeks"

 check(string)  
  
---  
  
 __

 __

 **Output :**

    
    
    Discard
    Accept
    Discard
    Accept
    

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

