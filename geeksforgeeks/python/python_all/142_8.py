Python Regex – Program to accept string starting with vowel



 **Prerequisite:**Regular expression in Python

Given a string, write a Python program to check whether the given string is
starting with Vowel or Not.

 **Examples:**

    
    
      
    **Input:** animal
    **Output:** Accepted
    
    **Input:** zebra
    **Output:** Not Accepted
    

In this program, we are using search() method of _re module_.

 **re.search()** : This method either returns None (if the pattern doesn’t
match), or re.MatchObject that contains information about the matching part
of the string. This method stops after the first match, so this is best suited
for testing a regular expression more than extracting data.

  

  

Let’s see the Python program for this :

 __

 __  
 __

 __

 __  
 __  
 __

# Python program to accept string starting with a vowel

 

# import re module

 

# re module provides support

# for regular expressions

import re

 

# Make a regular expression

# to accept string starting with vowel

regex = '^[aeiouAEIOU][A-Za-z0-9_]*'

 

# Define a function for

# accepting string start with vowel

def check(string): 

 

 # pass the regualar expression

 # and the string in search() method

 if(re.search(regex, string)): 

 print("Valid") 

 

 else: 

 print("Invalid") 

 

 

# Driver Code 

if __name__ == '__main__' : 

 

 # Enter the string 

 string = "ankit"

 

 # calling run function 

 check(string)

 

 string = "geeks"

 check(string)

 

 string = "sandeep"

 check(string)  
  
---  
  
 __

 __

 **Output:**

    
    
    Valid
    Invalid
    Invalid
    

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

