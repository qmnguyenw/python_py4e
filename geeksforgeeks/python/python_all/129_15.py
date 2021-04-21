Python | Get unique tuples from list



Sometimes, while working with Python list, we can come across a problem in
which we require to find the unique occurrences of list. Having elementary
data types is easy to handle, but sometime, we might have complex data types
and the problem becomes new in that cases. Let’s discuss certain ways in which
tuples are handled for this problem.

 **Method #1 : Usinglist() + set()**  
Alike integers, being immutable these can also be handled by set() for
removal of the duplicates. It converts the list to set and removes duplicates
and converted back to list by list()

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Get unique tuples from list

# using set() + list()

 

# initializing list

test_list = [(4, 5), (6, 1), (4, 5), (6,
1)]

 

# printing original list

print("The original list is : " + str(test_list))

 

# Get unique tuples from list

# using set() + list()

res = list(set(test_list))

 

# printing result 

print("List after removal of duplicates " + str(res))  
  
---  
  
 __

 __

 **Output :**

    
    
    The original list is : [(4, 5), (6, 1), (4, 5), (6, 1)]
    List after removal of duplicates [(4, 5), (6, 1)]
    

**Method #2 : Usingdict.fromkeys() + list()**  
Since newer versions of Python dictionaries, remember their order of
insertion, the list contents can be converted to dictionary element list,
which remembers the order and removes the duplicates. It is converted back
using list().

  

  

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Get unique tuples from list

# using dict.fromkeys() + list()

 

# initializing list

test_list = [(4, 5), (6, 1), (4, 5), (6,
1)]

 

# printing original list

print("The original list is : " + str(test_list))

 

# Get unique tuples from list

# using dict.fromkeys() + list()

res = list(dict.fromkeys(test_list))

 

# printing result 

print("List after removal of duplicates " + str(res))  
  
---  
  
 __

 __

 **Output :**

    
    
    The original list is : [(4, 5), (6, 1), (4, 5), (6, 1)]
    List after removal of duplicates [(4, 5), (6, 1)]
    

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

