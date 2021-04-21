Python | Add Label to a kivy window



Kivy is a platform independent GUI tool in Python. As it can be run on
Android, IOS, linux and Windows etc. It is basically used to develop the
Android application, but it does not mean that it can not be used on Desktops
applications.

 **Label widget –**  
The Label widget is for rendering text. It supports ascii and unicode strings.
Label is the text which we want to add on our window, give to the buttons and
so on. On labels, we can apply the styling also i.e increase text, size, color
and more.

Let’s see how to add Label to a Kivy window.

> 👉🏽 Kivy Tutorial – Learn Kivy with Examples.

 **How to add a label ?**

  

  

    
    
    1) import kivy
    2) import kivy App
    3) import label
    4) set minimum version (optional)
    5) Extend the App class
    6) overwrite the build function
    7) Add and return label
    8) Run the instance of class

Below is the code:

 __

 __  
 __

 __

 __  
 __  
 __

# import kivy module

import kivy

 

# this restricts the kivy version i.e

# below this kivy version you cannot use the app or software

kivy.require("1.9.1")

 

# base Class of your App inherits from the App class.

# app:always refers to the instance of your application

from kivy.app import App

 

# if you not import label and use it it through error

from kivy.uix.label import Label

 

# defining the App class

class MyLabelApp(App):

 def build(self):

 # label display the text on screen 

 lbl = Label(text ="Label is Added on screen !!:):)")

 return lbl

 

# creating the object

label = MyLabelApp()

# run the window

label.run()  
  
---  
  
 __

 __

 **Output:**  
![](https://media.geeksforgeeks.org/wp-
content/uploads/20190419094035/Capture34-2.png)

  
**How to do Styling in label ?**

 __

 __  
 __

 __

 __  
 __  
 __

# change only line 19 else all will same.

 

# text colour

l2 = Label(text ="Label is Added on \n screen !!:):) 

 and its Multi\nLine", font_size ='20sp',

 color =[0.41, 0.42, 0.74, 1])  
  
---  
  
 __

 __

 **Output:**  
![](https://media.geeksforgeeks.org/wp-
content/uploads/20190419103247/Capture55.png)  
  
**How to markup the text ?**

You can change the style of the text using Text Markup. The syntax is similar
to above syntax but some more things are there.

 __

 __  
 __

 __

 __  
 __  
 __

# markup text with different colour

l2 = Label(text ="[color = ff3333][b]'Label'[/b] is
Added [/color]\n

 [color = 3333ff]Screen !!:):):):)[/color]",

 font_size ='20sp', markup = True)  
  
---  
  
 __

 __

 **Output:**  
![](https://media.geeksforgeeks.org/wp-
content/uploads/20190419105448/markup.png)

 **More markup tags we can use –**

> [b][/b] **- >** Activate bold text
>
>  
>
>
>  
>
>
> [i][/i] **- >** Activate italic text
>
> [u][/u] **- >** Underlined text
>
> [s][/s] **- >** Strikethrough text
>
> [font=][/font] **- >** Change the font
>
> [size=][/size]] **- >** Change the font size
>
> [color=#][/color] **- >** Change the text color
>
> [ref=][/ref] **- >** Add an interactive zone. The reference + bounding box
> inside the reference will be available in Label.refs
>
> [anchor=] **- >** Put an anchor in the text. You can get the position of
> your anchor within the text with Label.anchors
>
> [sub][/sub] **- >** Display the text at a subscript position relative to
> the text before it.
>
> [sup][/sup] **- >** Display the text at a superscript position relative to
> the text before it.

Reference: https://kivy.org/doc/stable/api-kivy.uix.label.html

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

