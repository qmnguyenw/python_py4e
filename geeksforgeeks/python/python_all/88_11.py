Python – Pair elements with Rear element in Matrix Row



Sometimes, while working with data, we can have a problem in which we need to
pair each element in container to a specific index element, like rear element.
This kind of problem can have application in many domains. Lets discuss
certain ways in which this task can be performed.

 **Method #1 : Using list comprehension**  
This is one way in which this task can be performed. In this, we iterate
through each row element in list and pair it with rear element using negative
indexing of list.

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate

# Pair elements with Rear element in Matrix Row

# using list comprehension

 

# Initializing list

test_list = [[4, 5, 6], [2, 4, 5], [6, 7,
5]]

 

# printing original list

print("The original list is : " + str(test_list))

 

# Pair elements with Rear element in Matrix Row

# using list comprehension

res = []

for sub in test_list:

 res.append([[ele, sub[-1]] for ele in sub[:-1]])

 

# printing result 

print ("The list after pairing is : " + str(res))  
  
---  
  
 __

 __

 **Output :**

    
    
    The original list is : [[4, 5, 6], [2, 4, 5], [6, 7, 5]]
    The list after pairing is : [[[4, 6], [5, 6]], [[2, 5], [4, 5]], [[6, 5], [7, 5]]]
    

**Method #2 : Using product() \+ loop**  
The combination of above methods can also be used to perform this task. In
this, we iterate through the list and perform task of pairing using product
and hence reducing one pair of loop.

  

  

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate

# Pair elements with Rear element in Matrix Row

# using product() + loop

from itertools import product

 

# Initializing list

test_list = [[4, 5, 6], [2, 4, 5], [6, 7,
5]]

 

# printing original list

print("The original list is : " + str(test_list))

 

# Pair elements with Rear element in Matrix Row

# using product() + loop

res = []

for idx in test_list:

 res.append(list(product(idx[:-1], [idx[-1]])))

 

# printing result 

print ("The list after pairing is : " + str(res))  
  
---  
  
 __

 __

 **Output :**

    
    
    The original list is : [[4, 5, 6], [2, 4, 5], [6, 7, 5]]
    The list after pairing is : [[[4, 6], [5, 6]], [[2, 5], [4, 5]], [[6, 5], [7, 5]]]
    

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

