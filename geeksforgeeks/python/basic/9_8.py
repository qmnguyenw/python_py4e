Difference between List and Dictionary in Python



Lists are just like the arrays, declared in other languages. Lists need not be
homogeneous always which makes it a most powerful tool in Python. A single
list may contain DataTypes like Integers, Strings, as well as Objects. Lists
are mutable, and hence, they can be altered even after their creation.

 **Example:**

 __

 __  
 __

 __

 __  
 __  
 __

# Python program to demonstrate

# Lists

 

 

# Creating a List with 

# the use of multiple values 

List = ["Geeks", "For", "Geeks"] 

print("List containing multiple values: ") 

print(List[0]) 

print(List[2]) 

 

# Creating a Multi-Dimensional List 

# (By Nesting a list inside a List) 

List = [['Geeks', 'For'] , ['Geeks']] 

print("\nMulti-Dimensional List: ") 

print(List)   
  
---  
  
__

__

**Output:**

    
    
    List containing multiple values: 
    Geeks
    Geeks
    
    Multi-Dimensional List: 
    [['Geeks', 'For'], ['Geeks']]
    

Dictionary in Python on the other hand is an unordered collection of data
values, used to store data values like a map, which unlike other Data Types
that hold only single value as an element, Dictionary holds key:value pair.
Key-value is provided in the dictionary to make it more optimized. Each key-
value pair in a Dictionary is separated by a colon :, whereas each key is
separated by a ‘comma’.

 **Example:**

  

  

 __

 __  
 __

 __

 __  
 __  
 __

# Python program to demonstrate

# dictionary

 

 

# Creating a Dictionary 

# with Integer Keys 

Dict = {1: 'Geeks', 2: 'For', 3: 'Geeks'} 

print("Dictionary with the use of Integer Keys: ") 

print(Dict) 

 

# Creating a Dictionary 

# with Mixed keys 

Dict = {'Name': 'Geeks', 1: [1, 2, 3, 4]} 

print("\nDictionary with the use of Mixed Keys: ") 

print(Dict)   
  
---  
  
__

__

**Output:**

    
    
    Dictionary with the use of Integer Keys: 
    {1: 'Geeks', 2: 'For', 3: 'Geeks'}
    
    Dictionary with the use of Mixed Keys: 
    {1: [1, 2, 3, 4], 'Name': 'Geeks'}
    

#### Difference between List and Dictionary:

List| Dictionary| List is a collection of index values pairs as that of array
in c++.| Dictionary is a hashed structure of **key and value** pairs.| List is
created by placing elements in **[ ]** seperated by commas “, “| Dictionary is
created by placing elements in **{ }** as “key”:”value”, each key value pair
is seperated by commas “, ”| The indices of list are integers starting from
0.| The keys of dictionary can be of any data type.| The elements are accessed
via indices.| The elements are accessed via key-values.| The order of the
elements entered are maintained.| There is no guarantee for maintaining order.  
---|---  
  
#### Space-Time Trade-Off

It is more efficient to use a dictionary for lookup of elements because it
takes less time to traverse in the dictionary than a list.

For example, let’s consider a data set with 5000000 elements in a machine
learning model that relies on the speed of retrieval of data. To implement
this we have to choose wisely between two data structure i.e. list and
dictionary. The dictionary is preferred because of less time and less space
storage as dictionaries are implemented in the form of hash tables from
python3.6 so it is never a space-time trade-off problem in dictionaries.

 **Example 1:**

 __

 __  
 __

 __

 __  
 __  
 __

# Program to demonstrate

# space-time trade-off between

# dictionary and list

 

 

# To calculate the time

# difference

import time

 

 

# Creating a dictionary

d ={'john':1, 'alex':2}

 

x = time.time()

 

# Accessing elements

print("Accessing dictionary elements:")

for key in d:

 print(d[key], end=" ")

 

y = time.time()

print("\nTime taken by dictionary:", y-x)

 

# Creating a List

c =[1, 2]

 

x = time.time()

 

print("\nAccessing List elements:")

for i in c:

 print(i, end=" ")

 

y = time.time()

print("\nTime taken by dictionary:", y-x)  
  
---  
  
 __

 __

 **Output:**

    
    
    Accessing dictionary elements:
    1 2 
    Time taken by dictionary: 1.0013580322265625e-05
    
    Accessing List elements:
    1 2 
    Time taken by dictionary: 3.5762786865234375e-06
    

**Example 2:**

 __

 __  
 __

 __

 __  
 __  
 __

# Program to fetch particular

# elements of structure

 

 

import time

 

 

# Creating dictionary and list

dict_name ={"bob":12, "john":11}

list_name =[2, 3, 4, 5, 1]

 

# Time taken by dictionary

x = time.time()

L = dict_name["bob"]

y = time.time()

print("Time taken by dictionary:", y-x)

 

# Time taken by list

x = time.time()

L = list_name[2]

y = time.time()

print("\nTime taken by list:", y-x)  
  
---  
  
 __

 __

 **Output:**

    
    
    Time taken by dictionary: 9.5367431640625e-07
    
    Time taken by list: 4.76837158203125e-07
    

**Note:** It took more time for fetching a single element in a list than that
of a dictionary because dictionary uses has table for implementing the
arrangement.  

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

