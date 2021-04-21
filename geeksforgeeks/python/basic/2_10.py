How to Pass Arguments to Tkinter Button Command?



Tkinter is the standard GUI library for Python. Tkinter is the Python
interface to the Tk GUI toolkit shipped with Python. It provides a robust and
platform independent windowing toolkit, that is available to Python
programmers using this package. Python when combined with Tkinter provides a
fast and easy way to create GUI applications. Tkinter provides a powerful
object-oriented interface to the Tk GUI toolkit.

###  **Approach**

  * Import tkinter package.
  * Create a root window. Give the root window a title(using title()) and dimension(using geometry()).
  * Create a button using (Button()).
  * Use mainloop() to call the endless loop of the window.

These steps remain same for both methods, only thing that has to be changed is
how to apply these two methods.

 **Method 1: Using lambda function**

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# importing tkinter

import tkinter as tk

 

# defining function

 

 

def func(args):

 print(args)

 

 

# create root window

root = tk.Tk()

 

# root window title and dimension

root.title("Welcome to GeekForGeeks")

root.geometry("380x400")

 

# creating button

btn = tk.Button(root, text="Press", command=lambda:
func("See this worked!"))

btn.pack()

 

# running the main loop

root.mainloop()  
  
---  
  
 __

 __

**Output:**  

  

  

![](https://media.geeksforgeeks.org/wp-
content/uploads/20201203210052/usinglambda20201203204724.gif)

using lambda

 **Method 2: Using partial**

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# importing necessary libararies

from functools import partial

import tkinter as tk

 

# defining function

 

 

def function_name(func):

 print(func)

 

 

# creating root window

root = tk.Tk()

 

# root window title and dimension

root.title("Welcome to GeekForGeeks")

root.geometry("380x400")

 

# creating button

btn = tk.Button(root, text="Click Me", command=partial(

 function_name, "Thanks, Geeks for Geeks !!!"))

btn.pack()

 

# running the main loop

root.mainloop()  
  
---  
  
 __

 __

 **Output:**

![](https://media.geeksforgeeks.org/wp-
content/uploads/20201203210412/usingpartial20201203204931.gif)

using partal

  

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

