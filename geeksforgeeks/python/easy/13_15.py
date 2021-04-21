Check if email address valid or not in Python



 **Prerequisite:** Regex in Python  
Given a string, write a Python program to check if the string is a valid email
address or not.  
An email is a string (a subset of ASCII characters) separated into two parts
by @ symbol, a “personal_info” and a domain, that is personal_info@domain.  
 **Examples:**

    
    
    **Input:**  ankitrai326@gmail.com
    **Output:** Valid Email
    
    **Input:** my.ownsite@ourearth.org
    **Output:** Valid Email
    
    **Input:** ankitrai326.com
    **Output:** Invalid Email 

In this program, we are using search() method of re module. so let’s see the
description about it.  
 **re.search() :** This method either returns None (if the pattern doesn’t
match), or re.MatchObject that contains information about the matching part of
the string. This method stops after the first match, so this is best suited
for testing a regular expression more than extracting data.  
Let’s see the Python program to validate an Email :

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# Python program to validate an Email

# import re module

# re module provides support

# for regular expressions

import re

# Make a regular expression

# for validating an Email

regex = '^(\w|\.|\_|\-)+[@](\w|\_|\-|\.)+[.]\w{2,3}$'

# Define a function for

# for validating an Email

def check(email):

 # pass the regular expression

 # and the string in search() method

 if(re.search(regex, email)):

 print("Valid Email")

 else:

 print("Invalid Email")

# Driver Code

if __name__ == '__main__':

 # Enter the email

 email = "ankitrai326@gmail.com"

 # calling run function

 check(email)

 email = "my.ownsite@our-earth.org"

 check(email)

 email = "ankitrai326.com"

 check(email)  
  
---  
  
 __

 __

 **Output:**

    
    
    Valid Email
    Valid Email
    Invalid Email

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

