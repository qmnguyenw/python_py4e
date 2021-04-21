Python | Creating a button in tkinter



Tkinter is Python’s standard GUI (Graphical User Interface) package. It is one
of the most commonly used packages for GUI applications which comes with
Python itself. Let’s see how to create a button using Tkinter.  

**Follow the below steps:**

  1. Import tkinter module # Tkinter in Python 2.x. (Note Capital T)
  2. Create main window (root = Tk())
  3. Add as many widgets as you want.   

Importing tkinter module is same as importing any other module.  

    
    
    import tkinter   # In Python 3.x
    
    import Tkinter   # In python 2.x. (Note Capital T)

The **tkinter.ttk** module provides access to the Tk-themed widget set,
introduced in Tk 8.5. If Python has not been compiled against Tk 8.5, this
module can still be accessed if _Tile_ has been installed. The former method
using Tk 8.5 provides additional benefits including anti-aliased font
rendering under X11 and window transparency.  
The basic idea for **tkinter.ttk** is to separate, to the extent possible, the
code implementing a widget’s behavior from the code implementing its
appearance. **tkinter.ttk** is used to create modern GUI (Graphical User
Interface) applications that cannot be achieved by _tkinter_ itself.  

**Code #1:** Creating button using Tkinter.

  

  

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# import everything from tkinter module

from tkinter import *

# create a tkinter window

root = Tk() 

# Open window having dimension 100x100

root.geometry('100x100')

# Create a Button

btn = Button(root, text = 'Click me !', bd = '5',

 command = root.destroy)

# Set the position of button on the top of window. 

btn.pack(side = 'top') 

root.mainloop()  
  
---  
  
 __

 __

 **Output:**

![](https://media.geeksforgeeks.org/wp-content/uploads/20190306214501/Tkinter-
button-without-tk-themed-widget.jpg)

https://media.geeksforgeeks.org/wp-
content/uploads/20210216123330/FreeOnlineScreenRecorderProject3.mp4

  
**Creation of Button without using** _ **tk**_ **themed widget.**  

Creation of Button using **tk** themed widget (tkinter.ttk). This will give
you the effects of modern graphics. Effects will change from one OS to another
because it is basically for the appearance.  

**Code #2:**  

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# import tkinter module

from tkinter import *

# Following will import tkinter.ttk module and

# automatically override all the widgets

# which are present in tkinter module.

from tkinter.ttk import *

# Create Object

root = Tk()

# Initialize tkinter window with dimensions 100x100 

root.geometry('100x100') 

btn = Button(root, text = 'Click me !',

 command = root.destroy)

# Set the position of button on the top of window

btn.pack(side = 'top') 

root.mainloop()  
  
---  
  
 __

 __

 **Output:**

![](https://media.geeksforgeeks.org/wp-content/uploads/20190306215951/Tkinter-
button-using-tk-themed-widget.jpg)

https://media.geeksforgeeks.org/wp-
content/uploads/20210216123333/FreeOnlineScreenRecorderProject4.mp4

 **Note:** See in the Output of both the code, BORDER is not present in 2nd
output because **tkinter.ttk** does not support border. Also, when you hover
the mouse over both the buttons ttk.Button will change its color and become
light blue (effects may change from one OS to another) because it supports
modern graphics while in the case of a simple Button it won’t change color as
it does not support modern graphics.  

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

