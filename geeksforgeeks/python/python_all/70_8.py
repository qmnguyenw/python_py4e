Find the size of a Tuple in Python



Tuple is a collection of Python objects much like a list. The sequence of
values stored in a tuple can be of any type, and they are indexed by integers.  
Values of a tuple are syntactically separated by ‘commas’. Although it is not
necessary, it is more common to define a tuple by closing the sequence of
values in parentheses.  
The size of a Tuple means the amount of memory (in bytes) taken by a Tuple
object. In this article, we will learn various ways to get the size of a
python Tuple.

 **1.Usinggetsizeof() function:**

The getsizeof() function belongs to the python’s sys module. It has been
implemented in the below example.

 **Example 1:**

 __

 __  
 __

 __

 __  
 __  
 __

import sys

 

# sample Tuples

Tuple1 = ("A", 1, "B", 2, "C", 3)

Tuple2 = ("Geek1", "Raju", "Geek2", "Nikhil",
"Geek3", "Deepanshu")

Tuple3 = ((1, "Lion"), ( 2, "Tiger"), (3, "Fox"),
(4, "Wolf"))

 

# print the sizes of sample Tuples

print("Size of Tuple1: " + str(sys.getsizeof(Tuple1)) +
"bytes")

print("Size of Tuple2: " + str(sys.getsizeof(Tuple2)) +
"bytes")

print("Size of Tuple3: " + str(sys.getsizeof(Tuple3)) +
"bytes")  
  
---  
  
 __

 __

 **Output:**

  

  

    
    
    Size of Tuple1: 96bytes
    Size of Tuple2: 96bytes
    Size of Tuple3: 80bytes

 **Note:** The sys.getsizeof() function includes the marginal space usage,
which includes the garbage collection overhead for the object. Meaning it
returns the total space occupied by the object in addition to the garbage
collection overhead for the spaces being used.

 **1.Using inbuilt__sizeof__() method:**

Python also has an inbuilt __sizeof__() method to determine the space
allocation of an object without any additional garbage value. It has been
implemented in the below example.  
 **Example 2:**

 __

 __  
 __

 __

 __  
 __  
 __

# sample Tuples

Tuple1 = ("A", 1, "B", 2, "C", 3)

Tuple2 = ("Geek1", "Raju", "Geek2", "Nikhil",
"Geek3", "Deepanshu")

Tuple3 = ((1, "Lion"), ( 2, "Tiger"), (3, "Fox"),
(4, "Wolf"))

 

# print the sizes of sample Tuples

print("Size of Tuple1: " + str(Tuple1.__sizeof__()) +
"bytes")

print("Size of Tuple2: " + str(Tuple2.__sizeof__()) +
"bytes")

print("Size of Tuple3: " + str(Tuple3.__sizeof__()) +
"bytes")  
  
---  
  
 __

 __

 **Output:**

    
    
    Size of Tuple1: 72bytes
    Size of Tuple2: 72bytes
    Size of Tuple3: 56bytes

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

