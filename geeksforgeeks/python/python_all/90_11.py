Python – Sublist Maximum in custom sliced List



Sometimes, while working with data, we can have a problem in which we need to
extract maximum not of whole list but of certain customly broken sublists.
This kind of problem is peculiar and occurs in many domains. Let’s discuss
certain ways in which in which this task can be performed.

 **Method #1 : Usingitertools.islice() + max() \+ list comprehension**  
The combination of above methods can be used to solve this problem. In this
islice() is used to perform custom slicing and list comprehension is used to
iterate and max() is used to compute maximum.

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate

# Sublist Maximum in custom sliced List

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

# Sublist Maximum in custom sliced List

temp = iter(test_list)

res = [max(list(islice(temp, part))) for part in
slice_list]

 

# print result

print("The variable sliced list maximum is : " + str(res))  
  
---  
  
 __

 __

 **Output :**

    
    
    The original list : [1, 5, 3, 7, 8, 10, 11, 16, 9, 12]
    The slice list : [2, 1, 3, 4]
    The variable sliced list maximum is : [5, 3, 10, 16]
    

**Method #2 : Usingzip() + accumulate() + max() \+ list slicing**  
Apart from using the list comprehension to perform the task of binding, this
method uses zip function to hold sublist element together, accumulate function
joins the elements, and slicing is used to construct the required slicing. The
max() is used to perform maximum.

  

  

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate

# Sublist Maximum in custom sliced List

# using zip() + accumulate() + list slicing + max()

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

 

# using zip() + accumulate() + list slicing + max()

# Sublist Maximum in custom sliced List

res = [max(test_list[i - j: i]) for i, j in
zip(accumulate(slice_list), slice_list)]

 

# print result

print("The variable sliced list maximum is : " + str(res))  
  
---  
  
 __

 __

 **Output :**

    
    
    The original list : [1, 5, 3, 7, 8, 10, 11, 16, 9, 12]
    The slice list : [2, 1, 3, 4]
    The variable sliced list maximum is : [5, 3, 10, 16]
    

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

