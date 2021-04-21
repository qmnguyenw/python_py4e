Looping through buttons in Tkinter



In this article, let’s see how we can loop through the buttons in Tkinter.

 **Stepwise implementation:**

 **Step 1:** Import the Tkinter package and all of its modules and create a
root window (root = Tk()).

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# Import package and it's modules

from tkinter import *

 

# create root window

root = Tk()

 

# root window title and dimension

root.title("GeekForGeeks")

 

# Set geometry (widthxheight)

root.geometry('400x400')

 

# Execute Tkinter

root.mainloop()  
  
---  
  
 __

 __

 **Output**

  

  

![](https://media.geeksforgeeks.org/wp-
content/uploads/20210313005401/gfg1img.jpg)

 **Step 2:** Now let’s add a Entry() class and will display the button name as
soon as one of the buttons is clicked.

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# Import package and it's modules

from tkinter import *

 

# create root window

root = Tk()

 

# root window title and dimension

root.title("GeekForGeeks")

 

# Set geometry (widthxheight)

root.geometry('400x400')

 

# Entry Box

text = Entry(root, width = 30, bg = 'White')

text.pack(pady = 10)

 

# Execute Tkinter

root.mainloop()  
  
---  
  
 __

 __

 **Output**

![](https://media.geeksforgeeks.org/wp-
content/uploads/20210313010852/gfg2.jpg)

**Step 3:** Now let’s create an empty dictionary (button_dict) to save all the
button objects and a list consisting of names of all the buttons. Now loop
over each item of the list to create an button object of it and store it in
the dictionary. For the button command, create a function named ‘action’ and
for each button call the **text_update()** function to update the changes in
the entry in Entry() object created earlier.

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# Import package and it's modules

from tkinter import *

 

 

# text_update function

def text_updation(language):

 text.delete(0, END)

 text.insert(0, language)

 

# create root window

root = Tk()

 

# root window title and dimension

root.title("GeekForGeeks")

 

# Set geometry (widthxheight)

root.geometry('400x400')

 

# Entry Box

text = Entry(root, width=30, bg='White')

text.pack(pady=10)

 

# create buttons

button_dict = {}

words = ["Python", "Java", "R", "JavaScript"]

for lang in words:

 

 # pass each button's text to a function

 def action(x = lang): 

 return text_updation(x)

 

 # create the buttons 

 button_dict[lang] = Button(root, text = lang,

 command = action)

 button_dict[lang].pack(pady=10)

 

# Execute Tkinter

root.mainloop()  
  
---  
  
 __

 __

 **Output**

![loop through button tkinter](https://media.geeksforgeeks.org/wp-
content/uploads/20210317115505/loopthroughbuttontkinter.gif)  

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

