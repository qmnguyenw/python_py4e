Python | Check if element exists in list of lists



Given a list of lists, the task is to determine whether the given element
exists in any sublist or not. Given below are a few methods to solve the given
task.  
  
 **Method #1: Using any()**

any() method return true whenever a particular element is present in a given
iterator.

 __

 __  
 __

 __

 __  
 __  
 __

# Python code to demonstrate

# finding whether element

# exists in listof list

 

# initialising nested lists

ini_list = [[1, 2, 5, 10, 7],

 [4, 3, 4, 3, 21],

 [45, 65, 8, 8, 9, 9]]

 

elem_to_find = 8

elem_to_find1 = 0

 

# element exists in listof listor not?

res1 = any(elem_to_find in sublist for sublist in
ini_list)

res2 = any(elem_to_find1 in sublist for sublist in
ini_list)

 

# printing result

print(str(res1), "\n", str(res2))  
  
---  
  
 __

 __

 **Output:**

    
    
    True 
     False
    

  
**Method #2: Using operator _in_**

The ‘in’ operator is used to check if a value exists in a sequence or not.
Evaluates to _true_ if it finds a variable in the specified sequence and
_false_ otherwise.

  

  

 __

 __  
 __

 __

 __  
 __  
 __

# Python code to demonstrate

# finding whether element

# exists in listof list

 

# initialising nested lists

ini_list = [[1, 2, 5, 10, 7],

 [4, 3, 4, 3, 21],

 [45, 65, 8, 8, 9, 9]]

 

elem = 8

elem1 = 0

 

# element exists in listof listor not?

res1 = elem in (item for sublist in ini_list for item
in sublist)

res2 = elem1 in (item for sublist in ini_list for item
in sublist)

 

# printing result

print(str(res1), "\n", str(res2))  
  
---  
  
 __

 __

 **Output:**

    
    
    True 
     False
    

  
**Method #3: Usingitertools.chain()**

Make an iterator that returns elements from the first iterable until it is
exhausted, then proceeds to the next iterable, until all of the iterables are
exhausted.

 __

 __  
 __

 __

 __  
 __  
 __

# Python code to demonstrate

# finding whether element

# exists in listof list

from itertools import chain

 

# initialising nested lists

ini_list = [[1, 2, 5, 10, 7], 

 [4, 3, 4, 3, 21],

 [45, 65, 8, 8, 9, 9]]

 

elem_to_find = 8

elem_to_find1 = 0

 

# element exists in listof listor not?

res1 = elem_to_find in chain(*ini_list)

res2 = elem_to_find1 in chain(*ini_list)

 

# printing result

print(str(res1), "\n", str(res2))  
  
---  
  
 __

 __

 **Output:**

    
    
    True 
     False
    

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

