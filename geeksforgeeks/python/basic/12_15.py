Python | Introduction to PyQt5



There are so many options provided by Python to develop GUI application and
PyQt5 is one of them. PyQt5 is cross-platform GUI toolkit, a set of python
bindings for Qt v5. One can develop an interactive desktop application with so
much ease because of the tools and simplicity provided by this library.

A GUI application consists of Front-end and Back-end. PyQt5 has provided a
tool called ‘QtDesigner’ to design the front-end by drag and drop method so
that development can become faster and one can give more time on back-end
stuff.

 **Installation:**

First, we need to install PyQt5 library. For this, type the following command
in the terminal or command prompt:

    
    
    pip install pyqt5

If successfully installed one can verify it by running the code:

  

  

    
    
    >>>import PyQt5

PyQt5 provides lots of tools and QtDesigner is one of them. For this run this
command:

    
    
    pip install PyQt5-tools

### Create your first app –

This is a simple app having a single button in the window. After clicking that
button a message will appear “You clicked me”. **Let’s start**.

  * First of all, we need to find _QtDesigner_ to create the front-end part.  
– QtDesigner is present at ‘site-packages/pyqt5_tools’  
– For finding the location of site-packages write the following python code
using any editor of your choice and then run:

    
    
    >>> import site  
    
    >>> site.getsitepackages()

– Run the application named ‘designer’.

  * A window will open as shown in the figure:  
![](https://media.geeksforgeeks.org/wp-
content/uploads/20190515161508/mwimg-300x244.jpg)  
select the ‘Dialog without Button’ option and click ‘Create’

  * At the left side of the designer there will be various widgets which can be dragged and dropped in our window according to our requirement.

  * Find and drag-and-drop ‘Push Button’ and ‘Label’.  
![](https://media.geeksforgeeks.org/wp-
content/uploads/20190510021751/buttonlabel-300x250.jpg)

  * Change the text inside the widgets by right clicking it and selecting ‘Change plain text’. Keep the text of the Label blank.  
![](https://media.geeksforgeeks.org/wp-
content/uploads/20190510021827/changedtext-300x250.jpg)

  * We have created our front-end layout, just save it at your desired location.Remember, this file will have .ui as extension.

  * We need to convert the .ui file into .py file to get the python form of the widgets and attach necessary event listeners to them.  

### Converting .ui file into .py file:

For this we have to go to sitpackages directory in terminal or command prompt
and run the command as shown below. Getting the location of sitepackages is
mentioned previously.

> >>> cd “C:\\\Users\\\……\\\Programs\\\Python\\\Python36-32\\\lib\\\site-
> packages” [Location of sitepackages]
>
> >>> pyuic5 “C:\Users\……\FILENAME.ui”[Exact location of .ui file] -o ”
> C:\Users\…….\FILENAME.py” [Location where want to put .py file]

  * Finally we will add signals and slot in the python code to make it fully functional.
    
        widget.signal.connect(slot)

A **signal** is emitted by widgets after the occurrence of a certain kind of
event like a click, Double click, etc.  
A **slot** is any callable function which will perform some action after the
occurrence of an event.

  * Run the app and click the button.  
![](https://media.geeksforgeeks.org/wp-
content/uploads/20190515173852/clicked-300x247.jpg)

Below is the code –

 __

 __  
 __

 __

 __  
 __  
 __

import sys

from PyQt5 import QtCore, QtGui, QtWidgets

 

class Ui_Dialog(object):

 def setupUi(self, Dialog):

 Dialog.setObjectName("Dialog")

 Dialog.resize(400, 300)

 

 self.pushButton = QtWidgets.QPushButton(Dialog)

 self.pushButton.setGeometry(QtCore.QRect(150, 70, 93,
28))

 

 self.label = QtWidgets.QLabel(Dialog)

 self.label.setGeometry(QtCore.QRect(130, 149, 151, 31))

 self.label.setText("")

 

 self.retranslateUi(Dialog)

 QtCore.QMetaObject.connectSlotsByName(Dialog)

 

 # adding signal and slot

 self.pushButton.clicked.connect(self.showmsg) 

 

 def retranslateUi(self, Dialog):

 _translate = QtCore.QCoreApplication.translate

 Dialog.setWindowTitle(_translate("Dialog", "Dialog"))

 self.pushButton.setText(_translate("Dialog", "Click"))

 

 def showmsg(self):

 # slot

 self.label.setText("You clicked me")

 

if __name__ == "__main__":

 app = QtWidgets.QApplication(sys.argv)

 

 MainWindow = QtWidgets.QMainWindow()

 ui = Ui_Dialog()

 

 ui.setupUi(MainWindow)

 MainWindow.show()

 sys.exit(app.exec_())  
  
---  
  
 __

 __

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

