Python Traceback



In Python, A traceback is a report containing the function calls made in your
code at a specific point i.e when you get an error it is recommended that you
should trace it backward(traceback). Whenever the code gets an exception, the
traceback will give the information about what went wrong in the code.The
Python traceback contains great information that can help you find what is
going wrong in the code. These tracebacks can look a little wearisome, but
once you break it down to see what it’s trying to show you, they can be very
helpful.

Consider following example…

 __

 __  
 __

 __

 __  
 __  
 __

# Python program to demonstrate

# traceback

 

 

mylist = [1, 2, 3]

print(mylist[10])  
  
---  
  
 __

 __

In this example, we are trying to access the 10th element of the list. With
only 3 elements present in the list it will give Runtime error. When this
program is executed you will get the following traceback.

    
    
    Traceback (most recent call last):
      File "", line 2, in 
    print(mylist[10])
    IndexError: list index out of range
    

This traceback error has all the information about why this runtime error
occurred. Last line of the traceback tells you about what type of error
occurred along with relevant information. Previous lines of traceback points
to the code in which error occurred. In the above example, the last line
indicates the index occurred and the previous two lines show the exact
location where the exception has occurred. let us now see, How to read
traceback..

#### How to read traceback

Python traceback contains lots of helpful information about what exception is
raised. Going through a few tracebacks line by line will give you a better
understanding of the information they contain and help you get the most out of
them, in this section we will see how to read a particular exception.

  

  

![Python-traceback](https://media.geeksforgeeks.org/wp-
content/uploads/20191218200140/pt.jpg)

In python it is best to **read traceback from bottom to top**.

  *  **GREEN BOX** shows the what type of error occurred .
  *  **BLUE BOX** shows the relevant information about error
  *  **ORANGE BOX** shows traceback statement for recent calls, below The first **Runtime Error:**  
Traceback (most recent call last):  
File “”, line 1, in  
ModuleNotFoundError: No module named ‘asdf’ line of each call contains
information like the file name, line number, and module name

*  **RED** underlined part shows exact line where exception occurred.

