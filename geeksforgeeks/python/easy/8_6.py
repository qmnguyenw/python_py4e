PyQt5 – How to hide the title bar of window ?



When we design the GUI (Graphical User Interface) application using PyQt5,
there exist the window. A window is a (usually) rectangular portion of the
display on a computer monitor that presents its contents (e.g., the contents
of a directory, a text file or an image) seemingly independently of the rest
of the screen. Windows are one of the elements that comprise a graphical user
interface (GUI).

In a window we can see there exist a title bar which comprises the icon and
title on the left size and on the right side there exist control button.  
![](https://media.geeksforgeeks.org/wp-
content/uploads/20200316220913/color10.png)

In this article we will see how we can hide title bar. In order to do so we
will use setWindowFlag() method and pass which belongs to the QWidget
class.

>  **Syntax :** setWindowFlag(Qt.FramelessWindowHint)
>
>  **Argument :** It takes Window type as argument.
>
>  
>
>
>  
>
>
>  **Action performed :** It removes the title bar.

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

from PyQt5.QtGui import *

from PyQt5.QtCore import Qt

import sys

 

 

class Window(QMainWindow):

 def __init__(self):

 super().__init__()

 

 # this will hide the title bar

 self.setWindowFlag(Qt.FramelessWindowHint)

 

 # set the title

 self.setWindowTitle("no title")

 

 # setting the geometry of window

 self.setGeometry(100, 100, 400, 300)

 

 # creating a label widget

 # by default label will display at top left corner

 self.label_1 = QLabel('no title bar', self)

 

 # moving position

 self.label_1.move(100, 100)

 

 # setting up border and background color

 self.label_1.setStyleSheet("background-color: lightgreen;

 border: 3px solid green")

 

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
![pyqt-hide-titlebar](https://media.geeksforgeeks.org/wp-
content/uploads/20200316222357/nobar.png)

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

