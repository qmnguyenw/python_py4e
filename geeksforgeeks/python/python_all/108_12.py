Python | Valid Ranges Product



Many times we need to get the product of not the whole list but just a part of
it and at regular intervals. These intervals are sometimes decided statically
before traversal, but sometimes, the constraint is more dynamic and hence we
require to handle it in more complex way. Criteria discussed here is product
of non-zero groups. Let’s discuss certain ways in which this task can be done.

 **Method #1 : Using loops**  
This task can be performed using the brute force manner using the loops. We
just traverse the list each element to test for it’s succeeding element to be
non-zero value and perform the product once we find a next value to be zero
and append it in result list.

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate

# Valid Ranges Product

# Using loops

 

# initializing list

test_list = [4, 9, 0, 0, 3, 4, 5, 0,
0, 4, 0]

 

# printing original list

print("The original list : " + str(test_list))

 

# using loops

# Valid Ranges Product

res = []

val = 1

for ele in test_list:

 if ele == 0:

 if val != 1:

 res.append(val)

 val = 1

 else:

 val *= ele

 

# print result

print("The non-zero group product of list is : " + str(res))  
  
---  
  
 __

 __

 **Output :**

    
    
    The original list : [4, 9, 0, 0, 3, 4, 5, 0, 0, 4, 0]
    The non-zero group product of list is : [36, 60, 4]
    

**Method #2 : Usingitertools.groupby() \+ loop**  
This particular task can also be performed using groupby function to group all
the non-zero values and product can be performed using loop.

  

  

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate

# Valid Ranges Product

# Using itertools.groupby() + loop

from itertools import groupby

 

# getting Product

def prod(val) :

 res = 1

 for ele in val:

 res *= ele

 return res 

 

# initializing list

test_list = [4, 9, 0, 0, 3, 4, 5, 0,
0, 4, 0]

 

# printing original list

print("The original list : " + str(test_list))

 

# using itertools.groupby() + loop

# Valid Ranges Product

res = [prod(val) for keys, val in groupby(test_list, key =
lambda x: x != 0) if keys != 0]

 

# print result

print("The non-zero group product of list is : " + str(res))  
  
---  
  
 __

 __

 **Output :**

    
    
    The original list : [4, 9, 0, 0, 3, 4, 5, 0, 0, 4, 0]
    The non-zero group product of list is : [36, 60, 4]
    

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

