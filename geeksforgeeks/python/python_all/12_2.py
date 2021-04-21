Differences and Applications of List, Tuple, Set and Dictionary in Python



 ** _Lists:_** are just like dynamic sized arrays, declared in other languages
(vector in C++ and ArrayList in Java). Lists need not be homogeneous always
which makes it a most powerful tool in Python.

 ** _Tuple:_** A Tuple is a collection of Python objects separated by commas.
In someways a tuple is similar to a list in terms of indexing, nested objects
and repetition but a tuple is immutable unlike lists that are mutable.

 ** _Set:_** A Set is an unordered collection data type that is iterable,
mutable and has no duplicate elements. Python’s set class represents the
mathematical notion of a set.

 ** _Dictionary:_** **** in Python is an unordered collection of data values,
used to store data values like a map, which unlike other Data Types that hold
only single value as an element, Dictionary holds **key:value** pair. Key
value is provided in the dictionary to make it more optimized.

List, Tuple, Set, and Dictionary are the data structures in python that are
used to store and organize the data in an efficient manner.

  

  
 **List**|  **Tuple**|  **Set**|  **Dictionary**|  List is a non-homogeneous
data structure which stores the elements in single row and multiple rows and
columns| Tuple is also a non-homogeneous data structure which stores single
row and multiple rows and columns| Set data structure is also non-homogeneous
data structure but stores in single row| Dictionary is also a non-homogeneous
data structure which stores key value pairs| List can be represented by [ ]|

Tuple can be represented by

( )| Set can be represented by { }| Dictionary can be represented by { }| List
allows duplicate elements| Tuple allows duplicate elements| Set will not allow
duplicate elements| Set will not allow duplicate elements but keys are not
duplicated| List can use nested among all| Tuple can use nested among all| Set
can use nested among all| Dictonary can use nested among all| Example: [1, 2,
3, 4, 5]| Example: (1, 2, 3, 4, 5)| Example: {1, 2, 3, 4, 5}| Example: {1, 2,
3, 4, 5}| List can be created using **list()** function| Tuple can be created
using **tuple()** function.| Set can be created using **set()** function|
Dictonary can be created using **dict()** function.| List is mutable i.e we
can make any changes in list.| Tuple is immutable i.e we can not make any
changes in tuple| Set is mutable i.e we can make any changes in set. But
elements are not duplicated.| Dictionary is mutable. But Keys are not
duplicated.| List is ordered| Tuple is ordered| Set is unordered| Dictionary
is ordered|

Creating an empty list

l=[]|

Creating an empty Tuple

t=()|

Creating a set

a=set()

  

  

b=set(a)|

Creating an empty dictionary

d={}  
  
---|---|---|---  
  
Below is the program for implementation of List, tuple, set, and dictionary:

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 program for explaining

# use of list, tuple, set and 

# dictonary

 

# Lists

l = []

 

# Adding Element into list

l.append(5)

l.append(10)

print("Adding 5 and 10 in list", l)

 

# Popping Elements from list

l.pop()

print("Popped one element from list", l)

print()

 

# Set

s = set()

 

# Adding element into set

s.add(5)

s.add(10)

print("Adding 5 and 10 in set", s)

 

# Removing element from set

s.remove(5)

print("Removing 5 from set", s)

print()

 

# Tuple

t = tuple(l)

 

# Tuples are immutable

print("Tuple", t)

print()

 

# Dictonary

d = {}

 

# Adding the key value pair

d[5] = "Five"

d[10] = "Ten"

print("Dictonary", d)

 

# Removing key-value pair

del d[10]

print("Dictonary", d)  
  
---  
  
 __

 __

 **Output:**

    
    
    Adding 5 and 10 in list [5, 10]
    Popped one element from list [5]
    
    Adding 5 and 10 in set {10, 5}
    Removing 5 from set {10}
    
    Tuple (5, )
    
    Dictonary {10: 'Ten', 5: 'Five'}
    Dictonary {5: 'Five'}
    

### Applications of List, Set, Tuple, and Dictonary

 **List:**

  * Used in JSON format
  * Useful for Array operations
  * Used in Databases

 **Tuple:**

  * Used to insert records in the database through SQL query at a time  
Ex: (1.’sravan’, 34).(2.’geek’, 35)

  * Used in parentheses checker

 **Set**

  * Finding unique elements
  * Join operations

 **Dictionary**

  * Used to create a data frame with lists
  * Used in JSON

Attention reader! Don’t stop learning now. Get hold of all the important DSA
concepts with the **DSA Self Paced Course** at a student-friendly price and
become industry ready. To complete your preparation from learning a language
to DS Algo and many more, please refer **Complete Interview Preparation
Course** **.**

My Personal Notes _arrow_drop_up_

Save

