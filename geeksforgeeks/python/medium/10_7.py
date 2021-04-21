Port Scanner using Python



 **Prerequisites:** Socket Programming in Python

This article is just to provide a sample code to generate a Port Scanner. This
Port Scanner will work for both the Web Applications as well as remote Host.
This tool has been created to provide the basic functionality of a Port
Scanner. The general concept of Sockets had been used to provide the
functionality. Port Scanner is built on Python 3 and uses some extra libraries
such as socket and pyfiglet (for a fancy banner).

Please find the below source code for the Port Scanner :  
 **Source Code**

 __

 __  
 __

 __

 __  
 __  
 __

import pyfiglet

import sys

import socket

from datetime import datetime

 

ascii_banner = pyfiglet.figlet_format("PORT SCANNER")

print(ascii_banner)

 

# Defining a target

if len(sys.argv) == 2:

 

 # translate hostname to IPv4

 target = socket.gethostbyname(sys.argv[1]) 

else:

 print("Invalid ammount of Argument")

 

# Add Banner 

print("-" * 50)

print("Scanning Target: " + target)

print("Scanning started at:" + str(datetime.now()))

print("-" * 50)

 

try:

 

 # will scan ports between 1 to 65,535

 for port in range(1,65535):

 s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

 socket.setdefaulttimeout(1)

 

 # returns an error indicator

 result = s.connect_ex((target,port))

 if result ==0:

 print("Port {} is open".format(port))

 s.close()

 

except KeyboardInterrupt:

 print("\n Exitting Program !!!!")

 sys.exit()

except socket.gaierror:

 print("\n Hostname Could Not Be Resolved !!!!")

 sys.exit()

except socket.error:

 print("\ Server not responding !!!!")

 sys.exit()  
  
---  
  
 __

 __

 **Output:**

![python-port-scanner](https://media.geeksforgeeks.org/wp-
content/uploads/20200408183118/python-port-scanner.png)

  

  

 **Note:** In the above code at line 27 i.e for the port in range(1, 65535):
you can custom define your ports under which range you have to scan. This port
scanner will generally take the time of 2 mins maximum to produce output in
the format, that so and so ports are open or closed.

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

