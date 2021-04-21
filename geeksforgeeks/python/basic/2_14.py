How to Create Full Screen Window in Tkinter?



 **Prerequisite:**Tkinter

There are two ways to create a full screen window in tkinter using standard
python library for creating GUI applications.

### Method 1: **Using attributes() function**

 **Syntax:**

    
    
    window_name.attributes('-fullscreen',True)

We will set the parameter _**‘-fullscreen’**_ of attributes() to _ **True**_
for setting size of our window to fullscreen and to False otherwise.

**Approach:**

  

  

  * Importing tkinter package
  * Creating a tkinter window with name window
  * Setting the window attribute fullscreen as True
  * Giving title to the window, here ‘Geeks For Geeks’
  * Creating a label with text ‘Hello Tkinter’ (just for display to the user here)
  * Placing the label widget using pack()
  * Closing the endless loop of windows by calling mainloop()

 **Disadvantage:**

We get an output tkinter WINDOW with no toolbar. This disadvantage is covered
by the next method.

 **Program**

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# importing tkinter for gui

import tkinter as tk

 

# creating window

window = tk.Tk()

 

# setting attribute

window.attributes('-fullscreen', True)

window.title("Geeks For Geeks")

 

# creating text label to display on window screen

label = tk.Label(window, text="Hello Tkinter!")

label.pack()

 

window.mainloop()  
  
---  
  
 __

 __

 **Output:**

![](https://media.geeksforgeeks.org/wp-content/uploads/20201203120920/gfg.jpg)

### Method 2: Using geometry() function

We get an output tkinter window with the toolbar above along with the title of
window.

**Syntax:**

  

  

> width= window_name.winfo_screenwidth()
>
> height= window_name.winfo_screenheight()
>
> window_name.geometry(“%dx%d” % (width, height))

We can set the parameter of _ **geometry()**_ same as the width*height of the
screen of our original window _ ****_ to get our full screen tkinter window
without making the toolbar invisible. We can get the width and height of our
desktop screen by using ****_**winfo_screenwidth()** and
**winfo_screenheight()** _functions respectively.

**Approach:**

  * Importing tkinter package
  * Creating a tkinter window with name window
  * Getting width and height of the desktop screen using winfo_screenwidth() in variable width and winfo_screenheight() in variable height respectively.
  * Setting size of tkinter window using geometry () by setting dimensions equivalent to widthxheight.
  * Giving title to the window, here ‘Geeks For Geeks’
  * Creating a label with text ‘Hello Tkinter’ (just for display to the user here)
  * Placing the label widget using pack()
  * Closing the endless loop of windows by calling mainloop()

 **Program:**

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# importing tkinter gui

import tkinter as tk

 

#creating window

window=tk.Tk()

 

#getting screen width and height of display

width= window.winfo_screenwidth() 

height= window.winfo_screenheight()

#setting tkinter window size

window.geometry("%dx%d" % (width, height))

window.title("Geeeks For Geeks")

label = tk.Label(window, text="Hello Tkinter!")

label.pack()

 

window.mainloop()  
  
---  
  
 __

 __

 **Output:**

![](https://media.geeksforgeeks.org/wp-
content/uploads/20201203120932/gfg1.jpg)  

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

