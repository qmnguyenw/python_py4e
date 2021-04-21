How to Close a Tkinter Window With a Button?



 **Prerequisites:** Tkinter

Python’s Tkinter module offers the Button function to create a button in a
Tkinter Window to execute any task once the button is clicked. The task can be
assigned in the _command_ parameter of **Button()** function. Given below are
various methods by which this can be achieved.

###  **Method 1: Using destroy() Non-Class method**

 **Approach:**

  * Import tkinter module.
  * Create a main window named root.
  * Add a button.
  * Assign **root.destroy** to the command attribute of that button.

 **Example:** _ **** Using destroy() directly in command attribute_

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# Python program to create a close button

# using destroy Non-Class method

from tkinter import *

 

# Creating the tkinter window

root = Tk()

root.geometry("200x100")

 

# Button for closing

exit_button = Button(root, text="Exit", command=root.destroy)

exit_button.pack(pady=20)

 

root.mainloop()  
  
---  
  
 __

 __

 **Example:** _Using destroy() in a function_

## Python3

  

  

 __

 __  
 __

 __

 __  
 __  
 __

# Python program to create a close button

# using destroy Non-Class method

from tkinter import *

 

# Creating the tkinter window

root = Tk()

root.geometry("200x100")

 

# Function for closing window

 

 

def Close():

 root.destroy()

 

 

# Button for closing

exit_button = Button(root, text="Exit", command=Close)

exit_button.pack(pady=20)

 

root.mainloop()  
  
---  
  
 __

 __

