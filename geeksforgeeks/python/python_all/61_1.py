Python program to determine if the given IP Address is Public or Private using
ipaddress module



  
Given a Classful IP Address the task is to find whether it is Public or
Private.

 **Private IP address** of a system is the IP address which is used to
communicate within the same network. Using private IP data or information can
be sent or received within the same network.

 **Public IP address** of a system is the IP address which is used to
communicate outside the network. Public IP address is basically assigned by
the ISP (Internet Service Provider).

 **Examples:**

    
    
    **Input :** 17.5.7.8
    **Output :** Public
    
    **Input :** 172.16.0.10
    **Output :** Private
    

To implement it, we will use is_private method of ipaddress module of Python
3.3 .

  

  

 __

 __  
 __

 __

 __  
 __  
 __

# importing ip_address from

# ip address module

from ipaddress import ip_address

 

def IPAddress(IP: str) -> str:

 return "Private" if (ip_address(IP).is_private) else "Public"

 

if __name__ == '__main__' : 

 

 # Public IP

 print(IPAddress('17.5.7.8')) 

 

 # Private IP

 print(IPAddress('172.16.0.10'))  
  
---  
  
 __

 __

 **Output :**

    
    
    Public
    Private

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

