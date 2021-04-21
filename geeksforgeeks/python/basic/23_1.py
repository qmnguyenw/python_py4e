Python | Remove leading zeros from an IP address



  
Given an IP address, remove leading zeros from the IP address.

 **Examples:**

    
    
    Input : 100.020.003.400 
    Output : 100.20.3.400
    
    Input :001.200.001.004  
    Output : 1.200.1.4
    

## Recommended: Please solve it on **__PRACTICE__** first, before moving on to
the solution.

 **Method 1 : Traversal and join**

The **approach** is to split the given string by “.” and then convert it to an
integer which removes the leading zeros and then join back them to a string.To
convert a string to an integer we can use int(s) and then convert it back to
string by str(s) and then join them back by using join function.

  

  

 __

 __  
 __

 __

 __  
 __  
 __

# Python program to remove leading zeros

# an IP address and print the IP

 

# function to remove leading zeros

def removeZeros(ip):

 

 # splits the ip by "."

 # converts the words to integeres to remove leading removeZeros 

 # convert back the integer to string and join them back to a string

 new_ip = ".".join([str(int(i)) for i in
ip.split(".")]) 

 return new_ip ;

 

 

# driver code 

# example1

ip ="100.020.003.400"

print(removeZeros(ip))

 

 

# example2

ip ="001.200.001.004"

print(removeZeros(ip))  
  
---  
  
 __

 __

 **Output:**

    
    
    100.20.3.400
    1.200.1.4
    

**Method 2 :Regex**

Using a capture group, match the last digit and copy it and prevents all the
digits from being replaced.

regex \d can be explained as:

  *  **\d :** Matches any decimal digit
    
         ** **\d   Matches any decimal digit, this is equivalent
         to the set class [0-9].****

  * \b allows you to perform a “whole words only” search using a regular expression in the form of \bword\b  
 **regex \b can be explained as :**

    
         **\b allows you to perform a "whole words only" search u
    sing a regular expression in the form of \bword\b**

 __

 __  
 __

 __

 __  
 __  
 __

# Python program to remove leading zeros

# an IP address and print the IP using regex

import re 

 

# function to remove leading zeros

def removeZeros(ip):

 new_ip = re.sub(r'\b0+(\d)', r'\1', ip)

 # splits the ip by "."

 # converts the words to integeres to remove leading removeZeros 

 # convert back the integer to string and join them back to a string

 

 return new_ip 

 

 

# driver code 

# example1

ip ="100.020.003.400"

print(removeZeros(ip))

 

 

# example2

ip ="001.200.001.004"

print(removeZeros(ip))  
  
---  
  
 __

 __

 **Output:**

    
    
    100.20.3.400
    1.200.1.4
    

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

