Create Table Using Tkinter



Python offers multiple options for developing a GUI (Graphical User
Interface). Out of all the GUI methods, **Tkinter** is the most commonly used
method. It is a standard Python interface to the Tk GUI toolkit shipped with
Python. Python with Tkinter is the fastest and easiest way to create GUI
applications. Creating a GUI using Tkinter is an easy task.

 **Note:** For more information, refer to Python GUI – tkinter

## Creating Tables Using Tkinter

A table is useful to display data in the form of rows and columns.
Unfortunately, Tkinter does not provide a Table widget to create a table. But
we can create a table using alternate methods. For example, we can make a
table by repeatedly displaying entry widgets in the form of rows and columns.

To create a table with five rows and four columns we can use two for loops as:

    
    
    for i in range(5):
        for j in range(4):
    

Inside these loops, we have to create an Entry widget by creating an object of
Entry class, as:

  

  

    
    
    e = Entry(root, width=20, fg='blue', font=('Arial', 16, 'bold')
    

Now, we need logic to place this Entry widget in rows and columns. This can be
done by using grid() method to which we can pass row and column positions,
as:

    
    
    # here i and j indicate 
    # row and column positions
    e.grid(row=i, column=j)
    

We can insert data into the Entry widget using insert() method, as:

    
    
    e.insert(END, data)
    

Here, ‘END’ indicates that the data continuous to append at the end of
previous data in the Entry widget.

This is the logic that is used in the program given below using the data that
is coming from a list. We have taken a list containing 5 tuples and each tuple
contains four values which indicate student id, name, city and age.

Hence, we will have a table with 5 rows and 4 columns in each row. This
program can also be applied on data coming from a database to display the
entire data in the form of a table.

 **Source Code:**

 __

 __  
 __

 __

 __  
 __  
 __

# Python program to create a table

 

from tkinter import *

 

 

class Table:

 

 def __init__(self,root):

 

 # code for creating table

 for i in range(total_rows):

 for j in range(total_columns):

 

 self.e = Entry(root, width=20, fg='blue',

 font=('Arial',16,'bold'))

 

 self.e.grid(row=i, column=j)

 self.e.insert(END, lst[i][j])

 

# take the data

lst = [(1,'Raj','Mumbai',19),

 (2,'Aaryan','Pune',18),

 (3,'Vaishnavi','Mumbai',20),

 (4,'Rachna','Mumbai',21),

 (5,'Shubham','Delhi',21)]

 

# find total number of rows and

# columns in list

total_rows = len(lst)

total_columns = len(lst[0])

 

# create root window

root = Tk()

t = Table(root)

root.mainloop()  
  
---  
  
 __

 __

 **Output:**  
![python-table-using-tkinter](https://media.geeksforgeeks.org/wp-
content/uploads/20200403181253/table36.png)

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

