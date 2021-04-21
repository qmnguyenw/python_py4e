Python | Interleave multiple lists of same length



Given lists of same length, write a Python program to store alternative
elements of given lists in a new list.

Let’s discuss certain ways in which this can be performed.

 **Method #1 : Usingmap() + list comprehension**  
map() is used to handle the interleave of lists and the task of insertion at
alternate is performed by the list comprehension part of the shorthand code.
Only works in Python 2.  

 __

 __  
 __

 __

 __  
 __  
 __

# Python2 code to demonstrate

# to interleave lists

# using map() + list comprehension

 

# initializing lists 

test_list1 = [1, 4, 5]

test_list2 = [3, 8, 9]

 

# printing original lists

print ("Original list 1 : " + str(test_list1))

print ("Original list 2 : " + str(test_list2))

 

# using map() + list comprehension

# to interleave lists

res = [i for j in map(None, test_list1, test_list2) 

 for i in j if i is not None]

 

# printing result

print ("The interleaved list is : " + str(res))  
  
---  
  
 __

 __

 **Output:**

    
    
    Original list 1 : [1, 4, 5]
    Original list 2 : [3, 8, 9]
    The interleaved list is : [1, 3, 4, 8, 5, 9]
    

  
**Method #2 : Using List slicing**  
Power of list slicing of python can also be used to perform this particular
task. We first extend one list to another and then allow the original list to
desired alternate indices of the resultant list.

  

  

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate

# to interleave lists

# using list slicing

 

# initializing lists 

test_list1 = [1, 4, 5]

test_list2 = [3, 8, 9]

 

# printing original lists

print ("Original list 1 : " + str(test_list1))

print ("Original list 2 : " + str(test_list2))

 

# using list slicing

# to interleave lists

res = test_list1 + test_list2

res[::2] = test_list1

res[1::2] = test_list2

 

# printing result

print ("The interleaved list is : " + str(res))  
  
---  
  
 __

 __

 **Output:**

    
    
    Original list 1 : [1, 4, 5]
    Original list 2 : [3, 8, 9]
    The interleaved list is : [1, 3, 4, 8, 5, 9]
    

  
**Method #3 : Usingitertools.chain() + zip()**  
zip() can be used to link both the lists and then chain() can used to
perform the alternate append of the elements as desired. This is the most
efficient method to perform this task.  

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate

# to interleave lists

# using zip() + itertools.chain()

import itertools

 

# initializing lists 

test_list1 = [1, 4, 5]

test_list2 = [3, 8, 9]

 

# printing original lists

print ("Original list 1 : " + str(test_list1))

print ("Original list 2 : " + str(test_list2))

 

# using zip() + itertools.chain()

# to interleave lists

res = list(itertools.chain(*zip(test_list1, test_list2)))

 

# printing result

print ("The interleaved list is : " + str(res))  
  
---  
  
 __

 __

 **Output:**

    
    
    Original list 1 : [1, 4, 5]
    Original list 2 : [3, 8, 9]
    The interleaved list is : [1, 3, 4, 8, 5, 9]
    

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

