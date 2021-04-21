PyQt5 Label – Setting color to the Color Effect



In this article we will see how we can set color to the color effect of the
label by default there is no color effect to the label although we can create
color effect for the label. Color effect is not like background color it is
more like of colored filters we use on pictures.

>  **Syntax :** color_effect.setColor(color_object)  
> Here color_effect is the QGraphicsColorizeEffect object
>
>  **Argument :** It takes color object as argument example Qt.green
>
>  **Return :** It returns None

Below is the implementation

  

  

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

 

 # making background color light yellow

 self.setStyleSheet("background : lightyellow;")

 

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

 

 # creating label

 label = QLabel("Label", self)

 

 # setting geometry to the label

 label.setGeometry(200, 100, 150, 60)

 

 # setting alignment to the label

 label.setAlignment(Qt.AlignCenter)

 

 # creating a color effect

 color_effect = QGraphicsColorizeEffect()

 

 # setting color to color effect

 color_effect.setColor(Qt.darkGreen)

 

 # adding color effect to the label

 label.setGraphicsEffect(color_effect)

 

# create pyqt5 app

App = QApplication(sys.argv)

 

# create the instance of our Window

window = Window()

 

# start the app

sys.exit(App.exec())  
  
---  
  
 __

 __

 **Syntax :**  
![](https://media.geeksforgeeks.org/wp-
content/uploads/20200507002328/Python-07-05-2020-00_15_45.png)

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

