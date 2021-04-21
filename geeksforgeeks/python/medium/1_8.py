How to create Option Menu in Tkinter ?



The **Tkinter** package is the standard GUI (Graphical user interface) for
python, which provides a powerful interface for the Tk GUI Toolkit. In this
tutorial, we are expecting that the readers are aware of the concepts of
python and tkinter module.

## OptionMenu

In this tutorial, our main focus is to create option menu using tkinter in
python. As the name suggests, option menu is a list of options for the user in
simple language. This can be achieved using OptionMenu class, which creates a
pop-up menu and displays the options that the user can avail.

we can create an option menu by initializing the constructor of that class.

>  **Syntax:** OptionMenu(parent, variable, choice_1, choice_2, choice_3, …)
>
>   * parent- This is a parent object which is also called as master object.
> It’s main role is to create the window for GUI and also keep other widgets
> used in the program.
>   * variable- This is the default name that should be shown to the option
> menu.
>   * choice_1, choice_2, choice_3, …- These are the actual list of options
> that are available for the user.
>

As OptionMenu is a class, so obviously there will be some methods in it. Let’s
study some methods one-by-one.

  

  

  1. get() method- This method of OptionMenu return the value which is currently selected from the option menu.
  2. mainloop() method- This method is not only the part of OptionMenu class but also the part of whole tkinter package. It’s role is to combine all the widgets in our program before we run it and hence used at the end when we are done with our code.
  3. place() method- This method keeps all the widgets at the specified position by the programmer.
  4. pack() method- This method helps in arranging the OptionMenu in a specific position.

Let us now have a lot at some examples which will make our concepts more
clear.

This is a basic example to create a simple option menu.

 **Example 1:**

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# Importing the tkinter module using import keyword

from tkinter import *

 

# Initialize parent object or master object as "parent"

parent = Tk()

 

# passing master object as parameter and set "COLOURS" as

# the name of the OptionMenu using set() method.

variable = StringVar(parent)

variable.set("COLOURS")

 

# Constructor of OptionMenu class intialized by giving

# the parametrs as master object, variable name and the

# list of options in the menu.

option_menu = OptionMenu(parent, variable, "Yellow",

 "Blue", "Green", "Purple",

 "Black", "White")

 

# Using pack() method in OptionMenu class to arrange the

# option menu.

option_menu.pack()

 

# Using mainloop() method from OptionMenu class before we

# run the code.

parent.mainloop()  
  
---  
  
 __

 __

 **Output:**

![option menu tkinter](https://media.geeksforgeeks.org/wp-
content/uploads/20210308193319/optionmenutkinter.gif)

 **Example 2:**

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# Import tkinter using import keyword

import tkinter as tk

 

# set the master object in parent variable

parent = tk.Tk()

 

# Title for our window

parent.title("Geeksforgeeks- OptionMenu")

 

# Creating a Option Menu for AGE

# Set the variable for AGE and create the list 

# of options by initializing the constructor 

# of class OptionMenu.

Age_Variable = tk.StringVar(parent)

Age_Variable.set("Age")

Age_Option = tk.OptionMenu(parent, Age_Variable, 

 "below 14", "15", 

 "16", "17", 

 "above 18")

Age_Option.pack()

 

# Creating a Option Menu for GENDER

# Set the variable for GENDER and create the list 

# of options by initializing the constructor 

# of class OptionMenu.

Gender_Variable = tk.StringVar(parent)

Gender_Variable.set("Gender")

Gender_Option = tk.OptionMenu(parent, 

 Gender_Variable, 

 "Male", "Female")

Gender_Option.pack()

 

# Creating a Option Menu for HOBBY

# Set the variable for HOBBY and create the list 

# of options by initializing the constructor 

# of class OptionMenu.

Hobby_Variable = tk.StringVar(parent)

Hobby_Variable.set("Hobby")

Hobby_Option = tk.OptionMenu(parent, Hobby_Variable, 

 "Dance", "Code", "Sing", 

 "Draw")

Hobby_Option.pack()

 

# Combining all the widgets used in the 

# program before running it

parent.mainloop()  
  
---  
  
 __

 __

 **Output:**

![tkinter option menu](https://media.geeksforgeeks.org/wp-
content/uploads/20210308193443/tkinteroptionmenu.gif)  

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

