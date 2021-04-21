Display Hostname and IP address in Python



There are many ways to find hostname and IP address of a local machine. Here
is a simple method to find hostname and IP address using python code.  
Library used – **socket** : This module provides access to the BSD socket
interface. It is available on all modern Unix systems, Windows, MacOS, and
probably additional platforms.  
 **  
Method used :**

  *  **gethostname()** : The gethostname function retrieves the standard host name for the local computer.
  *  **gethostbyname()** : The gethostbyname function retrieves host information corresponding to a host name from a host database.

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to display hostname and

# IP address

 

# Importing socket library

import socket

 

# Function to display hostname and

# IP address

def get_Host_name_IP():

 try:

 host_name = socket.gethostname()

 host_ip = socket.gethostbyname(host_name)

 print("Hostname : ",host_name)

 print("IP : ",host_ip)

 except:

 print("Unable to get Hostname and IP")

 

# Driver code

get_Host_name_IP() #Function call

 

#This code is conributed by "Sharad_Bhardwaj".  
  
---  
  
 __

 __

Output:

    
    
    Hostname :   pppContainer
    IP :  10.98.162.168
    

**NOTE** : Output varies machine to machine.

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

