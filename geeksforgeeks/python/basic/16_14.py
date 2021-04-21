Check if element exists in list in Python



List is an important container in python as if stores elements of all the
datatypes as a collection. Knowledge of certain list operations are necessary
for day-day programming. This article discusses one of the basic list
operation of ways to check existence of element in list.  

 **Method 1 : Naive Method**

In Naive method, one easily uses a loop that iterates through all the elements
to check the existence of the target element. This is the simplest way to
check the existence of the element in the list.  

 **Method 2 : Usingin**

Python in is the most conventional way to check if an element exists in list
or not. This particular way returns True if element exists in list and False
if the element does not exists in list. List need not be sorted to practice
this approach of checking.  
  
 **Code #1 :** Demonstrating to check existence of element in list using Naive
method and in  

  

  

 __

 __  
 __

 __

 __  
 __  
 __

# Python code to demonstrate

# checking of element existence

# using loops and in

 

# Initializing list 

test_list = [ 1, 6, 3, 5, 3, 4 ]

 

print("Checking if 4 exists in list ( using loop ) : ")

 

# Checking if 4 exists in list 

# using loop

for i in test_list:

 if(i == 4) :

 print ("Element Exists")

 

print("Checking if 4 exists in list ( using in ) : ")

 

# Checking if 4 exists in list 

# using in

if (4 in test_list):

 print ("Element Exists")  
  
---  
  
 __

 __

 **Output :**

    
    
    Checking if 4 exists in list ( using loop ) : 
    Element Exists
    Checking if 4 exists in list ( using in ) : 
    Element Exists
    

**Method 3 : Usingset() \+ in**

Converting the list into set and then using in can possibly be more efficient
than only using in. But having efficiency for a plus also has certain
negatives. One among them is that the order of list is not preserved, and if
you opt to take a new list for it, you would require to use extra space. Other
drawback is that set disallows duplicacy and hence duplicate elements would be
removed from the original list.  

 **Method 4 : Usingsort() \+ bisect_left()**

The conventional binary search way of testing of element existence, hence list
has to be sorted first and hence not preserving the element ordering.
bisect_left() returns the first occurrence of element to be found and has
working similar to lower_bound() in C++ STL.  
  
 **Code #2 :** Demonstrating to check existence of element in list using
set() \+ in and sort() \+ bisect_left().  

 __

 __  
 __

 __

 __  
 __  
 __

# Python code to demonstrate

# checking of element existence

# using set() + in

# using sort() + bisect_left()

from bisect import bisect_left 

 

# Initializing list 

test_list_set = [ 1, 6, 3, 5, 3, 4 ]

test_list_bisect = [ 1, 6, 3, 5, 3, 4 ]

 

print("Checking if 4 exists in list ( using set() + in) : ")

 

# Checking if 4 exists in list 

# using set() + in

test_list_set = set(test_list_set)

if 4 in test_list_set :

 print ("Element Exists")

 

print("Checking if 4 exists in list ( using sort() + bisect_left() ) :
")

 

# Checking if 4 exists in list 

# using sort() + bisect_left()

test_list_bisect.sort()

if bisect_left(test_list_bisect, 4):

 print ("Element Exists")  
  
---  
  
 __

 __

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

