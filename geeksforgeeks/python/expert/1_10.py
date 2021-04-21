How to add custom fonts in Kivy – Python?



 **Prerequisites:**Kivy Tutorial

Kivy is a platform-independent GUI tool in Python. It can run on Android, IOS,
Linux and Windows, etc. This is the only GUI library from python which can
independently run on the android device even we can use it on Raspberry pi
also. It is an open-source Python library for the rapid development of multi-
touch applications. Its graphic engine is built over OpenGL, and it supports
fast graphics pipeline.

In this article, we will develop a GUI window using kivy framework of Python,
and we will add a button on this window and we will add our own font style on
this button’s text. For this task you should have a custom font style, don’t
worry if you don’t have yours you can download from this link here you will
get ample of font styles you can also download and unzip them. After unzipping
you will get files in .ttf format keep those files because they are holding
the actual font styles.

 **Step-by-step approach:**

Basic Approach for using the custom font in kivy application:

  

  

  * Import button
  * Import kivyApp
  * Import labelbase
  * Import builder
  * Create App class
  * Return layout
  * Run an instance of the class

 **Implementation:**

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# importing button widget from kivy framework

from kivy.uix.button import Button

from kivy.app import App

 

# importing labelbase which which 

# register our custom font for application

from kivy.core.text import LabelBase

from kivy.lang import Builder

 

 

# this is the main class which will

# render the whole application

class uiApp(App):

 

 # method which will render our application

 def build(self):

 return Builder.load_string("""

 

# adding our button

Button:

 

 # text which will appear on first button

 text:"first button"

 

 # specifying the fontstyle name that we 

 # have registered in main.py file

 font_name:"Lemonada"

 font_size:65

 """)

 

 

# registering our new custom fontstyle

LabelBase.register(name='Lemonada', 

 fn_regular='Lemonada-VariableFont_wght.ttf')

 

# running the application

uiApp().run()  
  
---  
  
 __

 __

 **Output:**

https://media.geeksforgeeks.org/wp-
content/uploads/20210204123848/customfontupdated.mp4

  

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

