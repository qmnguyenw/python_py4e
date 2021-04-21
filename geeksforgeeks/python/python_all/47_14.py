Python – Getting all the Wifi Devices the system has connected



In this article we will see how we can all those wifi network on which the
system is ever connected to. Wi-Fi is a wireless networking technology that
allows devices such as computers (laptops and desktops), mobile devices (smart
phones and wearables), and other equipment (printers and video cameras) to
interface with the Internet.

In order to do this we will use the subprocess module. The subprocess module
present in Python(both 2.x and 3.x) is used to run new applications or
programs through Python code by creating new processes. It also helps to
obtain the input/output/error pipes as well as the exit codes of various
commands.

In order to get the information about the wifi devices system is connected to
we will use the command given below

    
    
    subprocess.check_output(['netsh', 'wlan', 'show', 'profiles'])
    

This command will return the meta data in bytes format in order to get the
names of network we have to decode and filter it to get the desired output.

Below is the implementation

  

  

 __

 __  
 __

 __

 __  
 __  
 __

# importing subprocess

import subprocess

 

# getting meta data of the wifi network

meta_data = subprocess.check_output(['netsh', 'wlan', 'show',
'profiles'])

 

# decoding meta data from byte to string

data = meta_data.decode('utf-8', errors ="backslashreplace")

 

# spliting data by line by line

# string to list

data = data.split('\n')

 

# creating a list of wifi names

names = []

 

# traverse the list 

for i in data:

 

 # find "All User Profile" in each item

 # as this item will have the wifi name

 if "All User Profile" in i :

 

 # if found split the item

 # in order to get only the name

 i = i.split(":")

 

 # item at index 1 will be the wifi name

 i = i[1]

 

 # formatting the name

 # first and last chracter is use less

 i = i[1:-1]

 

 # appending the wifi name in the list

 names.append(i)

 

# printing the wifi names

print("All wifi that system has connected to are ")

print("-----------------------------------------")

for name in names:

 print(name)  
  
---  
  
 __

 __

 **Output :**

    
    
    All wifi that system has connected to are 
    -----------------------------------------
    Engineer_5GHz
    Engineer
    honor
    Redmi
    Ayush
    BiGX-cmtqaGFtYjc
    UERJTTBV8e0GUmVkbWkg 2
    DESKTOP-F32H70N 5009
    UERJTTBV8e0GUmVkbWkg
    Bunns
    Hogwarts
    Cgc wireless
    Moto G (5) Plus 8691
    AndroidAP
    AndroidAPab7e
    roshan
    Svj?
    Hey
    AndroidAP202
    JARVIS
    B6NO-wq5hamF0IGt1bWHCrg
    CDAC
    

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

