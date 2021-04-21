Python program to find the type of IP Address using Regex



 **Prerequisite:** Python Regex

Given an IP address as input, write a Python program to find the type of IP
address i.e. either **IPv4** or **IPv6**. If the given is neither of them then
print neither.

###  **What is an IP (Internet Protocol) Address?**

Every computer connected to the Internet is identified by a unique four-part
string, known as its Internet Protocol (IP) address. **IPv4** and **IPv6** are
internet protocol version 4 and internet protocol version 6, IP version 6 is
the new version of Internet Protocol, which is way better than IP version 4 in
terms of complexity and efficiency.

  *  **IPv4** was the primary version brought into action for production within the ARPANET in 1983. IP version four addresses are 32-bit integers which will be expressed in hexadecimal notation.
  *  **IPv6** was developed by the Internet Engineering Task Force (IETF) to deal with the problem of IP v4 exhaustion. IP v6 is 128-bits address having an address space of 2128, which is way bigger than IPv4. In IPv6 we use Colon-Hexa representation. There are 8 groups and each group represents 2 Bytes.

 **Examples:**

    
    
     **Input:** 192.0.2.126
    **Output:** IPv4
    
    **Input:** 3001:0da8:75a3:0000:0000:8a2e:0370:7334
    **Output:** IPv6
    
    **Input:** 36.12.08.20.52
    **Output:** Neither

###  **Approach:**

  * Take the IP address as input.
  * Now, check if this IP address resembles IPv4 type addresses using regex.
  * If yes, then print “IPv4” else check if this IP address resembles IPv6 type addresses using regex.
  * If yes, then print “IPv6”.
  * If the address doesn’t resemble any of the above types then we will print “Neither”.

 **Below is the implementation of the above approach:**

  

  

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# Python program to find the type of Ip address

 

# re module provides support 

# for regular expressions

import re

 

# Make a regular expression 

# for validating an Ipv4

ipv4 = '''^(25[0-5]|2[0-4][0-9]|[0-1]?[0-9][0-9]?)\.( 

 25[0-5]|2[0-4][0-9]|[0-1]?[0-9][0-9]?)\.( 

 25[0-5]|2[0-4][0-9]|[0-1]?[0-9][0-9]?)\.( 

 25[0-5]|2[0-4][0-9]|[0-1]?[0-9][0-9]?)$'''

 

# Make a regular expression 

# for validating an Ipv6

ipv6 = '''(([0-9a-fA-F]{1,4}:){7,7}[0-9a-fA-F]{1,4}|

 ([0-9a-fA-F]{1,4}:){1,7}:|([0-9a-fA-F]{1,4}:)

 {1,6}:[0-9a-fA-F]{1,4}|([0-9a-fA-F]{1,4}:){1

 ,5}(:[0-9a-fA-F]{1,4}){1,2}|([0-9a-fA-F]{1,4}

 :){1,4}(:[0-9a-fA-F]{1,4}){1,3}|([0-9a-fA-F]{

 1,4}:){1,3}(:[0-9a-fA-F]{1,4}){1,4}|([0-9a-fA

 -F]{1,4}:){1,2}(:[0-9a-fA-F]{1,4}){1,5}|[0-9a

 -fA-F]{1,4}:((:[0-9a-fA-F]{1,4}){1,6})|:((:[0

 -9a-fA-F]{1,4}){1,7}|:)|fe80:(:[0-9a-fA-F]{0,

 4}){0,4}%[0-9a-zA-Z]{1,}|::(ffff(:0{1,4}){0,1}

 :){0,1}((25[0-5]|(2[0-4]|1{0,1}[0-9]){0,1}[0-9

 ])\.){3,3}(25[0-5]|(2[0-4]|1{0,1}[0-9]){0,1}[0

 -9])|([0-9a-fA-F]{1,4}:){1,4}:((25[0-5]|(2[0-4]

 |1{0,1}[0-9]){0,1}[0-9])\.){3,3}(25[0-5]|(2[0-4]

 |1{0,1}[0-9]){0,1}[0-9]))'''

 

# Define a function for finding 

# the type of Ip addess 

def find(Ip): 

 

 # pass the regular expression 

 # and the string in search() method

 if re.search(ipv4, Ip):

 print("IPv4")

 elif re.search(ipv6, Ip):

 print("IPv6")

 else:

 print("Neither")

 

# Driver Code 

if __name__ == '__main__' : 

 

 # Enter the Ip address 

 Ip = "192.0.2.126"

 

 # calling run function 

 find(Ip) 

 

 Ip = "3001:0da8:75a3:0000:0000:8a2e:0370:7334"

 find(Ip) 

 

 Ip = "36.12.08.20.52"

 find(Ip)  
  
---  
  
 __

 __

 **Output:**

    
    
    IPv4
    IPv6
    Neither

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

