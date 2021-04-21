How to make a Hyperlink in a Button in Kivy?



Kivy is a platform-independent GUI tool in Python. It can run on Android, IOS,
Linux and Windows, etc. This is the only GUI library from python which can
independently run on the android device even we can use it on Raspberry Pi
also. If you are new to kivy you can learn from this link.

In this article, we will develop a GUI window using kivy framework of Python,
and we will add a button on this window. Usually what happens is we attach a
method to a button and the whole method is defined in another python file but
this time we will write the button code of python in the same kivy string.

 **Note:** We are using the on_release event here with the button to make it
functional. We can also use the on_press event also rather than the on_release
event, both events can open the link, the only difference is on_release event
will open the link when we release our finger from the button while on_press
will open the link as soon as we touch the button. For using on_press event
simply replace on_release with on_press.

Here, the IDE we are going to use is pycharm and the version of python we are
going to use is python 3.6.

 **Implementation**

  

  

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

 

 

# this is the main class which will render the whole application

class uiApp(App):

 

 # method which will render our application

 def build(self):

 return Builder.load_string("""

 

Button:

 

 # text which will appear on button

 text:"click here to open google search"

 

 on_release:

 

 # importing webbrowser module

 import webbrowser

 

 # it will open google window in your browser

 webbrowser.open('http://www.google.com')

 

 print("see like this way you can write python supported code in kivy
file")

 

 

 """)

 

# running the application

uiApp().run()  
  
---  
  
 __

 __

 **Output:**

https://media.geeksforgeeks.org/wp-content/uploads/20210204133102/brow.mp4

  

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

