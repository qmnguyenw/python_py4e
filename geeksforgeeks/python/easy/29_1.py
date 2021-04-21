Python Docstrings



  
Python documentation strings (or docstrings) provide a convenient way of
associating documentation with Python modules, functions, classes, and
methods.

It’s specified in source code that is used, like a comment, to document a
specific segment of code. Unlike conventional source code comments, the
docstring should describe what the function does, not how.

 **What should a docstring look like?**

  * The doc string line should begin with a capital letter and end with a period.
  * The first line should be a short description.
  * If there are more lines in the documentation string, the second line should be blank, visually separating the summary from the rest of the description.
  * The following lines should be one or more paragraphs describing the object’s calling conventions, its side effects, etc.

 **Declaring Docstrings:** The docstrings are declared using ”’triple single
quotes”’ or “””triple double quotes””” just below the class, method or
function declaration. All functions should have a docstring.

 **Accessing Docstrings:** The docstrings can be accessed using the __doc__
method of the object or using the help function.  
The below examples demonstrates how to declare and access a docstring.

  

  

 **Example 1:** Using triple single quotes

 __

 __  
 __

 __

 __  
 __  
 __

def my_function():

 '''Demonstrates triple double quotes

 docstrings and does nothing really.'''

 

 return None

 

print("Using __doc__:")

print(my_function.__doc__)

 

print("Using help:")

help(my_function)  
  
---  
  
 __

 __

 **Output:**

    
    
    Using __doc__:
    Demonstrates triple double quotes
        docstrings and does nothing really.
    Using help:
    Help on function my_function in module __main__:
    
    my_function()
        Demonstrates triple double quotes
        docstrings and does nothing really.
    

**Example 2:** Using triple double quotes

 __

 __  
 __

 __

 __  
 __  
 __

def my_function():

 """Demonstrates triple double quotes

 docstrings and does nothing really."""

 

 return None

 

print("Using __doc__:")

print(my_function.__doc__)

 

print("Using help:")

help(my_function)  
  
---  
  
 __

 __

 **Output:**

    
    
    Using __doc__:
    Demonstrates triple double quotes
        docstrings and does nothing really.
    Using help:
    Help on function my_function in module __main__:
    
    my_function()
        Demonstrates triple double quotes
        docstrings and does nothing really.
    

**One-line Docstrings**

As the name suggests, one line docstrings fit in one line. They are used in
obvious cases. The closing quotes are on the same line as the opening quotes.
This looks better for one-liners.  
For example:

 __

 __  
 __

 __

 __  
 __  
 __

def power(a, b):

 """Returns arg1 raised to power arg2."""

 

 return a**b

 

print(power.__doc__)  
  
---  
  
 __

 __

 **Output:**

    
    
    Returns arg1 raised to power arg2.
    

**Multi-line Docstrings**

  

  

Multi-line docstrings consist of a summary line just like a one-line
docstring, followed by a blank line, followed by a more elaborate description.
The summary line may be on the same line as the opening quotes or on the next
line.  
The example below shows a multi-line docstring.

 __

 __  
 __

 __

 __  
 __  
 __

def my_function(arg1):

 """

 Summary line.

 

 Extended description of function.

 

 Parameters:

 arg1 (int): Description of arg1

 

 Returns:

 int: Description of return value

 

 """

 

 return arg1

 

print(my_function.__doc__)  
  
---  
  
 __

 __

 **Output:**

    
    
        Summary line.
        Extended description of function.
        Parameters:
        arg1 (int): Description of arg1
    
        Returns:
        int: Description of return value
    
    

**Indentation in Docstrings**

The entire docstring is indented the same as the quotes at its first line.
Docstring processing tools will strip a uniform amount of indentation from the
second and further lines of the docstring, equal to the minimum indentation of
all non-blank lines after the first line. Any indentation in the first line of
the docstring (i.e., up to the first newline) is insignificant and removed.
Relative indentation of later lines in the docstring is retained.

 **Docstrings in Classes**

Let us take an example to show how to write docstrings for a class and its
methods. **help** is used to access the docstring.

 __

 __  
 __

 __

 __  
 __  
 __

class ComplexNumber:

 """

 This is a class for mathematical operations on complex numbers.

 

 Attributes:

 real (int): The real part of complex number.

 imag (int): The imaginary part of complex number.

 """

 

 def __init__(self, real, imag):

 """

 The constructor for ComplexNumber class.

 

 Parameters:

 real (int): The real part of complex number.

 imag (int): The imaginary part of complex number. 

 """

 

 def add(self, num):

 """

 The function to add two Complex Numbers.

 

 Parameters:

 num (ComplexNumber): The complex number to be added.

 

 Returns:

 ComplexNumber: A complex number which contains the sum.

 """

 

 re = self.real + num.real

 im = self.imag + num.imag

 

 return ComplexNumber(re, im)

 

help(ComplexNumber) # to access Class docstring

help(ComplexNumber.add) # to access method's docstring  
  
---  
  
 __

 __

Output:

    
    
    Help on class ComplexNumber in module __main__:
    
    class ComplexNumber
     |  This is a class for mathematical operations on complex numbers.
     |  
     |  Attributes:
     |          real (int): The real part of complex number.
     |          imag (int): The imaginary part of complex number.
     |  
     |  Methods defined here:
     |  
     |  __init__(self, real, imag)
     |      The constructor for ComplexNumber class.
     |      
     |      Parameters:
     |      real (int): The real part of complex number.
     |      imag (int): The imaginary part of complex number.
     |  
     |  add(self, num)
     |      The function to add two Complex Numbers.
     |      
     |      Parameters:
     |              num (ComplexNumber): The complex number to be added.
     |      
     |      Returns:
     |              ComplexNumber: A complex number which contains the sum.
    
    Help on method add in module __main__:
    
    add(self, num) unbound __main__.ComplexNumber method
        The function to add two Complex Numbers.
        
        Parameters:
                num (ComplexNumber): The complex number to be added.
        
        Returns:
                ComplexNumber: A complex number which contains the sum.
    
    

**The difference between Python comments and docstrings**

You all must have got an idea about Python docstrings but have you ever
wondered what is the difference between Python comments and docstrings. Let’s
have a look at them.

Python Comments are the useful information that the developers provide to make
the reader understand the source code. It explains the logic or a part of it
used in the code. It is written by using # symbol.

 **Example:**

 __

 __  
 __

 __

 __  
 __  
 __

# Python program to demonstrate comments

print("GFG")  
  
---  
  
 __

 __

 **Output:**

    
    
    GFG

Whereas Python Docstrings as mentioned above provides a convenient way of
associating documentation with Python modules, functions, classes, and
methods.

This article is contributed by **Mayank Agrawal**. If you like GeeksforGeeks
and would like to contribute, you can also write an article using
contribute.geeksforgeeks.org or mail your article to
contribute@geeksforgeeks.org. See your article appearing on the GeeksforGeeks
main page and help other Geeks.

Please write comments if you find anything incorrect, or you want to share
more information about the topic discussed above.

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

