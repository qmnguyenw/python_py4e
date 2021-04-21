Python | Method Overloading



Like other languages (for example, method overloading in C++) do, python does
not support method overloading by default. But there are different ways to
achieve method overloading in Python.

The problem with method overloading in Python is that we may overload the
methods but can only use the latest defined method.

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# First product method.

# Takes two argument and print their

# product

def product(a, b):

 p = a * b

 print(p)

 

# Second product method

# Takes three argument and print their

# product

def product(a, b, c):

 p = a * b*c

 print(p)

 

# Uncommenting the below line shows an error 

# product(4, 5)

 

# This line will call the second product method

product(4, 5, 5)  
  
---  
  
 __

 __

 **Output:**

    
    
    100

In the above code, we have defined two product method, but we can only use the
second product method, as python does not support method overloading. We may
define many methods of the same name and different arguments, but we can only
use the latest defined method. Calling the other method will produce an error.
Like here calling ![product\(4, 5\)    ](https://www.geeksforgeeks.org/wp-
content/ql-cache/quicklatex.com-010ba8a74afef814fc7b243d95182b89_l3.png)will
produce an error as the latest defined product method takes three arguments.

Thus, to overcome the above problem we can use different ways to achieve the
method overloading.

  

  

 **Method 1 (Not The Most Efficient Method):**  
We can use the arguments to make the same function work differently i.e. as
per the arguments.

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# Function to take multiple arguments

def add(datatype, *args):

 

 # if datatype is int

 # initialize answer as 0

 if datatype =='int':

 answer = 0

 

 # if datatype is str

 # initialize answer as ''

 if datatype =='str':

 answer =''

 

 # Traverse through the arguments

 for x in args:

 

 # This will do addition if the 

 # arguments are int. Or concatenation 

 # if the arguments are str

 answer = answer + x

 

 print(answer)

 

# Integer

add('int', 5, 6)

 

# String

add('str', 'Hi ', 'Geeks')  
  
---  
  
 __

 __

 **Output:**

    
    
    11
    Hi Geeks

The problem with above code is that makes code more complex with multiple
if/else statement and is not the desired way to achieve the method
overloading.

 **Method 2 (Efficient One):**  
By Using Multiple Dispatch Decorator  
Multiple Dispatch Decorator Can be installed by:

    
    
    pip3 install multipledispatch

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

from multipledispatch import dispatch

 

#passing one parameter

@dispatch(int,int)

def product(first,second):

 result = first*second

 print(result);

 

#passing two parameters

@dispatch(int,int,int)

def product(first,second,third):

 result = first * second * third

 print(result);

 

#you can also pass data type of any value as per requirement

@dispatch(float,float,float)

def product(first,second,third):

 result = first * second * third

 print(result);

 

 

#calling product method with 2 arguments

product(2,3,2) #this will give output of 12

product(2.2,3.4,2.3) # this will give output of
17.985999999999997  
  
---  
  
 __

 __

 **Output:**

    
    
    12
    17.985999999999997

In Backend, Dispatcher creates an object which stores different implementation
and on runtime, it selects the appropriate method as the type and number of
parameters passed.  

  

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

