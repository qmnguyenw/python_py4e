Python – Retain K match index values from other list



Sometimes, while working with Python lists, we can have a problem in which we
need to retain only the strings with match a particular value from the
corresponding list at same index. This can have application in many domains.
Lets discuss certain ways in which this task can be performed.

 **Method #1 : Using list comprehension +zip()**  
The combination of above functionalities can be used to perform this task. In
this, we extract the list after selective zipping of both the list matching K.

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate

# Retain K match index values from other list

# using zip() + list comprehension

 

# Initializing lists

test_list1 = ['Gfg', 'is', 'best', 'for', 'Geeks',
'and', 'CS']

test_list2 = [4, 1, 4, 3, 4, 2, 4]

 

# printing original lists

print("The original list 1 is : " + str(test_list1))

print("The original list 2 is : " + str(test_list2))

 

# Initializing K 

K = 4

 

# Group elements from Dual List Matrix

# using zip() + list comprehension

res = [x for x, y in zip(test_list1, test_list2) if y
== K]

 

# printing result 

print ("The filtered list : " + str(res))  
  
---  
  
 __

 __

 **Output :**

> The original list 1 is : [‘Gfg’, ‘is’, ‘best’, ‘for’, ‘Geeks’, ‘and’, ‘CS’]  
> The original list 2 is : [4, 1, 4, 3, 4, 2, 4]  
> The filtered list : [‘Gfg’, ‘best’, ‘Geeks’, ‘CS’]

 **Method #2 : Usingcompress() \+ list comprehension**  
This is yet another way in which this task can be performed. In this, we use
compress() instead of zip() to solve the problem.

  

  

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate

# Retain K match index values from other list

# using compress + list comprehension

from itertools import compress

 

# Initializing lists

test_list1 = ['Gfg', 'is', 'best', 'for', 'Geeks',
'and', 'CS']

test_list2 = [4, 1, 4, 3, 4, 2, 4]

 

# printing original lists

print("The original list 1 is : " + str(test_list1))

print("The original list 2 is : " + str(test_list2))

 

# Initializing K 

K = 4

 

# Group elements from Dual List Matrix

# using compress + list comprehension

res = list(compress(test_list1, map(lambda ele: ele == K,
test_list2)))

 

# printing result 

print ("The filtered list : " + str(res))  
  
---  
  
 __

 __

 **Output :**

> The original list 1 is : [‘Gfg’, ‘is’, ‘best’, ‘for’, ‘Geeks’, ‘and’, ‘CS’]  
> The original list 2 is : [4, 1, 4, 3, 4, 2, 4]  
> The filtered list : [‘Gfg’, ‘best’, ‘Geeks’, ‘CS’]

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

