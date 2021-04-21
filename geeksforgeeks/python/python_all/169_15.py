Python | Custom list split



Development and sometimes machine learning applications require splitting
lists into smaller list in a custom way, i.e on certain values on which split
has to be performed. This is quite a useful utility to have knowledge about.
Let’s discuss certain ways in which this task can be performed.

 **Method #1 : Using list comprehension +zip()**

By coupling the power of list comprehension and zip(), this task can be
achieved. In this, we zip beginning and end of list and then keep slicing the
list as they arrive and cutting off new lists from them.

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate

# to perform custom list split

# using list comprehension + zip()

 

# initializing string 

test_list = [1, 4, 5, 6, 7, 3, 5, 9,
2, 4]

 

# initializing split index list 

split_list = [2, 5, 7]

 

# printing original list

print ("The original list is : " + str(test_list))

 

# printing original split index list

print ("The original split index list : " + str(split_list))

 

# using list comprehension + zip()

# to perform custom list split

res = [test_list[i : j] for i, j in zip([0] +

 split_list, split_list + [None])]

 

# printing result

print ("The splitted lists are : " + str(res))  
  
---  
  
 __

 __

 **Output:**

    
    
    The original list is : [1, 4, 5, 6, 7, 3, 5, 9, 2, 4]
    The original split index list : [2, 5, 7]
    The splitted lists are : [[1, 4], [5, 6, 7], [3, 5], [9, 2, 4]]
    

  
**Method #2 : Usingitertools.chain() + zip()**

  

  

The task performed by the list comprehension function of getting the split
chunks can also be done using chain function. This is more useful when we wish
to handle larger lists as this method is more efficient.

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate

# to perform custom list split

# using itertools.chain() + zip()

from itertools import chain

 

# initializing string 

test_list = [1, 4, 5, 6, 7, 3, 5, 9,
2, 4]

 

# initializing split index list 

split_list = [2, 5, 7]

 

# printing original list

print ("The original list is : " + str(test_list))

 

# printing original split index list

print ("The original split index list : " + str(split_list))

 

# using itertools.chain() + zip()

# to perform custom list split

temp = zip(chain([0], split_list), chain(split_list, [None]))

res = list(test_list[i : j] for i, j in temp)

 

# printing result

print ("The splitted lists are : " + str(res))  
  
---  
  
 __

 __

 **Output:**

    
    
    The original list is : [1, 4, 5, 6, 7, 3, 5, 9, 2, 4]
    The original split index list : [2, 5, 7]
    The splitted lists are : [[1, 4], [5, 6, 7], [3, 5], [9, 2, 4]]
    

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

