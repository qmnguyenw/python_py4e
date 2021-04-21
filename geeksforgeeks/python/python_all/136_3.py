Python Script to Restart Computer



As we know, Python is a popular scripting language because of its versatile
features. In this article, we will write a Python script to restart a
computer. Let’s start with how to restart the system with Python.

>  **Note:** For this to work, you have to import os library in the ide. If
> you don’t have it, then ‘pip install os‘ through the Command Prompt.
>
>  **Causion:** Please ensure that you save and close all the program before
> running this code on the IDLE, as the below program will immediately restart
> your computer.

Below is the Python implementation –

 __

 __  
 __

 __

 __  
 __  
 __

import os

 

restart = input("Do you wish to restart your computer ? (yes / no):
")

 

if restart == 'no':

 exit()

else:

 os.system("shutdown /r /t 1")  
  
---  
  
 __

 __

 **Output:**  
![Restart](https://media.geeksforgeeks.org/wp-
content/uploads/20190710002915/restarb.png)  
Here is the Python Program which will ask the user to restart the computer
providing the option of Yes or No. Also, when you type yes & then press the
ENTER key, the system will be restart instantly.

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

