Multiline comments in Python



Python developers often make use of the comment system as, without the use of
it, things can get real confusing, real fast. Comments are useful information
that the developers provide to make the reader understand the source code. It
explains the logic or a part of it used in the code. Comments are usually
helpful to someone maintaining or enhancing your code when you are no longer
around to answer questions about it. These are often cited as a useful
programming convention that does not take part in the output of the program
but improves the readability of the whole program.

However, there is no concept of multiline comments in Python. But it can be
achieved by the following ways.

 **Ways to achieve multiline comments in Python**

  * Consecutive Single line comment
  * Using Multi-line string as comment

#### Consecutive Single line comment

Hash character(#) is used to comment the line in the python program. Comments
does not have to be text to explain the code, it can also be used to prevent
Python from executing code. The hash character should be placed before the
line to be commented. Consecutive single line comments can be used as
multiline comments in Python.

 **Example:**

  

  

 __

 __  
 __

 __

 __  
 __  
 __

# Write Python3 code here

# Single line comment used

 

print("Python Comments")

 

# print("Mathematics")  
  
---  
  
 __

 __

 **Input and Output**

![](https://media.geeksforgeeks.org/wp-
content/uploads/20191212222340/Screenshot-1553-300x164.png)

Here, the first two lines contain hash character(#) and the interpreter
prevents the two lines from execution. Then it prints the “Python Comments”
and finally, it will prevent the last line from execution.

#### Using Multi-line string as comment

Python multi-line comment is a piece of text enclosed in a delimiter (""")
on each end of the comment. Again there should be no white space between
delimiter ("""). They are useful when the comment text does not fit into one
line; therefore needs to span across lines. Multi-line comments or paragraphs
serve as documentation for others reading your code. See the following code
snippet demonstrating multi-line comment:

 **Example:**

 __

 __  
 __

 __

 __  
 __  
 __

# Write Python code here

 

""" Multi-line comment used

print("Python Comments") """

 

print("Mathematics")  
  
---  
  
 __

 __

 **Input and Output**  
![](https://media.geeksforgeeks.org/wp-
content/uploads/20191212222448/Screenshot-1564-300x139.png)

In the above example, the multi-line comments are used to comment more than
one line. The first line is a single line comment. The second and third line
can be commented using triple quotes(""" """"). This prevents the execution
of the above code. Finally, it prints “Mathematics” in the output.

However, if these multiline comments are placed directly after a function or
class signature, then these turn into **docstrings**. Docstring is an in-built
feature of Python, which is used to associate documentation that has been
written with Python modules, functions, classes and methods. It is added right
below the functions, modules or classes to describe what they do. In Python,
the docstring is then made available via the __doc__ attribute.

 **Example:**

 __

 __  
 __

 __

 __  
 __  
 __

def multiply(a, b):

 """Multiplies the value of a and b"""

 return a*b

 

 

# Print the docstring of multiply function

print(multiply.__doc__)  
  
---  
  
 __

 __

 **Output:**

    
    
    Multiplies the value of a and b
    

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

