Getting Saved Wifi Passwords using Python



Usually while connecting with the wifi we have to enter some password to
access the network, but we are not directly able to see the password we have
entered earlier i.e password of saved network. In this article, we will see
how we can get all the saved WiFi name and passwords using Python, in order to
do this we will use subprocess module of python.  
 **Wi-Fi** is a wireless networking technology that allows devices such as
computers (laptops and desktops), mobile devices (smartphones and wearables),
and other equipment (printers and video cameras) to interface with the
Internet.  
The **subprocess** module present in Python(both 2.x and 3.x) is used to run
new applications or programs through Python code by creating new processes. It
also helps to obtain the input/output/error pipes as well as the exit codes of
various commands.  

> **Steps for Implementation :**  
>  1\. Import the subprocess module  
> 2\. Get the metadata of the wlan(wifi) with the help of check_output method  
> 3\. Decode the metadata and split the meta data according to the line  
> 4\. From the decoded metadata get the names of the saved wlan networks  
> 5\. Now for each name again get the metadata of wlan according to the name  
> 6\. Start try and catch block and inside the try block, decode and split
> this metadata and get the password of the given wifi name  
> 7\. Print the password and the wifi name and print blank if there is no
> password  
> 8\. In except block if process error occurred print encoding error occurred  
>

Below is the implementation  

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# importing subprocess

import subprocess

# getting meta data

meta_data = subprocess.check_output(['netsh', 'wlan', 'show',
'profiles'])

# decoding meta data

data = meta_data.decode('utf-8', errors ="backslashreplace")

# spliting data by line by line

data = data.split('\n')

# creating a list of profiles

profiles = []

# traverse the data

for i in data:

 

 # find "All User Profile" in each item

 if "All User Profile" in i :

 

 # if found

 # split the item

 i = i.split(":")

 

 # item at index 1 will be the wifi name

 i = i[1]

 

 # formatting the name

 # first and last chracter is use less

 i = i[1:-1]

 

 # appending the wifi name in the list

 profiles.append(i)

 

# printing heading 

print("{:<30}| {:<}".format("Wi-Fi Name", "Password"))

print("----------------------------------------------")

# traversing the profiles 

for i in profiles:

 

 # try catch block beigins

 # try block

 try:

 # getting meta data with password using wifi name

 results = subprocess.check_output(['netsh', 'wlan',
'show', 'profile', i, 'key = clear'])

 

 # decoding and splitting data line by line

 results = results.decode('utf-8', errors
="backslashreplace")

 results = results.split('\n')

 

 # finding password from the result list

 results = [b.split(":")[1][1:-1] for b in
results if "Key Content" in b]

 

 # if there is password it will print the pass word

 try:

 print("{:<30}| {:<}".format(i, results[0]))

 

 # else it will print blank in fornt of pass word

 except IndexError:

 print("{:<30}| {:<}".format(i, ""))

 

 

 

 # called when this process get failed

 except subprocess.CalledProcessError:

 print("Encoding Error Occured")  
  
---  
  
 __

 __

 **Output :**  

  

  

    
    
    Wi-Fi Name                    | Password
    -----------------------------------------------
    Engineer                      | ayush123
    honor                         | 1234567890
    Engineer_5GHz                 | ayush123
    Redmi                         | 12345677
    Ayush                         | 123123123
    BiGX-cmtqaGFtYjc              | rakshit123
    UERJTTBV8e0GUmVkbWkg 2        | 987654321
    DESKTOP-F32H70N 5009          | SUSHANT@123
    UERJTTBV8e0GUmVkbWkg          | 
    Bunns                         | heyhotspot
    Hogwarts                      | sushant@123
    Cgc wireless                  | database1234
    Moto G (5) Plus 8691          | rakshit123
    AndroidAP                     | udrw7859
    AndroidAPab7e                 | 123000123
    roshan                        | 12345678
    Svj?                          | salonivij
    Hey                           | heythere
    AndroidAP202                  | bhuvanbroo
    JARVIS                        | abhishek09
    B6NO-wq5hamF0IGt1bWHCrg       | 12345678
    CDAC                          | 

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

