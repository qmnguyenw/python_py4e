Python | Switch widget in Kivy using .kv file



Kivy is a platform independent GUI tool in Python. As it can be run on
Android, IOS, linux and Windows etc. It is basically used to develop the
Android application, but it does not mean that it can not be used on Desktops
applications.

> 👉🏽 Kivy Tutorial – Learn Kivy with Examples.

### Switch widget:

The Switch widget is active or inactive, as a mechanical light switch. The
user can swipe to the left/right to activate/deactivate it.  
The value represented by the switch is either True or False. That is the
switch can be either in On position or Off position.

To work with Switch you must have to import:

    
    
    from kivy.uix.switch import Switch

 **Attaching Callback to Switch:**

  

  

  * A switch can be attached with a call back to retrieve the value of the switch.
  * The state transition of a switch is from either ON to OFF or OFF to ON.
  * When switch makes any transition the callback is triggered and new state can be retrieved i.e came and any other action can be taken based on the state.
  * By default, the representation of the widget is static. The minimum size required is 83*32 pixels.
  * The entire widget is active, not just the part with graphics. As long as you swipe over the widget’s bounding box, it will work.

    
    
     **Basic Approach:**
    
    1) import kivy
    2) import kivyApp
    3) import Switch
    4) import Gridlayout
    5) import Label
    6) Set minimum version(optional)
    7) create Layout class(In this you create a switch):
            --> define the callback of the switch in this
    8) create App class
    9) create .kv file (name same as the app class):
            1) create boxLayout
            2) Give Lable
            3) Create Switch
            4) Bind a callback if needed
    10) return Layout/widget/Class(according to requirement)
    11) Run an instance of the class

 **Below is the Implementation:**

We have explained how to create button, attach a callback to it and how to
disable a button after making it active/inactive.

 **main.py file:**

 __

 __  
 __

 __

 __  
 __  
 __

# Program to explain how switch works

 

# import kivy module 

import kivy 

 

# base Class of your App inherits from the App class. 

# app:always refers to the instance of your application 

from kivy.app import App

 

# this restrict the kivy version i.e 

# below this kivy version you cannot 

# use the app or software 

kivy.require('1.9.0')

 

# The Switch widget is active or inactive

# The state transition of a switch is from

# either on to off or off to on.

from kivy.uix.switch import Switch

 

# The GridLayout arranges children in a matrix.

# It takes the available space and

# divides it into columns and rows,

# then adds widgets to the resulting “cells”.

from kivy.uix.gridlayout import GridLayout

 

# The Label widget is for rendering text. 

from kivy.uix.label import Label

 

# A Gridlayout with a label a switch

# A class which contains all stuff about the switch 

class SimpleSwitch(GridLayout):

 

 # number of rows 

 rows = 4

 

 # Callback for the switch state transition

 # Defining a Callback function

 # Contains Two parameter switchObject, switchValue

 def switch_callback(self, switchObject, switchValue):

 

 # Switch value are True and False

 if(switchValue):

 print('Switch is ON:):):)')

 else:

 print('Switch is OFF:(:(:(')

 

 

# Defining the App Class

class SwitchApp(App):

 # define build function

 def build(self):

 # retuen the switch class

 return SimpleSwitch()

 

 

# Run the kivy app

if __name__ == '__main__':

 SwitchApp().run()  
  
---  
  
 __

 __

  
.kv file : in this we have done the callbacks and done the button disable
also.

 __

 __  
 __

 __

 __  
 __  
 __

# .kv file in which the whole functions of a switch

# Along with labels are present

 

<SimpleSwitch>:

 

 # creating box layout for better view

 BoxLayout:

 size_hint_y: None

 height: '48dp'

 

 # Adding label to switch

 Label:

 text: 'Switch normal'

 

 # creating the switch

 Switch:

 

 # False means OFF and True means ON

 active: False

 

 # Arranging a callback to the switch

 on_active: root.switch_callback(self, self.active)

 

 # Another for another switch

 

 BoxLayout:

 size_hint_y: None

 height: '48dp'

 

 Label:

 text: 'Switch active'

 Switch:

 active: True

 on_active: root.switch_callback(self, self.active)

 

 

 BoxLayout:

 size_hint_y: None

 height: '48dp'

 

 Label:

 text: 'Switch off & disabled'

 

 Switch:

 # disabled True means After making switch False

 # it is disabled now you cannot change its state

 disabled: True

 active: False

 

 BoxLayout:

 size_hint_y: None

 height: '48dp'

 

 Label:

 text: 'Switch on & disabled'

 Switch:

 disabled: True

 active: True  
  
---  
  
 __

 __

 **Output:**

Image 1:  
![](https://media.geeksforgeeks.org/wp-
content/uploads/20190530161923/Capture34-3-300x165.png)

Image 2:  
![](https://media.geeksforgeeks.org/wp-
content/uploads/20190530161927/Capture227-300x165.png)

Image to show callbacks:  
![](https://media.geeksforgeeks.org/wp-
content/uploads/20190530161919/Capture34-3-282x300.png)

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

