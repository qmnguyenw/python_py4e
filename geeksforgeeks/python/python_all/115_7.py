Subtract String Lists in Python



Sometimes, while working with lists, we can have a problem in which we need to
remove one list elements from other, i.e perform subtraction. This has
application across many domains. Let’s discuss certain ways in which this task
can be performed.

 **Method #1 : Using loop +remove()**  
The combination of above functionalities can be used to perform this task. In
this, we perform the removal of elements using remove() and check for similar
elements using loop.

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Subtract String Lists

# using loop + remove()

 

# initialize lists

test_list1 = ["gfg", "is", "best", "for", "CS"]

test_list2 = ["preffered", "is", "gfg"]

 

# printing original lists

print("The original list 1 : " + str(test_list1))

print("The original list 2 : " + str(test_list2))

 

# Subtract String Lists

# using loop + remove()

res = [ ele for ele in test_list1 ]

for a in test_list2:

 if a in test_list1:

 res.remove(a)

 

# printing result

print("The Subtracted list is : " + str(res))  
  
---  
  
 __

 __

 **Output :**

    
    
    The original list 1 : ['gfg', 'is', 'best', 'for', 'CS']
    The original list 2 : ['preffered', 'is', 'gfg']
    The Subtracted list is : ['best', 'for', 'CS']
    

**Method #2 : UsingCounter() + elements()**  
The combination of above functions provide a shorthand to solve this problem.
In this, we extract the count of elements in both list and then perform
separation by their extraction using element().

  

  

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Subtract String Lists

# using Counter() + elements()

from collections import Counter

 

# initialize lists

test_list1 = ["gfg", "is", "best", "for", "CS"]

test_list2 = ["preffered", "is", "gfg"]

 

# printing original lists

print("The original list 1 : " + str(test_list1))

print("The original list 2 : " + str(test_list2))

 

# Subtract String Lists

# using Counter() + elements()

res = list((Counter(test_list1)-Counter(test_list2)).elements())

 

# printing result

print("The Subtracted list is : " + str(res))  
  
---  
  
 __

 __

 **Output :**

    
    
    The original list 1 : ['gfg', 'is', 'best', 'for', 'CS']
    The original list 2 : ['preffered', 'is', 'gfg']
    The Subtracted list is : ['best', 'for', 'CS']
    

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

