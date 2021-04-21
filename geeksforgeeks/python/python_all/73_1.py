PyQt5 – QTableWidget



In this article, we will learn how to add and work with a table in our PyQt5
application. A table is an arrangement of data in rows and columns and widely
used in communication, research, and data analysis. We can add one or more
tables in our PyQt application using **QTableWidget**.

For a better understanding of the concept, we will take an example where we
want to display the name and the city of different people in a table in our
application. We can extract the data from a database, JSON file, or any other
storage platform.

 **Example:**

 __

 __  
 __

 __

 __  
 __  
 __

import sys

from PyQt5.QtWidgets import *

 

 

#Main Window

class App(QWidget):

 def __init__(self):

 super().__init__()

 self.title = 'PyQt5 - QTableWidget'

 self.left = 0

 self.top = 0

 self.width = 300

 self.height = 200

 

 self.setWindowTitle(self.title)

 self.setGeometry(self.left, self.top, self.width,
self.height)

 

 self.createTable()

 

 self.layout = QVBoxLayout()

 self.layout.addWidget(self.tableWidget)

 self.setLayout(self.layout)

 

 #Show window

 self.show()

 

 #Create table

 def createTable(self):

 self.tableWidget = QTableWidget()

 

 #Row count

 self.tableWidget.setRowCount(4) 

 

 #Column count

 self.tableWidget.setColumnCount(2) 

 

 self.tableWidget.setItem(0,0, QTableWidgetItem("Name"))

 self.tableWidget.setItem(0,1, QTableWidgetItem("City"))

 self.tableWidget.setItem(1,0, QTableWidgetItem("Aloysius"))

 self.tableWidget.setItem(1,1, QTableWidgetItem("Indore"))

 self.tableWidget.setItem(2,0, QTableWidgetItem("Alan"))

 self.tableWidget.setItem(2,1, QTableWidgetItem("Bhopal"))

 self.tableWidget.setItem(3,0, QTableWidgetItem("Arnavi"))

 self.tableWidget.setItem(3,1, QTableWidgetItem("Mandsaur"))

 

 #Table will fit the screen horizontally

 self.tableWidget.horizontalHeader().setStretchLastSection(True)

 self.tableWidget.horizontalHeader().setSectionResizeMode(

 QHeaderView.Stretch)

 

if __name__ == '__main__':

 app = QApplication(sys.argv)

 ex = App()

 sys.exit(app.exec_())  
  
---  
  
 __

 __

 **Output:**

![](https://media.geeksforgeeks.org/wp-
content/uploads/20200404220655/Screenshot-2020-04-04-at-22.05.51.png)

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

  
  

  

My Personal Notes _arrow_drop_up_

Save

