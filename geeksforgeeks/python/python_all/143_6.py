Python program to validate an IP Address



 **Prerequisite:** Python Regex  

Given an IP address as input, write a Python program to check whether the
given IP Address is Valid or not.  

**What is an IP (Internet Protocol) Address ?**  
Every computer connected to the Internet is identified by a unique four-part
string, known as its Internet Protocol (IP) address. An IP address (version 4)
consists of four numbers (each between 0 and 255) separated by periods. The
format of an IP address is a 32-bit numeric address written as four decimal
numbers (called _octets_ ) separated by periods; each number can be written as
0 to 255 (E.g. – 0.0.0.0 to 255.255.255.255).  

**Examples:**

    
    
    **Input:**  192.168.0.1
    **Output:** Valid Ip address
    
    **Input:** 110.234.52.124
    **Output:** Valid Ip address
    
    **Input:** 666.1.2.2
    **Output:** Invalid Ip addess 
     
    **Input:** 25.99.208.255 
    **Output:** Valid Ip address

In this program, we are using **search()** method of _re module_.  
**re.search() :** This method either returns None (if the pattern doesn’t
match), or re.MatchObject that contains information about the matching part of
the string. This method stops after the first match, so this is best suited
for testing a regular expression more than extracting data.  

  

  

Let’s see the Python program to validate an IP address :  

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# Python program to validate an Ip address

# re module provides support

# for regular expressions

import re

# Make a regular expression

# for validating an Ip-address

regex =
"^((25[0-5]|2[0-4][0-9]|1[0-9][0-9]|[1-9]?[0-9])\.){3}(25[0-5]|2[0-4][0-9]|1[0-9][0-9]|[1-9]?[0-9])$"

 

# Define a function for

# validate an Ip addess

def check(Ip):

 # pass the regular expression

 # and the string in search() method

 if(re.search(regex, Ip)):

 print("Valid Ip address")

 

 else:

 print("Invalid Ip address")

 

# Driver Code

if __name__ == '__main__' :

 

 # Enter the Ip address

 Ip = "192.168.0.1"

 

 # calling run function

 check(Ip)

 Ip = "110.234.52.124"

 check(Ip)

 Ip = "366.1.2.2"

 check(Ip)  
  
---  
  
 __

 __

 **Output:**

    
    
    Valid Ip address
    Valid Ip address
    Invalid Ip address

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

