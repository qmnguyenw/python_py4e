Python | Kivy .kv File



As when we write the application in Python kivy, to write all the things on
the same code make a mess in the code and it is hard to understand that by
someone another. Also writing a large code makes hard to maintain the
construction of the widget tree and explicit the declaration of bindings.

The KV language, allows us to create own widget tree in a declarative way and
to bind the widget properties to each other or to callbacks in a natural way.

> 👉🏽 Kivy Tutorial – Learn Kivy with Examples.

 **How to load _kv_ file:**

There are 2-ways to load the .kv file into code or Application

  

  

  1.  **By name convention method-**

While writing code we will make the App class. For this method, the name of
the file and the app class is same and save the kv file with
appclassname.kv.  
Kivy looks for a Kv file with the same name as your App class in lowercase,
minus “App” if it ends with ‘App’ e.g:

    
        classnameApp ---> classname.kv

If this file defines a Root Widget it will be attached to the App’s root
attribute and used as the base of the application widget tree.

The sample code on how to use .kv file in kivy is given below:

 __

 __  
 __

 __

 __  
 __  
 __

# code how to use .kv file in kivy

 

# import kivy module

import kivy

 

# base Class of your App inherits from the App class.

# app:always refers to the instance of your application

from kivy.app import App

 

# this restrict the kivy version i.e

# below this kivy version you cannot 

# use the app or software

# not coumpulsary to write it

kivy.require('1.9.1')

 

# define the App class

# and just pass rest write on kvfile

# not necessary to pass

# can also define function in it

class kvfileApp(App):

 pass

 

kv = kvfileApp()

kv.run()  
  
---  
  
 __

 __

 **.kv file code save with the same name as the app class –**

 __

 __  
 __

 __

 __  
 __  
 __

Label:

 text:

 ('[b]Hello[/b] [color = ff0099]World[/color]\n'

 '[color = ff0099]Hello[/color] [b]World[/b]\n'

 '[b]Hello[/b] [color = ff0099]World:):)[/color]')

 markup: True

 font_size: '64pt'  
  
---  
  
 __

 __

 **Output:**  
![](https://media.geeksforgeeks.org/wp-
content/uploads/20190419142445/Capture34-2.png)

  2.  **Builder method-**  
For this method to use you first have to import Builder by writing

    
        from kivy.lang import builder

Now by the builder you can directly load the whole file as a string or as a
file. By doing this for loading .kv file as a file:

    
        Builder.load_file('.kv/file/path')

or, for loading, kv file as a string:

    
        Builder.load_string(kv_string)

 __

 __  
 __

 __

 __  
 __  
 __

# code to use the .kv file as a string in the main file

# code how to use .kv file in kivy

 

# import kivy module

import kivy

 

# base Class of your App inherits from the App class.

# app:always refers to the instance of your application

from kivy.app import App

 

# it is to import Builder

from kivy.lang import Builder

 

# this restrict the kivy version i.e

# below this kivy version you cannot use the app or software

# not coumpulsary to write it

kivy.require('1.9.1')

 

# building kv file as string

kvfile = Builder.load_string("""

Label:

 text:

 ('[b]Hello[/b] [color = ff0099]World[/color]\\n'

 '[color = ff0099]Hello[/color] [b]World[/b]\\n'

 '[b]Hello[/b] [color = ff0099]World:):)[/color]')

 markup: True

 font_size: '64pt'

""")

 

# define the App class

# and just pass rest write on kvfile

# not necessary to pass

# can also define function in it

class kvfileApp(App):

 def build(self):

 return kvfile

 

kv = kvfileApp()

kv.run()  
  
---  
  
 __

 __

 **Output:**  
![](https://media.geeksforgeeks.org/wp-
content/uploads/20190419142445/Capture34-2.png)

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

