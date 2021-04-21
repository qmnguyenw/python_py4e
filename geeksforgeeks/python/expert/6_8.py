PyQt Hello World



There are so many options provided by Python to develop GUI application and
PyQt5 is one of them. PyQt5 is cross-platform GUI toolkit, a set of python
bindings for Qt v5. One can develop an interactive desktop application with so
much ease because of the tools and simplicity provided by this library.

 **Installation :**

    
    
    pip install PyQt5

In this article we will see how to make simple PyQt5 application which print
the message “Hello World !”  
  
**Code :**

 __

 __  
 __

 __

 __  
 __  
 __

# importing the required libraries

from PyQt5.QtWidgets import *

import sys

 

class Window(QMainWindow):

 def __init__(self):

 super().__init__()

 

 # set the title

 self.setWindowTitle("hellow world !")

 

 # set the geometry

 self.setGeometry(0, 0, 300, 300)

 

 # create label widget

 # to display content on screen

 self.label = QLabel("Hello World !!", self)

 

 # show all the widgets

 self.show()

 

# create pyqt5 app

App = QApplication(sys.argv)

 

# create the instance of our Window

window = Window()

 

# start the app

sys.exit(App.exec())  
  
---  
  
 __

 __

 **Output :**  
![pyqt-hello-world](https://media.geeksforgeeks.org/wp-
content/uploads/20200312014047/pyqt.png)

 **Explanation :**  
First of all we have created the Window class which inherits QMainWindow
class. Within this class we can add widgets which will get displayed on main
window, we have used setWindowTiltle method to set title. setGeometry
method to set size and position of the window and for displaying message we
have used QLabel.

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

