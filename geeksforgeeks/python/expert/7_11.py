Passing function as an argument in Python



A function can take multiple arguments, these arguments can be objects,
variables(of same or different data types) and functions. Python functions are
first class objects. In the example below, a function is assigned to a
variable. This assignment doesn’t call the function. It takes the function
object referenced by shout and creates a second name pointing to it, yell.

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

 

print(shout('Hello')) 

 

yell = shout 

 

print(yell('Hello'))   
  
---  
  
__

__

**Output:**

    
    
    HELLO
    HELLO
    

## Higher Order Functions

Because functions are objects we can pass them as arguments to other
functions. Functions that can accept other functions as arguments are also
called **higher-order functions**. In the example below, a function greet is
created which takes a function as an argument.

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

 greeting = func("Hi, I am created by a function passed as an
argument.") 

 print(greeting)

 

greet(shout) 

greet(whisper)   
  
---  
  
__

__

**Output**

    
    
    HI, I AM CREATED BY A FUNCTION PASSED AS AN ARGUMENT.
    hi, i am created by a function passed as an argument.
    

## Wrapper function

Wrapper function or decorator allows us to wrap another function in order to
extend the behavior of the wrapped function, without permanently modifying it.
In Decorators, functions are taken as the argument into another function and
then called inside the wrapper function. To know more about decorator click
here.

  

  

Below is the example of a simple decorator.

 __

 __  
 __

 __

 __  
 __  
 __

# defining a decorator

def hello_decorator(func): 

 

 # inner1 is a Wrapper function in 

 # which the argument is called 

 

 # inner function can access the outer local 

 # functions like in this case "func" 

 def inner1(): 

 print("Hello, this is before function execution") 

 

 # calling the actual function now 

 # inside the wrapper function. 

 func() 

 

 print("This is after function execution") 

 

 return inner1 

 

 

# defining a function, to be called inside wrapper 

def function_to_be_used(): 

 print("This is inside the function !!") 

 

 

# passing 'function_to_be_used' inside the 

# decorator to control its behavior 

function_to_be_used = hello_decorator(function_to_be_used) 

 

 

# calling the function 

function_to_be_used()   
  
---  
  
__

__

**Output:**

    
    
    Hello, this is before function execution
    This is inside the function !!
    This is after function execution
    

## Lambda wrapper function

In Python, anonymous function means that a function is without a name. As we
already know that def keyword is used to define the normal functions and the
lambda keyword is used to create anonymous functions. This function can have
any number of arguments but only one expression, which is evaluated and
returned. Lambda function can also have another function as an argument. The
below example shows a basic lambda function where another lambda function is
passed as an argument.

 __

 __  
 __

 __

 __  
 __  
 __

# Defining lambda function

square = lambda x:x * x

 

# Defining lambda function

# and passing function as an argument

cube = lambda func:func**3

 

 

print("square of 2 is :"+str(square(2)))

print("\nThe cube of "+str(square(2))+" is "
+str(cube(square(2))))  
  
---  
  
 __

 __

 **Output:**

    
    
    square of 2 is :4
    
    The cube of 4 is 64
    

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

