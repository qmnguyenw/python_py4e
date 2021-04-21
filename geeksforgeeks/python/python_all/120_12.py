Python | Binary Group Tuple list elements



Sometimes, while working with tuples, we can have problems of grouping them,
be it based on gender or any particular binary category. This can have
applications in many domains. Let’s discuss certain ways in which this can be
performed.

 **Method #1 : Using generator + loop +zip()**  
The brute force method to perform this task, in this, we perform the
combination grouping with the help of zip(), and iteration logic is handled
by generator and loop.

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Binary Group Tuple list elements

# using generator + loop + zip()

 

# helper function to perform task 

def bin_group(test_list):

 for tup1, tup2 in zip(test_list[0::2],
test_list[1::2]):

 yield (tup1[0], tup1[1], tup2[1])

 

# initialize list 

test_list = [(1, 56, 'M'), (1, 14, 'F'), (2,
43, 'F'), (2, 10, 'M')]

 

# printing original list 

print("The original list : " + str(test_list))

 

# Binary Group Tuple list elements

# using generator + loop + zip()

res = list(bin_group(test_list))

 

# printing result

print("The list after binary grouping : " + str(res))  
  
---  
  
 __

 __

 **Output :**

    
    
    The original list : [(1, 56, 'M'), (1, 14, 'F'), (2, 43, 'F'), (2, 10, 'M')]
    The list after binary grouping : [(1, 56, 14), (2, 43, 10)]
    

**Method #2 : Using defaultdict() + list comprehension +sorted() + items()**  
Combination of above functions can be used to perform this task. In this, we
convert the list into dictionary and then perform key based grouping and
rearrange back to tuple list.

  

  

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Binary Group Tuple list elements

# using defaultdict() + list comprehension + sorted() + items()

from collections import defaultdict

 

# initialize list 

test_list = [(1, 56, 'M'), (1, 14, 'F'), (2,
43, 'F'), (2, 10, 'M')]

 

# printing original list 

print("The original list : " + str(test_list))

 

# Binary Group Tuple list elements

# using defaultdict() + list comprehension + sorted() + items()

temp = defaultdict(list)

for ele in test_list:

 temp[ele[0]].append(ele[1])

res = sorted((key, ) + tuple(val) for key, val in
temp.items())

 

# printing result

print("The list after binary grouping : " + str(res))  
  
---  
  
 __

 __

 **Output :**

    
    
    The original list : [(1, 56, 'M'), (1, 14, 'F'), (2, 43, 'F'), (2, 10, 'M')]
    The list after binary grouping : [(1, 56, 14), (2, 43, 10)]
    

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

