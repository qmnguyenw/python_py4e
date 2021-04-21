Python – Find minimum of non zero groups



Many times we need to get the minimum of not the whole list but just a part of
it and at regular intervals. These intervals are sometimes decided statically
before traversal, but sometimes, the constraint is more dynamic and hence we
require to handle it in more complex way. Criteria discussed here is minimum
of non-zero groups. Let’s discuss certain ways in which this task can be done.

 **Method #1 : Using loops**  
This task can be performed using the brute force manner using the loops. We
just traverse the list each element to test for it’s succeeding element to be
non-zero value and perform the minimum once we find a next value to be zero
and append it in result list.

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate

# Natural Numbers Minimum

# Using loops

 

# initializing list

test_list = [4, 9, 0, 0, 3, 4, 5, 0,
0, 4, 0]

 

# printing original list

print("The original list : " + str(test_list))

 

# using loops

# Natural Numbers Minimum

res = []

val = 99999

for ele in test_list:

 if ele == 0:

 if val != 99999:

 res.append(val)

 val = 99999

 else:

 val = min(val, ele)

 

# print result

print("The non-zero group Minimum of list is : " + str(res))  
  
---  
  
 __

 __

 **Output :**

    
    
    The original list : [4, 9, 0, 0, 3, 4, 5, 0, 0, 4, 0]
    The non-zero group Minimum of list is : [4, 3, 4]
    

**Method #2 : Usingitertools.groupby() + min()**  
This particular task can also be performed using groupby function to group all
the non-zero values and min function can be used to perform their minimum.

  

  

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate

# Natural Numbers Minimum

# Using itertools.groupby() + min()

from itertools import groupby

 

# initializing list

test_list = [4, 9, 0, 0, 3, 4, 5, 0,
0, 4, 0]

 

# printing original list

print("The original list : " + str(test_list))

 

# using itertools.groupby() + min()

# Natural Numbers Minimum

res = [min(val) for keys, val in groupby(test_list, key =
lambda x: x != 0) if keys != 0]

 

# print result

print("The non-zero group minimum of list is : " + str(res))  
  
---  
  
 __

 __

 **Output :**

    
    
    The original list : [4, 9, 0, 0, 3, 4, 5, 0, 0, 4, 0]
    The non-zero group Minimum of list is : [4, 3, 4]
    

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

