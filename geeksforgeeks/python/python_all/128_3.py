PyQt5 QCheckBox



 **Check Box** is one of the PyQt5 widgets used to select one or more choices
from multiple options. It is a small box which gets checked when selected,
else remains blank. For adding Check boxe in application QCheckBox class is
used.  
![](https://media.geeksforgeeks.org/wp-
content/uploads/20190815203907/check2.jpg)

 **Example:**

A window asking the user to select all the programming languages user knows.
After each selection or deselection by the user, the message gets updated
which contains the list of all the languages selected by him/her like: “You
know c, c++ …”.

 **Below is the code:**

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

 MainWindow.resize(476, 308)

 self.centralwidget = QtWidgets.QWidget(MainWindow)

 

 # Languages are not selected initially hence initialised to zero.

 self.langs ={'c':0, 'cpp':0, 'java':0,
'python':0}

 

 # For showing message 

 self.label = QtWidgets.QLabel(self.centralwidget)

 self.label.setGeometry(QtCore.QRect(140, 80, 191, 20))

 

 self.checkBox_c = QtWidgets.QCheckBox(self.centralwidget)

 self.checkBox_c.setGeometry(QtCore.QRect(170, 120, 81,
20))

 self.checkBox_c.stateChanged.connect(self.checkedc)

 

 self.checkBox_cpp = QtWidgets.QCheckBox(self.centralwidget)

 self.checkBox_cpp.setGeometry(QtCore.QRect(170, 140, 81,
20))

 self.checkBox_cpp.stateChanged.connect(self.checkedcpp)

 

 self.checkBox_java = QtWidgets.QCheckBox(self.centralwidget)

 self.checkBox_java.setGeometry(QtCore.QRect(170, 160, 81,
20))

 self.checkBox_java.stateChanged.connect(self.checkedjava)

 

 self.checkBox_py = QtWidgets.QCheckBox(self.centralwidget)

 self.checkBox_py.setGeometry(QtCore.QRect(170, 180, 81,
20))

 self.checkBox_py.stateChanged.connect(self.checkedpy)

 

 MainWindow.setCentralWidget(self.centralwidget)

 

 self.retranslateUi(MainWindow)

 QtCore.QMetaObject.connectSlotsByName(MainWindow)

 

 def checkedc(self, checked):

 if checked:

 self.langs['c']= 1

 else:

 self.langs['c']= 0

 self.show()

 

 def checkedcpp(self, checked):

 if checked:

 self.langs['cpp']= 1

 else:

 self.langs['cpp']= 0

 self.show()

 

 def checkedjava(self, checked):

 if checked:

 self.langs['java']= 1

 else:

 self.langs['java']= 0

 self.show()

 

 def checkedpy(self, checked):

 if checked:

 self.langs['python']= 1

 else:

 self.langs['python']= 0

 self.show() 

 

 # For showing updated list of all selected languages. 

 def show(self):

 checkedlangs =', '.join([key for key in self.langs.keys()

 if self.langs[key]== 1]) 

 

 # Updates message having list of all selected languages. 

 self.label.setText("You know "+checkedlangs)

 

 

 def retranslateUi(self, MainWindow):

 _translate = QtCore.QCoreApplication.translate

 MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))

 

 self.label.setText(_translate("MainWindow", "Select your preferred
language"))

 self.checkBox_c.setText(_translate("MainWindow", "C"))

 self.checkBox_cpp.setText(_translate("MainWindow", "C++"))

 self.checkBox_java.setText(_translate("MainWindow", "Java"))

 self.checkBox_py.setText(_translate("MainWindow", "Python"))

 

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
content/uploads/20190817223408/cbox-300x215.jpg)

Message showing user’s selected languages. Message will get updated after each
selection or deselection by the user.  
![](https://media.geeksforgeeks.org/wp-
content/uploads/20190817223918/sc2-300x215.jpg)  
![](https://media.geeksforgeeks.org/wp-
content/uploads/20190817223932/scpp-300x216.jpg)  
![](https://media.geeksforgeeks.org/wp-
content/uploads/20190817223949/sjava-300x215.jpg)  
![](https://media.geeksforgeeks.org/wp-
content/uploads/20190817224009/spy-300x216.jpg)  

Attention reader! Don’t stop learning now. Get hold of all the important DSA
concepts with the **DSA Self Paced Course** at a student-friendly price and
become industry ready.

My Personal Notes _arrow_drop_up_

Save

