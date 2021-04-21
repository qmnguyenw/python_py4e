Python GUI – PyQt VS TKinter



A **GUI toolkit** contains widgets that are used to create a graphical
interface. Python includes a wide range of Interface implementations
available, from TkInter (it comes with Python, ) to a variety of various
cross-platform solutions, such as PyQt5, which is known for its more
sophisticated widgets and sleek look.

## **PyQt**

PyQt is a toolkit for graphical user interface (GUI) widgets. It is extracted
from the library of Qt. PyQt is the product of the combination of the Python
language and the Qt library. PyQt is coming with the Qt Builder. We will use
it to get the python code from the Qt Creator. With the support of a qt
designer, we can build a GUI, and then we can get python code for that GUI.
PyQt supports all platforms including Windows, macOS and UNIX. PyQt can be
used to create stylish GUIs, a modern and portable python framework.

**Code:**

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# Import sys for handle the

# exit status of the application.

import sys

 

# Importing required widgets

from PyQt5.QtWidgets import QApplication

from PyQt5.QtWidgets import QLabel

from PyQt5.QtWidgets import QWidget

 

# To create an instance of QApplication

# sys.argv contains the list of

# command-line argument

app = QApplication(sys.argv)

 

# To create an instance of application GUI

# root is an instance of QWidget,

# it provides all the features to

# create the application's window

root = QWidget() 

 

# adding title to window

root.setWindowTitle('Geeks App') 

 

# to place txt at the coordinates

root.move(60, 15) 

 

# to display text

txt = QLabel('Welcome, Geeks!', parent = root) 

txt.move(60, 15)

 

# Show application's GUI

root.show()

 

# Run application's main loop

sys.exit(app.exec_())  
  
---  
  
 __

 __

 **Output:**

  

  

![](https://media.geeksforgeeks.org/wp-
content/uploads/20201206222515/Screenshotfrom20201206222508-300x145.png)

A simple app to display text using PyQt.

### Advantages of using PyQt

  * Coding versatility –GUI programming with Qt is built around the idea of signals and slots for creating contact between objects. This allows versatility in dealing with GUI incidents which results in a smoother code base.
  * More than a framework : Qt uses a broad variety of native platform APIs for networking, database development, and more. It provides primary access to them through a special API.
  * Various UI components: Qt provides multiple widgets, such as buttons or menus, all designed with a basic interface for all compatible platforms.
  * Various learning resources: As PyQt is one of the most commonly used UI systems for Python, you can conveniently access a broad variety of documentation.

### Disadvantages of using PyQt

  * Lack of Python-specific documentation for classes in PyQt5
  * It takes a lot of time to grasp all the specifics of PyQt, meaning it’s a pretty steep learning curve.
  * If the application is not open-source, you must pay for a commercial license.

###  **Tkinter**

Tkinter is an open-source Python Graphic User Interface (GUI) library well
known for its simplicity. It comes pre-installed in Python, so you don’t even
need to think about installing it. These characteristics make it a strong
position for beginners and intermediates to begin with. Tkinter cannot be used
for larger-scale projects.

 **Code:**

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# importing the module tkinter

import tkinter as tk

 

# create main window (parent window)

root = tk.Tk()

 

# Label() it display box

# where you can put any text. 

txt = tk.Label(root,

 text="Welcome to GeekForGeeks")

 

# pack() It organizes the widgets

# in blocks before placing in the parent widget.

txt.pack()

 

# running the main loop

root.mainloop()  
  
---  
  
 __

 __

 **Output:**

![](https://media.geeksforgeeks.org/wp-
content/uploads/20201206211809/Screenshotfrom20201206211741.png)

A simple app to display text using tkinter.

### Advantages of using Tkinter

  * Tkinter is easy and fast to implement as compared to any other GUI toolkit.
  * Tkinter is more flexible and stable.
  * Tkinter is included in Python, so nothing extra need to download.
  * Tkinter provides a simple syntax.
  * Tkinter is really easy to understand and master.
  * Tkinter provides three geometry managers: place, pack, and grid. That is much more powerful and easy to use.

### Disadvantages of using Tkinter

  * Tkinter does not include advanced widgets.
  * It has no similar tool as Qt Designer for Tkinter.
  * It doesn’t have a reliable UI.
  * Sometime, it is hard to debug in Tkinter.
  * It is not purely Pythonic.

##  **Difference between PyQt and Tkinter**

No.|  **Basis**|

 **PyQt**|

 **Tkinter**|  1.| License| PyQt is available under Riverbank Commercial
License and GPL v3 (General Public License v 3.0) and if you do not wish to
release your application under a GPL-compatible license, you must apply for a
commercial license. | Tkinter is open source and free for any commercial use.|
2.| Ease of Understanding| It requires a lot of time for understanding all the
details of PyQt.| Tkinter is easy to understand and master due to a small
library.| 3.| Design| PyQt has a modern look and a good UI.| Tk had an older
design and it looks outdated.| 4.| Widgets| thenPyQt comes with many powerful
and advanced widgets. | TkInter does not come with advanced widgets.| 5.| UI
Builder| PyQt have a Qt Designer tool which we can use to build GUIs than get
python code of that GUI using Qt Designer.| It has no similar tool as Qt
Designer for Tkinter.| 6.| Installation| PyQt is not included by default with
Python installations.| It is included in the standard Python library so no
need to install it separately.  
---|---|---|---  
  
Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

