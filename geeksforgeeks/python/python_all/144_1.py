Python | Check if given string is numeric or not



Given a string, write a Python program to check if the string is numeric or
not.

 **Examples:**

    
    
    **Input:**  28
    **Output:** digit
    
    **Input:** a
    **Output:** not a digit. 
    
    **Input:** 21ab
    **Output:** not a digit. 
    

  
**Code #1:** Using Python regex

 **re.search() :** This method either returns None (if the pattern doesn’t
match), or a re.MatchObject that contains information about the matching part
of the string. This method stops after the first match, so this is best suited
for testing a regular expression more than extracting data.

 __

 __  
 __

 __

 __  
 __  
 __

# Python program to identify the Digit

 

# import re module

 

# re module provides support

# for regular expressions

import re

 

# Make a regular expression

# for identifying a digit

regex = '^[0-9]+$'

 

# Define a function for

# identifying a Digit

def check(string): 

 

 # pass the regualar expression

 # and the string in search() method

 if(re.search(regex, string)): 

 print("Digit") 

 

 else: 

 print("Not a Digit") 

 

 

# Driver Code 

if __name__ == '__main__' : 

 

 # Enter the string 

 string = "28"

 

 # calling run function 

 check(string)

 

 string = "a"

 check(string)

 

 string = "21ab"

 check(string)

 

 string = "12ab12"

 check(string)  
  
---  
  
 __

 __

 **Output:**

  

  

    
    
    Digit
    Not a Digit
    Not a Digit
    Not a Digit
    

