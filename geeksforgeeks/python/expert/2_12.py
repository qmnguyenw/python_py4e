How to close a window in Tkinter?



Python offers multiple options for developing GUI (Graphical User Interface).
Out of all the GUI methods, _tkinter_ is the most commonly used method. It is
a standard Python interface to the Tk GUI toolkit shipped with Python. Python
with _tkinter_ is the fastest and easiest way to create GUI applications.
Creating a GUI using _tkinter_ is an easy task.

To close a _tkinter_ window, we can use the _destroy()_ method. The
_destroy()_ is a universal widget method i.e we can use this method with any
of the available widgets as well as with the main _tkinter_ window.

 **Example:**

In the below example, we are going to implement the _destroy()_ method using a
button.

## Python

  

  

 __

 __  
 __

 __

 __  
 __  
 __

# import required module

from tkinter import *

 

# create object

root = Tk()

 

# create button to implement destroy()

Button(root, text="Quit", command=root.destroy).pack()

 

root.mainloop()  
  
---  
  
 __

 __

