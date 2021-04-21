PyQt5 – Changing color of pressed Push Button



In this article we will see how to make a push button react when it is
pressed. When button get releases it comes back to its original color, by
default when button get clicked it becomes light blue color although we can
change this color.

In order to change pressed button color we have to change the style sheet of
pressed button, below is the style sheet code which is used with push button
object.

    
    
    QPushButton::clicked
    {
    background-color : red;
    }
    

Below is the implementation.

 __

 __  
 __

 __

 __  
 __  
 __

# importing libraries

from PyQt5.QtWidgets import *

from PyQt5 import QtCore, QtGui

from PyQt5.QtGui import *

from PyQt5.QtCore import *

import sys

 

 

class Window(QMainWindow):

 

 def __init__(self):

 super().__init__()

 

 # setting title

 self.setWindowTitle("Python ")

 

 # setting geometry

 self.setGeometry(100, 100, 600, 400)

 

 # calling method

 self.UiComponents()

 

 # showing all the widgets

 self.show()

 

 # method for widgets

 def UiComponents(self):

 

 # creating push button widget

 button = QPushButton("Button ", self)

 

 # setting geometry

 button.setGeometry(200, 100, 100, 40)

 

 # adding background color to button

 # and background color to pressed button

 button.setStyleSheet("QPushButton"

 "{"

 "background-color : lightblue;"

 "}"

 "QPushButton::pressed"

 "{"

 "background-color : red;"

 "}"

 )

 

 

 

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

https://media.geeksforgeeks.org/wp-
content/uploads/20200328224553/Python-28-03-2020-22_42_38.mp4

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

  
  

  

My Personal Notes _arrow_drop_up_

Save

