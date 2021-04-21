Python | PageLayout in Kivy



Kivy is a platform independent GUI tool in Python. As it can be run on
Android, IOS, linux and Windows etc. It is basically used to develop the
Android application, but it does not mean that it can not be used on Desktops
applications.

> 👉🏽 Kivy Tutorial – Learn Kivy with Examples.

### PageLayout:

The PageLayout works in a different manner from other layouts. It is a dynamic
layout, in the sense that it allows flipping through pages using its borders.
The idea is that its components are stacked in front of each other, and we can
just see the one that is on top.  
The PageLayout class is used to create a simple multi-page layout, in a way
that allows easy flipping from one page to another using border.

To use PageLayout you have to import it by the below command:

    
    
    from kivy.uix.pagelayout import PageLayout

 **Note:**  
PageLayout does not currently honor the size_hint, size_hint_min,
size_hint_max, or pos_hint properties.That means we can not use all these in a
page layout.

  

  

 **Basic Approach to create PageLayout:**

    
    
    1) import kivy
    2) import kivyApp
    3) import Pagelayout
    4) import button
    5) Set minimum version(optional)
    6) create App class:
            - define build() function
    7) return Layout/widget/Class(according to requirement)
    8) Run an instance of the class
    

  
**Implementation of the Approach:**

 __

 __  
 __

 __

 __  
 __  
 __

# Sample Python application demonstrating

# How to create PageLayout in Kivy 

 

import kivy 

 

# base Class of your App inherits from the App class. 

# app:always refers to the instance of your application 

from kivy.app import App 

 

# The PageLayout class is used to create

# a simple multi-page layout,

# in a way that allows easy flipping from

# one page to another using borders.

from kivy.uix.pagelayout import PageLayout

 

# creates the button in kivy 

# if not imported shows the error 

from kivy.uix.button import Button

 

class PageLayout(PageLayout):

 """

 Define class PageLayout here

 """

 

 def __init__(self):

 

 # The super function in Python can be

 # used to gain access to inherited methods

 # which is either from a parent or sibling class.

 super(PageLayout, self).__init__()

 

 # creating buttons on diffent pages

 btn1 = Button(text ='Page 1')

 

 btn2 = Button(text ='Page 2')

 

 btn3 = Button(text ='Page 3')

 

 # adding button on the screen

 # by add widget method

 self.add_widget(btn1)

 

 self.add_widget(btn2)

 

 self.add_widget(btn3)

 

 

# creating the App class

class Page_LayoutApp(App):

 """

 App class here

 """

 

 def build(self):

 """

 build function here

 """

 return PageLayout()

 

 

# Run the App

if __name__ == '__main__':

 Page_LayoutApp().run()  
  
---  
  
 __

 __

 **Output:**

 **Page 1 image**  
![](https://media.geeksforgeeks.org/wp-
content/uploads/20190523203046/page-12-300x165.png)

 **Page 2 image**  
![](https://media.geeksforgeeks.org/wp-
content/uploads/20190523203043/page-23-300x165.png)

 **Page 3 image**  
![](https://media.geeksforgeeks.org/wp-
content/uploads/20190523203045/page-31-300x165.png)

In PageLayout You can add some features on every page. We can add image,
create canvas, add color, add multiple widgets, multiple layouts  
This is how we can use the PageLayout in an efficient way. One of the best
example Our gallery Contains multiple pages.

Below is the code in which i am adding the different color to every page with
the help of get_color_from_hex

  

  

 **Implementation of the PageLayout with features**

 __

 __  
 __

 __

 __  
 __  
 __

# Sample Python application demonstrating the

# working of PageLayout in Kivy with some features

 

import kivy 

 

# base Class of your App inherits from the App class. 

# app:always refers to the instance of your application 

from kivy.app import App 

 

# The PageLayout class is used to create

# a simple multi-page layout,

# in a way that allows easy flipping from

# one page to another using borders.

from kivy.uix.pagelayout import PageLayout

 

# creates the button in kivy 

# if not imported shows the error 

from kivy.uix.button import Button

 

 

# The Utils module provides a selection of general utility

# functions and classes that may be useful for various applications.

# These include maths, color, algebraic and platform functions.

# Here we are usinmg color from the module

# By get_color_from_hex

# Transform a hex string color to a kivy Color.

from kivy.utils import get_color_from_hex

 

class PageLayout(PageLayout):

 """

 Define class PageLayout here

 """

 

 def __init__(self):

 

 # The super function in Python can be

 # used to gain access to inherited methods

 # which is either from a parent or sibling class.

 super(PageLayout, self).__init__()

 

 # creating buttons on diffent pages

 

 # Button 1 or Page 1

 btn1 = Button(text ='Page 1')

 # Adding Colour to page

 # Here we are using colour from

 

 btn1.background_color = get_color_from_hex('# FF0000')

 

 btn2 = Button(text ='Page 2')

 btn2.background_color = get_color_from_hex('# 00FF00')

 

 btn3 = Button(text ='Page 3')

 btn3.background_color = get_color_from_hex('# 0000FF')

 

 

 # adding button on the screen

 # by add widget method

 self.add_widget(btn1)

 

 self.add_widget(btn2)

 

 self.add_widget(btn3)

 

 

# creating the App class

class Page_LayoutApp(App):

 """

 App class here

 """

 

 def build(self):

 """

 build function here

 """

 return PageLayout()

 

 

# Run the App

if __name__ == '__main__':

 Page_LayoutApp().run()  
  
---  
  
 __

 __

 **Output:**

 **Page 1**  
![](https://media.geeksforgeeks.org/wp-
content/uploads/20190523204109/page-c-1-300x165.png)

 **Page 2**  
![](https://media.geeksforgeeks.org/wp-
content/uploads/20190523204104/page-2-c-300x165.png)

 **Page 3**  
![](https://media.geeksforgeeks.org/wp-
content/uploads/20190523204106/page-3-c-300x165.png)

 **Video Output:**  

https://media.geeksforgeeks.org/wp-content/uploads/20190523204914/Page-
layout.webm

 **Note:** More effective when works on Android, Ios, any other touch
supported Laptops.

Reference: https://kivy.org/doc/stable/api-kivy.uix.pagelayout.html

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

