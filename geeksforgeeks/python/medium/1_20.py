Multiplication Table Generator using Python



 **Prerequisites:** **Python GUI- Tkinter**

We all know that Tkinter is the standard GUI library for Python. Python when
combined with Tkinter provides a fast and easy way to create GUI applications.
In this article, we will learn How to create a Times-table using Tkinter.

 **Approach:**

  * Import Tkinter Library
  * Create Function of Multiplication Table
  * Create the main window (container)
  * Create Variabletext field that store value of Number
  * Call the function By Generate Table Button
  * Execute code

 **Program:**

## Python

  

  

 __

 __  
 __

 __

 __  
 __  
 __

#import library

import sys

from tkinter import *

 

 

def MultiTable():

 

 print("\n:Multiplication Table:\n")

 print("\nTimes-Table of Number", (EnterTable.get()), '\n')

 

 for x in range(1, 13):

 number = int(EnterTable.get())

 print('\t\t', (number), 'x', (x), '=', (x*number),)

 

 

# Create Main window

Table = Tk()

Table.geometry('250x250+700+200')

Table.title('Multiplication Table')

 

# Variable Declaration

EnterTable = StringVar()

 

label1 = Label(Table, text='Enter Your Times-table Number:',

 font=30, fg='Black').grid(row=1, column=6)

label1 = Label(Table, text=' ').grid(row=2, column=6)

 

# Store Number in Textvariable

entry = Entry(Table, textvariable=EnterTable,

 justify='center').grid(row=3, column=6)

label1 = Label(Table, text=' ').grid(row=4, column=6)

 

# Call the function

button1 = Button(Table, text="Generate Table", fg="Blue",

 command=MultiTable).grid(row=5, column=6)

label1 = Label(Table, text=' ').grid(row=6, column=6)

 

# Exit

EXIT = Button(Table, text="Quit", fg="red",

 command=Table.destroy).grid(row=7, column=6)

 

Table.mainloop()  
  
---  
  
 __

 __

