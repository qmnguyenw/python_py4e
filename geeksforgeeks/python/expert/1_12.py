Kivy – Material design Icon button



Kivy is a platform-independent GUI tool in Python. It can run on Android, IOS,
Linux and Windows, etc. This is the only GUI library from python which can
independently run on an android device even we can use it on Raspberry pi
also. It is an open-source Python library for rapid development of
applications that make use of innovative user interfaces, such as multi-touch
apps. Its graphic engine is built over OpenGL ES 2 and has fast graphics
pipeline.

In this article, we will develop a GUI window using kivy framework of python,
and we will add material design icon buttons of different sizes on this
window.

 **Approach:**

  * Import required modules.
  * Create an App class.
  * Add Buttons.
  * Return layout.
  * Run an instance of the class.

 **Implementation:**

## Python3

  

  

 __

 __  
 __

 __

 __  
 __  
 __

# importing mdapp from kivymd framework

from kivymd.app import MDApp

 

# importing builder from kivy

from kivy.lang import Builder

 

# this is the main class which

# will render the whole application

class uiApp(MDApp):

 

 # method which will render our application

 def build(self):

 return Builder.load_string("""

 

MDBoxLayout:

 spacing:300

 MDIconButton:

 

 # name of mdicon

 icon:"language-python" 

 pos_hint: {"center_x": .5, "center_y": .5}

 user_font_size: "64sp"

 

 # bgcolor of iconbutton

 md_bg_color:[1,1,0,1] 

 

 MDIconButton:

 

 # custom image as mdicon

 icon:"gfg.png" 

 pos_hint: {"center_x": .5, "center_y": .5}

 user_font_size: "16sp"

 

 MDIconButton:

 

 icon:"language-python"

 pos_hint: {"center_x": .5, "center_y": .5}

 

 """)

 

# running the application

uiApp().run()  
  
---  
  
 __

 __

