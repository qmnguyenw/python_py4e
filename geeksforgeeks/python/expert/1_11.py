How to run Python script directly in Kivy file?



Kivy is a platform-independent GUI tool in Python. It can run on Android, IOS,
Linux and Windows, etc. This is the only GUI library from python which can
independently run on the android device even we can use it on Raspberry pi
also. It is an open-source Python library for the rapid development of
applications that make use of innovative user interfaces, such as multi-touch
apps. Its graphic engine is built over OpenGL ES 2, and has fast graphics
pipeline. If you are new to kivy you can learn from this link.

In this article, we will develop a GUI window using kivy framework of python
and we will add a button on this window. Usually what happens is we attach a
method to a button and the whole method is defined in another python file but
this time we will add button code to same .kv file

The IDE we are going to use is pycharm and the version of python we are going
to use is python 3.6.

### Approach

  * Create new project in pycharm
  * Installing required packages
  * Add new python file in venv directory of your project. To add file video has been attaches.

https://media.geeksforgeeks.org/wp-content/uploads/20210202201343/main-file-
maker.mp4

  * Add new .kv file in project. Implentation us depicted here:

https://media.geeksforgeeks.org/wp-content/uploads/20210202201440/ui-file-
maker.mp4

  * Adding code to both files

> main.py

## Python3

  

  

 __

 __  
 __

 __

 __  
 __  
 __

# importing image widget of kivy framework

from kivy.uix.image import Image

from kivy.uix.button import Button

from kivy.app import App

 

# importing boxlayout for our application

from kivy.uix.boxlayout import BoxLayout

 

 

# this will connect MainWindow which we have created in ui.kv with main.py
file

class MainWindow(BoxLayout):

 pass

 

 

"""

Note:- keep in mind that our .kv file name was ui.kv so our rendering
class(class which will render our application) name 

should be like uiApp otherwise we will not get the desired output!!

"""

 

 

# this is the main class which will render the whole application

class uiApp(App):

 

 # method which will render our application

 def build(self):

 return MainWindow()

 

 

# running the application

uiApp().run()  
  
---  
  
 __

 __

