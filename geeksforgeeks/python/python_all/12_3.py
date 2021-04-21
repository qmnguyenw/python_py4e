Validate an IP address using Python without using RegEx



Given an IP address as input, the task is to write a Python program to check
whether the given IP Address is Valid or not without using RegEx.

 **What is an IP (Internet Protocol) Address?**  
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

 **Method #1:** Checking the number of periods using _count()_ method and then
the range of numbers between each period.

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# Python program to verify IP without using RegEx

 

# explicit function to verify IP

def isValidIP(s):

 

 # check number of periods

 if s.count('.') != 3:

 return 'Invalid Ip addess'

 

 l = list(map(str, s.split('.')))

 

 # check range of each number between periods

 for ele in l:

 if int(ele) < 0 or int(ele) > 255:

 return 'Invalid Ip addess'

 

 return 'Valid Ip address'

 

 

# Driver Code

print(isValidIP('666.1.2.2'))  
  
---  
  
 __

 __

 **Output:**

  

  

    
    
    Invalid Ip addess

 **Method #2:** Using a variable to check the number of periods and using a
_set_ to check if the range of numbers between periods is between 0 and
255(inclusive).

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# Python program to verify IP without using RegEx

 

# explicit function to verify IP

def isValidIP(s):

 

 # initialize counter

 counter = 0

 

 # check if period is present

 for i in range(0, len(s)):

 if(s[i] == '.'):

 counter = counter+1

 if(counter != 3):

 return 0

 

 # check the range of numbers between periods

 st = set()

 for i in range(0, 256):

 st.add(str(i))

 counter = 0

 temp = ""

 for i in range(0, len(s)):

 if(s[i] != '.'):

 temp = temp+s[i]

 else:

 if(temp in st):

 counter = counter+1

 temp = ""

 if(temp in st):

 counter = counter+1

 

 # verifying all conditions

 if(counter == 4):

 return 'Valid Ip address'

 else:

 return 'Invalid Ip addess'

 

 

# Driver Code

print(isValidIP('110.234.52.124'))  
  
---  
  
 __

 __

 **Output:**

    
    
    Valid Ip address

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

