Python Script to Logout Computer



As we know, Python is a popular scripting language because of its versatile
features. In this article, we will write a Python script to logout a computer.
Let’s start with how to logout the system with Python. To logout your
computer/PC/laptop only by using a Python script, you have to use the
os.system() function with the code “shutdown -l” . The **shutdown -l** command
is the windows shell command for logging off.

Let’s start with how to log out the system with Python.

>  **Note:** For this to work, you have to import os library in the ide. If
> you don’t have it, then ‘pip install os‘ through the Command Prompt.
>
>  **Causion:** Please ensure that you save and close all the program before
> running this code on the IDLE, as the below program will immediately log out
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

 

logout = input("Do you wish to log out your computer ? (yes / no):
")

 

if logout == 'no':

 exit()

else:

 os.system("shutdown -l")  
  
---  
  
 __

 __

 **Output:**  
![](https://media.geeksforgeeks.org/wp-
content/uploads/20190710004213/ogor.png)  
Here is the Python Program which will ask the user to log out the computer
providing the option of Yes or No. Also, when you type yes & then press the
ENTER key, the system will be log out instantly.

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

