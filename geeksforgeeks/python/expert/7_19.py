PyQt5 QToolButton



 **Tool button** is a PyQt5 widget which looks like the buttons used in
Toolbar. This button contains icon which gives an idea about its utility. For
adding this button in application QToolButton class is used.  
![](https://media.geeksforgeeks.org/wp-
content/uploads/20190815203749/tool.jpg)

 **Example:**

A window having a Tool button with an exit icon. When the user clicks this
button the application gets closed.

 __

 __  
 __

 __

 __  
 __  
 __

import sys

from PyQt5 import QtCore, QtGui, QtWidgets

 

class Ui_MainWindow(object):

 def setupUi(self, MainWindow):

 MainWindow.resize(506, 312)

 self.centralwidget = QtWidgets.QWidget(MainWindow)

 self.centralwidget.setObjectName("centralwidget")

 

 self.toolButton = QtWidgets.QToolButton(self.centralwidget)

 self.toolButton.setGeometry(QtCore.QRect(220, 120, 41,
41))

 

 icon = QtGui.QIcon()

 icon.addPixmap(QtGui.QPixmap("exiticon.png [exact location of
image]"),

 QtGui.QIcon.Normal, QtGui.QIcon.Off)

 

 # adding icon to the toolbutton

 self.toolButton.setIcon(icon)

 MainWindow.setCentralWidget(self.centralwidget)

 

 self.retranslateUi(MainWindow)

 QtCore.QMetaObject.connectSlotsByName(MainWindow)

 

 # adding signal and slot 

 self.toolButton.clicked.connect(self.exitapp)

 

 def retranslateUi(self, MainWindow):

 _translate = QtCore.QCoreApplication.translate

 MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))

 

 # For closing the application

 def exitapp(self):

 sys.exit()

 

if __name__ == "__main__": 

 app = QtWidgets.QApplication(sys.argv) 

 

 MainWindow = QtWidgets.QMainWindow() 

 ui = Ui_MainWindow() 

 ui.setupUi(MainWindow) 

 MainWindow.show() 

 sys.exit(app.exec_()) 

   
  
---  
  
__

__

**Output:**

![](https://media.geeksforgeeks.org/wp-
content/uploads/20190817192853/tbut-300x206.jpg)  
When user clicks this button, application get closed.  

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

  
  

  

My Personal Notes _arrow_drop_up_

Save

