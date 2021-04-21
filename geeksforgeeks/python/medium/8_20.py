What are Widgets in Tkinter?



 **Tkinter** is Python’s standard GUI (Graphical User Interface) package.
**tkinter** provides us with a variety of common GUI elements which we can use
to build out interface – such as buttons, menus and various kind of entry
fields and display areas. We call these elements **Widgets**.

##  **Widgets**

In general, **Widget** is an element of Graphical User Interface (GUI) that
displays/illustrates information or gives a way for the user to interact with
the OS. In **Tkinter** , **W** **idgets** are objects ; instances of classes
that represent buttons, frames, and so on.

Each separate widget is a Python object. When creating a widget, you must pass
its parent as a parameter to the widget creation function. The only exception
is the “root” window, which is the top-level window that will contain
everything else and it does not have a parent.

**Example :**

## Python

  

  

 __

 __  
 __

 __

 __  
 __  
 __

from tkinter import *

 

 

# create root window

root = Tk() 

 

# frame inside root window

frame = Frame(root) 

 

# geometry method

frame.pack() 

 

# button inside frame which is 

# inside root

button = Button(frame, text ='Geek') 

button.pack() 

 

# Tkinter event loop

root.mainloop()   
  
---  
  
__

__

