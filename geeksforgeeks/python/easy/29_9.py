First Class functions in Python



  
 **First class** objects in a language are handled uniformly throughout. They
may be stored in data structures, passed as arguments, or used in control
structures. A programming language is said to support first-class functions if
it treats functions as first-class objects. Python supports the concept of
First Class functions.

 **Properties of first class functions:**

  * A function is an instance of the Object type.
  * You can store the function in a variable.
  * You can pass the function as a parameter to another function.
  * You can return the function from a function.
  * You can store them in data structures such as hash tables, lists, …

 **Examples illustrating First Class functions in Python**

 **1\. Functions are objects:** Python functions are first class objects. In
the example below, we are assigning function to a variable. This assignment
doesn’t call the function. It takes the function object referenced by shout
and creates a second name pointing to it, yell.

 __

 __  
 __

 __

 __  
 __  
 __

# Python program to illustrate functions

# can be treated as objects

def shout(text):

 return text.upper()

 

print (shout('Hello'))

 

yell = shout

 

print (yell('Hello'))  
  
---  
  
 __

 __

 **Output:**

  

  

    
    
    HELLO
    HELLO
    

**2\. Functions can be passed as arguments to other functions:** Because
functions are objects we can pass them as arguments to other functions.
Functions that can accept other functions as arguments are also called higher-
order functions. In the example below, we have created a function **greet**
which takes a function as an argument.

 __

 __  
 __

 __

 __  
 __  
 __

# Python program to illustrate functions

# can be passed as arguments to other functions

def shout(text):

 return text.upper()

 

def whisper(text):

 return text.lower()

 

def greet(func):

 # storing the function in a variable

 greeting = func("""Hi, I am created by a function

 passed as an argument.""")

 print (greeting) 

 

greet(shout)

greet(whisper)  
  
---  
  
 __

 __

 **Output**

    
    
    HI, I AM CREATED BY A FUNCTION PASSED AS AN ARGUMENT.
    hi, i am created by a function passed as an argument.
    

**3\. Functions can return another function:** Because functions are objects
we can return a function from another function. In the below example, the
create_adder function returns adder function.

 __

 __  
 __

 __

 __  
 __  
 __

# Python program to illustrate functions

# Functions can return another function

 

def create_adder(x):

 def adder(y):

 return x+y

 

 return adder

 

add_15 = create_adder(15)

 

print (add_15(10))  
  
---  
  
 __

 __

 **Output:**

    
    
    25
    

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

