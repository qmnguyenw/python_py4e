Python program to find if two IP Address belongs to Same or Different Network



 **Prerequisites:** Classless Inter Domain Routing (CIDR)

Given two IP Addresses in CIDR Notation determine whether they belong to Same
Network or Different Network. Two IP addresses are said to be in Same Network
if the Network ID of both the IP Addresses are same.

 **Examples:**

>  **Input :** IP1 = 192.168.1.0/8, IP2 = 192.32.45.7/8  
>  **Output :** Same Network  
>  **Explanation :** The number of bits in Network ID of both the IP Addresses
> is 8 bits and the first  
> 8 bits (i.e 1st octet) of both the IP Addresses is same (i.e 192). Hence
> both IP Addresses  
> belong to Same Network.
>
>  **Input :** IP1 = 17.53.128.0/20, IP2 = 17.53.127.0/20  
>  **Output :** Different Network  
>  **Explanation :** The number of bits in Network ID of both the IP Addresses
> is 20 bits but the first  
> 20 bits of both the IP Addresses are different. Hence both IP Addresses
> belong to Different  
> Network.
>
>  
>
>
>  
>

To implement it, we will use **ip_network** and **network_address** method of
ipaddress module of Python 3.3 .

 __

 __  
 __

 __

 __  
 __  
 __

# importing ip_network from ipaddress module

from ipaddress import ip_network

 

def sameNetwork(IP1: str, IP2: str) -> str:

 

 a = ip_network(IP1, strict = False).network_address

 b = ip_network(IP2, strict = False).network_address

 

 if(a == b) :

 return "Same Network"

 

 else :

 return "Different Network"

 

# main function 

if __name__ == '__main__' : 

 

 # Same Network 

 print(sameNetwork('192.168.1.0/8', '192.32.45.7/8')) 

 

 # Different Network 

 print(sameNetwork('17.53.128.0/20', '17.53.127.0/20'))

   
  
---  
  
__

__

**Output :**

    
    
    Same Network
    Different Network

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

