Function Decorators in Python | Set 1 (Introduction)



 **Background**  
Following are important facts about functions in Python that are useful to
understand decorator functions.

  1. In Python, we can define a function inside another function.
  2. In Python, a function can be passed as parameter to another function (a function can also return another function).

 __

 __  
 __

 __

 __  
 __  
 __

# A Python program to demonstrate that a function

# can be defined inside another function and a

# function can be passed as parameter.

 

# Adds a welcome message to the string

def messageWithWelcome(str):

 

 # Nested function

 def addWelcome():

 return "Welcome to "

 

 # Return concatenation of addWelcome()

 # and str.

 return addWelcome() + str

 

# To get site name to which welcome is added

def site(site_name):

 return site_name

 

print messageWithWelcome(site("GeeksforGeeks"))  
  
---  
  
 __

 __

Output:

    
    
    Welcome to GeeksforGeeks

 **Function Decorator**  
A decorator is a function that takes a function as its only parameter and
returns a function. This is helpful to “wrap” functionality with the same code
over and over again. For example, above code can be re-written as following.

We use @func_name to specify a decorator to be applied on another function.

 __

 __  
 __

 __

 __  
 __  
 __

# Adds a welcome message to the string

# returned by fun(). Takes fun() as

# parameter and returns welcome().

def decorate_message(fun):

 

 # Nested function

 def addWelcome(site_name):

 return "Welcome to " + fun(site_name)

 

 # Decorator returns a function

 return addWelcome

 

@decorate_message

def site(site_name):

 return site_name;

 

# Driver code

 

# This call is equivalent to call to

# decorate_message() with function

# site("GeeksforGeeks") as parameter

print site("GeeksforGeeks")  
  
---  
  
 __

 __

Output:

  

  

    
    
    Welcome to GeeksforGeeks

Decorators can also be useful to attach data (or add attribute) to functions.

 __

 __  
 __

 __

 __  
 __  
 __

# A Python example to demonstrate that

# decorators can be useful attach data

 

# A decorator function to attach

# data to func

def attach_data(func):

 func.data = 3

 return func

 

@attach_data

def add (x, y):

 return x + y

 

# Driver code

 

# This call is equivalent to attach_data()

# with add() as parameter

print(add(2, 3))

 

print(add.data)  
  
---  
  
 __

 __

Output:

    
    
    5
    3

‘add()’ returns sum of x and y passed as arguments but it is wrapped by a
decorator function, calling add(2, 3) would simply give sum of two numbers but
when we call add.data then ‘add’ function is passed into then decorator
function ‘attach_data’ as argument and this function returns ‘add’ function
with an attribute ‘data’ that is set to 3 and hence prints it.

Python decorators are a powerful tool to remove redundancy.

Please refer Decorators in Python for more details.

This article is contributed by **Shwetanshu Rohatgi**. Please write comments
if you find anything incorrect, or you want to share more information about
the topic discussed above

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

