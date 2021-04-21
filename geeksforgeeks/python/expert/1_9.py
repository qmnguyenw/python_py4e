Python – Adding double tap on any widget in kivy



Kivy is a platform-independent GUI tool in Python. It can run on Android, IOS,
Linux and Windows, etc. This is the only GUI library from python which can
independently run on an android device even we can use it on Raspberry Pi
also. It is an open-source Python library for the rapid development of
applications that make use of innovative user interfaces, such as multi-touch
apps. Its graphic engine is built over OpenGL ES 2 and has fast graphics
pipeline. If you are new to kivy you can learn from this link.

In this article, we will develop a GUI window using kivy framework of python,
and we will add an image on this window(you can follow the same pattern for
implementing double-tap event on other widgets also) and we will add a double-
tap event on this image.

#### A basic approach to implement double-tap on image widget

  1. Import image widget from kivy package
  2. Import touchbehaviour from kivy package
  3. Import kivy app
  4. Import boxlayout from kivy package
  5. Add widget
  6. Extend the class
  7. Return layout
  8. Run an instance of the class

 **Code:**

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

 

# importing Touch behaviour event from kivy framework

from kivymd.uix.behaviors import TouchBehavior

from kivy.app import App

 

# importing boxlayout for our application

from kivy.uix.boxlayout import BoxLayout

 

# attaching touch behaviour with image widget

class ImageWithDoubleTouch(Image, TouchBehavior):

 

 # event for double-tap

 def on_double_tap(self, instance, *args):

 print("wow!! you have double clicked an image named
"+self.source)

 

# this will connect MainWindow which we have 

# created in ui.kv with main.py file

class MainWindow(BoxLayout):

 pass

"""

Note:- keep in mind that our .kv file name was ui.kv so our rendering 

class(class which will render our application) name 

should be like uiApp otherwise we will not get the desired output!!

"""

 

# this is the main class which will render 

# the whole application

class uiApp(App):

 

 # method which will render our application

 def build(self):

 return MainWindow()

 

# running the application

uiApp().run()  
  
---  
  
 __

 __

#### kivy Code:

> #window which contains our image
>
>  
>
>
>  
>
>
> <MainWindow>:
>
> BoxLayout:
>
> # adding our ImageWithDoubleTouch widget that we have created in main.py
> file
>
> ImageWithDoubleTouch:
>
> # adding path of image file
>
> source:”gfg.png”

 **Output:**

https://media.geeksforgeeks.org/wp-
content/uploads/20210202203356/doubletap.mp4

  

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

