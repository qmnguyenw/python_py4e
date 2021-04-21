Important differences between Python 2.x and Python 3.x with examples



 **Division operator**

If we are porting our code or executing python 3.x code in python 2.x, it can
be dangerous if integer division changes go unnoticed (since it doesn’t raise
any error). It is preferred to use the floating value (like 7.0/5 or 7/5.0) to
get the expected result when porting our code.  

## Python

 __

 __  
 __

 __

 __  
 __  
 __

print 7 / 5

print -7 / 5

 

'''

Output in Python 2.x

1

-2

Output in Python 3.x :

1.4

-1.4

 

# Refer below link for details

# https://www.geeksforgeeks.org/division-operator-in-python/

'''  
  
---  
  
 __

 __

 **print function**

This is the most well-known change. In this, the **print** keyword in Python
2.x is replaced by the **print()** function in Python 3.x. However,
parentheses work in Python 2 if space is added after the **print** keyword
because the interpreter evaluates it as an expression.  

## Python

 __

 __  
 __

 __

 __  
 __  
 __

print 'Hello, Geeks' # Python 3.x doesn't support

print('Hope You like these facts')

 

'''

Output in Python 2.x :

Hello, Geeks

Hope You like these facts

 

Output in Python 3.x :

File "a.py", line 1

 print 'Hello, Geeks'

 ^

SyntaxError: invalid syntax

 

Refer below link for details

https://www.geeksforgeeks.org/g-fact-25-print-single-multiple-variable-
python/

'''  
  
---  
  
 __

 __

As we can see, if we use parentheses in python 2.x then there is no issue but
if we don’t use parentheses in python 3.x, we get SyntaxError.  

  

  

**Unicode:**

In Python 2, an implicit str type is ASCII. But in Python 3.x implicit str
type is Unicode.  

## Python

 __

 __  
 __

 __

 __  
 __  
 __

print(type('default string '))

print(type(b'string with b '))

 

'''

Output in Python 2.x (Bytes is same as str)

<type 'str'>

<type 'str'>

 

Output in Python 3.x (Bytes and str are different)

<class 'str'>

<class 'bytes'>

'''  
  
---  
  
 __

 __

Python 2.x also supports Unicode  

## Python

 __

 __  
 __

 __

 __  
 __  
 __

print(type('default string '))

print(type(u'string with b '))

 

'''

Output in Python 2.x (Unicode and str are different)

<type 'str'>

<type 'unicode'>

 

Output in Python 3.x (Unicode and str are same)

<class 'str'>

<class 'str'>

'''  
  
---  
  
 __

 __

 **xrange:**

xrange() of Python 2.x doesn’t exist in Python 3.x. In Python 2.x, range
returns a list i.e. range(3) returns [0, 1, 2] while xrange returns a xrange
object i. e., xrange(3) returns iterator object which works similar to Java
iterator and generates number when needed.  
If we need to iterate over the same sequence multiple times, we prefer range()
as range provides a static list. xrange() reconstructs the sequence every
time. xrange() doesn’t support slices and other list methods. The advantage of
xrange() is, it saves memory when the task is to iterate over a large range.  
In Python 3.x, the range function now does what xrange does in Python 2.x, so
to keep our code portable, we might want to stick to using a range instead. So
Python 3.x’s range function _is_ xrange from Python 2.x.  

## Python

 __

 __  
 __

 __

 __  
 __  
 __

for x in xrange(1, 5):

 print(x),

 

for x in range(1, 5):

 print(x),

 

'''

Output in Python 2.x

1 2 3 4 1 2 3 4

 

Output in Python 3.x

NameError: name 'xrange' is not defined

'''  
  
---  
  
 __

 __

 **Error Handling:**

There is a small change in error handling in both versions. In python 3.x,
‘as’ keyword is required.  

## Python

 __

 __  
 __

 __

 __  
 __  
 __

try:

 trying_to_check_error

except NameError, err:

 print err, 'Error Caused' # Would not work in Python 3.x

 

'''

Output in Python 2.x:

name 'trying_to_check_error' is not defined Error Caused

 

Output in Python 3.x :

File "a.py", line 3

 except NameError, err:

 ^

SyntaxError: invalid syntax

'''  
  
---  
  
 __

 __

## Python

 __

 __  
 __

 __

 __  
 __  
 __

try:

 trying_to_check_error

except NameError as err: # 'as' is needed in Python 3.x

 print (err, 'Error Caused')

 

'''

Output in Python 2.x:

(NameError("name 'trying_to_check_error' is not defined",), 'Error Caused')

 

Output in Python 3.x :

name 'trying_to_check_error' is not defined Error Caused

'''  
  
---  
  
 __

 __

 **__future__ module:**

  

  

This is basically not a difference between the two versions, but a useful
thing to mention here. The idea of the __future__ module is to help migrate to
Python 3.x.  
If we are planning to have Python 3.x support in our 2.x code, we can use
**_future_** imports in our code.  
For example, in the Python 2.x code below, we use Python 3.x’s integer
division behavior using the __future__ module.  

## Python

 __

 __  
 __

 __

 __  
 __  
 __

# In below python 2.x code, division works

# same as Python 3.x because we use __future__

from __future__ import division

 

print 7 / 5

print -7 / 5  
  
---  
  
 __

 __

Output :  

    
    
    1.4 
    
    -1.4 

Another example where we use brackets in Python 2.x using __future__ module:  

## Python

 __

 __  
 __

 __

 __  
 __  
 __

from __future__ import print_function 

 

print('GeeksforGeeks')  
  
---  
  
 __

 __

Output:  

    
    
    GeeksforGeeks 

Refer to this for more details of the __future__ module.  

This article is contributed by **Arpit Agarwal**. If you like GeeksforGeeks
and would like to contribute, you can also write an article and mail your
article to contribute@geeksforgeeks.org. See your article appearing on the
GeeksforGeeks main page and help other Geeks.

Please write comments if you find anything incorrect, or you want to share
more information about the topic discussed above.  

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

