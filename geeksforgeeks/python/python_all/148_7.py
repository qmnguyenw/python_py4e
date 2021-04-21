Python | Row lengths in Matrix



The problems concerning matrix are quite common in both competitive
programming and Data Science domain. One such problem that we might face is of
finding the lengths of rows of matrix in uneven sized matrix. Let’s discuss
certain ways in which this problem can be solved.

 **Method #1 : Usingmax() + map() + sum() \+ list comprehension**

The combination of above functions can help to get the solution to this
particular problem in just a one line and hence quite useful. The sum function
computes the sum of sublists, max function can be used to order in descending
and all this bound together using list comprehension.

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate

# Row lengths in matrix

# using max() + map() + sum() + list comprehension

 

# initializing list

test_list = [[4, 5, 6], [7, 8], [2]]

 

# printing original list

print("The original list : " + str(test_list))

 

# using max() + map() + sum() + list comprehension

# Row lengths in matrix

res = [sum(len(row) > idx for row in test_list)

 for idx in range(max(map(len, test_list)))]

 

# print result

print("The row lengths in matrix : " + str(res))  
  
---  
  
 __

 __

 **Output :**

    
    
    The original list : [[4, 5, 6], [7, 8], [2]]
    The row lengths in matrix : [3, 2, 1]
    

  

  

**Method #2 : Usingsum() + filter() + zip_longest()**

This problem can also be solved using the set of functions above. The filter
function can be used to get the separate lists and the task of binding for
summation done by sum function is performed by zip_longest function.

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate

# Row lengths in matrix

# using sum() + filter() + zip_longest()

from itertools import zip_longest

 

# initializing list

test_list = [[4, 5, 6], [7, 8], [2]]

 

# printing original list

print("The original list : " + str(test_list))

 

# using sum() + filter() + zip_longest()

# Row lengths in matrix

res = [sum(1 for idx in filter(None.__ne__, i))

 for i in zip_longest(*test_list)]

 

# print result

print("The row lengths in matrix : " + str(res))  
  
---  
  
 __

 __

 **Output :**

    
    
    The original list : [[4, 5, 6], [7, 8], [2]]
    The row lengths in matrix : [3, 2, 1]
    

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

