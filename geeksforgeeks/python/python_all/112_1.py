Python – Maximum element in consecutive subsets



Some of the classical problems in programming domain come from different
categories and one among them is finding the max of subsets. This particular
problem is also common when we need to compute the max and store consecutive
group max value. Let’s try different approaches to this problem in python
language.

 **Method #1 : Using list comprehension + max()**  
The list comprehension can be used to perform this particular task to filter
out successive groups and max function can be used to get the max of the
filtered solution.

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate

# Maximum element in consecutive subsets

# using list comprehension + max()

 

# initializing list

test_list = [4, 7, 8, 10, 12, 15, 13, 17,
14]

 

# printing original list 

print("The original list : " + str(test_list))

 

# using list comprehension + max()

# Maximum element in consecutive subsets

res = [ max(test_list[x : x + 3]) 

 for x in range(0, len(test_list), 3)]

 

# printing result

print("The grouped maximized list is : " + str(res))  
  
---  
  
 __

 __

 **Output :**

    
    
    The original list : [4, 7, 8, 10, 12, 15, 13, 17, 14]
    The grouped maximized list is : [8, 15, 17]
    

**Method #2 : Usingmax() + itertools.islice()**  
The task of slicing the list into chunks is done by islice method here and the
conventional task of getting the maximum is done by the max function as the
above method.

  

  

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate

# Maximum element in consecutive subsets

# using itertools.islice() + max()

import itertools

 

# initializing list

test_list = [4, 7, 8, 10, 12, 15, 13, 17,
14]

 

# printing original list 

print("The original list : " + str(test_list))

 

# using itertools.islice() + max()

# Maximum element in consecutive subsets

res = [max(list(itertools.islice(test_list, i, i + 3)))

 for i in range(0, len(test_list), 3)]

 

# printing result

print("The grouped maximized list is : " + str(res))  
  
---  
  
 __

 __

 **Output :**

    
    
    The original list : [4, 7, 8, 10, 12, 15, 13, 17, 14]
    The grouped maximized list is : [8, 15, 17]
    

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

