Python – How to save canvas in pyqt5?



There are so many options provided by Python to develop GUI application and
PyQt5 is one of them. PyQt5 is cross-platform GUI toolkit, a set of python
bindings for Qt v5. One can develop an interactive desktop application with so
much ease because of the tools and simplicity provided by this library.

In this tutorial we’ll take a look how to save canvas in pyqt5. We draw
things on canvas using **QPainter class**.

 **QPainter :** Qt’s painting system is able to render vector graphics,
images, and outline font-based text with sub-pixel accuracy using anti-
aliasing to improve rendering quality.

In this article, we create a canvas and will draw a line on it and see how to
save that canvas as image file at desired location on the system. Below is the
implementation.

 __

 __  
 __

 __

 __  
 __  
 __

# importing modules

from PyQt5.QtWidgets import *

from PyQt5.QtGui import *

from PyQt5.QtCore import * import sys

 

# creating class fo winow

class Window(QMainWindow):

 def __init__(self):

 super().__init__()

 

 

 title = "Paint and save Application"

 

 top = 400

 left = 400

 width = 800

 height = 600

 

 # setting title of window

 self.setWindowTitle(title)

 

 # setting geometry

 self.setGeometry(top, left, width, height)

 

 # creating canvas

 self.image = QImage(self.size(), QImage.Format_RGB32)

 

 # setting canvas color to white

 self.image.fill(Qt.white)

 

 # creating menu bar

 mainMenu = self.menuBar()

 

 # adding file menu in it

 fileMenu = mainMenu.addMenu("File")

 

 # creating save action

 saveAction = QAction("Save", self)

 

 # setting save action shortcut

 saveAction.setShortcut("Ctrl + S")

 

 # adding save action to filemenu

 fileMenu.addAction(saveAction)

 

 # setting triggered method

 saveAction.triggered.connect(self.save)

 

 # calling draw_something method

 self.draw_something()

 

 # paintEvent for creating blank canvas

 def paintEvent(self, event):

 canvasPainter = QPainter(self)

 canvasPainter.drawImage(self.rect(), self.image,

 self.image.rect())

 

 # this method will draw a line

 def draw_something(self):

 

 painter = QPainter(self.image)

 

 painter.setPen(QPen(Qt.black, 5, Qt.SolidLine, 

 Qt.RoundCap, Qt.RoundJoin))

 

 # drawing a line

 painter.drawLine(100, 100, 300, 300)

 

 # updating it to canvas

 self.update()

 

 # save method

 def save(self):

 

 # selecting file path

 filePath, _ = QFileDialog.getSaveFileName(self, "Save Image",
"",

 "PNG(*.png);;JPEG(*.jpg *.jpeg);;All Files(*.*) ")

 

 # if file path is blank return back

 if filePath == "":

 return

 

 # saving canvas at desired path

 self.image.save(filePath)

 

# main method

if __name__ == "__main__":

 app = QApplication(sys.argv)

 window = Window()

 window.show()

 

 # looping for window

 sys.exit(app.exec())  
  
---  
  
 __

 __

 **Output :**  
After running the code window will appear with a canvas of white color on
which line is drawn.  
![](https://media.geeksforgeeks.org/wp-content/uploads/20200304203828/Paint-
and-save-Application-04-03-2020-20_21_48.png)

  

  

After clicking on the file menu save button will appear.  
![](https://media.geeksforgeeks.org/wp-content/uploads/20200304203848/Paint-
and-save-Application-04-03-2020-20_21_55.png)

When save button is pressed it will ask for the location and name and image
will get saved at desirable location.  
![](https://media.geeksforgeeks.org/wp-content/uploads/20200304203904/Paint-
and-save-Application-04-03-2020-20_22_05.png)  
This code will save the canvas in png format at the desired location.

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

