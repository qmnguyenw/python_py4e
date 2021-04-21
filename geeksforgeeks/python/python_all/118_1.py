Python | List Element Count with Order



Sometimes, while working with lists or numbers we can have a problem in which
we need to attach with each element of list, a number, which is the position
of that element’s occurrence in that list. This type of problem can come
across many domains. Let’s discuss a way in which this problem can be solved.

 **Method : Usingdefaultdict() \+ loop**  
We can perform this task using defaultdict() and loop by carefully assigning
and incrementing order of elements.

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# List Element Count Order

# using defaultdict() + loop

from collections import defaultdict

 

# initialize list 

test_list = [1, 4, 1, 5, 4, 1, 5]

 

# printing original list 

print("The original list : " + str(test_list))

 

# List Element Count Order

# using defaultdict() + loop

temp = defaultdict(int)

res = []

for ele in test_list:

 temp[ele] += 1

 res.append((ele, temp[ele]))

 

# printing result

print("List elements with their order count : " + str(res))  
  
---  
  
 __

 __

 **Output :**

    
    
    The original list : [1, 4, 1, 5, 4, 1, 5]
    List elements with their order count : [(1, 1), (4, 1), (1, 2), (5, 1), (4, 2), (1, 3), (5, 2)]
    

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

