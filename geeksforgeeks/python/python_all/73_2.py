PyQt5 – QTabWidget



In this article, you will learn how to add and work with a tab window in your
PyQt5 application. Each tab has a different layout and page under a selected
tab is displayed, while keeping the others hidden. To select a tab, you need
to click the desired tab from the tab bar which is provided by this
**QTabWidget**.

The below article describes the process of creating a sample application that
has three tabs and each tab has a different layout.  
 **Example:**

 __

 __  
 __

 __

 __  
 __  
 __

import sys

from PyQt5.QtWidgets import QMainWindow, QApplication, QPushButton,
QWidget, QAction, QTabWidget, QVBoxLayout, QLabel

 

# Creating the main window

class App(QMainWindow):

 def __init__(self):

 super().__init__()

 self.title = 'PyQt5 - QTabWidget'

 self.left = 0

 self.top = 0

 self.width = 300

 self.height = 200

 self.setWindowTitle(self.title)

 self.setGeometry(self.left, self.top, self.width,
self.height)

 

 self.tab_widget = MyTabWidget(self)

 self.setCentralWidget(self.tab_widget)

 

 self.show()

 

# Creating tab widgets

class MyTabWidget(QWidget):

 def __init__(self, parent):

 super(QWidget, self).__init__(parent)

 self.layout = QVBoxLayout(self)

 

 # Initialize tab screen

 self.tabs = QTabWidget()

 self.tab1 = QWidget()

 self.tab2 = QWidget()

 self.tab3 = QWidget()

 self.tabs.resize(300, 200)

 

 # Add tabs

 self.tabs.addTab(self.tab1, "Geeks")

 self.tabs.addTab(self.tab2, "For")

 self.tabs.addTab(self.tab3, "Geeks")

 

 # Create first tab

 self.tab1.layout = QVBoxLayout(self)

 self.l = QLabel()

 self.l.setText("This is the first tab")

 self.tab1.layout.addWidget(self.l)

 self.tab1.setLayout(self.tab1.layout)

 

 # Add tabs to widget

 self.layout.addWidget(self.tabs)

 self.setLayout(self.layout)

 

if __name__ == '__main__':

 app = QApplication(sys.argv)

 ex = App()

 sys.exit(app.exec_())  
  
---  
  
 __

 __

 **Output:**  
![](https://media.geeksforgeeks.org/wp-
content/uploads/20200407222308/Screenshot-2020-04-07-at-22.13.31.png)

If you want to add an icon on any tab. You just need to replace

    
    
    self.tabs.addTab(self.tab1, "Geeks")

with

  

  

    
    
    self.tabs.addTab(self.tab1, QIcon("Location of the icon"), ('Geeks')) 

and import the QIcon library from PyQt5.QtWidgets.

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

