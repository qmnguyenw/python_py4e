GUI to Shutdown, Restart and Logout from the PC using Python



In this article, we are going to write a python script to shut down or Restart
or Logout your system and bind it with GUI Application.

The **OS module** in Python provides functions for interacting with the
operating system. OS is an inbuilt library python.

 **Syntax :**

>  **For shutdown your system :** os.system(“shutdown /s /t 1”)
>
>  **For restart your system :** os.system(“shutdown /r /t 1”)
>
>  
>
>
>  
>
>
>  **For Logout your system :** os.system(“shutdown -l”)

 **Implementation GUI Application using Tkinter:**

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# import modules

from tkinter import *

import os

 

 

# user define funtion

def shutdown():

 return os.system("shutdown /s /t 1")

 

def restart():

 return os.system("shutdown /r /t 1")

 

def logout():

 return os.system("shutdown -l")

 

 

# tkinter object

master = Tk()

 

# background set to grey

master.configure(bg='light grey')

 

# creating a button using the widget

# Buttons that will call the submit function

Button(master, text="Shutdown",
command=shutdown).grid(row=0)

Button(master, text="Restart", command=restart).grid(row=1)

Button(master, text="Log out", command=logout).grid(row=2)

 

mainloop()  
  
---  
  
 __

 __

 **Output:**

![](https://media.geeksforgeeks.org/wp-
content/uploads/20201028153147/Screenshot256.png)

 **Note:** _Please ensure that you save and close all the_ programs _before
running this code on the IDLE, as this program will immediately shutdown and
restart your computer._

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

