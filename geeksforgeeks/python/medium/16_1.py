Python | setting and retrieving values of Tkinter variable



Tkinter supports some variables which are used to manipulate the values of
Tkinter widgets. These variables work like normal variables.  
set() and get() methods are used to set and retrieve the values of these
variables.  
The values of these variables can be set using set() method or by using
constructor of these variables.

There are 4 tkinter variables.

  * BooleanVar()
  * StringVar()
  * IntVar()
  * DoubleVar()

## Setting values of Tkinter variables –

 **1\. Using variable’s constructor**

 **Syntax:**

    
    
    var = Tkinter_variable(master, value = any_value)
    

__

__  
__

__

__  
__  
__

# importing tkinter module

from tkinter import *

 

# creating Tk() variable

# required by Tkinter classes

master = Tk()

 

# Tkinter variables

# initialization using constructor

intvar = IntVar(master, value = 25, name ="2")

strvar = StringVar(master, "Hello !")

boolvar = BooleanVar(master, True)

doublevar = DoubleVar(master, 10.25)  
  
---  
  
 __

 __

  
 **2\. Using set() method**

