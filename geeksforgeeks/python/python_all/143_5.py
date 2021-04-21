Python regex | Check whether the input is Floating point number or not



 **Prerequisite:** Regular expression in Python

Given an input, write a Python program to check whether the given Input is
Floating point number or not.

 **Examples:**

    
    
    **Input:**  1.20
    **Output:** Floating point number
    
    **Input:** -2.356
    **Output:** Floating point number
    
    **Input:** 0.2
    **Output:** Floating point number
    
    **Input:** -3
    **Output:** Not a Floating point number
    

In this program, we are using **search()** method of _re module_.

 **re.search() :** This method either returns None (if the pattern doesn’t
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

# Python program to check input is

# Floating point number or not

 

# import re module

 

# re module provides support

# for regular expressions

import re

 

# Make a regular expression for

# identifying Floating point number 

regex = '[+-]?[0-9]+\.[0-9]+'

 

# Define a function to

# check Floating point number 

def check(floatnum): 

 

 # pass the regular expression

 # and the string in search() method

 if(re.search(regex, floatnum)): 

 print("Floating point number") 

 

 else: 

 print("Not a Floating point number") 

 

 

# Driver Code 

if __name__ == '__main__' : 

 

 # Enter the floating point number

 floatnum = "1.20"

 

 # calling run function 

 check(floatnum)

 

 floatnum = "-2.356"

 check(floatnum)

 

 floatnum = "0.2"

 check(floatnum)

 

 floatnum = "-3"

 check(floatnum)  
  
---  
  
 __

 __

 **Output:**

    
    
    Floating point number
    Floating point number
    Floating point number
    Not a Floating point number
    

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

