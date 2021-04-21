Python | Check if string is a valid identifier



Given a string, write a Python program to check if it is a valid identifier or
not.

An **identifier** must begin with either an alphabet or underscore, it can not
begin with a digit or any other special character, moreover, digits can come
after.

    
    
    gfg : valid identifier
    123 : invalid identifier
    _abc12 : valid identifier
    #abc : invalid identifier
    

In this program, we are using search() method of regex module.  
 **re.search() :** This method either returns None (if the pattern doesn’t
match), or re.MatchObject that contains information about the matching part
of the string. This method stops after the first match, so this is best suited
for testing a regular expression more than extracting data.

Let’s see the Python program to determine whether string is an identifier or
not.

 __

 __  
 __

 __

 __  
 __  
 __

# Python program to identify the identifier

 

# import re module

 

# re module provides support

# for regular expressions

import re

 

# Make a regular expression

# for identify valid identifier

regex = '^[A-Za-z_][A-Za-z0-9_]*'

 

# Define a function for

# identifying valid identifier

def check(string): 

 

 # pass the regualar expression

 # and the string in search() method

 if(re.search(regex, string)): 

 print("Valid Identifier") 

 

 else: 

 print("Invalid Identifier") 

 

 

# Driver Code 

if __name__ == '__main__' : 

 

 # Enter the string 

 string = "gfg"

 

 # calling run function 

 check(string)

 

 string = "123"

 check(string)

 

 string = "#abc"

 check(string)  
  
---  
  
 __

 __

 **Output :**

    
    
    Valid Identifier
    Invalid Identifier
    Invalid Identifier
    

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

