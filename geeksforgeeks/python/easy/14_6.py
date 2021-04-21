Python | Create a digital clock using Tkinter



As we know Tkinter is used to create a variety of GUI (Graphical User
Interface) applications. In this article we will learn how to create a Digital
clock using Tkinter.

>  **Prerequisites:**  
>  -> Python functions  
> -> Tkinter basics (Label Widget)  
> -> Time module

 **UsingLabel widget from Tkinter and time module :**  
In the following application, we are going to use _ **Label widget**_ and also
going to use _**time module**_ which we will use to retrieve system’s time.

Below is the implementation:

 __

 __  
 __

 __

 __  
 __  
 __

# importing whole module

from tkinter import *

from tkinter.ttk import *

 

# importing strftime function to

# retrieve system's time

from time import strftime

 

# creating tkinter window

root = Tk()

root.title('Clock')

 

# This function is used to 

# display time on the label

def time():

 string = strftime('%H:%M:%S %p')

 lbl.config(text = string)

 lbl.after(1000, time)

 

# Styling the label widget so that clock

# will look more attractive

lbl = Label(root, font = ('calibri', 40, 'bold'),

 background = 'purple',

 foreground = 'white')

 

# Placing clock at the centre

# of the tkinter window

lbl.pack(anchor = 'center')

time()

 

mainloop()  
  
---  
  
 __

 __

 **Output:**  
![](https://media.geeksforgeeks.org/wp-
content/uploads/20190411014514/clock_photo.png)

https://media.geeksforgeeks.org/wp-content/uploads/20190411013837/clock.mp4

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

