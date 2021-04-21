How to Get the Tkinter Label Text?



 **Prerequisite:**Python GUI – Tkinter

Python offers multiple options for developing a GUI (Graphical User
Interface). Out of all the GUI methods, _tkinter_ is the most commonly used
method. It is a standard Python interface to the Tk GUI toolkit shipped with
Python. Python with _tkinter_ is the fastest and easiest way to create GUI
applications. Creating a GUI using tkinter is an easy task.

In this article, we are going to write a Python script to get the _tkinter_
label text. Below are the various methods discussed:

 **Method #1:** Using _cget()_ method.

 **Approach:**

  

  

  * Importing the module.
  * Create the main window (container).
  * Add Label widgets to the main window.
  * Apply the _cget()_ method and get label text.

 **Implementation:**

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# import modules

import tkinter as tk

 

# object of tkinter

# and background set for light grey

master = tk.Tk()

master.configure(bg='light grey')

 

# create label

l = tk.Label(master,

 text="Welcome to geeksforgeeks",

 bg="red")

 

# apply cget()

print("Label text: ", l.cget("text"))

 

l.pack()

master.mainloop()  
  
---  
  
 __

 __

 **Output:**

![](https://media.geeksforgeeks.org/wp-
content/uploads/20201205201908/Capture.PNG)

 **Method #2:** Using Dictionary label object.

 **Approach:**

  * Importing the module.
  * Create the main window (container).
  * Add Label widgets to the main window.
  * Use Dictionary label object and get label text.

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# import modules

import tkinter as tk

 

# object of tkinter 

# and background set for light grey 

master = tk.Tk() 

master.configure(bg = 'light grey') 

 

# create label

l = tk.Label(master, 

 text = "Welcome to geeksforgeeks", 

 bg = "red")

 

# using dictionary label object

print("Label text: ", l["text"])

 

l.pack()

tk.mainloop()  
  
---  
  
 __

 __

 **Output:**

![](https://media.geeksforgeeks.org/wp-
content/uploads/20201205201908/Capture.PNG)  

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

