PyQt5 – How to add icon to Radio Button ?



In this article we will see how to set logo to a radio button. By default
there is no logo set to the radio button, although we can set icon to the
radio button it is similar to setting icon to a main window but unlike main
window, icon of radio button appear in between the indicator and the text
part.

Below is how default radio button looks vs the the radio button with icon
looks like.  
![](https://media.geeksforgeeks.org/wp-
content/uploads/20200401010039/1st61.png)
![](https://media.geeksforgeeks.org/wp-
content/uploads/20200401010047/2nd66.png)

> **In order to add icon to the radio button we have to do the following:**
>
> 1\. Create a radio button.  
> 2\. Load the icon and create the object with the help of QIcon class  
> 3\. Set the object of QIcon as icon to the radio button with the help of
> setIcon method.

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

 

 # creating a radio button

 radio_button = QRadioButton(self)

 

 # setting geometry of radio button

 radio_button.setGeometry(200, 150, 120, 40)

 

 # setting text to radio button

 radio_button.setText("Radio Button")

 

 # creating object of QICon and loading the icon

 icon = QIcon('logo.png')

 

 # setting icon to radio button

 radio_button.setIcon(icon)

 

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
![](https://media.geeksforgeeks.org/wp-
content/uploads/20200401010531/final179.png)

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

