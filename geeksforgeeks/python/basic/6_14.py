Hello World in Tkinter



 **Tkinter** is the Python _GUI framework_ that is build into the Python
standard library. Out of all the GUI methods, tkinter is the most commonly
used method as it provides the fastest and the easiest way to create the GUI
application.

## Creating the Hello World program in Tkinter

Lets start with the ‘hello world’ tutorial. Here is the explanation for the
first program in tkinter:

  *     from tkinter import *

In Python3 firstly we import all the classes, functions and variables from the
tkinter package.

  *     root=Tk()

Now we create a root widget, by calling the Tk(). This automatically creates
a graphical window with the title bar, minimize, maximize and close buttons.
This handle allows us to put the contents in the window and reconfigure it as
necessary.

  *     a = Label(root, text="Hello, world!")

Now we create a Label widget as a child to the root window. Here root is the
parent of our label widget. We set the default text to “Hello, World!”

  

  

 **Note:** This gets displayed in the window. A **Label** widget can display
either text or an icon or other image.

  *     a.pack()

Next, we call the **pack()** method on this widget. This tells it to size
itself to fit the given text, and make itself visible.It just tells the
geometry manager to put widgets in the same row or column. It’s usually the
easiest to use if you just want one or a few widgets to appear.

  *     root.mainloop()

The application window does not appear before you enter the main loop. This
method says to take all the widgets and objects we created, render them on our
screen, and respond to any interactions. The program stays in the loop until
we close the window.

Below is the implementation.

 __

 __  
 __

 __

 __  
 __  
 __

# Python tkinter hello world program

 

from tkinter import *

 

root = Tk()

a = Label(root, text ="Hello World")

a.pack()

 

root.mainloop()  
  
---  
  
 __

 __

 **Output:**

![python-tkinter-hello-world](https://media.geeksforgeeks.org/wp-
content/uploads/20200513171342/python-tkinter-hello-world.png)

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

