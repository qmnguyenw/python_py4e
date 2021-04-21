How to Delete Tkinter Text Box’s Contents?



 **Prerequisite:**

  * Python GUI – tkinter
  * Text Widget

Python offers multiple options for developing GUI (Graphical User Interface)
out of which Tkinter is the most preferred means. It is a standard Python
interface to the Tk GUI toolkit shipped with Python. Python with Tkinter is
the fastest, most reliable and easiest way to create a desired GUI
application.

## **What is Text Widget?**

The Text widget is used to for showing text data on the Python application.
However, Tkinter supports Entry widget which can be used to implement a single
line text box. But, a text widget can be used to display the multi-line
formatted text with various styles and attributes.

### Approach

  * Import module
  * Create a normal Tkinter window.
  * Add text Box

 **Syntax:**

    
    
    Text(Object Name, **attr)

  * For deleting content from Text Box, we will create a delete button to implement delete method. Clicking on this button will erase the content written in the text box.

 **Syntax:**

  

  

    
    
    Object_name.delete(first=number, last=number)

Given below is the program to implement the same:

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# Import Module

from tkinter import *

 

# Create Object

root = Tk()

 

# specify size of window.

root.geometry("400x500")

 

# delete content from Text Box

 

 

def delete_text():

 T.delete("1.0", "end")

 

 

# Create text widget

T = Text(root)

T.pack()

 

# Create Delete Button

Button(root, text="Delete", command=delete_text).pack()

 

# Excute Tkinter

root.mainloop()  
  
---  
  
 __

 __

 **Output:**

https://media.geeksforgeeks.org/wp-
content/uploads/20201203184322/FreeOnlineScreenRecorderProject1.mp4

  

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

