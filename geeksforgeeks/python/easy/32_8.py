Packing and Unpacking Arguments in Python



We use two operators * (for tuples) and ** (for dictionaries).  

**Background**  
Consider a situation where we have a function that receives four arguments. We
want to make a call to this function and we have a list of size 4 with us that
has all arguments for the function. If we simply pass a list to the function,
the call doesn’t work.  

## Python

 __

 __  
 __

 __

 __  
 __  
 __

# A Python program to demonstrate need

# of packing and unpacking

# A sample function that takes 4 arguments

# and prints them.

def fun(a, b, c, d):

 print(a, b, c, d)

# Driver Code

my_list = [1, 2, 3, 4]

# This doesn't work

fun(my_list)  
  
---  
  
 __

 __

 **Output :**

    
    
    TypeError: fun() takes exactly 4 arguments (1 given)

  
**Unpacking**  
We can use ***** to unpack the list so that all elements of it can be passed
as different parameters.  

## Python

 __

 __  
 __

 __

 __  
 __  
 __

# A sample function that takes 4 arguments

# and prints the,

def fun(a, b, c, d):

 print(a, b, c, d)

# Driver Code

my_list = [1, 2, 3, 4]

# Unpacking list into four arguments

fun(*my_list)  
  
---  
  
 __

 __

 **Output :**

  

  

    
    
    (1, 2, 3, 4)

We need to keep in mind that the no. of arguments must be the same as the
length of the list that we are unpacking for the arguments.

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# Error when len(args) != no of actual arguments

# required by the funcntion

args = [0, 1, 4, 9]

def func(a, b, c):

 return a + b + c

# calling function with unpacking args

func(*args)  
  
---  
  
 __

 __

 **Output:**

    
    
    Traceback (most recent call last):
      File "/home/592a8d2a568a0c12061950aa99d6dec3.py", line 10, in <module>
        func(*args)
    TypeError: func() takes 3 positional arguments but 4 were given

As another example, consider the built-in range() function that expects
separate start and stops arguments. If they are not available separately,
write the function call with the *-operator to unpack the arguments out of a
list or tuple:

## Python

 __

 __  
 __

 __

 __  
 __  
 __

>>>

>>> range(3, 6) # normal call with separate arguments

[3, 4, 5]

>>> args = [3, 6]

>>> range(*args) # call with arguments unpacked from a list

[3, 4, 5]  
  
---  
  
 __

 __

 **Packing**  
When we don’t know how many arguments need to be passed to a python function,
we can use Packing to pack all arguments in a tuple.  

## Python

 __

 __  
 __

 __

 __  
 __  
 __

# A Python program to demonstrate use

# of packing

# This function uses packing to sum

# unknown number of arguments

def mySum(*args):

 return sum(args)

# Driver code

print(mySum(1, 2, 3, 4, 5))

print(mySum(10, 20))  
  
---  
  
 __

 __

 **Output:**  

    
    
    15
    30

The above function mySum() does ‘packing’ to pack all the arguments that this
method call receives into one single variable. Once we have this ‘packed’
variable, we can do things with it that we would with a normal tuple. args[0]
and args[1] would give you the first and second argument, respectively. Since
our tuples are immutable, you can convert the args tuple to a list so you can
also modify, delete, and re-arrange items in i.  

**Packing and Unpacking**  
Below is an example that shows both packing and unpacking.  

## Python

 __

 __  
 __

 __

 __  
 __  
 __

# A Python program to demonstrate both packing and

# unpacking.

# A sample python function that takes three arguments

# and prints them

def fun1(a, b, c):

 print(a, b, c)

# Another sample function.

# This is an example of PACKING. All arguments passed

# to fun2 are packed into tuple *args.

def fun2(*args):

 # Convert args tuple to a list so we can modify it

 args = list(args)

 # Modifying args

 args[0] = 'Geeksforgeeks'

 args[1] = 'awesome'

 # UNPACKING args and calling fun1()

 fun1(*args)

# Driver code

fun2('Hello', 'beautiful', 'world!')  
  
---  
  
 __

 __

 **Output:**  

  

  

    
    
    (Geeksforgeeks, awesome, world!)

 **** is used for dictionaries**  

## Python

 __

 __  
 __

 __

 __  
 __  
 __

# A sample program to demonstrate unpacking of

# dictionary items using **

def fun(a, b, c):

 print(a, b, c)

# A call with unpacking of dictionary

d = {'a':2, 'b':4, 'c':10}

fun(**d)  
  
---  
  
 __

 __

 **Output:**  

    
    
    2 4 10

Here ** unpacked the dictionary used with it, and passed the items in the
dictionary as keyword arguments to the function. So writing “fun(1, **d)” was
equivalent to writing “fun(1, b=4, c=10)”.  

## Python

 __

 __  
 __

 __

 __  
 __  
 __

# A Python program to demonstrate packing of

# dictionary items using **

def fun(**kwargs):

 # kwargs is a dict

 print(type(kwargs))

 # Printing dictionary items

 for key in kwargs:

 print("%s = %s" % (key, kwargs[key]))

# Driver code

fun(name="geeks", ID="101", language="Python")  
  
---  
  
 __

 __

 **Output :**  

    
    
    <class 'dict'>
    language = Python
    name = geeks
    ID = 101

Applications and Important Points

  1. Used in socket programming to send a vast number of requests to a server. 
  2. Used in the Django framework to send variable arguments to view functions. 
  3. There are wrapper functions that require us to pass in variable arguments.
  4. Modification of arguments becomes easy, but at the same time validation is not proper, so they must be used with care. 

**Reference :**  
http://hangar.runway7.net/python/packing-unpacking-arguments  
This article is contributed by **Shwetanshu Rohatgi**. If you like
GeeksforGeeks and would like to contribute, you can also write an article
using contribute.geeksforgeeks.org or mail your article to
contribute@geeksforgeeks.org. See your article appearing on the GeeksforGeeks
main page and help other Geeks.  
Please write comments if you find anything incorrect, or you want to share
more information about the topic discussed above  

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

