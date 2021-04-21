Python program to determine if the given IPv4 Address is reserved using
ipaddress module



  
Given a IPv4 Address, the task is to determine whether it is reserved (i.e
belongs to class E) or not.

 **What is class E?**

IP addresses belonging to class E are reserved for experimental and research
purposes. IP addresses of class E range from 240.0.0.0 – 255.255.255.254. This
class doesn’t have any sub-net mask. The higher-order bits of the first octet
of class E is always set to 1111.

 **Examples:**

    
    
    **Input :** 10.0.0.1
    **Output :** Not Reserved
    
    **Input :** 241.0.0.133
    **Output :** Reserved
    

To implement it, we will use the **is_reserved** method of **ipaddress**
module of Python3.3.

  

  

 __

 __  
 __

 __

 __  
 __  
 __

# importing ip_address

# from ipaddress module

from ipaddress import ip_address

 

def reservedIPAddress(IP: str) -> str:

 return "Reserved" if (ip_address(IP).is_reserved) else "Not
Reserved"

 

if __name__ == '__main__' : 

 

 # Not Reserved

 print(reservedIPAddress('10.0.0.1')) 

 

 # Reserved

 print(reservedIPAddress('241.0.0.133'))   
  
---  
  
__

__

**Output :**

    
    
    Not Reserved
    Reserved
    

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

