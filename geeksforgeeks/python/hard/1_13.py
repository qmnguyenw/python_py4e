Hex Color for Button Background – Kivy



Kivy is a platform-independent GUI tool in Python. It can run on Android, IOS,
Linux and Windows, etc. This is the only GUI library from python which can
independently run on the android device even we can use it on Raspberry pi
also. It is an open-source Python library for the rapid development of multi-
touch applications. Its graphic engine is built over OpenGL and it also
supports a fast graphics pipeline.

This article focuses on creating a GUI window using kivy with a button and
then add colors to it using hex color codes.

### Approach

  * Import kivy button
  * Import kivy app
  * Import kivy builder
  * Create App class
  * Create button
  * Create mechanism to change color on click of the button
  * Return builder string
  * Run an instance of the class

 **Program:**

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

 

# importing builder from kivy

from kivy.lang import Builder

 

 

# this is the main class which will 

# render the whole application

class uiApp(App):

 

 # method which will render our application

 def build(self):

 

 return Builder.load_string("""

 

#:import C kivy.utils.get_color_from_hex

Button:

 

 # text which will appear on first button

 text:"first button"

 

 background_color: C("#f9f871")

 """)

 

 

# running the application

uiApp().run()  
  
---  
  
 __

 __

 **Output:**

  

  

https://media.geeksforgeeks.org/wp-
content/uploads/20210204124445/hexupdated.mp4

  

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

