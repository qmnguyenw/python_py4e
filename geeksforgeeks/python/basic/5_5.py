How to write Comments in Python3?



Comments are text notes added to the program to provide explanatory
information about the source code. They are used in a programming language to
document the program and remind programmers of what tricky things they just
did with the code and also helps the later generation for understanding and
maintenance of code. The compiler considers these as non-executable
statements. Since comments do not execute, when you run a program you will not
see any indication of the comment in the output.

 **Syntax :**  
The hash(#) symbol denotes the staring of a comment in Python.

    
    
    # This is a comment in Python

 **Example :**

 __

 __  
 __

 __

 __  
 __  
 __

# This is the syntax of a comment in Python

print("GFG")

 

# Comments dont have any effect on the interpreter / output  
  
---  
  
 __

 __

 **Output :**

    
    
    GFG

Comments should be made at the same indent as the code it is commenting on.

  

  

 __

 __  
 __

 __

 __  
 __  
 __

# This comment has no indent

def GFG():

 

 # Since, this comment is inside a function

 # It would have indent same as the function body

 print("GeeksforGeeks")

 

 for i in range(1, 2):

 

 # Be careful of indentation

 # This comment is inside the body of for loop

 print("Welcome to Comments in Python")

 

# This comment is again outside the body

# of function so it wont have any indent.

 

print("Hello !!")

GFG()  
  
---  
  
 __

 __

 **Output**

    
    
    Hello!!
    GeeksforGeeks
    Welcome to Comments in Python
    

#### Types of Comments :

 **1\. Single-Line Comments** : Comments starting with a ‘#’ and whitespace
are called single-line comments in Python. These comments can only stretch to
a single line and are the only way for comments in Python. e.g.

    
    
    # This a single line comment.

 **2\. Multi-line (Block) comments** : Unlike other programming languages
Python doesn’t support multi-line comment blocks out of the box. HOwever we
can use consecutive # single-line comments to comment out multiple lines of
code. Some examples of block comments-

    
    
    # This type of comments can serve
    # both as a single-line as well
    # as multi-line (block) in Python.

 **3\. Inline Style comments** : Inline comments occur on the same line of a
statement, following the code itself. Generally, inline comments look like
this:

    
    
    x = 3        # This is called an inline comment
    
    a = b + c    # Adding value of 'b' and 'c' to 'a'

 **4\. Docstring comments:** Python documentation strings (or docstrings)
provide a convenient way of associating documentation with Python modules,
functions, classes, and methods. It’s specified in source code that is used,
like a comment, to document a specific segment of code. Unlike conventional
source code comments, the docstring should describe what the function does,
not how.

 **Example :**

 __

 __  
 __

 __

 __  
 __  
 __

def my_function(): 

 """Demonstrates docstrings and does nothing really."""

 

 return None

 

print("Using __doc__:")

print(my_function.__doc__) 

 

print("Using help:")

help(my_function)  
  
---  
  
 __

 __

 **Output :**

    
    
    Using __doc__:
    Demonstrates docstrings and does nothing really.
    Using help:
    Help on function my_function in module __main__:
    
    my_function()
        Demonstrates docstrings and does nothing really.
    

#### Advantages and Uses of Comments :

  *  **Planning and reviewing :** In comments, we can write the pseudocode which we planned before writing the source code. Pseudocode is a mixture of natural language and high-level programming language. This helps in reviewing the source code more easily because pseudocode is more understandable than the program.

 __

 __  
 __

 __

 __  
 __  
 __

# This function is adding two given numbers

def addition(a, b):

 

 # storing the sum of given numbers in 'c'.

 c = a + b

 

 # returning the sum here

 return c

 

# passing the value of a and b to addition()

a = 10

b = 3

sum = addition(a, b)

 

# printing the sum calculated by above function

print(sum)  
  
---  
  
 __

 __

 **Output :**

    
    
    13
    

  * **Debugging** : Brute force method is a common method of debugging. In this approach, print statements are inserted throughout the program to print the intermediate values with the hope that some of the printed values will help to identify the errors. After doing debugging we comment those print statements. Hence comment is also used for debugging.

 __

 __  
 __

 __

 __  
 __  
 __

a= 12

 

if(a == 12):

 print("True")

 

# elif(a == 0):

 # print("False")

 

else:

 print("Debugging")  
  
---  
  
 __

 __

 **Output :**

    
    
    True
    

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

