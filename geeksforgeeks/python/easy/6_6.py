Introduction to Tkinter



 **Graphical User Interface(GUI)** is a form of user interface which allows
users to interact with computers through visual indicators using items such as
icons, menus, windows, etc. It has advantages over the Command Line
Interface(CLI) where users interact with computers by writing commands using
keyboard only and whose usage is more difficult than GUI.  

## What is Tkinter?

 **Tkinter** is the inbuilt python module that is used to create GUI
applications. It is one of the most commonly used modules for creating GUI
applications in Python as it is simple and easy to work with. You don’t need
to worry about the installation of the Tkinter module separately as it comes
with Python already. It gives an object-oriented interface to the Tk GUI
toolkit.  
  
Some other Python Libraries available for creating our own GUI applications
are

* Kivy
* Python Qt
* wxPython

Among all Tkinter is most widely used  

## What are Widgets?

 **Widgets** in Tkinter are the elements of GUI application which provides
various controls (such as Labels, Buttons, ComboBoxes, CheckBoxes, MenuBars,
RadioButtons and many more) to users to interact with the application.

 **Fundamental structure of tkinter program**  
  
![](https://media.geeksforgeeks.org/wp-
content/uploads/20200518184446/pik8.png)  
  
 **Basic Tkinter Widgets:**

  

  
Widgets| Description| Label| It is used to display text or image on the
screen| Button| It is used to add buttons to your application| Canvas| It is
used to draw pictures and others layouts like texts, graphics etc.| ComboBox|
It contains a down arrow to select from list of available options|
CheckButton| It displays a number of options to the user as toggle buttons
from which user can select any number of options.| RadiButton| It is used to
implement one-of-many selection as it allows only one option to be selected|
Entry| It is used to input single line text entry from user| Frame| It is used
as container to hold and organize the widgets| Message| It works same as that
of label and refers to multi-line and non-editable text| Scale| It is used to
provide a graphical slider which allows to select any value from that scale|
Scrollbar| It is used to scroll down the contents. It provides a slide
controller.| SpinBox| It is allows user to select from given set of values|
Text| It allows user to edit multiline text and format the way it has to be
displayed| Menu| It is used to create all kinds of menu used by an application  
---|---  
  

 **Example**

 __

 __  
 __

 __

 __  
 __  
 __

from tkinter import *

from tkinter.ttk import *

 

# writing code needs to

# create the main window of 

# the application creating 

# main window object named root

root = Tk()

 

# giving title to the main window

root.title("First_Program")

 

# Label is what output will be 

# show on the window

label = Label(root, text ="Hello World !").pack()

 

# calling mainloop method which is used

# when your application is ready to run

# and it tells the code to keep displaying 

root.mainloop()  
  
---  
  
 __

 __

 **Output**  
![](https://media.geeksforgeeks.org/wp-
content/uploads/20200518183107/pik7.png)

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

