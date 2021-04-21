Creating a simple browser using PyQt5



In this article we will see how we can create a simple browser using PyQt5.

 **Web browser** is a software application for accessing information on the
World Wide Web. When a user requests a web page from a particular website, the
web browser retrieves the necessary content from a web server and then
displays the page on the screen.

 **PyQt5** is cross-platform GUI toolkit, a set of python bindings for Qt v5.
One can develop an interactive desktop application with so much ease because
of the tools and simplicity provided by this library.

>  **GUI Implementation steps :**  
>  1\. Create a main window  
> 2\. Create a QWebEngineView object and add it as the central widget to the
> main window  
> 3\. Add Status bar to the main window  
> 4\. Create a toolbar and add navigation button and the line edit to show the
> url, below is hot the toolbar will look like
>
> ![](https://media.geeksforgeeks.org/wp-
> content/uploads/20200606170425/final462.png)
>
>  
>
>
>  
>
>
>  **Back-End Implementation Steps :**  
>  1\. Add update url action to QWebEngineView object when url is changed.  
> 2\. Inside the update url action change the url of url bar and change cursor
> position  
> 3\. Add another update title action to the QWebEngineView object when
> loading is finished  
> 4\. Inside the update title method update the title of the window as the
> page title  
> 5\. Add actions to the navigation buttons using the build-in functions of
> the QWebEngineView object for reload, back, stop and forward buttons  
> 6\. Add action to the home button and inside the action change the url to
> google.com  
> 7\. Add action to the line edit when return key is pressed  
> 8\. Inside the line edit action get the text and covert this text to the
> QUrl object and set the scheme if it is null and set this url to the
> QWebEngineView object

Below is the implementation

 __

 __  
 __

 __

 __  
 __  
 __

# importing required libraries

from PyQt5.QtCore import *

from PyQt5.QtWidgets import *

from PyQt5.QtGui import *

from PyQt5.QtWebEngineWidgets import *

from PyQt5.QtPrintSupport import *

import os

import sys

 

# creating main window class

class MainWindow(QMainWindow):

 

 # constructor

 def __init__(self, *args, **kwargs):

 super(MainWindow, self).__init__(*args, **kwargs)

 

 

 # creating a QWebEngineView

 self.browser = QWebEngineView()

 

 # setting default browser url as google

 self.browser.setUrl(QUrl("http://google.com"))

 

 # adding action when url get changed

 self.browser.urlChanged.connect(self.update_urlbar)

 

 # adding action when loading is finished

 self.browser.loadFinished.connect(self.update_title)

 

 # set this browser as central widget or main window

 self.setCentralWidget(self.browser)

 

 # creating a status bar object

 self.status = QStatusBar()

 

 # adding status bar to the main window

 self.setStatusBar(self.status)

 

 # creating QToolBar for navigation

 navtb = QToolBar("Navigation")

 

 # adding this tool bar tot he main window

 self.addToolBar(navtb)

 

 # adding actions to the tool bar

 # creating a action for back

 back_btn = QAction("Back", self)

 

 # setting status tip

 back_btn.setStatusTip("Back to previous page")

 

 # adding action to the back button

 # making browser go back

 back_btn.triggered.connect(self.browser.back)

 

 # adding this action to tool bar

 navtb.addAction(back_btn)

 

 # similarly for forward action

 next_btn = QAction("Forward", self)

 next_btn.setStatusTip("Forward to next page")

 

 # adding action to the next button

 # making browser go forward

 next_btn.triggered.connect(self.browser.forward)

 navtb.addAction(next_btn)

 

 # similarly for reload action

 reload_btn = QAction("Reload", self)

 reload_btn.setStatusTip("Reload page")

 

 # adding action to the reload button

 # making browser to reload

 reload_btn.triggered.connect(self.browser.reload)

 navtb.addAction(reload_btn)

 

 # similarly for home action

 home_btn = QAction("Home", self)

 home_btn.setStatusTip("Go home")

 home_btn.triggered.connect(self.navigate_home)

 navtb.addAction(home_btn)

 

 # adding a separator in the tool bar

 navtb.addSeparator()

 

 # creating a line edit for the url

 self.urlbar = QLineEdit()

 

 # adding action when return key is pressed

 self.urlbar.returnPressed.connect(self.navigate_to_url)

 

 # adding this to the tool bar

 navtb.addWidget(self.urlbar)

 

 # adding stop action to the tool bar

 stop_btn = QAction("Stop", self)

 stop_btn.setStatusTip("Stop loading current page")

 

 # adding action to the stop button

 # making browser to stop

 stop_btn.triggered.connect(self.browser.stop)

 navtb.addAction(stop_btn)

 

 # showing all the components

 self.show()

 

 

 # method for updating the title of the window

 def update_title(self):

 title = self.browser.page().title()

 self.setWindowTitle("% s - Geek Browser" % title)

 

 

 # method called by the home action

 def navigate_home(self):

 

 # open the google

 self.browser.setUrl(QUrl("http://www.google.com"))

 

 # method called by the line edit when return key is pressed

 def navigate_to_url(self):

 

 # getting url and converting it to QUrl objetc

 q = QUrl(self.urlbar.text())

 

 # if url is scheme is blank

 if q.scheme() == "":

 # set url scheme to html

 q.setScheme("http")

 

 # set the url to the browser

 self.browser.setUrl(q)

 

 # method for updating url

 # this method is called by the QWebEngineView object

 def update_urlbar(self, q):

 

 # setting text to the url bar

 self.urlbar.setText(q.toString())

 

 # setting cursor position of the url bar

 self.urlbar.setCursorPosition(0)

 

 

# creating a pyQt5 application

app = QApplication(sys.argv)

 

# setting name to the application

app.setApplicationName("Geek Browser")

 

# creating a main window object

window = MainWindow()

 

# loop

app.exec_()  
  
---  
  
 __

 __

 **Output :**  

https://media.geeksforgeeks.org/wp-content/uploads/20200606172102/Google-Geek-
Browser-2020-06-06-17-20-27.mp4

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

