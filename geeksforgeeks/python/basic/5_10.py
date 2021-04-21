Difference between List VS Set VS Tuple in Python



 **List:**Lists **** are just like dynamic sized arrays, declared in other
languages (vector in C++ and ArrayList in Java). Lists need not be homogeneous
always which makes it the most powerful tool in Python. The main
characteristics of lists are –

  * The list is a datatype available in Python which can be written as a list of comma-separated values (items) between square brackets.
  * List are mutable .i.e it can be converted into another data type and can store any data element in it.
  * List can store any type of element.

 **Example:**

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 program to demonstrate

# List 

 

# Creating a List

List = []

print("Blank List: ")

print(List)

 

# Creating a List of numbers

List = [10, 20, 14]

print("\nList of numbers: ")

print(List)

 

# Creating a List of strings and accessing

# using index

List = ["Geeks", "For", "Geeks"]

print("\nList Items: ")

print(List[0]) 

print(List[2])  
  
---  
  
 __

 __

 **Output:**

    
    
    Blank List: 
    []
    
    List of numbers: 
    [10, 20, 14]
    
    List Items: 
    Geeks
    Geeks
    
    
    
    
    

**Tuple:**Tuple **** is a collection of Python objects much like a list. The
sequence of values stored in a tuple can be of any type, and they are indexed
by integers. Values of a tuple are syntactically separated by ‘commas’.
Although it is not necessary, it is more common to define a tuple by closing
the sequence of values in parentheses. The main characteristics of tuples are
–

  * Tuple is an immutable sequence in python.
  * It cannot be changed or replaced since it is immutable.
  * It is defined under parenthesis().
  * Tuples can store any type of element.

 **Example:**

  

  

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# Creating an empty Tuple

Tuple1 = ()

print("Initial empty Tuple: ")

print (Tuple1)

 

# Creating a Tuple with

# the use of list

list1 = [1, 2, 4, 5, 6]

print("\nTuple using List: ")

print(tuple(list1))

 

#Creating a Tuple 

#with the use of built-in function

Tuple1 = tuple('Geeks')

print("\nTuple with the use of function: ")

print(Tuple1)  
  
---  
  
 __

 __

 **Output:**

    
    
    Initial empty Tuple: 
    ()
    
    Tuple using List: 
    (1, 2, 4, 5, 6)
    
    Tuple with the use of function: 
    ('G', 'e', 'e', 'k', 's')
    
    
    
    
    

**Set:** In Python, Set **** is an unordered collection of data type that is
iterable, mutable, and has no duplicate elements. The major advantage of using
a set, as opposed to a list, is that it has a highly optimized method for
checking whether a specific element is contained in the set. The main
characteristics of set are –

  * Sets are an unordered collection of elements or unintended collection of items In python.
  * Here the order in which the elements are added into the set is not fixed, it can change frequently.
  * It is defined under curly braces{}
  * Sets are mutable, however, only immutable objects can be stored in it.

 **Example:**

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 program to demonstrate

# Set in Python

 

# Creating a Set

set1 = set()

print("Intial blank Set: ")

print(set1)

 

# Creating a Set with

# the use of Constructor

# (Using object to Store String)

String = 'GeeksForGeeks'

set1 = set(String)

print("\nSet with the use of an Object: " )

print(set1)

 

# Creating a Set with

# the use of a List

set1 = set(["Geeks", "For", "Geeks"])

print("\nSet with the use of List: ")

print(set1)  
  
---  
  
 __

 __

 **Output:**

    
    
    Intial blank Set: 
    set()
    
    Set with the use of an Object: 
    {'G', 's', 'e', 'o', 'r', 'F', 'k'}
    
    Set with the use of List: 
    {'Geeks', 'For'}
    
    
    
    
    

### Table of Difference between List, Set, and Tuple

List| Set| Tuple| Lists is Mutable| Set is Mutable| Tuple is Immutable| It is
Ordered collection of items| It is Unordered collection of items| It is
Ordered collection of items| Items in list can be replaced or changed| Items
in set cannot be changed or replaced| Items in tuple cannot be changed or
replaced  
---|---|---  
  
Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

