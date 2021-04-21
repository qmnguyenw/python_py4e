Python | Variable list slicing



The problem of slicing a list has been dealt earlier, but sometimes we need to
perform the slicing in variable lengths according to the input given in other
list. This problem has its potential application in web development. Let’s
discuss certain ways in which this can be done.

 **Method #1 : Usingitertools.islice() \+ list comprehension**  
The list comprehension can be used to iterate through the list and the
component issue is solved using the islice function.

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate

# variable length slicing

# using itertools.islice() + list comprehension

from itertools import islice

 

# initializing test list

test_list = [1, 5, 3, 7, 8, 10, 11, 16,
9, 12]

 

# initializing slice list 

slice_list = [2, 1, 3, 4]

 

# printing original list 

print("The original list : " + str(test_list))

 

# printing slice list 

print("The slice list : " + str(slice_list))

 

# using itertools.islice() + list comprehension

# variable length slicing

temp = iter(test_list)

res = [list(islice(temp, part)) for part in slice_list]

 

# print result

print("The variable sliced list is : " + str(res))  
  
---  
  
 __

 __

 **Output :**

    
    
    The original list : [1, 5, 3, 7, 8, 10, 11, 16, 9, 12]
    The slice list : [2, 1, 3, 4]
    The variable sliced list is : [[1, 5], [3], [7, 8, 10], [11, 16, 9, 12]]
    

**Method #2 : Usingzip() + accumulate() \+ list slicing**  
Apart from using the list comprehension to perform the task of binding, this
method uses zip function to hold sublist element together, accumulate function
joins the elements, and slicing is used to construct the required slicing.

  

  

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate

# variable length slicing

# using zip() + accumulate() + list slicing

from itertools import accumulate

 

# initializing test list

test_list = [1, 5, 3, 7, 8, 10, 11, 16,
9, 12]

 

# initializing slice list 

slice_list = [2, 1, 3, 4]

 

# printing original list 

print("The original list : " + str(test_list))

 

# printing slice list 

print("The slice list : " + str(slice_list))

 

# using zip() + accumulate() + list slicing

# variable length slicing

res = [test_list[i - j: i] for i, j in
zip(accumulate(slice_list), slice_list)]

 

# print result

print("The variable sliced list is : " + str(res))  
  
---  
  
 __

 __

 **Output :**

    
    
    The original list : [1, 5, 3, 7, 8, 10, 11, 16, 9, 12]
    The slice list : [2, 1, 3, 4]
    The variable sliced list is : [[1, 5], [3], [7, 8, 10], [11, 16, 9, 12]]
    

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

