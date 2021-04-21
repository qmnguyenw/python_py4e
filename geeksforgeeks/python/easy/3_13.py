Build an Application to translate English to Hindi in Python



In these articles, We are going to write python scripts to translate English
word to Hindi word and bind it with the GUI application. We are using the
**englisttohindi** module to translate the English word to the Hindi word.

 **Installation:**

Run this code into your terminal:

    
    
    pip install englisttohindi
    

**Approach:**

  * Import englisttohindi modules.
  * Create an object of EngtoHindi() by passing the message.
  * Use convert() methods for the translation.

 **Example:**

  

  

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# importing the module

from englisttohindi.englisttohindi import EngtoHindi

 

# message to be translated

message = "Yes, I am geeks"

 

# creating a EngtoHindi() object

res = EngtoHindi(message)

 

# displaying the translation

print(res.convert)  
  
---  
  
 __

 __

 **Output:**

    
    
    हां, मैं गीक्स हूं
    

**English to Hindi Translator Application with Tkinter:** This Script
implements the above Implementation into a GUI.

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# import modules

from tkinter import *

from englisttohindi.englisttohindi import EngtoHindi

 

# user define funtion

def eng_to_hindi():

 trans = EngtoHindi(str(e.get()))

 res = trans.convert

 result.set(res) 

 

# object of tkinter

# and background set for grey

master = Tk()

master.configure(bg = 'light grey')

 

# Variable Classes in tkinter

result = StringVar();

 

# Creating label for each information

# name using widget Label 

Label(master, text="Enter Text : " , bg = "light grey").grid(row
= 0, sticky = W)

Label(master, text="Result :", bg = "light grey").grid(row =
3, sticky = W)

 

# Creating lebel for class variable

# name using widget Entry

Label(master, text="", textvariable=result,bg = "light
grey").grid(row = 3,

 column = 1, 

 sticky = W)

 

e = Entry(master, width = 100)

e.grid(row = 0, column = 1)

 

# creating a button using the widget 

# Button that will call the submit function 

b = Button(master, text = "Show", command = eng_to_hindi, bg
= "Blue")

b.grid(row = 0, column = 2, columnspan = 2, rowspan =
2, padx = 5, pady = 5,)

 

mainloop()  
  
---  
  
 __

 __

 **Output:**

![](https://media.geeksforgeeks.org/wp-
content/uploads/20200914135934/Screenshot177.png)  

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

