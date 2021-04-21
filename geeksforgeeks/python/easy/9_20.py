Hello World in Kivy



Kivy is an opensource multi-platform GUI development library for Python and
can run on iOS, Android, Windows, OS X, and GNU/Linux. It helps develop
applications that make use of innovative, multi-touch UI. The fundamental idea
behind Kivy is to enable the developer to build an app once and use it across
all devices, making the code reusable and deployable, allowing for quick and
easy interaction design and rapid prototyping.

 **Note:** Since Kivy is based in Python, Python is a prerequisite before
installing Kivy. For more information, refer to Python Programming Language.

#### Installation

There are several ways to get Kivy installed in your system, depending upon
your Operating System. Let’s dive into it.  
 **Windows OS**

  *  **Using pip**
    
        pip install kivy

  *  **Using conda**
    
        conda install -c conda-forge kivy

 **Linux**

  *  **Add the PPA using the following command:**
    
        sudo add-apt-repository ppa:kivy-team/kivy

  *  **Update your package list using your package manager-**
    
        sudo apt-get update

  *  **Install Kivy**
    
        sudo apt-get install python3-kivy

 **OS X**

  

  

  *  **Using Wheels**  
Wheels are precompiled binaries for the specific platform you are on. All you
need to do to install Kivy using wheels on osx is

    
        $ python -m pip install kivy

## Hello World in Kivy

  * Let’s create a Python file i.e. with .py extension.
  * First of all let’s import kivy and ensure it’s up-to-date.  

    
    
    import kivy
    
    # Replace this with your 
    # current version
    kivy.require('1.11.1')   
    # To find your kivy version use,
    # print(kivy.__version__)
    

  * Now to create a Kivy interface we need to import Kivy App module in our program using the following code:  

    
    
    from kivy.app import App
    

  * Now import Label from kivy.uix.label  

    
    
    from kivy.uix.label import Label
    

  * Now let’s write main block that prints Hello World, yayy finally!!  

    
    
    class MyFirstKivyApp(App):
        def build(self):
            return Label(text ="Hello World !")
    

**Complete Program**

 __

 __  
 __

 __

 __  
 __  
 __

import kivy

from kivy.app import App

from kivy.uix.label import Label

 

 

# Replace this with your 

# current version

kivy.require('1.11.1') 

 

# Defining a class

class MyFirstKivyApp(App):

 

 # Function that returns 

 # the root widget

 def build(self):

 

 # Label with text Hello World is 

 # returned as root widget

 return Label(text ="Hello World !") 

 

 

# Here our class is initialized

# and its run() method is called. 

# This initializes and starts 

# our Kivy application.

MyFirstKivyApp().run()   
  
---  
  
__

__

**Output:**

![hello-world-kivy](https://media.geeksforgeeks.org/wp-
content/uploads/20200128023758/Screenshot-2632.png)

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

