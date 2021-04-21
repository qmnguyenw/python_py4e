Python Script to Shutdown Computer



As we know, Python is a popular scripting language because of its versatile
features. In this article, we will write a Python script to shutdown a
computer.  
To shut down the computer/PC/laptop by using a Python script, you have to use
the os.system() function with the code “shutdown /s /t 1” .

>  **Note:** For this to work, you have to import os library in the ide. If
> you don’t have it, then ‘pip install os‘ through the Command Prompt.
>
>  **Causion:** Please ensure that you save and close all the program before
> running this code on the IDLE, as the below program will immediately shut
> down your computer.

Below is the Python implementation –

 __

 __  
 __

 __

 __  
 __  
 __

import os

 

shutdown = input("Do you wish to shutdown your computer ? (yes / no):
")

 

if shutdown == 'no':

 exit()

else:

 os.system("shutdown /s /t 1")  
  
---  
  
 __

 __

 **Output:**  
![Organized Folder](https://media.geeksforgeeks.org/wp-
content/uploads/20190709235822/shutdown.png)

  

  

Here is the Python Program which will ask the user to shut down the computer
providing the option of Yes or No. Also, when you type yes & then press the
ENTER key, the system will be shut down instantly.

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

