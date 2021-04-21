Unpacking a Tuple in Python



 **Python Tuples** In python tuples are used to store immutable objects.
Python Tuples are very similar to lists except to some situations. Python
tuples are immutable means that they can not be modified in whole program.

 **Packing and Unpacking a Tuple:** In Python, there is a very powerful tuple
assignment feature that assigns the right-hand side of values into the left-
hand side. In another way, it is called unpacking of a tuple of values into a
variable. In packing, we put values into a new tuple while in unpacking we
extract those values into a single variable.

 **Example 1**

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# Program to understand about

# packing and unpacking in Python

# this lines PACKS values

# into variable a

a = ("MNNIT Allahabad", 5000, "Engineering") 

# this lines UNPACKS values

# of variable a

(college, student, type_ofcollege) = a 

# print college name

print(college)

# print no of student

print(student)

# print type of college

print(type_ofcollege)  
  
---  
  
 __

 __

 **Output:**

    
    
    MNNIT Allahabad
    5000
    Engineering

**NOTE :** In unpacking of tuple number of variables on left-hand side should
be equal to number of values in given tuple a.  
Python uses a special syntax to pass optional arguments (*args) for tuple
unpacking. This means that there can be many number of arguments in place of
(*args) in python. All values will be assigned to every variable on the left-
hand side and all remaining values will be assigned to *args .For better
understanding consider the following code.

  

  

**Example 2**

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to study about

# unpacking python tuple using *

# first and last will be assigned to x and z

# remaining will be assined to y

x, *y, z = (10, "Geeks ", " for ", "Geeks ", 50)

# print details

print(x)

print(y)

print(z)

# first and second will be assigned to x and y

# remaining will be assined to z

x, y, *z = (10, "Geeks ", " for ", "Geeks ", 50)

print(x)

print(y)

print(z)  
  
---  
  
 __

 __

 **Output:**

    
    
    10
    ['Geeks ', ' for ', 'Geeks ']
    50
    10
    Geeks 
    [' for ', 'Geeks ', 50]

In python tuples can be unpacked using a function in function tuple is passed
and in function values are unpacked into normal variable. Consider the
following code for better understanding.

**Example 3 :**

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to study about

# unpacking python tuple using function

# function takes normal arguments

# and multiply them

def result(x, y):

 return x * y

# function with normal variables

print (result(10, 100))

# A tuple is created

z = (10, 100)

# Tuple is passed

# function unpacked them

print (result(*z))  
  
---  
  
 __

 __

 **Output:**

    
    
    1000
    1000

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

