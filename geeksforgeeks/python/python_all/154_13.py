Python | Increasing alternate element pattern in list



This particular article solves a very specific issue in which we need to
insert every alternate element as the increased size pattern of repeated
element to form a pattern. This can have a utility in demonstrative projects.
Let’s discuss certain ways in which this can be done.

 **Method #1 : Using list comprehension +enumerate()**  
List comprehension with the help of enumerate function can be used to perform
this particular task in which we use the tuple which increases its length
every alternate element for the insertion using the enumerate function.

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate

# increasing alternate element pattern

# using list comprehension + enumerate()

 

# initializing list 

test_list = [1, 2, 3, 4, 5]

 

# printing original list 

print("The original list : " + str(test_list))

 

# using list comprehension + enumerate()

# increasing alternate element pattern

res = [j for sub in ((i, '*' * k)

 for k, i in enumerate(test_list, 1))

 for j in sub]

 

# print result

print("The increasing element pattern list : " + str(res))  
  
---  
  
 __

 __

 **Output :**

    
    
    The original list : [1, 2, 3, 4, 5]
    The increasing element pattern list : [1, '*', 2, '**', 3, '***', 4, '****', 5, '*****']
    

**Method #2 : Usingitertools.chain.from_iterable() + zip()**  
This task can be performed efficiently using the above functions. The zip
function interleaves the formed strings using string multiplication with the
lists and from_iterable function does the task of flattening the obtained
tuples.

  

  

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate

# increasing alternate element pattern

# using itertools.chain.from_iterable() + zip()

import itertools

 

# initializing list 

test_list = [1, 2, 3, 4, 5]

 

# printing original list 

print("The original list : " + str(test_list))

 

# using itertools.chain.from_iterable() + zip()

# increasing alternate element pattern

res = list(itertools.chain.from_iterable(

 zip(test_list, ("*" * (i + 1)

 for i in range(len(test_list))))))

 

# print result

print("The increasing element pattern list : " + str(res))  
  
---  
  
 __

 __

 **Output :**

    
    
    The original list : [1, 2, 3, 4, 5]
    The increasing element pattern list : [1, '*', 2, '**', 3, '***', 4, '****', 5, '*****']
    

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

