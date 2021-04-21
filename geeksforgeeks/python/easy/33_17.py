Class or Static Variables in Python



All objects share class or static variables. An instance or non-static
variables are different for different objects (every object has a copy). For
example, let a Computer Science Student be represented by class **CSStudent**.
The class may have a static variable whose value is “cse” for all objects. And
class may also have non-static members like **name** and **roll**. In C++ and
Java, we can use static keywords to make a variable a class variable. The
variables which don’t have a preceding static keyword are instance variables.
See this for Java example and this for C++ example.  
The **Python** approach is simple; it doesn’t require a static keyword.

> _All variables which are assigned a value in_ the _class declaration are
> class variables. And variables_ that _are assigned values inside methods are
> instance variables._  
>

## Python

 __

 __  
 __

 __

 __  
 __  
 __

# Python program to show that the variables with a value

# assigned in class declaration, are class variables

 

# Class for Computer Science Student

class CSStudent:

 stream = 'cse' # Class Variable

 def __init__(self,name,roll):

 self.name = name # Instance Variable

 self.roll = roll # Instance Variable

 

# Objects of CSStudent class

a = CSStudent('Geek', 1)

b = CSStudent('Nerd', 2)

 

print(a.stream) # prints "cse"

print(b.stream) # prints "cse"

print(a.name) # prints "Geek"

print(b.name) # prints "Nerd"

print(a.roll) # prints "1"

print(b.roll) # prints "2"

 

# Class variables can be accessed using class

# name also

print(CSStudent.stream) # prints "cse"

 

# Now if we change the stream for just a it won't be changed for b

a.stream = 'ece'

print(a.stream) # prints 'ece'

print(b.stream) # prints 'cse'

 

# To change the stream for all instances of the class we can change it 

# directly from the class

CSStudent.stream = 'mech'

 

print(a.stream) # prints 'mech'

print(b.stream) # prints 'mech'  
  
---  
  
 __

 __

 **Output:**

    
    
    cse
    cse
    Geek
    Nerd
    1
    2
    cse
    ece
    cse
    ece
    mech

This article is contributed by **Harshit Gupta**. If you like GeeksforGeeks
and would like to contribute, you can also write an article and mail your
article to contribute@geeksforgeeks.org. See your article appearing on the
GeeksforGeeks main page and help other Geeks.

  

  

Please write comments if you find anything incorrect, or you want to share
more information about the topic discussed above

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

