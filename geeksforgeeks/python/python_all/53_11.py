Place_forget() method using Tkinter in Python



To hide or forget a widget from the parent widget or screen in **tkinter**,
the **place_forget(** ) method is used on that widget based on place geometry
management.

>  **Syntax** : widget.place_forget()
>
> **Parameter:** None  
>  **Return:** None

Below is the implementation :

## Python3

  

  

 __

 __  
 __

 __

 __  
 __  
 __

# Imports everything from tkinter

# and ttk module

from tkinter import *

from tkinter.ttk import *

 

# toplevel window

root = Tk()

 

# setting window size

root.geometry("150x100")

 

# label widget

label = Label(root, text="LABEL")

 

# place in the window

label.place(relx=0.4, y=5)

 

# button widgets

# In command attribute of Button,

# place_forget() method is passed

# in the lambda function to temporarily

# hide the label

b1 = Button(root, text = "hide text",

 command = lambda: label.place_forget())

 

b1.place(relx = 0.3, y = 30)

 

# the label is placed again

b2 = Button(root, text = "retrieve text",

 command = lambda: label.place(

 relx = 0.4))

 

b2.place(relx = 0.3, y = 50)

 

# Start the GUI

root.mainloop()  
  
---  
  
 __

 __

